import os,subprocess

fcst_file = 'testFile'
HOST = 'myLapTop'
#subprocess.run('echo "Hello World This Email From Python Direct To Shell" | mail -s "Test email" godric.phoenix@gmail.com',shell=True)
subprocess.run(f'echo "{fcst_file} missing on {HOST}" | mail -s "Problem with MSLP forecast ingest on {HOST}" godric.phoenix@gmail.com',shell=True)
