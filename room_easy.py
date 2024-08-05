from random import randint
from objects import *
from items import *
from room import *

code = str(randint(1000,9999))

roomA1 = Room(
    'A1', None, None, None, 'B1',
    {'dn':None, 'dw':None, 'de':None, 'ds':GreenKey()},
    [Paper(Note('more Projects: github.com/Pys0n/')),
        Secret(SecretText('Carry on!')),
        Paper(Note('Developer: Pys0n (Jason Krüger)'))]
    )

roomA2 = Room(
    'A2', None, None, None, 'B2',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Table(GoldenKey()), Plant(), Socket()]
    )

roomA3 = Room(
    'A3', None, None, None, 'B3',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(GreenKey()), Plant(), Painting(), Chair()]
    )

roomB1 = Room(
    'B1', 'A1', None, 'B2', 'C1',
    {'dn':GreenKey(), 'dw':None, 'de':'code:'+code, 'ds':None},
    [Plant(), Plant(), Plant(), Plant()]
    )

roomB2 = Room(
    'B2', 'A2', 'B1', 'B3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Table(), Chair(), Chair(), Chair(),
        Chair()]
    )

roomB3 = Room(
    'B3', 'A3', 'B2', 'Exit', None,
    {'dn':None, 'dw':None, 'de':GoldenKey(), 'ds':None},
    [Plant(), Plant(), Socket(), Painting(),
        Painting()], e_info='Exit'
    )

roomC1 = Room(
    'C1', 'B1', None, 'C2', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Socket()]
    )

roomC2 = Room(
    'C2', None, 'C1', 'C3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
        Window()]
    )

roomC3 = Room(
    'C3', None, 'C2', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Mobile(MobileMessage('Der Code lautet:\n\n\t'+code)),
        Window(), Window(), Painting(), Socket()]
    )

rooms = {
    'A1':roomA1, 'A2':roomA2, 'A3':roomA3,
    'B1':roomB1, 'B2':roomB2, 'B3':roomB3,
    'C1':roomC1, 'C2':roomC2, 'C3':roomC3
}

room = roomC3

def showMap():
    print()
    input('\nContinue...')