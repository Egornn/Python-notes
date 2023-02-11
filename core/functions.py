import sys
from core.Note import Note
import core.NotesList 
import json
import core.functions

global COMMANDS, NOTE_LIST, ID
ID=0
COMMANDS = ['help', 'read', 'find', 'add', 'list', 'change', 'remove', 'save', 'load', "exit"]
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

    if command == "change":
        id = transform(input ("Введите ID заметки для обновления: "))
        isExist=False
        for i in range (len(NOTE_LIST)):
            if NOTE_LIST[i].id == id:
                changeNote(NOTE_LIST[i])
                isExist=True
        if not isExist:
            print('Заметки с таким ID не существует, используйте list, чтобы просмотреть ID существующих заметок')
   
    if command == 'remove':
        id = transform(input ("Введите ID заметки для удаления: "))
        isExist=False
        for note in NOTE_LIST:
            if note.id == id:
                NOTE_LIST.remove(note)
                isExist=True
        if not isExist:
            print('Заметки с таким ID не существует, используйте list, чтобы просмотреть ID существующих заметок')
   
    if command == 'save':
        pass

    if command == 'load':
        pass
    
    if command == 'find':
        pass
    
    if command == 'read':
        id = transform(input ("Введите ID заметки для чтения: "))
        isExist=False
        for i in range (len(NOTE_LIST)):
            if NOTE_LIST[i].id == id:
                note=NOTE_LIST[i]
                print (f'Заметка ID#{note.id} под заголовком "{note.title}" сообщает "{note.body}". Последнее изменение {note.date} в {note.time}.')
                isExist=True
        if not isExist:
            print('Заметки с таким ID не существует, используйте list, чтобы просмотреть ID существующих заметок')
   
    
    if command=='exit':
        # exit = input('Убедитесь, что изменения были сохранены. Введите "exit" повторно для закрытия программы:  ')
        # if exit == 'exit':
        sys.exit()



def checkCommand(command):
    return command in COMMANDS

def changeNote(note):
    print(note.title)
    new_title = input ("Введите новый заголовок (оставьте пустым, чтобы не вносить изменения): ")
    if not new_title=="":
        note.title=new_title
        note.updateDate()
    print(note.body)
    new_body = input ("Введите новый текст заметки (оставьте пустым, чтобы не вносить изменения): ")
    if not new_body=="":
        note.body=new_body
        note.updateDate()
    

def transform(inp):
    try:
        return int(inp)
    except:
        print("Введено некорректное число")
        return inp