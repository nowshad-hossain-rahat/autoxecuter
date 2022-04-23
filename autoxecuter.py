from genericpath import exists
from signal import SIGINT, signal
import subprocess


# executers list
executers = (
    { 'name': 'Node.js', 'command': 'node', 'type': 'interpreter' },
    { 'name': 'Python', 'command': 'python', 'type': 'interpreter' },
    { 'name': 'PHP', 'command': 'php', 'type': 'interpreter' },
    { 'name': 'Ruby', 'command': 'ruby', 'type': 'interpreter' },
    { 'name': 'Perl', 'command': 'perl', 'type': 'interpreter' },
    { 'name': 'TypeScript', 'command': 'tsc', 'type': 'compiler' },
    { 'name': 'C++ (GCC)', 'command': 'g++', 'type': 'compiler' },
)


# this will response to the Ctrl + C event
def stop_auto_executer(sig, frame):
    print('[#]-> Auto Executer stopped!')
    exit(0)


# this will execute the python file whenever it'll find any changes into the file
def auto_execute(executer:str, filename: str):

    # storing the file content
    prev_content = open(filename).read()

    # adding event listener to the Ctrl + C event
    signal(SIGINT, stop_auto_executer)

    print('[#]-> Execution started...')

    while(True):

        current_content = open(filename).read()

        if( current_content != None and current_content != '' and current_content != prev_content ):

            sp = subprocess.run([executer, filename], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if( executer == 'g++' ):
                sp = subprocess.run(['./a.out'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            elif( executer == 'tsc' ):
                filename = filename[0:-2] + 'js'
                sp = subprocess.run(['node', filename], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if( sp.stdout ):
                print(sp.stdout, end='')
            elif( sp.stderr ):
                print(sp.stderr, end='')

            prev_content = open(filename).read()


print('[#]-> Welcome to Auto Executer!')
print('[#]-> Author : Nowshad Hossain Rahat')
print('[#]-> Git repo : https://github.com/nowshad-hossain-rahat/autoxecuter')
print('[#]-> Select Executer : ')

# printing the executers
i = 0
for executer in executers:
    print(f"  [{i}]-> {executer['name']}")
    i+=1

executer_id = input('[#]-> Enter the ID : ')
filename = input('[#]-> File name : ')

if( executer_id != None and executer_id != '' and filename != '' ):

    executer_id = int(executer_id)

    if( executer_id >= len(executers) or executer_id < 0 ):
        print('[!]-> Invalid Executer ID!')
    elif( not exists(filename) ):
        print('[!]-> File does not exists!')
    else:
        auto_execute(executers[executer_id]['command'], filename)

else:
    print('[!]-> Invalid Executer or Filename!')
