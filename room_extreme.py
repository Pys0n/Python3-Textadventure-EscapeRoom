from random import randint
from objects import *
from items import *
from room import *

code = str(randint(1000,9999))

roomA1 = Room(
    'A1', False, False, True, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomA2 = Room(
    'A2', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomA3 = Room(
    'A3', True, False, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomA4 = Room(
    'A4', False, False, True, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomA5 = Room(
    'A5', False, True, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomA6 = Room(
    'A5', False, True, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomA7 = Room(
    'A5', False, True, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomB1 = Room(
    'B1', True, False, True, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomB2 = Room(
    'B2', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomB3 = Room(
    'B3', True, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomB4 = Room(
    'B4', True, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomB5 = Room(
    'B5', False, False, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomB6 = Room(
    'B5', False, False, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomB7 = Room(
    'B5', False, False, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomC1 = Room(
    'C1', True, False, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomC2 = Room(
    'C2', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomC3 = Room(
    'C3', False, True, True, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomC4 = Room(
    'C4', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomC5 = Room(
    'C5', True, True, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomC6 = Room(
    'C5', True, True, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomC7 = Room(
    'C5', True, True, False, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomD1 = Room(
    'D1', False, False, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomD2 = Room(
    'D2', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomD3 = Room(
    'D3', True, True, True, True,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomD4 = Room(
    'D4', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomD5 = Room(
    'D5', True, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomD6 = Room(
    'D5', True, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomD7 = Room(
    'D5', True, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomE1 = Room(
    'E1', False, False, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomE2 = Room(
    'E2', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomE3 = Room(
    'E3', True, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomE4 = Room(
    'E4', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomE5 = Room(
    'E5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomE6 = Room(
    'E5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomE7 = Room(
    'E5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomF1 = Room(
    'F1', False, False, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomF2 = Room(
    'F2', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomF3 = Room(
    'F3', True, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomF4 = Room(
    'F4', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomF5 = Room(
    'F5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomF6 = Room(
    'F5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomF7 = Room(
    'F5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomG1 = Room(
    'G1', False, False, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomG2 = Room(
    'G2', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomG3 = Room(
    'G3', True, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomG4 = Room(
    'G4', False, True, True, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomG5 = Room(
    'G5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomG6 = Room(
    'G5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
    )

roomG7 = Room(
    'G5', False, True, False, False,
    None, None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    []
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