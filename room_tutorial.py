from random import randint
from objects import *
from items import *
from room import *

code = str(randint(1000,9999))

roomA1 = Room(
    'A1', None, None, 'A2', 'B1',
    {'dn':None, 'dw':None, 'de':YellowKeycard(), 'ds':None},
    [Plant(), Plant(YellowKeycard()), Plant()]
    )

roomA2 = Room(
    'A2', None, 'A1', 'Exit', 'B2',
    {'dn':None, 'dw':None, 'de':GreenKey(), 'ds':None},
    [Plant(), Plant(), Book()], e_info='Exit'
    )

roomB1 = Room(
    'B1', 'A1', None, None, None,
    {'dn':'code:'+code, 'dw':None, 'de':None, 'ds':None},
    [Book(), Table(Note('code: '+code)), Plant(), Bed()]
    )

roomB2 = Room(
    'B2', 'A2', None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Book(GreenKey())]
    )

rooms = {
    'A1':roomA1, 'A2':roomA2,
    'B1':roomB1, 'B2':roomB2
}

room = roomB1

def showMap(room):
    print('┏━━━━━━━━━┳━━━━━━━━━┓')
    print('┃         ┃         ┃')
    print('┃    '+('X' if room.name == 'A1' else ' ')+'         '+('X' if room.name == 'A2' else ' ')+'      ➡ EXIT ➡')
    print('┃         ┃         ┃')
    print('┣━━━   ━━━╋━━━   ━━━┫')
    print('┃         ┃         ┃')
    print('┃    '+('X' if room.name == 'B1' else ' ')+'    ┃    '+('X' if room.name == 'B2' else ' ')+'    ┃')
    print('┃         ┃         ┃')
    print('┗━━━━━━━━━┻━━━━━━━━━┛')
    input('\nContinue...')