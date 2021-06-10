import os
player = 'bob'

filename = player+'.txt'

if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

highscore = open(filename,append_write)
highscore.write("Username: " + player + '\n')
highscore.close()
