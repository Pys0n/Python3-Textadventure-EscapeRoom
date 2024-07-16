from random import randint
from objects import *
from items import *
from room import *

code1 = str(randint(1000,9999))
code2 = str(randint(1000,9999))
code3 = str(randint(1000,9999))

roomA1 = Room(
    'A1', None, None, 'A2', 'B1',
    {'dn':None, 'dw':None, 'de':'code:'+code1, 'ds':None},
    [Window(), Socket(), Painting(), Painting(),
        Plant()]
    )

roomA2 = Room(
    'A2', None, 'A1', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Bookpile(WhiteKeycard()), Table(), Chair(), Socket(),
        Plant(), Plant()]
    )

roomA3 = Room(
    'A3', 'Exit', None, None, 'B3',
    {'dn':WhiteKeycard(), 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant()]
    )

roomA4 = Room(
    'A4', None, None, 'B4', 'A5',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Paper(Note('Code: '+code1)), Paper(), Chair(), Table(),
        Window(), Plant(), Plant(), Socket()]
    )

roomA5 = Room(
    'A5', None, 'A4', None, 'B5',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Toilet()]
    )

roomB1 = Room(
    'B1', 'A1', None, 'B2', 'C1',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Mobile(MobileMessage('Hallo Eric,\n der Code für die 2. Tür ist:\n'+code2)),
        Shelf(), Plant(), Plant(), Socket()]
    )

roomB2 = Room(
    'B2', None, 'B1', 'B3', None,
    {'dn':None, 'dw':None, 'de':YellowKeycard(), 'ds':None},
    [Plant(YellowKeycard()), Plant()]
    )

roomB3 = Room(
    'B3', 'A3', 'B2', 'B4', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting()]
    )

roomB4 = Room(
    'B4', 'A4', 'B3', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Table(), Chair(), Mobile(), Notebook(),
        Plant(), Plant()]
    )

roomB5 = Room(
    'B5', 'A5', None, None, 'C5',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(GreenKeycard()), Socket(), Socket(), Plant()]
    )

roomC1 = Room(
    'C1', 'B1', None, 'C2', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
        Socket(), Window()]
    )

roomC2 = Room(
    'C2', None, 'C1', 'C3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Book(), Book(), Book(), Book(),
        Bookpile(), Bookpile(), Secret(SecretText('Schön dich zu sehen!!!')), Paper(),
        Paper(), Pen(), Table(), Chair(),
        Chair(), Shelf(), Shelf(), Mobile()]
    )

roomC3 = Room(
    'C3', None, 'C2', 'C4', 'D3',
    {'dn':None, 'dw':None, 'de':None, 'ds':GreenKeycard()},
    [Socket(), Socket(), Shelf()]
    )

roomC4 = Room(
    'C4', None, 'C3', 'C5', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Table(), Chair(), Chair(),
        Plant()]
    )

roomC5 = Room(
    'C5', 'B5', 'C4', None, 'D5',
    {'dn':'code:'+code2, 'dw':None, 'de':None, 'ds':BlueKeycard()},
    [Mobile(), Window(), Plant(), Plant(),
        Socket(), Table(), Chair()]
    )

roomD1 = Room(
    'D1', None, None, 'D2', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(BlueKeycard()), Plant(), Plant(), Plant(),
        Socket()]
    )

roomD2 = Room(
    'D2', None, 'D1', 'D3', None,
    {'dn':None, 'dw':'code:'+code3, 'de':None, 'ds':None},
    [Fridge(), Table(), Chair(), Chair(),
    Chair(), Chair(), Chair(), Chair()]
    )

roomD3 = Room(
    'D3', 'C3', 'D2', 'D4', 'E3',
    {'dn':GreenKeycard(), 'dw':None, 'de':None, 'ds':RedKeycard()},
    [Plant(), Plant(), Plant(), Plant(),
        Socket()]
    )

roomD4 = Room(
    'D4', None, 'D3', 'D5', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
        Socket()]
    )

roomD5 = Room(
    'D5', 'C5', 'D4', None, None,
    {'dn':BlueKeycard(), 'dw':None, 'de':None, 'ds':None},
    [Book(), Book(), Book(Note('Code: '+code3)), Book(),
        Bookpile(), Bookpile(), Shelf(), Shelf()]
    )

roomE1 = Room(
    'E1', None, None, 'E2', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Bed(), Bed(), Table(), Chair(),
        Shelf(), Shelf(), Wardrobe(), Plant()]
    )

roomE2 = Room(
    'E2', None, 'E1', 'E3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Table(RedKeycard()), Shelf(),
        Shelf(), Socket(), Chair(), Chair()]
    )

roomE3 = Room(
    'E3', 'D3', 'E2', 'E4', None,
    {'dn':RedKeycard(), 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
        Window(), Window()]
    )

roomE4 = Room(
    'E4', None, 'E3', 'E5', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
        Shelf(), Shelf(), Shelf(), Socket()]
    )

roomE5 = Room(
    'E5', None, 'E4', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
        Shelf(), Socket()]
    )

rooms = {
    'A1':roomA1, 'A2':roomA2, 'A3':roomA3, 'A4':roomA4, 'A5':roomA5,
    'B1':roomB1, 'B2':roomB2, 'B3':roomB3, 'B4':roomB4, 'B5':roomB5,
    'C1':roomC1, 'C2':roomC2, 'C3':roomC3, 'C4':roomC4, 'C5':roomC5,
    'D1':roomD1, 'D2':roomD2, 'D3':roomD3, 'D4':roomD4, 'D5':roomD5,
    'E1':roomE1, 'E2':roomE2, 'E3':roomE3, 'E4':roomE4, 'E5':roomE5
}

room = roomE5