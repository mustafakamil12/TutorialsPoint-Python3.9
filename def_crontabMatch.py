import re,subprocess
from subprocess import PIPE

def readfile(filename):
    myFile = open(filename,'r')
    cronLines = myFile.readlines()
    print(cronLines)
    return cronLines

def cronMatching(cronlinesArr):
    cronop = subprocess.run('crontab -l | grep cycle',stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
    subprocess_rc = cronop.returncode
    print(f"subprocess_rc{subprocess_rc}")
    cronop = cronop.stdout
    cronop = cronop.decode("utf-8")

    print(f"cronop = {cronop}")

    """
        cycleArr = []
        for line in cronlinesArr:
            #print(f"line = {line}")
            cycle = re.findall(r'cycle .\S+',line)
            cycleArr.append(cycle)
            print(cycle)
    """

    cycle = re.findall(r'cycle .\S+',cronop)
    print(f"the period of cycle in crontab {cycle}")
    return cycle

cronAllLines = []
cronAllLines = readfile('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/testcron.txt')
mycycleArr = cronMatching(cronAllLines)
print(mycycleArr)
