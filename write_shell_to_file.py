import subprocess
file_ = open('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/shell_output.txt', 'w+')
subprocess.run('echo Hello from shell', shell=True, stdout=file_)
file_.close()
