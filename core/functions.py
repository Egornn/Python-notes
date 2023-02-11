import sys
from core.Note import Note
import core.NotesList 
import json
import core.functions

global COMMANDS, NOTE_LIST, ID
ID=0
COMMANDS = ['help', 'add', 'list', 'change', 'remove', 'save', 'load', "exit"]
NOTE_LIST= []


def execute(command):
    global ID, NOTE_LIST
    if command=='help':
        print (COMMANDS)
    if command == 'add':
        print(ID)
        new_note =  Note(ID)
        ID=ID+1
        new_note.title=input ('Введите заголовок: ')
        new_note.body=input ('Введите текст заметки: ')
        NOTE_LIST.append(new_note)
    if command =="list":
        for note in NOTE_LIST:
            print(str(note))
    if command=='exit':
        sys.exit()



def checkCommand(command):
    return command in COMMANDS