
import sys
import note


global COMMANDS, ID 
ID=0
COMMANDS = ['help', 'add', 'list' 'change', 'remove', 'save', 'load', "exit"]




def main_loop():
    while True:
        print('Введите команду (help для помощи)')
        command = input().lower()
        if command in COMMANDS:
            execute(command)
        else:
            print('Wrong command')



def execute(command):
    if command=='help':
        print (COMMANDS)
    if command == 'add':



    if command=='exit':
        sys.exit()
    