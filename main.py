from time import time, sleep
from os import system
from random import randint
import pathlib
import platform

from objects import *
from items import *
from room import *

PATH = pathlib.Path().parent.resolve()

os = platform.system()
if os == 'Linux':
    clear = 'clear'
elif os == 'Windows':
    clear = 'cls'


def main():
    global escape, room, secrets, secret_data, lvl
    inventory = []
    while escape:
        eval('system("'+clear+'")')

        print('You are in the room', room.name,'\n')
        if room.dn: print('W - Up' if room.rn != 'Exit' else 'W - Up [Exit]')
        if room.dw: print('A - To the left' if room.rw != 'Exit' else 'A - To the left [Exit]')
        if room.ds: print('S - Down' if room.rs != 'Exit' else 'S - Down [Exit]')
        if room.de: print('D - To the right' if room.re != 'Exit' else 'D - To the right [Exit]')
        print('\nI - inspect')
        print('0 - leave')
        choice = input('\nChoose: ')

        if choice.lower() == 'w':
            if room.rn == 'Exit':
                error = True
                if room.closedDoors['dn'] == None:
                    escape = False
                    return True
                try:
                    if 'code:' in room.closedDoors['dn']:
                        code = room.closedDoors['dn'].split('code:')
                        code = code[-1]
                        eval('system("'+clear+'")')
                        code_input = input('Enter the code:\n\n\t')
                        if code_input == code:
                            escape = False
                            return True
                        else:
                            eval('system("'+clear+'")')
                            print('Wrong code!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    key_list = []
                    for item in inventory:
                        if 'Keycard' in item.name or 'Key' in item.name:
                            key_list.append(item)
                    eval('system("'+clear+'")')
                    run = 1
                    for key in key_list:
                        print(run,'-',key.name)
                        run += 1
                    num = input('\nWhich key would you like to use? Number: ')
                    eval('system("'+clear+'")')
                    different = ''
                    try:
                        if int(num) > len(key_list) or int(num) <= 0:
                            print('The number', num, 'does not exist!')
                            input('\nContinue...')
                        elif key_list[int(num)-1].name == room.closedDoors['dn'].name:
                            print('This key fits.')
                            input('\nContinue...')
                            escape = False
                            return True
                        else:
                            print('This key does not fit.')
                            input('\nContinue...')
                            different = ' different'
                    except:
                        print(num, 'is not a number!')
                        input('\nContinue...')
                    eval('system("'+clear+'")')
                    if error and escape:
                        eval('system("'+clear+'")')
                        print('You need a'+different+' key or keycard to open the door!\n')
                        input('Continue...')
                        eval('system("'+clear+'")')
            elif room.closedDoors['dn'] == None: 
                if room.rn != None:
                    room = rooms[room.rn]
            else:
                error = True
                try:
                    if 'code:' in room.closedDoors['dn']:
                        code = room.closedDoors['dn'].split('code:')
                        code = code[-1]
                        eval('system("'+clear+'")')
                        code_input = input('Enter the code:\n\n\t')
                        if code_input == code:
                            room = rooms[room.rn]
                            error = False
                        else:
                            eval('system("'+clear+'")')
                            print('Wrong code!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    key_list = []
                    for item in inventory:
                        if 'Keycard' in item.name or 'Key' in item.name:
                            key_list.append(item)
                    eval('system("'+clear+'")')
                    run = 1
                    for key in key_list:
                        print(run,'-',key.name)
                        run += 1
                    num = input('\nWhich key would you like to use? Number: ')
                    eval('system("'+clear+'")')
                    different = ''
                    try:
                        if int(num) > len(key_list) or int(num) <= 0:
                            print('The number', num, 'does not exist!')
                            input('\nContinue...')
                        elif key_list[int(num)-1].name == room.closedDoors['dn'].name:
                            print('This key fits.')
                            input('\nContinue...')
                            room = rooms[room.rn]
                            error = False
                        else:
                            print('This key does not fit.')
                            input('\nContinue...')
                            different = ' different'
                    except:
                        print(num, 'is not a number!')
                        input('\nContinue...')
                    eval('system("'+clear+'")')
                    if error and escape:
                        eval('system("'+clear+'")')
                        print('You need a'+different+' key or keycard to open the door!\n')
                        input('Continue...')
                        eval('system("'+clear+'")')
        elif choice.lower() == 'a':
            if room.rw == 'Exit':
                error = True
                if room.closedDoors['dw'] == None:
                    escape = False
                    return True
                try:
                    if 'code:' in room.closedDoors['dw']:
                        code = room.closedDoors['dw'].split('code:')
                        code = code[-1]
                        eval('system("'+clear+'")')
                        code_input = input('Enter the code:\n\n\t')
                        if code_input == code:
                            escape = False
                            return True
                        else:
                            eval('system("'+clear+'")')
                            print('Wrong code!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    key_list = []
                    for item in inventory:
                        if 'Keycard' in item.name or 'Key' in item.name:
                            key_list.append(item)
                    eval('system("'+clear+'")')
                    run = 1
                    for key in key_list:
                        print(run,'-',key.name)
                        run += 1
                    num = input('\nWhich key would you like to use? Number: ')
                    eval('system("'+clear+'")')
                    different = ''
                    try:
                        if int(num) > len(key_list) or int(num) <= 0:
                            print('The number', num, 'does not exist!')
                            input('\nContinue...')
                        elif key_list[int(num)-1].name == room.closedDoors['dw'].name:
                            print('This key fits.')
                            input('\nContinue...')
                            escape = False
                            return True
                        else:
                            print('This key does not fit.')
                            input('\nContinue...')
                            different = ' different'
                    except:
                        print(num, 'is not a number!')
                        input('\nContinue...')
                    eval('system("'+clear+'")')
                    if error and escape:
                        eval('system("'+clear+'")')
                        print('You need a'+different+' key or keycard to open the door!\n')
                        input('Continue...')
                        eval('system("'+clear+'")')
            elif room.closedDoors['dw'] == None: 
                if room.rw != None:
                    room = rooms[room.rw]
            else:
                error = True
                try:
                    if 'code:' in room.closedDoors['dw']:
                        code = room.closedDoors['dw'].split('code:')
                        code = code[-1]
                        eval('system("'+clear+'")')
                        code_input = input('Enter the code:\n\n\t')
                        if code_input == code:
                            room = rooms[room.rw]
                            error = False
                        else:
                            eval('system("'+clear+'")')
                            print('Wrong code!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    key_list = []
                    for item in inventory:
                        if 'Keycard' in item.name or 'Key' in item.name:
                            key_list.append(item)
                    eval('system("'+clear+'")')
                    run = 1
                    for key in key_list:
                        print(run,'-',key.name)
                        run += 1
                    num = input('\nWhich key would you like to use? Number: ')
                    eval('system("'+clear+'")')
                    different = ''
                    try:
                        if int(num) > len(key_list) or int(num) <= 0:
                            print('The number', num, 'does not exist!')
                            input('\nContinue...')
                        elif key_list[int(num)-1].name == room.closedDoors['dw'].name:
                            print('This key fits.')
                            input('\nContinue...')
                            room = rooms[room.rw]
                            error = False
                        else:
                            print('This key does not fit.')
                            input('\nContinue...')
                            different = ' different'
                    except:
                        print(num, 'is not a number!')
                        input('\nContinue...')
                    eval('system("'+clear+'")')
                    if error and escape:
                        eval('system("'+clear+'")')
                        print('You need a'+different+' key or keycard to open the door!\n')
                        input('Continue...')
                        eval('system("'+clear+'")')
        elif choice.lower() == 's':
            if room.rs == 'Exit':
                error = True
                if room.closedDoors['ds'] == None:
                    escape = False
                    return True
                try:
                    if 'code:' in room.closedDoors['ds']:
                        code = room.closedDoors['ds'].split('code:')
                        code = code[-1]
                        eval('system("'+clear+'")')
                        code_input = input('Enter the code:\n\n\t')
                        if code_input == code:
                            escape = False
                            return True
                        else:
                            eval('system("'+clear+'")')
                            print('Wrong code!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    key_list = []
                    for item in inventory:
                        if 'Keycard' in item.name or 'Key' in item.name:
                            key_list.append(item)
                    eval('system("'+clear+'")')
                    run = 1
                    for key in key_list:
                        print(run,'-',key.name)
                        run += 1
                    num = input('\nWhich key would you like to use? Number: ')
                    eval('system("'+clear+'")')
                    different = ''
                    try:
                        if int(num) > len(key_list) or int(num) <= 0:
                            print('The number', num, 'does not exist!')
                            input('\nContinue...')
                        elif key_list[int(num)-1].name == room.closedDoors['ds'].name:
                            print('This key fits.')
                            input('\nContinue...')
                            escape = False
                            return True
                        else:
                            print('This key does not fit.')
                            input('\nContinue...')
                            different = ' different'
                    except:
                        print(num, 'is not a number!')
                        input('\nContinue...')
                    eval('system("'+clear+'")')
                    if error and escape:
                        eval('system("'+clear+'")')
                        print('You need a'+different+' key or keycard to open the door!\n')
                        input('Continue...')
                        eval('system("'+clear+'")')
            elif room.closedDoors['ds'] == None: 
                if room.rs != None:
                    room = rooms[room.rs]
            else:
                error = True
                try:
                    if 'code:' in room.closedDoors['ds']:
                        code = room.closedDoors['ds'].split('code:')
                        code = code[-1]
                        eval('system("'+clear+'")')
                        code_input = input('Enter the code:\n\n\t')
                        if code_input == code:
                            room = rooms[room.rs]
                            error = False
                        else:
                            eval('system("'+clear+'")')
                            print('Wrong code!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    key_list = []
                    for item in inventory:
                        if 'Keycard' in item.name or 'Key' in item.name:
                            key_list.append(item)
                    eval('system("'+clear+'")')
                    run = 1
                    for key in key_list:
                        print(run,'-',key.name)
                        run += 1
                    num = input('\nWhich key would you like to use? Number: ')
                    eval('system("'+clear+'")')
                    different = ''
                    try:
                        if int(num) > len(key_list) or int(num) <= 0:
                            print('The number', num, 'does not exist!')
                            input('\nContinue...')
                        elif key_list[int(num)-1].name == room.closedDoors['ds'].name:
                            print('This key fits.')
                            input('\nContinue...')
                            room = rooms[room.rs]
                            error = False
                        else:
                            print('This key does not fit.')
                            input('\nContinue...')
                            different = 'different '
                    except:
                        print(num, 'is not a number!')
                        input('\nContinue...')
                    eval('system("'+clear+'")')
                    if error and escape:
                        eval('system("'+clear+'")')
                        print('You need a '+different+'key or keycard to open the door!\n')
                        input('Continue...')
                        eval('system("'+clear+'")')
        elif choice.lower() == 'd':
            if room.re == 'Exit':
                error = True
                if room.closedDoors['de'] == None:
                    escape = False
                    return True
                try:
                    if 'code:' in room.closedDoors['de']:
                        code = room.closedDoors['de'].split('code:')
                        code = code[-1]
                        eval('system("'+clear+'")')
                        code_input = input('Enter the code:\n\n\t')
                        if code_input == code:
                            escape = False
                            return True
                        else:
                            eval('system("'+clear+'")')
                            print('Wrong code!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    key_list = []
                    for item in inventory:
                        if 'Keycard' in item.name or 'Key' in item.name:
                            key_list.append(item)
                    eval('system("'+clear+'")')
                    run = 1
                    for key in key_list:
                        print(run,'-',key.name)
                        run += 1
                    num = input('\nWhich key would you like to use? Number: ')
                    eval('system("'+clear+'")')
                    different = ''
                    try:
                        if int(num) > len(key_list) or int(num) <= 0:
                            print('The number', num, 'does not exist!')
                            input('\nContinue...')
                        elif key_list[int(num)-1].name == room.closedDoors['de'].name:
                            print('This key fits.')
                            input('\nContinue...')
                            escape = False
                            return True
                        else:
                            print('This key does not fit.')
                            input('\nContinue...')
                            different = ' different'
                    except:
                        print(num, 'is not a number!')
                        input('\nContinue...')
                    eval('system("'+clear+'")')
                    if error and escape:
                        eval('system("'+clear+'")')
                        print('You need a'+different+' key or keycard to open the door!\n')
                        input('Continue...')
                        eval('system("'+clear+'")')
            elif room.closedDoors['de'] == None: 
                if room.re != None:
                    room = rooms[room.re]
            else:
                error = True
                try:
                    if 'code:' in room.closedDoors['de']:
                        code = room.closedDoors['de'].split('code:')
                        code = code[-1]
                        eval('system("'+clear+'")')
                        code_input = input('Enter the code:\n\n\t')
                        if code_input == code:
                            room = rooms[room.re]
                            error = False
                        else:
                            eval('system("'+clear+'")')
                            print('Wrong code!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    key_list = []
                    for item in inventory:
                        if 'Keycard' in item.name or 'Key' in item.name:
                            key_list.append(item)
                    eval('system("'+clear+'")')
                    run = 1
                    for key in key_list:
                        print(run,'-',key.name)
                        run += 1
                    num = input('\nWhich key would you like to use? Number: ')
                    eval('system("'+clear+'")')
                    different = ''
                    try:
                        if int(num) > len(key_list) or int(num) <= 0:
                            print('The number', num, 'does not exist!')
                            input('\nContinue...')
                        elif key_list[int(num)-1].name == room.closedDoors['de'].name:
                            print('This key fits.')
                            input('\nContinue...')
                            room = rooms[room.re]
                            error = False
                        else:
                            print('This key does not fit.')
                            input('\nContinue...')
                            different = ' different'
                    except:
                        print(num, 'is not a number!')
                        input('\nContinue...')
                    eval('system("'+clear+'")')
                    if error and escape:
                        eval('system("'+clear+'")')
                        print('You need a'+different+' key or keycard to open the door!\n')
                        input('Continue...')
                        eval('system("'+clear+'")')
        elif choice.lower() == 'i':
            while True:
                run = 1
                eval('system("'+clear+'")')
                for object in room.interactions:
                    print(run, '-', object.name)
                    run += 1
                print('\ni - Back')
                interaction_choice = input('\nInspect Number: ')
                eval('system("'+clear+'")')
                if interaction_choice.lower() == 'i':
                    break
                try: 
                    if int(interaction_choice) > len(room.interactions) or int(interaction_choice) <= 0:
                        eval('system("'+clear+'")')
                        print('You can\'t inspect number', interaction_choice, 'because it doesn\'t exist!')
                        input('\nContinue...')
                    else:
                        index = int(interaction_choice)-1
                        
                        # |▮▮▮▮▢▢▢▢▢|

                        progress = 0
                        steps_per_s = room.interactions[index].steps_per_s
                        step = steps_per_s/75
                        step = step*10
                        while progress < 10:
                            eval('system("'+clear+'")')
                            progress += step
                            if round(progress) > 10:
                                progress = 10
                            print('Inspect Progress: |'+('▮'*round(progress))+('▢'*(10-round(progress)))+'|')
                            sleep(0.1)

                        eval('system("'+clear+'")')

                        if room.interactions[index].item == None:
                            print('Unfortunately, you haven\'t found anything!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                        elif room.interactions[index].item.name == 'Note':
                            print('You have found a note:\n')
                            print(room.interactions[index].item.text)
                            input('\nContinue...')
                        elif room.interactions[index].item.name == 'Smartphone-Message':
                            print('You have found a message on a smartphone:\n')
                            print(room.interactions[index].item.text)
                            input('\nContinue...')
                        elif room.interactions[index].item.name == 'Diary-Entry':
                            print('You have found an entry in a diary:\n')
                            print(room.interactions[index].item.text)
                            input('\nContinue...')
                        elif room.interactions[index].item.name == 'Carpet-Text':
                            print('It says on the carpet:\n')
                            print(room.interactions[index].item.text)
                            input('\nContinue...')
                        elif room.interactions[index].name == 'SECRET':
                            print('You have found a secret:\n')
                            print(room.interactions[index].item.text)
                            secrets += 1 if 'n' in secret_data[lvl] else 0
                            if secret_data[lvl] == 'j':
                                print('\nAlready found!')
                            else:
                                print('\n['+str(secrets)+'/3] Secrets')
                            secret_data[lvl] = 'j'
                            input('\nContinue...')
                        else:
                            if room.interactions[index].item not in inventory:
                                print('You have found “'+ room.interactions[index].item.name+ '”!\n')
                                inventory.append(room.interactions[index].item)
                            else:
                                print('Unfortunately, you haven\'t found anything!\n')
                            input('Continue...')
                            eval('system("'+clear+'")')
                except:
                    eval('system("'+clear+'")')
                    print(interaction_choice, 'is not a number!')
                    input('\nContinue...')
        elif choice.lower() == '0':
            eval('system("'+clear+'")')
            if input('Do you really want to leave the escape room (y/n)? ').lower() == 'y':
                return False
            eval('system("'+clear+'")')
            


if __name__ == '__main__':
    #with open(str(PATH)+'\\escapeRoom\\data.txt', 'r', encoding='utf-8') as file:
    with open(str(PATH)+'/data.txt', 'r', encoding='utf-8') as file:
        run = 1
        secret_data = []
        for line in file.readlines():
            if run == 1:
                secrets = int(line)
            if run == 2:
                for i in line:
                    secret_data.append(i)
            run += 1
        file.close() 

    while True:
        eval('system("'+clear+'")')
        print('\t\t--- Python3 Escape Room ---\n')
        print('\t1 - Choose Escape Room')
        print('\t2 - Secrets')
        print('\t0 - Exit\n')
        mainchoice = input('Choose: ')
        if mainchoice == '1':
            while True:
                eval('system("'+clear+'")')
                print('\t\t--- Python3 Escape Room ---')
                print('\nChoose a difficulty:')
                print('\t1 - Tutorial')
                print('\t2 - Easy')
                print('\t3 - Normal')
                print('\t4 - Hard')
                print('\t5 - Extreme')
                print('\t0 - Back\n')
                choice = input('Choose: ')
                if choice == '1':
                    while True:
                        eval('system("'+clear+'")')
                        print('\t\t--- Python3 Escape Room ---\n')
                        print('\t1 - Start')
                        print('\t2 - Ranking')
                        print('\t0 - Back')
                        room_choice = input('\nChoose: ')
                        if room_choice == '0':
                            break
                        elif room_choice == '1':
                
                            from room_tutorial import *
                            
                            escape = True
                            start_time=time()
                            win = main()
                            end_time=time()-start_time
                            eval('system("'+clear+'")')
                            if win:
                                print('You have escaped!\n')
                                print('Time required:', str(round(end_time,2))+'s')
                                jn = input('If this time is to be saved (y/n)? ') 
                                if jn.lower() != 'n':
                                    name = input('Enter your name: ')
                                    #with open(str(PATH)+'\\escapeRoom\\tutorial_data.txt', 'a', encoding='utf-8') as file:
                                    with open(str(PATH)+'/tutorial_data.txt', 'a', encoding='utf-8') as file:
                                        file.write(str(round(end_time,2))+'|'+name+'\n')
                                        file.close()
                        if room_choice == '2':
                            eval('system("'+clear+'")')
                            times:dict = {}
                            #with open(str(PATH)+'\\escapeRoom\\tutorial_data.txt', 'r', encoding='utf-8') as file:
                            with open(str(PATH)+'/tutorial_data.txt', 'r', encoding='utf-8') as file:
                                for line in file.readlines():
                                    line = line.split('\n')
                                    line = line[0].split('|')
                                    if float(line[0]) in times.keys():
                                        times[float(line[0])].append(line[-1])
                                    else:
                                        times[float(line[0])] = []
                                        times[float(line[0])].append(line[-1])
                                file.close()
                            
                            print('\t\t--- Ranking Tutorial ---')
                            run = 0
                            key_list = []
                            for key in times.keys():
                                key_list.append(key)
                            key_list.sort(reverse=False)
                            for key in key_list:
                                run += 1
                                for player in times[key]:
                                    print(str(run)+'. '+str(key)+'s: '+player)
                            input('\nContinue...')
                elif choice == '2':
                    while True:
                        eval('system("'+clear+'")')
                        print('\t\t--- Python3 Escape Room ---\n')
                        print('\t1 - Start')
                        print('\t2 - Ranking')
                        print('\t0 - Back')
                        room_choice = input('\nChoose: ')
                        if room_choice == '0':
                            break
                        elif room_choice == '1':
                            lvl = 0
                            
                            from room_easy import *

                            escape = True
                            start_time=time()
                            win = main()
                            end_time=time()-start_time
                            eval('system("'+clear+'")')
                            if win:
                                print('You have escaped!\n')
                                print('Time required:', str(round(end_time,2))+'s')
                                jn = input('If this time is to be saved (y/n)? ') 
                                if jn.lower() != 'n':
                                    name = input('Enter your name: ')
                                    #with open(str(PATH)+'\\escapeRoom\\easy_data.txt', 'a', encoding='utf-8') as file:
                                    with open(str(PATH)+'/easy_data.txt', 'a', encoding='utf-8') as file:
                                        file.write(str(round(end_time,2))+'|'+name+'\n')
                                        file.close()
                        if room_choice == '2':
                            eval('system("'+clear+'")')
                            times:dict = {}
                            #with open(str(PATH)+'\\escapeRoom\\easy_data.txt', 'r', encoding='utf-8') as file:
                            with open(str(PATH)+'/easy_data.txt', 'r', encoding='utf-8') as file:
                                for line in file.readlines():
                                    line = line.split('\n')
                                    line = line[0].split('|')
                                    if float(line[0]) in times.keys():
                                        times[float(line[0])].append(line[-1])
                                    else:
                                        times[float(line[0])] = []
                                        times[float(line[0])].append(line[-1])
                                file.close()
                            
                            print('\t\t--- Ranking Easy ---')
                            run = 0
                            key_list = []
                            for key in times.keys():
                                key_list.append(key)
                            key_list.sort(reverse=True)
                            for key in key_list:
                                run += 1
                                for player in times[key]:
                                    print(str(run)+'. '+str(key)+'s: '+player)
                            input('\nContinue...')
                elif choice == '3':
                    while True:
                        eval('system("'+clear+'")')
                        print('\t\t--- Python3 Escape Room ---\n')
                        print('\t1 - Start')
                        print('\t2 - Ranking')
                        print('\t0 - Back')
                        room_choice = input('\nChoose: ')
                        if room_choice == '0':
                            break
                        elif room_choice == '1':
                            lvl = 1

                            from room_normal import *

                            escape = True
                            start_time=time()
                            win = main()
                            end_time=time()-start_time
                            eval('system("'+clear+'")')
                            if win:
                                print('You have escaped!\n')
                                print('Time required:', str(round(end_time,2))+'s')
                                jn = input('If this time is to be saved (y/n)? ') 
                                if jn.lower() != 'n':
                                    name = input('Enter your name: ')
                                    #with open(str(PATH)+'\\escapeRoom\\normal_data.txt', 'a', encoding='utf-8') as file:
                                    with open(str(PATH)+'/normal_data.txt', 'a', encoding='utf-8') as file:
                                        file.write(str(round(end_time,2))+'|'+name+'\n')
                                        file.close()
                        if room_choice == '2':
                            eval('system("'+clear+'")')
                            times:dict = {}
                            #with open(str(PATH)+'\\escapeRoom\\normal_data.txt', 'r', encoding='utf-8') as file:
                            with open(str(PATH)+'/normal_data.txt', 'r', encoding='utf-8') as file:
                                for line in file.readlines():
                                    line = line.split('\n')
                                    line = line[0].split('|')
                                    if float(line[0]) in times.keys():
                                        times[float(line[0])].append(line[-1])
                                    else:
                                        times[float(line[0])] = []
                                        times[float(line[0])].append(line[-1])
                                file.close()
                            
                            print('\t\t--- Ranking Normal ---')
                            run = 0
                            key_list = []
                            for key in times.keys():
                                key_list.append(key)
                            key_list.sort(reverse=True)
                            for key in key_list:
                                run += 1
                                for player in times[key]:
                                    print(str(run)+'. '+str(key)+'s: '+player)
                            input('\nContinue...')
                elif choice == '4':
                    while True:
                        eval('system("'+clear+'")')
                        print('\t\t--- Python3 Escape Room ---\n')
                        print('\t1 - Start')
                        print('\t2 - Ranking')
                        print('\t0 - Back')
                        room_choice = input('\nChoose: ')
                        if room_choice == '0':
                            break
                        elif room_choice == '1':
                            lvl = 2
                            
                            from room_hard import *

                            escape = True
                            start_time=time()
                            win = main()
                            end_time=time()-start_time
                            eval('system("'+clear+'")')
                            if win:
                                print('You have escaped!\n')
                                print('Time required:', str(round(end_time,2))+'s')
                                jn = input('If this time is to be saved (y/n)? ') 
                                if jn.lower() != 'n':
                                    name = input('Enter your name: ')
                                    #with open(str(PATH)+'\\escapeRoom\\hard_data.txt', 'a', encoding='utf-8') as file:       
                                    with open(str(PATH)+'/hard_data.txt', 'a', encoding='utf-8') as file:
                                        file.write(str(round(end_time,2))+'|'+name+'\n')
                                        file.close()
                        if room_choice == '2':
                            eval('system("'+clear+'")')
                            times:dict = {}
                            #with open(str(PATH)+'\\escapeRoom\\hard_data.txt', 'r', encoding='utf-8') as file:
                            with open(str(PATH)+'/hard_data.txt', 'r', encoding='utf-8') as file:
                                for line in file.readlines():
                                    line = line.split('\n')
                                    line = line[0].split('|')
                                    if float(line[0]) in times.keys():
                                        times[float(line[0])].append(line[-1])
                                    else:
                                        times[float(line[0])] = []
                                        times[float(line[0])].append(line[-1])
                                file.close()
                            
                            print('\t\t--- Ranking Hard ---')
                            run = 0
                            key_list = []
                            for key in times.keys():
                                key_list.append(key)
                            key_list.sort(reverse=True)
                            for key in key_list:
                                run += 1
                                for player in times[key]:
                                    print(str(run)+'. '+str(key)+'s: '+player)
                            input('\nContinue...')
                elif choice == '5':
                    while True:
                        eval('system("'+clear+'")')
                        print('\t\t--- Python3 Escape Room ---\n')
                        print('\t1 - Start')
                        print('\t2 - Ranking')
                        print('\t0 - Back')
                        room_choice = input('\nChoose: ')
                        if room_choice == '0':
                            break
                        elif room_choice == '1':
                            #lvl = 3
                            
                            print('Loading...')
                            
                            from room_extreme import *
                            from keys_extreme import *

                            inventory = [KeyA303()]
                            
                            eval('system("'+clear+'")')

                            escape = True
                            start_time=time()
                            win = main()
                            end_time=time()-start_time
                            eval('system("'+clear+'")')
                            if win:
                                print('You have escaped!\n')
                                print('Time required:', str(round(end_time,2))+'s')
                                jn = input('If this time is to be saved (y/n)? ') 
                                if jn.lower() != 'n':
                                    name = input('Enter your name: ')
                                    #with open(str(PATH)+'\\escapeRoom\\extreme_data.txt', 'a', encoding='utf-8') as file:       
                                    with open(str(PATH)+'/extreme_data.txt', 'a', encoding='utf-8') as file:
                                        file.write(str(round(end_time,2))+'|'+name+'\n')
                                        file.close()
                        if room_choice == '2':
                            eval('system("'+clear+'")')
                            times:dict = {}
                            #with open(str(PATH)+'\\escapeRoom\\extreme_data.txt', 'r', encoding='utf-8') as file:
                            with open(str(PATH)+'/extreme_data.txt', 'r', encoding='utf-8') as file:
                                for line in file.readlines():
                                    line = line.split('\n')
                                    line = line[0].split('|')
                                    if float(line[0]) in times.keys():
                                        times[float(line[0])].append(line[-1])
                                    else:
                                        times[float(line[0])] = []
                                        times[float(line[0])].append(line[-1])
                                file.close()
                            
                            print('\t\t--- Ranking Extreme ---')
                            run = 0
                            key_list = []
                            for key in times.keys():
                                key_list.append(key)
                            key_list.sort(reverse=True)
                            for key in key_list:
                                run += 1
                                for player in times[key]:
                                    print(str(run)+'. '+str(key)+'s: '+player)
                            input('\nContinue...')
                        if choice == '0':
                            break
                elif choice == '0':
                    break
        elif mainchoice == '2':
            eval('system("'+clear+'")')
            print('\t\t--- Python3 Escape Room ---\n')
            print('\t['+str(secrets)+'/3] Secrets found\n')
            input('\n Back...')
        elif mainchoice == '0':
            break

#with open(str(PATH)+'\\escapeRoom\\data.txt', 'w', encoding='utf-8') as file:
with open(str(PATH)+'/data.txt', 'w', encoding='utf-8') as file:
    file.write(str(secrets)+'\n')
    file.write(''.join(secret_data))
    file.close() 