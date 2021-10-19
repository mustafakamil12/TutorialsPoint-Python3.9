import re,subprocess
from subprocess import PIPE

def cronMatching():
    cronop = subprocess.run('crontab -l | grep cycle',stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
    subprocess_rc = cronop.returncode
    #print(f"subprocess_rc{subprocess_rc}")
    cronop = cronop.stdout
    cronop = cronop.decode("utf-8")

    #print(f"cronop = {cronop}")
    cycle_payload = []
    cycle = re.findall(r'cycle .\S+',cronop)
    #print(f"cycle before cleaning = {cycle}")
    #print(f"the period of cycle in crontab {cycle}")
    for elem in cycle:
        #print(f"elem = {elem}")
        clean_cycle = elem.lstrip('cycle ')
        clean_cycle = clean_cycle.replace("'",'')
        #print(f"clean_cycle = {clean_cycle}")
        cycle_payload.append(clean_cycle.strip())

    #print(f"cycle_payload = {cycle_payload}")
    psqlcontArr = []
    psqlPeriod = subprocess.run('psql -c "select distinct(period) from product_update_times "',stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
    subprocess_rc = psqlPeriod.returncode
    #print(f"subprocess_rc{subprocess_rc}")
    psqlPeriodop = psqlPeriod.stdout
    psqlPeriodop = psqlPeriodop.decode("utf-8")
    psqlcont = psqlPeriodop.splitlines()

    for elem in psqlcont:
        psqlcontelem = elem.rstrip()
        psqlcontArr.append(psqlcontelem.strip())
    newpsqlcontArr =  psqlcontArr[2:]

    #psqlcontArr.pop(2)
    newpsqlcontArr.pop(len(newpsqlcontArr)-1)
    #print(f"psqlcontArr = {newpsqlcontArr}")
    print(f"lenght of cycle_payload = {len(cycle_payload)}")
    print(f"length of psqlcontArr = {len(psqlcontArr)}")

    cycle_payload_as_set = set(cycle_payload)
    intersection = cycle_payload_as_set.intersection(psqlcontArr)
    intersection_as_list = list(intersection)
    print(f"length of intersection_as_list = {len(intersection_as_list)}")
    #print(intersection_as_list)
    return intersection_as_list

def fetch_product_list_names_from_cycle_list(cycle_arr):
    cycle_arr = ['ET_12PM']
    products_per_period = {}
    for cycle_elem in cycle_arr:
        print(f"cycle_elem = {cycle_elem}")
        prodcontArr = []
        cmd = "select product_name from product_update_times where period = '%s' order by product_name" % cycle_elem
        print(f'psql -c "{cmd}"')
        cyclePeriod = subprocess.run(f'psql -c "{cmd}"',stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
        subprocess_rc = cyclePeriod.returncode
        #print(f"subprocess_rc{subprocess_rc}")
        cyclePeriodop = cyclePeriod.stdout
        cyclePeriodop = cyclePeriodop.decode("utf-8")
        cyclecont = cyclePeriodop.splitlines()
        print(f"cyclecont = {cyclecont}")
        for elem in cyclecont:
            cyclecontelem = elem.rstrip()
            prodcontArr.append(cyclecontelem.strip())
        newcyclecontArr =  prodcontArr[2:]

        #psqlcontArr.pop(2)
        newcyclecontArr.pop(len(newcyclecontArr)-1)
        newcyclecontArr.pop(len(newcyclecontArr)-1)
        print(f"newcyclecontArr = {newcyclecontArr}")

cycleArr = cronMatching()
print(cycleArr)
fetch_product_list_names_from_cycle_list(cycleArr)
