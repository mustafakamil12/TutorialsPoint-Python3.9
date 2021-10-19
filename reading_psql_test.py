"""
psqlPeriod = subprocess.run('psql -c "select distinct(period) from product_update_times "',stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
subprocess_rc = psqlPeriod.returncode
#print(f"subprocess_rc{subprocess_rc}")
psqlPeriodop = psqlPeriod.stdout
psqlPeriodop = psqlPeriodop.decode("utf-8")
"""
psqlcontArr = []
psqlfile = open('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/psql_test.txt','r')
psqlcont = psqlfile.readlines()
for elem in psqlcont:
    psqlcontelem = elem.rstrip()
    psqlcontArr.append(psqlcontelem)
newpsqlcontArr =  psqlcontArr[2:]

#psqlcontArr.pop(2)
newpsqlcontArr.pop(len(newpsqlcontArr)-1)
print(f"psqlcontArr = {newpsqlcontArr}")
