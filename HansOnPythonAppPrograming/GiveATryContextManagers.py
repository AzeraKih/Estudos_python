##Define a function
##    'writeTo' with two parameters, 'filename' and 'text'.
##    'text' takes any input string and
##    'filename' refers to name of the file into which input 'text' is written.
##Hint : Use 'with' to open the file into which input text is written.

##import zipfile
##
##def writeTo(filename, input_text):
##    with open(filename, 'w+') as f:
##        f.write(input_text)
##        
##def zipe(zfile, filename):
##    with zipfile.ZipFile(zfile,'w') as z: 
##        z.write(filename) 
##
##writeTo('t.txt', 'teste')
##zipe('t.zip', 't.txt')

##Define a function 'run_process', which accepts a system command,
##runs the command at the background, and returns the results.
##Hint : Use 'Popen' utility in 'subprocess' module to run a system command.
##Hint : Use 'with' along with 'Popen'

import sys
import os
import subprocess
import inspect

def run_process(cmd_args):
    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
        out, err = p.communicate()
        return out



print(run_process('ping google.com'))
