from random import randint
from objects import *
from items import *
from room import *

code = str(randint(1000,9999))

roomA1 = Room(
    'A1', None, None, 'A2', 'B1',
    {'dn':None, 'dw':None, 'de':RedKeycard(), 'ds':None},
    [Plant(), Plant(), Socket(), Table(),
     Paper(), Pen(), Bookpile(), Book(),
     Window(), Window(), Chair(), Rubbishbin()]
    )

roomA2 = Room(
    'A2', None, 'A1', 'A3', None,
    {'dn':None, 'dw':RedKeycard(), 'de':None, 'ds':None},
    [Table(), Chair(), Chair(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Window(),
     Painting(), Rubbishbin()]
    )

roomA3 = Room(
    'A3', None, 'A2', 'A4', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomA4 = Room(
    'A4', None, 'A3', 'A5', 'B4',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Plant(), Plant(), Plant(),
     Plant(), Socket(), Socket()]
    )

roomA5 = Room(
    'A5', None, 'A4', 'A6', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomA6 = Room(
    'A6', None, 'A5', 'A7', None,
    {'dn':None, 'dw':None, 'de':BlueKeycard(), 'ds':None},
    [Window(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomA7 = Room(
    'A7', None, 'A6', None, 'B7',
    {'dn':None, 'dw':BlueKeycard(), 'de':None, 'ds':None},
    [Window(), Window(), Plant(), Socket(),
     Socket(), Rubbishbin()]
    )

roomB1 = Room(
    'B1', 'A1', None, None, 'C1',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomB2 = Room(
    'B2', None, None, 'B3', 'C2',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Socket(), Table(),
     Paper(), Pen(), Bookpile(), Book(),
     Window(), Window(), Chair(), Rubbishbin()]
    )

roomB3 = Room(
    'B3', None, 'B2', 'B4', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomB4 = Room(
    'B4', 'A4', 'B3', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
     Socket(), Socket(), Painting()]
    )

roomB5 = Room(
    'B5', None, None, 'B6', 'C5',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Table(Note('I almost got it, the third digit\nwas '+code[2]+' or '+str(int(code)+10)[2]+'!')),
     Chair(), Socket(), Socket(), Notebook(),
     Mobile(), Diary(), Pen()]
    )

roomB6 = Room(
    'B6', None, 'B5', 'B7', 'C6',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
     Painting()]
    )

roomB7 = Room(
    'B7', 'A7', 'B6', None, 'C7',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
     Painting()]
    )

roomC1 = Room(
    'C1', 'B1', None, None, 'D1',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
     Painting(), Window()]
    )

roomC2 = Room(
    'C2', 'B2', None, 'C3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Socket(), Table(),
     Paper(), Pen(), Bookpile(), Book(),
     Window(), Window(), Chair(), Rubbishbin()]
    )

roomC3 = Room(
    'C3', None, 'C2', 'C4', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomC4 = Room(
    'C4', None, 'C3', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(RedKeycard()), Plant(), Plant(),
     Socket()]
    )

roomC5 = Room(
    'C5', 'B5', None, 'C6', 'D5',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Socket(), Socket(), Plant(),
     Plant()]
    )

roomC6 = Room(
    'C6', 'B6', 'C5', 'C7', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Socket(), Socket(), Plant(),
     Plant()]
    )

roomC7 = Room(
    'C7', 'B7', 'C6', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Painting(), Socket(), Plant(),
     Plant()]
    )

roomD1 = Room(
    'D1', 'C1', None, None, 'E1',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
     Painting(), Window()]
    )

roomD2 = Room(
    'D2', None, None, 'D3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Book(), Book(), Book(), Book(),
     Diary(DiaryEntry('The code...\nWhat is it again?\nBut I know that it starts with:\n '+code[1]+code[0]+' or the other way around.')),
     Bookpile(), Bookpile(), Shelf(), Shelf(),
     Shelf(), Table(), Chair(), Pen(),
     Paper()]
    )

roomD3 = Room(
    'D3', None, 'D2', 'D4', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomD4 = Room(
    'D4', None, 'D3', 'D5', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomD5 = Room(
    'D5', 'C5', 'D4', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(), Socket(), Plant(),
     Plant(BlueKeycard())]
    )

roomD6 = Room(
    'D6', None, None, 'D7', 'E6',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(), Socket(), Plant(),
     Plant()]
    )

roomD7 = Room(
    'D7', None, 'D6', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Painting(), Plant(), Plant(),
     Socket(YellowKeycard())]
    )

roomE1 = Room(
    'E1', 'D1', None, 'E2', 'F1',
    {'dn':None, 'dw':None, 'de':None, 'ds':WhiteKeycard()},
    [Window(), Plant(), Plant(), Socket(),
     Paper(), Paper()]
    )

