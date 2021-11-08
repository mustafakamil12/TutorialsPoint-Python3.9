#!/usr/bin/python3

import os,sys,subprocess
from os import environ
from subprocess import PIPE
from termcolor import colored

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))



#------------Main------------

if __name__ == "__main__":
    prYellow("""

 __  __     ______     ______     ______   ______     ______    
/\ \_\ \   /\  __ \   /\  __ \   /\  == \ /\  __ \   /\  ___\   
\ \  __ \  \ \ \/\ \  \ \ \/\ \  \ \  _-/ \ \ \/\ \  \ \  __\   
 \ \_\ \_\  \ \_____\  \ \_____\  \ \_\    \ \_____\  \ \_____\ 
  \/_/\/_/   \/_____/   \/_____/   \/_/     \/_____/   \/_____/ 
                                                                
...............................................................
    """)

    mode = "build"
    build_by = "-TEST"

    if mode == "build":
        prCyan("Build Mode")
        if(build_by == "-cycle"):
            prCyan("build by cycle")            
            os.system("ssh op@18.212.5.40 '/pgs/bin/prod_build.py -cycle ET_03PM'")
            os.system("ssh gfs@energy-dev-gfs1 '/data/gfs/v10/bin/prod_build.pl -cycle ET_03PM'")
        
        elif(build_by == "-product"):
            prCyan("build by product")
            os.system("ssh op@18.212.5.40 '/pgs/bin/prod_build.py -product OXYOBSDAY'")
            os.system("ssh gfs@energy-dev-gfs1 '/data/gfs/v10/bin/prod_build.pl -product OXYOBSDAY'")
        
        else:
            prRed("Error: Mode Must Be Either -cycle Or -product")
    elif mode == "compare":
        prCyan("Compare Mode")

    

