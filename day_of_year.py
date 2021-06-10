import subprocess

date_num=subprocess.run('date +%j',capture_output=True,text=True,shell=True)
print("date_num = ", date_num.stdout)
subprocess_rc=date_num.returncode
print("subprocess_rc = ", subprocess_rc)
date_num=date_num.stdout
print("date_num = ", date_num)

print ("\n\n\n")
print ("                       5 DAY NORMALS\n")
print ("                       -------------\n\n")
print ("Days:     Day 1      Day 2      Day 3      Day 4      Day 5\n")
print ("ALB     ")