roomE2 = Room(
    'E2', None, 'E1', 'E3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Shelf(), Socket(), Plant(),
     Plant(), Bookpile(), Book(), Book()]
    )

roomE3 = Room(
    'E3', None, 'E2', 'E4', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Table(), Chair(), Socket(), Socket(),
     Mobile(MobileMessage('You asked me about the 4th digit of the code!?\nIt should be '+code[3]+'.\n\nJohanna')),
     Notebook()]
    )

roomE4 = Room(
    'E4', None, 'E3', 'E5', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(), Socket(), Plant(),
     Plant()]
    )

roomE5 = Room(
    'E5', None, 'E4', 'E6', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(), Socket(), Plant(),
     Plant()]
    )

roomE6 = Room(
    'E6', 'D6', 'E5', 'E7', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Table(), Chair(), Chair(), Pen(),
     Paper(), Pen(), Paper(), Book(),
     Book()]
    )

roomE7 = Room(
    'E7', None, 'E6', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Shelf(), Bed(WhiteKeycard()),
     Bed(), Shelf(), Plant(), Plant()]
    )

roomF1 = Room(
    'F1', 'E1', None, None, 'G1',
    {'dn':WhiteKeycard(), 'dw':None, 'de':None, 'ds':YellowKeycard()},
    [Window(), Plant(), Plant(), Socket(),
     Paper(), Paper()]
    )

roomF2 = Room(
    'F2', None, None, None, 'G2',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Shelf(), Shelf(), Shelf(), Shelf(),
     Shelf(), Shelf(), Shelf(), Shelf(),
     Socket(), Socket()]
    )

roomF3 = Room(
    'F3', None, None, 'F4', 'G3',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(), Plant(), Socket(),
     Socket()]
    )

roomF4 = Room(
    'F4', None, 'F3', 'F5', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomF5 = Room(
    'F5', None, 'F4', 'F6', None,
    {'dn':None, 'dw':None, 'de':'code:'+code, 'ds':None},
    [Painting(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomF6 = Room(
    'F6', None, 'F5', 'F7', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomF7 = Room(
    'F7', None, 'F6', None, 'G7',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Window(), Plant(), Socket(),
     Socket()]
    )

roomG1 = Room(
    'G1', 'F1', None, 'G2', None,
    {'dn':YellowKeycard(), 'dw':None, 'de':None, 'ds':None},
    [Window(), Window(), Plant(), Socket(),
     Socket()]
    )

roomG2 = Room(
    'G2', 'F2', 'G1', 'G3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Painting(), Window(), Plant(), Socket(),
     Socket()]
    )

roomG3 = Room(
    'G3', 'F3', 'G2', 'G4', None,
    {'dn':None, 'dw':None, 'de':GoldenKey(), 'ds':None},
    [Painting(), Window(), Plant(), Socket(),
     Socket()]
    )

roomG4 = Room(
    'G4', None, 'G3', 'G5', None,
    {'dn':None, 'dw':GoldenKey(), 'de':'code:'+code, 'ds':None},
    [Plant(), Plant()]
    )

roomG5 = Room(
    'G5', None, 'G4', 'G6', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant()]
    )

roomG6 = Room(
    'G6', None, 'G5', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Table(), Chair(), Secret(SecretText('That was hard!\nBut it gets even harder!'))]
    )

roomG7 = Room(
    'G7', 'F7', None, None, 'Exit',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(GoldenKey()), Plant(), Plant(), Plant(),
     Plant(), Socket()]
    )

rooms = {
    'A1':roomA1, 'A2':roomA2, 'A3':roomA3, 'A4':roomA4, 'A5':roomA5, 'A6':roomA6, 'A7':roomA7,
    'B1':roomB1, 'B2':roomB2, 'B3':roomB3, 'B4':roomB4, 'B5':roomB5, 'B6':roomB6, 'B7':roomB7,
    'C1':roomC1, 'C2':roomC2, 'C3':roomC3, 'C4':roomC4, 'C5':roomC5, 'C6':roomC6, 'C7':roomC7,
    'D1':roomD1, 'D2':roomD2, 'D3':roomD3, 'D4':roomD4, 'D5':roomD5, 'D6':roomD6, 'D7':roomD7,
    'E1':roomE1, 'E2':roomE2, 'E3':roomE3, 'E4':roomE4, 'E5':roomE5, 'E6':roomE6, 'E7':roomE7,
    'F1':roomF1, 'F2':roomF2, 'F3':roomF3, 'F4':roomF4, 'F5':roomF5, 'F6':roomF6, 'F7':roomF7,
    'G1':roomG1, 'G2':roomG2, 'G3':roomG3, 'G4':roomG4, 'G5':roomG5, 'G6':roomG6, 'G7':roomG7
}

room = roomA7