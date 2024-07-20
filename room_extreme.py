from random import randint
from objects import *
from items import *
from room import *

from keys_extreme import *

###########################################################################################################################################
###############################################################    A100    ################################################################
###########################################################################################################################################

############################################################### A101 - A102 ###############################################################
roomA101LI = Room(
    'A101 - Living room',
    None, 'A101BA', 'A100.01', 'A101KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA101BE = Room(
    'A101 - Bedroom',
    None, None, 'A101KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA101BA = Room(
    'A101 - Bathroom',
    None, None, 'A101LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA101KI = Room(
    'A101 - Kitchen',
    'A101LI', 'A101BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_01 = Room(
    'A100.01 - Corridor',
    None, 'A101LI', 'A102LI', 'A100.02',
    {'dn':None, 'dw':KeyA101(), 'de':KeyA102(), 'ds':None},
    [Plant(), Plant(), Window(), Carpet(CarpetText('A101')), Carpet(CarpetText('A102'))]
    )

roomA100_02 = Room(
    'A100.02 - Corridor',
    'A100.01', None, None, 'A100.03',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA102LI = Room(
    'A102 - Living room',
    None, 'A100.01', 'A102BA', 'A102KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA102BE = Room(
    'A102 - Bedroom',
    None, 'A102KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA102BA = Room(
    'A102 - Bathroom',
    None, 'A102LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA102KI = Room(
    'A102 - Kitchen',
    'A102LI', None, 'A102BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A103 - A104 ###############################################################
roomA103LI = Room(
    'A103 - Living room',
    None, 'A103BA', 'A100.03', 'A103KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA103BE = Room(
    'A103 - Bedroom',
    None, None, 'A103KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA103BA = Room(
    'A103 - Bathroom',
    None, None, 'A103LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA103KI = Room(
    'A103 - Kitchen',
    'A103LI', 'A103BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_03 = Room(
    'A100.03 - Corridor',
    'A100.02', 'A103LI', 'A104LI', 'A100.04',
    {'dn':None, 'dw':KeyA103(), 'de':KeyA104(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A103')), Carpet(CarpetText('A104'))]
    )

roomA100_04 = Room(
    'A100.04 - Corridor',
    'A100.03', None, None, 'A100.05',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA104LI = Room(
    'A104 - Living room',
    None, 'A100.03', 'A104BA', 'A104KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA104BE = Room(
    'A104 - Bedroom',
    None, 'A104KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA104BA = Room(
    'A104 - Bathroom',
    None, 'A104LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA104KI = Room(
    'A104 - Kitchen',
    'A104LI', None, 'A104BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A105 - A106 ###############################################################
roomA105LI = Room(
    'A105 - Living room',
    None, 'A105BA', 'A100.05', 'A105KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA105BE = Room(
    'A105 - Bedroom',
    None, None, 'A105KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA105BA = Room(
    'A105 - Bathroom',
    None, None, 'A105LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA105KI = Room(
    'A105 - Kitchen',
    'A105LI', 'A105BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_05 = Room(
    'A100.05 - Corridor',
    'A100.04', 'A105LI', 'A106LI', 'A100.06',
    {'dn':None, 'dw':KeyA105(), 'de':KeyA106(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A105')), Carpet(CarpetText('A106'))]
    )

roomA100_06 = Room(
    'A100.06 - Corridor',
    'A100.05', None, None, 'A100.07',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA106LI = Room(
    'A106 - Living room',
    None, 'A100.05', 'A106BA', 'A106KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA106BE = Room(
    'A106 - Bedroom',
    None, 'A106KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA106BA = Room(
    'A106 - Bathroom',
    None, 'A106LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA106KI = Room(
    'A106 - Kitchen',
    'A106LI', None, 'A106BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A107 - A108 ###############################################################
roomA107LI = Room(
    'A107 - Living room',
    None, 'A107BA', 'A100.07', 'A107KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA107BE = Room(
    'A107 - Bedroom',
    None, None, 'A107KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA107BA = Room(
    'A107 - Bathroom',
    None, None, 'A107LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA107KI = Room(
    'A107 - Kitchen',
    'A107LI', 'A107BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_07 = Room(
    'A100.07 - Corridor',
    'A100.06', 'A107LI', 'A108LI', 'A100.08',
    {'dn':None, 'dw':KeyA107(), 'de':KeyA108(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A107')), Carpet(CarpetText('A108'))]
    )

roomA100_08 = Room(
    'A100.08 - Corridor',
    'A100.07', None, None, 'A100.09',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA108LI = Room(
    'A108 - Living room',
    None, 'A100.07', 'A108BA', 'A108KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA108BE = Room(
    'A108 - Bedroom',
    None, 'A108KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA108BA = Room(
    'A108 - Bathroom',
    None, 'A108LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA108KI = Room(
    'A108 - Kitchen',
    'A108LI', None, 'A108BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A109 - A110 ###############################################################
roomA109LI = Room(
    'A109 - Living room',
    None, 'A109BA', 'A100.09', 'A109KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA109BE = Room(
    'A109 - Bedroom',
    None, None, 'A109KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA109BA = Room(
    'A109 - Bathroom',
    None, None, 'A109LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA109KI = Room(
    'A109 - Kitchen',
    'A109LI', 'A109BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_09 = Room(
    'A100.09 - Corridor',
    'A100.08', 'A109LI', 'A110LI', 'A100.10',
    {'dn':None, 'dw':KeyA109(), 'de':KeyA110(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A109')), Carpet(CarpetText('A110'))]
    )

roomA100_10 = Room(
    'A100.10 - Corridor',
    'A100.09', None, None, 'A100.11',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA110LI = Room(
    'A110 - Living room',
    None, 'A100.09', 'A110BA', 'A110KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA110BE = Room(
    'A110 - Bedroom',
    None, 'A110KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA110BA = Room(
    'A110 - Bathroom',
    None, 'A110LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA110KI = Room(
    'A110 - Kitchen',
    'A110LI', None, 'A110BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A100 - Storage room ###############################################################

roomA100_11 = Room(
    'A100.11 - Corridor',
    'A100.10', 'A100SR', 'A100.11.1', 'A100.12',
    {'dn':None, 'dw':KeySRA100(), 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA100_11_1 = Room(
    'A100.11.1 - Corridor',
    None, 'A100.11', 'A100.11.2', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA100_11_2 = Room(
    'A100.11.2 - Corridor',
    None, 'A100.11.1', 'M100.1', None,                               ########################### Mittelweg
    {'dn':None, 'dw':None, 'de':KeySecurityDoorA100(), 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA100SR = Room(
    'A100 - Storage room',
    None, None, 'A100.11', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     Carton(), Carton(), Carton(), Carton(),
     Carton(), Carton(), Carton(), Carton()]
    )

############################################################### A111 - A112 ###############################################################
roomA111LI = Room(
    'A111 - Living room',
    None, 'A111BA', 'A100.12', 'A111KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA111BE = Room(
    'A111 - Bedroom',
    None, None, 'A111KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA111BA = Room(
    'A111 - Bathroom',
    None, None, 'A111LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA111KI = Room(
    'A111 - Kitchen',
    'A111LI', 'A111BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_12 = Room(
    'A100.12 - Corridor',
    'A100.11', 'A111LI', 'A112LI', 'A100.13',
    {'dn':None, 'dw':KeyA111(), 'de':KeyA112(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A111')), Carpet(CarpetText('A112'))]
    )

roomA100_13 = Room(
    'A100.13 - Corridor',
    'A100.12', None, None, 'A100.14',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA112LI = Room(
    'A112 - Living room',
    None, 'A100.12', 'A112BA', 'A112KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA112BE = Room(
    'A112 - Bedroom',
    None, 'A112KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA112BA = Room(
    'A112 - Bathroom',
    None, 'A112LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA112KI = Room(
    'A112 - Kitchen',
    'A112LI', None, 'A112BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A113 - A114 ###############################################################
roomA113LI = Room(
    'A113 - Living room',
    None, 'A113BA', 'A100.14', 'A113KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA113BE = Room(
    'A113 - Bedroom',
    None, None, 'A113KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA113BA = Room(
    'A113 - Bathroom',
    None, None, 'A113LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA113KI = Room(
    'A113 - Kitchen',
    'A113LI', 'A113BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_14 = Room(
    'A100.14 - Corridor',
    'A100.13', 'A113LI', 'A114LI', 'A100.15',
    {'dn':None, 'dw':KeyA113(), 'de':KeyA114(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A113')), Carpet(CarpetText('A114'))]
    )

roomA100_15 = Room(
    'A100.15 - Corridor',
    'A100.14', None, None, 'A100.16',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA114LI = Room(
    'A114 - Living room',
    None, 'A100.14', 'A114BA', 'A114KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA114BE = Room(
    'A114 - Bedroom',
    None, 'A114KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA114BA = Room(
    'A114 - Bathroom',
    None, 'A114LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA114KI = Room(
    'A114 - Kitchen',
    'A114LI', None, 'A114BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A115 - A116 ###############################################################
roomA115LI = Room(
    'A115 - Living room',
    None, 'A115BA', 'A100.16', 'A115KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA115BE = Room(
    'A115 - Bedroom',
    None, None, 'A115KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA115BA = Room(
    'A115 - Bathroom',
    None, None, 'A115LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA115KI = Room(
    'A115 - Kitchen',
    'A115LI', 'A115BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_16 = Room(
    'A100.16 - Corridor',
    'A100.15', 'A115LI', 'A116LI', 'A100.17',
    {'dn':None, 'dw':KeyA115(), 'de':KeyA116(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A115')), Carpet(CarpetText('A116'))]
    )

roomA100_17 = Room(
    'A100.17 - Corridor',
    'A100.16', None, None, 'A100.18',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA116LI = Room(
    'A116 - Living room',
    None, 'A100.16', 'A116BA', 'A116KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA116BE = Room(
    'A116 - Bedroom',
    None, 'A116KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA116BA = Room(
    'A116 - Bathroom',
    None, 'A116LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA116KI = Room(
    'A116 - Kitchen',
    'A116LI', None, 'A116BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A117 - A118 ###############################################################
roomA117LI = Room(
    'A117 - Living room',
    None, 'A117BA', 'A100.18', 'A117KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA117BE = Room(
    'A117 - Bedroom',
    None, None, 'A117KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA117BA = Room(
    'A117 - Bathroom',
    None, None, 'A117LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA117KI = Room(
    'A117 - Kitchen',
    'A117LI', 'A117BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_18 = Room(
    'A100.18 - Corridor',
    'A100.17', 'A117LI', 'A118LI', 'A100.19',
    {'dn':None, 'dw':KeyA117(), 'de':KeyA118(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A117')), Carpet(CarpetText('A118'))]
    )

roomA100_19 = Room(
    'A100.19 - Corridor',
    'A100.18', None, None, 'A100.20',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA118LI = Room(
    'A118 - Living room',
    None, 'A100.18', 'A118BA', 'A118KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA118BE = Room(
    'A118 - Bedroom',
    None, 'A118KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA118BA = Room(
    'A118 - Bathroom',
    None, 'A118LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA118KI = Room(
    'A118 - Kitchen',
    'A118LI', None, 'A118BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A119 - A120 ###############################################################
roomA119LI = Room(
    'A119 - Living room',
    None, 'A119BA', 'A100.20', 'A119KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA119BE = Room(
    'A119 - Bedroom',
    None, None, 'A119KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA119BA = Room(
    'A119 - Bathroom',
    None, None, 'A119LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA119KI = Room(
    'A119 - Kitchen',
    'A119LI', 'A119BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA100_20 = Room(
    'A100.20 - Corridor',
    'A100.19', 'A119LI', 'A120LI', 'A100.21',
    {'dn':None, 'dw':KeyA119(), 'de':KeyA120(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A119')), Carpet(CarpetText('A120'))]
    )

roomA100_21 = Room(
    'A100.21 - Corridor',
    'A100.20', None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Window(), Painting(), Painting()]
    )

roomA120LI = Room(
    'A120 - Living room',
    None, 'A100.20', 'A120BA', 'A120KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA120BE = Room(
    'A120 - Bedroom',
    None, 'A120KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA120BA = Room(
    'A120 - Bathroom',
    None, 'A120LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA120KI = Room(
    'A120 - Kitchen',
    'A120LI', None, 'A120BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

###########################################################################################################################################
###############################################################    B100    ################################################################
###########################################################################################################################################



############################################################### A101 - A102 ###############################################################
roomB101LI = Room(
    'B101 - Living room',
    None, 'B101BA', 'B100.01', 'B101KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB101BE = Room(
    'B101 - Bedroom',
    None, None, 'B101KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB101BA = Room(
    'B101 - Bathroom',
    None, None, 'B101LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB101KI = Room(
    'B101 - Kitchen',
    'B101LI', 'B101BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_01 = Room(
    'B100.01 - Corridor',
    None, 'B101LI', 'B102LI', 'B100.02',
    {'dn':None, 'dw':KeyB101(), 'de':KeyB102(), 'ds':None},
    [Plant(), Plant(), Window(), Carpet(CarpetText('B101')), Carpet(CarpetText('B102'))]
    )

roomB100_02 = Room(
    'B100.02 - Corridor',
    'B100.01', None, None, 'B100.03',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB102LI = Room(
    'B102 - Living room',
    None, 'B100.01', 'B102BA', 'B102KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB102BE = Room(
    'B102 - Bedroom',
    None, 'B102KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB102BA = Room(
    'B102 - Bathroom',
    None, 'B102LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB102KI = Room(
    'B102 - Kitchen',
    'B102LI', None, 'B102BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B103 - B104 ###############################################################
roomB103LI = Room(
    'B103 - Living room',
    None, 'B103BA', 'B100.03', 'B103KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB103BE = Room(
    'B103 - Bedroom',
    None, None, 'B103KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB103BA = Room(
    'B103 - Bathroom',
    None, None, 'B103LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB103KI = Room(
    'B103 - Kitchen',
    'B103LI', 'B103BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_03 = Room(
    'B100.03 - Corridor',
    'B100.02', 'B103LI', 'B104LI', 'B100.04',
    {'dn':None, 'dw':KeyB103(), 'de':KeyB104(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B103')), Carpet(CarpetText('B104'))]
    )

roomB100_04 = Room(
    'B100.04 - Corridor',
    'B100.03', None, None, 'B100.05',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB104LI = Room(
    'B104 - Living room',
    None, 'B100.03', 'B104BA', 'B104KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB104BE = Room(
    'B104 - Bedroom',
    None, 'B104KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB104BA = Room(
    'B104 - Bathroom',
    None, 'B104LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB104KI = Room(
    'B104 - Kitchen',
    'B104LI', None, 'B104BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B105 - B106 ###############################################################
roomB105LI = Room(
    'B105 - Living room',
    None, 'B105BA', 'B100.05', 'B105KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB105BE = Room(
    'B105 - Bedroom',
    None, None, 'B105KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB105BA = Room(
    'B105 - Bathroom',
    None, None, 'B105LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB105KI = Room(
    'B105 - Kitchen',
    'B105LI', 'B105BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_05 = Room(
    'B100.05 - Corridor',
    'B100.04', 'B105LI', 'B106LI', 'B100.06',
    {'dn':None, 'dw':KeyB105(), 'de':KeyB106(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B105')), Carpet(CarpetText('B106'))]
    )

roomB100_06 = Room(
    'B100.06 - Corridor',
    'B100.05', None, None, 'B100.07',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB106LI = Room(
    'B106 - Living room',
    None, 'B100.05', 'B106BA', 'B106KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB106BE = Room(
    'B106 - Bedroom',
    None, 'B106KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB106BA = Room(
    'B106 - Bathroom',
    None, 'B106LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB106KI = Room(
    'B106 - Kitchen',
    'B106LI', None, 'B106BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B107 - B108 ###############################################################
roomB107LI = Room(
    'B107 - Living room',
    None, 'B107BA', 'B100.07', 'B107KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB107BE = Room(
    'B107 - Bedroom',
    None, None, 'B107KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB107BA = Room(
    'B107 - Bathroom',
    None, None, 'B107LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB107KI = Room(
    'B107 - Kitchen',
    'B107LI', 'B107BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_07 = Room(
    'B100.07 - Corridor',
    'B100.06', 'B107LI', 'B108LI', 'B100.08',
    {'dn':None, 'dw':KeyB107(), 'de':KeyB108(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B107')), Carpet(CarpetText('B108'))]
    )

roomB100_08 = Room(
    'B100.08 - Corridor',
    'B100.07', None, None, 'B100.09',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB108LI = Room(
    'B108 - Living room',
    None, 'B100.07', 'B108BA', 'B108KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB108BE = Room(
    'B108 - Bedroom',
    None, 'B108KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB108BA = Room(
    'B108 - Bathroom',
    None, 'B108LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB108KI = Room(
    'B108 - Kitchen',
    'B108LI', None, 'B108BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B109 - B110 ###############################################################
roomB109LI = Room(
    'B109 - Living room',
    None, 'B109BA', 'B100.09', 'B109KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB109BE = Room(
    'B109 - Bedroom',
    None, None, 'B109KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB109BA = Room(
    'B109 - Bathroom',
    None, None, 'B109LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB109KI = Room(
    'B109 - Kitchen',
    'B109LI', 'B109BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_09 = Room(
    'B100.09 - Corridor',
    'B100.08', 'B109LI', 'B110LI', 'B100.10',
    {'dn':None, 'dw':KeyB109(), 'de':KeyB110(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B109')), Carpet(CarpetText('B110'))]
    )

roomB100_10 = Room(
    'B100.10 - Corridor',
    'B100.09', None, None, 'B100.11',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB110LI = Room(
    'B110 - Living room',
    None, 'B100.09', 'B110BA', 'B110KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB110BE = Room(
    'B110 - Bedroom',
    None, 'B110KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB110BA = Room(
    'B110 - Bathroom',
    None, 'B110LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB110KI = Room(
    'B110 - Kitchen',
    'B110LI', None, 'B110BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B100 - Storage room ###############################################################

roomB100_11 = Room(
    'B100.11 - Corridor',
    'B100.10', 'B100.11.1', 'B100SR', 'B100.12',
    {'dn':None, 'dw':None, 'de':KeySRB100(), 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB100_11_1 = Room(
    'B100.11.1 - Corridor',
    None, 'B100.11.2', 'B100.11', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB100_11_2 = Room(
    'B100.11.2 - Corridor',
    None, 'M100.4', 'B100.11.1', None,                               ########################### Mittelweg
    {'dn':None, 'dw':KeySecurityDoorB100(), 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB100SR = Room(
    'B100 - Storage room',
    None, 'B100.11', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     Carton(), Carton(), Carton(), Carton(),
     Carton(), Carton(), Carton(), Carton()]
    )

############################################################### B111 - B112 ###############################################################
roomB111LI = Room(
    'B111 - Living room',
    None, 'B111BA', 'B100.12', 'B111KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB111BE = Room(
    'B111 - Bedroom',
    None, None, 'B111KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB111BA = Room(
    'B111 - Bathroom',
    None, None, 'B111LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB111KI = Room(
    'B111 - Kitchen',
    'B111LI', 'B111BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_12 = Room(
    'B100.12 - Corridor',
    'B100.11', 'B111LI', 'B112LI', 'B100.13',
    {'dn':None, 'dw':KeyB111(), 'de':KeyB112(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B111')), Carpet(CarpetText('B112'))]
    )

roomB100_13 = Room(
    'B100.13 - Corridor',
    'B100.12', None, None, 'B100.14',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB112LI = Room(
    'B112 - Living room',
    None, 'B100.12', 'B112BA', 'B112KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB112BE = Room(
    'B112 - Bedroom',
    None, 'B112KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB112BA = Room(
    'B112 - Bathroom',
    None, 'B112LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB112KI = Room(
    'B112 - Kitchen',
    'B112LI', None, 'B112BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B113 - B114 ###############################################################
roomB113LI = Room(
    'B113 - Living room',
    None, 'B113BA', 'B100.14', 'B113KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB113BE = Room(
    'B113 - Bedroom',
    None, None, 'B113KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB113BA = Room(
    'B113 - Bathroom',
    None, None, 'B113LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB113KI = Room(
    'B113 - Kitchen',
    'B113LI', 'B113BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_14 = Room(
    'B100.14 - Corridor',
    'B100.13', 'B113LI', 'B114LI', 'B100.15',
    {'dn':None, 'dw':KeyB113(), 'de':KeyB114(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B113')), Carpet(CarpetText('B114'))]
    )

roomB100_15 = Room(
    'B100.15 - Corridor',
    'B100.14', None, None, 'B100.16',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB114LI = Room(
    'B114 - Living room',
    None, 'B100.14', 'B114BA', 'B114KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB114BE = Room(
    'B114 - Bedroom',
    None, 'B114KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB114BA = Room(
    'B114 - Bathroom',
    None, 'B114LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB114KI = Room(
    'B114 - Kitchen',
    'B114LI', None, 'B114BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B115 - B116 ###############################################################
roomB115LI = Room(
    'B115 - Living room',
    None, 'B115BA', 'B100.16', 'B115KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB115BE = Room(
    'B115 - Bedroom',
    None, None, 'B115KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB115BA = Room(
    'B115 - Bathroom',
    None, None, 'B115LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB115KI = Room(
    'B115 - Kitchen',
    'B115LI', 'B115BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_16 = Room(
    'B100.16 - Corridor',
    'B100.15', 'B115LI', 'B116LI', 'B100.17',
    {'dn':None, 'dw':KeyB115(), 'de':KeyB116(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B115')), Carpet(CarpetText('B116'))]
    )

roomB100_17 = Room(
    'B100.17 - Corridor',
    'B100.16', None, None, 'B100.18',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB116LI = Room(
    'B116 - Living room',
    None, 'B100.16', 'B116BA', 'B116KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB116BE = Room(
    'B116 - Bedroom',
    None, 'B116KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB116BA = Room(
    'B116 - Bathroom',
    None, 'B116LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB116KI = Room(
    'B116 - Kitchen',
    'B116LI', None, 'B116BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B117 - B118 ###############################################################
roomB117LI = Room(
    'B117 - Living room',
    None, 'B117BA', 'B100.18', 'B117KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB117BE = Room(
    'B117 - Bedroom',
    None, None, 'B117KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB117BA = Room(
    'B117 - Bathroom',
    None, None, 'B117LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB117KI = Room(
    'B117 - Kitchen',
    'B117LI', 'B117BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_18 = Room(
    'B100.18 - Corridor',
    'B100.17', 'B117LI', 'B118LI', 'B100.19',
    {'dn':None, 'dw':KeyB117(), 'de':KeyB118(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B117')), Carpet(CarpetText('B118'))]
    )

roomB100_19 = Room(
    'B100.19 - Corridor',
    'B100.18', None, None, 'B100.20',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB118LI = Room(
    'B118 - Living room',
    None, 'B100.18', 'B118BA', 'B118KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB118BE = Room(
    'B118 - Bedroom',
    None, 'B118KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB118BA = Room(
    'B118 - Bathroom',
    None, 'B118LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB118KI = Room(
    'B118 - Kitchen',
    'B118LI', None, 'B118BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B119 - B120 ###############################################################
roomB119LI = Room(
    'B119 - Living room',
    None, 'B119BA', 'B100.20', 'B119KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB119BE = Room(
    'B119 - Bedroom',
    None, None, 'B119KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB119BA = Room(
    'B119 - Bathroom',
    None, None, 'B119LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB119KI = Room(
    'B119 - Kitchen',
    'B119LI', 'B119BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB100_20 = Room(
    'B100.20 - Corridor',
    'B100.19', 'B119LI', 'B120LI', 'B100.21',
    {'dn':None, 'dw':KeyB119(), 'de':KeyB120(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B119')), Carpet(CarpetText('B120'))]
    )

roomB100_21 = Room(
    'B100.21 - Corridor',
    'B100.20', None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Window(), Painting(), Painting()]
    )

roomB120LI = Room(
    'B120 - Living room',
    None, 'B100.20', 'B120BA', 'B120KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB120BE = Room(
    'B120 - Bedroom',
    None, 'B120KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB120BA = Room(
    'B120 - Bathroom',
    None, 'B120LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB120KI = Room(
    'B120 - Kitchen',
    'B120LI', None, 'B120BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

###########################################################################################################################################
###############################################################    M100    ################################################################
###########################################################################################################################################

roomM100_1 = Room(
    'M100.1 - Corridor',
    None, 'A100.11.2', 'M100.2', None,
    {'dn':None, 'dw':KeySecurityDoorA100(), 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM100_2 = Room(
    'M100.2 - Corridor',
    None, 'M100.1', 'M100.3', 'RM100',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM100_3 = Room(
    'M100.3 - Corridor',
    'M200.3', 'M100.2', 'M100.4', 'RM100',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM100_4 = Room(
    'M100.4 - Corridor',
    None, 'M100.3', 'B100.11.2', None,
    {'dn':None, 'dw':None, 'de':KeySecurityDoorB100(), 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomRM100 = Room(
    'M100 - Reception',
    'M100.2', 'KBM100.1', 'KBM100.2', 'Exit',
    {'dn':None, 'dw':None, 'de':None, 'ds':KeyEntrence()},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting(), Painting(), Painting(),
    Painting(), PC(Note('Can you pack a present for Maik with the spare entrence key, thanks.\n\n(If you want to know more about the party you should go to Peter (B203) or Marc (B305))')), Chair(), Rubbishbin(),
    Bar(Note('Would you like to come to my birthday party on August 3rd?\nPlease let me know by tomorrow.\n\n\t\t- Maik')), 
    KeyHook(KeySecurityDoorA100()), KeyHook(KeySecurityDoorA200()), KeyHook(),
    KeyHook(KeySecurityDoorB100()), KeyHook(KeySecurityDoorB200()), KeyHook(KeySecurityDoorB300())]
    )

roomKBM100_1 = Room(
    'M100 - Key bearing 1',
    None, None, 'RM100', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [KeyHook(KeyA101()), KeyHook(KeyA102()), KeyHook(KeyA103()), KeyHook(KeyA104()), KeyHook(KeyA105()),
     KeyHook(),          KeyHook(KeyA107()), KeyHook(KeyA108()), KeyHook(KeyA109()), KeyHook(KeyA110()),
     KeyHook(KeyA111()), KeyHook(KeyA112()), KeyHook(KeyA113()), KeyHook(KeyA114()), KeyHook(KeyA115()),
     KeyHook(KeyA116()), KeyHook(KeyA117()), KeyHook(KeyA118()), KeyHook(),          KeyHook(KeyA120()),
     KeyHook(KeyA201()), KeyHook(KeyA202()), KeyHook(KeyA203()), KeyHook(KeyA204()), KeyHook(KeyA205()),
     KeyHook(KeyA206()), KeyHook(),          KeyHook(KeyA208()), KeyHook(KeyA209()), KeyHook(KeyA210()),
     KeyHook(KeyA211()), KeyHook(KeyA212()), KeyHook(KeyA213()), KeyHook(KeyA214()), KeyHook(KeyA215()),
     KeyHook(KeyA216()), KeyHook(KeyA217()), KeyHook(KeyA218()), KeyHook(KeyA219()), KeyHook(KeyA220()),
     KeyHook(KeyA301()), KeyHook(KeyA302()), KeyHook(),          KeyHook(KeyA304()), KeyHook(KeyA305()),
     KeyHook(),          KeyHook(KeyA307()), KeyHook(),          KeyHook(KeyA309()), KeyHook(KeyA310()),
     KeyHook(KeyA311()), KeyHook(KeyA312()), KeyHook(KeyA313()), KeyHook(KeyA314()), KeyHook(KeyA315()),
     KeyHook(KeyA316()), KeyHook(KeyA317()), KeyHook(),          KeyHook(KeyA319()), KeyHook(KeyA320())]
    )

roomKBM100_2 = Room(
    'M100 - Key bearing 2',
    None, 'RM100', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [KeyHook(KeyB101()), KeyHook(KeyB102()), KeyHook(KeyB103()), KeyHook(KeyB104()), KeyHook(KeyB105()),
     KeyHook(KeyB106()), KeyHook(KeyB107()), KeyHook(KeyB108()), KeyHook(KeyB108()), KeyHook(KeyB110()),
     KeyHook(KeyB111()), KeyHook(),          KeyHook(KeyB113()), KeyHook(KeyB114()), KeyHook(KeyB115()),
     KeyHook(KeyB116()), KeyHook(KeyB117()), KeyHook(KeyB118()), KeyHook(KeyB118()), KeyHook(KeyB120()),
     KeyHook(KeyB201()), KeyHook(KeyB202()), KeyHook(KeyB203()), KeyHook(),          KeyHook(KeyB205()),
     KeyHook(KeyB206()), KeyHook(KeyB207()), KeyHook(KeyB208()), KeyHook(KeyB208()), KeyHook(KeyB210()),
     KeyHook(KeyB211()), KeyHook(KeyB212()), KeyHook(KeyB213()), KeyHook(KeyB214()), KeyHook(KeyB215()),
     KeyHook(KeyB216()), KeyHook(KeyB217()), KeyHook(KeyB218()), KeyHook(KeyB218()), KeyHook(KeyB220()),
     KeyHook(),          KeyHook(KeyB302()), KeyHook(KeyB303()), KeyHook(KeyB304()), KeyHook(KeyB305()),
     KeyHook(KeyB306()), KeyHook(KeyB307()), KeyHook(KeyB308()), KeyHook(KeyB308()), KeyHook(KeyB310()),
     KeyHook(KeyB311()), KeyHook(KeyB312()), KeyHook(KeyB313()), KeyHook(KeyB314()), KeyHook(KeyB315()),
     KeyHook(KeyB316()), KeyHook(KeyB317()), KeyHook(KeyB318()), KeyHook(KeyB318()), KeyHook()]
    )

###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################


###########################################################################################################################################
###############################################################    A200    ################################################################
###########################################################################################################################################

############################################################### A201 - A202 ###############################################################
roomA201LI = Room(
    'A201 - Living room',
    None, 'A201BA', 'A200.01', 'A201KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA201BE = Room(
    'A201 - Bedroom',
    None, None, 'A201KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA201BA = Room(
    'A201 - Bathroom',
    None, None, 'A201LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA201KI = Room(
    'A201 - Kitchen',
    'A201LI', 'A201BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_01 = Room(
    'A200.01 - Corridor',
    None, 'A201LI', 'A202LI', 'A200.02',
    {'dn':None, 'dw':KeyA201(), 'de':KeyA202(), 'ds':None},
    [Plant(), Plant(), Window(), Carpet(CarpetText('A201')), Carpet(CarpetText('A202'))]
    )

roomA200_02 = Room(
    'A200.02 - Corridor',
    'A200.01', None, None, 'A200.03',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA202LI = Room(
    'A202 - Living room',
    None, 'A200.01', 'A202BA', 'A202KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA202BE = Room(
    'A202 - Bedroom',
    None, 'A202KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA202BA = Room(
    'A202 - Bathroom',
    None, 'A202LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA202KI = Room(
    'A202 - Kitchen',
    'A202LI', None, 'A202BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A203 - A204 ###############################################################
roomA203LI = Room(
    'A203 - Living room',
    None, 'A203BA', 'A200.03', 'A203KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA203BE = Room(
    'A203 - Bedroom',
    None, None, 'A203KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA203BA = Room(
    'A203 - Bathroom',
    None, None, 'A203LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA203KI = Room(
    'A203 - Kitchen',
    'A203LI', 'A203BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_03 = Room(
    'A200.03 - Corridor',
    'A200.02', 'A203LI', 'A204LI', 'A200.04',
    {'dn':None, 'dw':KeyA203(), 'de':KeyA204(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A203')), Carpet(CarpetText('A204'))]
    )

roomA200_04 = Room(
    'A200.04 - Corridor',
    'A200.03', None, None, 'A200.05',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA204LI = Room(
    'A204 - Living room',
    None, 'A200.03', 'A204BA', 'A204KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA204BE = Room(
    'A204 - Bedroom',
    None, 'A204KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA204BA = Room(
    'A204 - Bathroom',
    None, 'A204LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA204KI = Room(
    'A204 - Kitchen',
    'A204LI', None, 'A204BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A205 - A206 ###############################################################
roomA205LI = Room(
    'A205 - Living room',
    None, 'A205BA', 'A200.05', 'A205KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA205BE = Room(
    'A205 - Bedroom',
    None, None, 'A205KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA205BA = Room(
    'A205 - Bathroom',
    None, None, 'A205LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA205KI = Room(
    'A205 - Kitchen',
    'A205LI', 'A205BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_05 = Room(
    'A200.05 - Corridor',
    'A200.04', 'A205LI', 'A206LI', 'A200.06',
    {'dn':None, 'dw':KeyA205(), 'de':KeyA206(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A205')), Carpet(CarpetText('A206'))]
    )

roomA200_06 = Room(
    'A200.06 - Corridor',
    'A200.05', None, None, 'A200.07',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA206LI = Room(
    'A206 - Living room',
    None, 'A200.05', 'A206BA', 'A206KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA206BE = Room(
    'A206 - Bedroom',
    None, 'A206KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA206BA = Room(
    'A206 - Bathroom',
    None, 'A206LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA206KI = Room(
    'A206 - Kitchen',
    'A206LI', None, 'A206BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A207 - A208 ###############################################################
roomA207LI = Room(
    'A207 - Living room',
    None, 'A207BA', 'A200.07', 'A207KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA207BE = Room(
    'A207 - Bedroom',
    None, None, 'A207KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA207BA = Room(
    'A207 - Bathroom',
    None, None, 'A207LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA207KI = Room(
    'A207 - Kitchen',
    'A207LI', 'A207BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_07 = Room(
    'A200.07 - Corridor',
    'A200.06', 'A207LI', 'A208LI', 'A200.08',
    {'dn':None, 'dw':KeyA207(), 'de':KeyA208(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A207')), Carpet(CarpetText('A208'))]
    )

roomA200_08 = Room(
    'A200.08 - Corridor',
    'A200.07', None, None, 'A200.09',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA208LI = Room(
    'A208 - Living room',
    None, 'A200.07', 'A208BA', 'A208KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA208BE = Room(
    'A208 - Bedroom',
    None, 'A208KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA208BA = Room(
    'A208 - Bathroom',
    None, 'A208LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA208KI = Room(
    'A208 - Kitchen',
    'A208LI', None, 'A208BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A209 - A210 ###############################################################
roomA209LI = Room(
    'A209 - Living room',
    None, 'A209BA', 'A200.09', 'A209KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA209BE = Room(
    'A209 - Bedroom',
    None, None, 'A209KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA209BA = Room(
    'A209 - Bathroom',
    None, None, 'A209LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA209KI = Room(
    'A209 - Kitchen',
    'A209LI', 'A209BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_09 = Room(
    'A200.09 - Corridor',
    'A200.08', 'A209LI', 'A210LI', 'A200.10',
    {'dn':None, 'dw':KeyA209(), 'de':KeyA210(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A209')), Carpet(CarpetText('A210'))]
    )

roomA200_10 = Room(
    'A200.10 - Corridor',
    'A200.09', None, None, 'A200.11',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA210LI = Room(
    'A210 - Living room',
    None, 'A200.09', 'A210BA', 'A210KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA210BE = Room(
    'A210 - Bedroom',
    None, 'A210KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA210BA = Room(
    'A210 - Bathroom',
    None, 'A210LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA210KI = Room(
    'A210 - Kitchen',
    'A210LI', None, 'A210BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A200 - Storage room ###############################################################

roomA200_11 = Room(
    'A200.11 - Corridor',
    'A200.10', 'A200SR', 'A200.11.1', 'A200.12',
    {'dn':None, 'dw':KeySRA200(), 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA200_11_1 = Room(
    'A200.11.1 - Corridor',
    None, 'A200.11', 'A200.11.2', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA200_11_2 = Room(
    'A200.11.2 - Corridor',
    None, 'A200.11.1', 'M200.1', None,                               ########################### Mittelweg
    {'dn':None, 'dw':None, 'de':KeySecurityDoorA200(), 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA200SR = Room(
    'A200 - Storage room',
    None, None, 'A200.11', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     Carton(), Carton(), Carton(), Carton(),
     Carton(), Carton(), Carton(), Carton()]
    )

############################################################### A211 - A212 ###############################################################
roomA211LI = Room(
    'A211 - Living room',
    None, 'A211BA', 'A200.12', 'A211KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA211BE = Room(
    'A211 - Bedroom',
    None, None, 'A211KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA211BA = Room(
    'A211 - Bathroom',
    None, None, 'A211LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA211KI = Room(
    'A211 - Kitchen',
    'A211LI', 'A211BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_12 = Room(
    'A200.12 - Corridor',
    'A200.11', 'A211LI', 'A212LI', 'A200.13',
    {'dn':None, 'dw':KeyA211(), 'de':KeyA212(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A211')), Carpet(CarpetText('A212'))]
    )

roomA200_13 = Room(
    'A200.13 - Corridor',
    'A200.12', None, None, 'A200.14',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA212LI = Room(
    'A212 - Living room',
    None, 'A200.12', 'A212BA', 'A212KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA212BE = Room(
    'A212 - Bedroom',
    None, 'A212KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA212BA = Room(
    'A212 - Bathroom',
    None, 'A212LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA212KI = Room(
    'A212 - Kitchen',
    'A212LI', None, 'A212BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A213 - A214 ###############################################################
roomA213LI = Room(
    'A213 - Living room',
    None, 'A213BA', 'A200.14', 'A213KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA213BE = Room(
    'A213 - Bedroom',
    None, None, 'A213KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA213BA = Room(
    'A213 - Bathroom',
    None, None, 'A213LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA213KI = Room(
    'A213 - Kitchen',
    'A213LI', 'A213BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_14 = Room(
    'A200.14 - Corridor',
    'A200.13', 'A213LI', 'A214LI', 'A200.15',
    {'dn':None, 'dw':KeyA213(), 'de':KeyA214(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A213')), Carpet(CarpetText('A214'))]
    )

roomA200_15 = Room(
    'A200.15 - Corridor',
    'A200.14', None, None, 'A200.16',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA214LI = Room(
    'A214 - Living room',
    None, 'A200.14', 'A214BA', 'A214KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA214BE = Room(
    'A214 - Bedroom',
    None, 'A214KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA214BA = Room(
    'A214 - Bathroom',
    None, 'A214LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA214KI = Room(
    'A214 - Kitchen',
    'A214LI', None, 'A214BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A215 - A216 ###############################################################
roomA215LI = Room(
    'A215 - Living room',
    None, 'A215BA', 'A200.16', 'A215KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA215BE = Room(
    'A215 - Bedroom',
    None, None, 'A215KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA215BA = Room(
    'A215 - Bathroom',
    None, None, 'A215LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA215KI = Room(
    'A215 - Kitchen',
    'A215LI', 'A215BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_16 = Room(
    'A200.16 - Corridor',
    'A200.15', 'A215LI', 'A216LI', 'A200.17',
    {'dn':None, 'dw':KeyA215(), 'de':KeyA216(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A215')), Carpet(CarpetText('A216'))]
    )

roomA200_17 = Room(
    'A200.17 - Corridor',
    'A200.16', None, None, 'A200.18',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA216LI = Room(
    'A216 - Living room',
    None, 'A200.16', 'A216BA', 'A216KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA216BE = Room(
    'A216 - Bedroom',
    None, 'A216KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA216BA = Room(
    'A216 - Bathroom',
    None, 'A216LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA216KI = Room(
    'A216 - Kitchen',
    'A216LI', None, 'A216BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A217 - A218 ###############################################################
roomA217LI = Room(
    'A217 - Living room',
    None, 'A217BA', 'A200.18', 'A217KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA217BE = Room(
    'A217 - Bedroom',
    None, None, 'A217KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA217BA = Room(
    'A217 - Bathroom',
    None, None, 'A217LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA217KI = Room(
    'A217 - Kitchen',
    'A217LI', 'A217BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_18 = Room(
    'A200.18 - Corridor',
    'A200.17', 'A217LI', 'A218LI', 'A200.19',
    {'dn':None, 'dw':KeyA217(), 'de':KeyA218(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A217')), Carpet(CarpetText('A218'))]
    )

roomA200_19 = Room(
    'A200.19 - Corridor',
    'A200.18', None, None, 'A200.20',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA218LI = Room(
    'A218 - Living room',
    None, 'A200.18', 'A218BA', 'A218KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA218BE = Room(
    'A218 - Bedroom',
    None, 'A218KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA218BA = Room(
    'A218 - Bathroom',
    None, 'A218LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA218KI = Room(
    'A218 - Kitchen',
    'A218LI', None, 'A218BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A219 - A220 ###############################################################
roomA219LI = Room(
    'A219 - Living room',
    None, 'A219BA', 'A200.20', 'A219KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA219BE = Room(
    'A219 - Bedroom',
    None, None, 'A219KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA219BA = Room(
    'A219 - Bathroom',
    None, None, 'A219LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA219KI = Room(
    'A219 - Kitchen',
    'A219LI', 'A219BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA200_20 = Room(
    'A200.20 - Corridor',
    'A200.19', 'A219LI', 'A220LI', 'A200.21',
    {'dn':None, 'dw':KeyA219(), 'de':KeyA220(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A219')), Carpet(CarpetText('A220'))]
    )

roomA200_21 = Room(
    'A200.21 - Corridor',
    'A200.20', None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Window(), Painting(), Painting()]
    )

roomA220LI = Room(
    'A220 - Living room',
    None, 'A200.20', 'A220BA', 'A220KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA220BE = Room(
    'A220 - Bedroom',
    None, 'A220KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA220BA = Room(
    'A220 - Bathroom',
    None, 'A220LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA220KI = Room(
    'A220 - Kitchen',
    'A220LI', None, 'A220BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

###########################################################################################################################################
###############################################################    B200    ################################################################
###########################################################################################################################################



############################################################### A101 - A102 ###############################################################
roomB201LI = Room(
    'B201 - Living room',
    None, 'B201BA', 'B200.01', 'B201KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB201BE = Room(
    'B201 - Bedroom',
    None, None, 'B201KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB201BA = Room(
    'B201 - Bathroom',
    None, None, 'B201LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB201KI = Room(
    'B201 - Kitchen',
    'B201LI', 'B201BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_01 = Room(
    'B200.01 - Corridor',
    None, 'B201LI', 'B202LI', 'B200.02',
    {'dn':None, 'dw':KeyB201(), 'de':KeyB202(), 'ds':None},
    [Plant(), Plant(), Window(), Carpet(CarpetText('B201')), Carpet(CarpetText('B202'))]
    )

roomB200_02 = Room(
    'B200.02 - Corridor',
    'B200.01', None, None, 'B200.03',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB202LI = Room(
    'B202 - Living room',
    None, 'B200.01', 'B202BA', 'B202KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB202BE = Room(
    'B202 - Bedroom',
    None, 'B202KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB202BA = Room(
    'B202 - Bathroom',
    None, 'B202LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB202KI = Room(
    'B202 - Kitchen',
    'B202LI', None, 'B202BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B203 - B204 ###############################################################
roomB203LI = Room(
    'B203 - Living room',
    None, 'B203BA', 'B200.03', 'B203KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(),
     Mobile(MobileMessage('''
                          You on August 2, 2024:\n
                          Hi Marc, were you also invited to Maiks\'s birthday party?\n\n
                          
                          Marc on August 2, 2024:\n
                          Hi Peter, yes I was.\n\n
                          
                          You on August 2, 2024:\n
                          Maik is the hotel\'s IT specialist, right?\n\n
                          
                          Marc on August 2, 2024:\n
                          Yes.\n
                          How old will he be tomorrow?\n\n

                          You on August 2, 2024:\n
                          I think 44.\n\n

                          Marc on August 2, 2024:\n
                          He even gave me his spare key.\n\n

                          You on August 2, 2024:\n
                          Wow, can you see him?\n\n

                          Marc on August 2, 2024:\n
                          Why I should able to see him?\n\n

                          You on August 2, 2024:\n
                          He lives just on the other side when you look out of the window!\n\n

                          Marc on August 2, 2024:\n
                          Opposite is the A306, he lives next to it. And no, I can\'t se him! Good Night.\n\n
                          
                          You on August 2, 2024:\n
                          Good Night.
                          ''')),
     Armchair(), Armchair(),
     Painting(), Painting(), Plant(), Plant(),
     Socket()]
    )

roomB203BE = Room(
    'B203 - Bedroom',
    None, None, 'B203KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB203BA = Room(
    'B203 - Bathroom',
    None, None, 'B203LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB203KI = Room(
    'B203 - Kitchen',
    'B203LI', 'B203BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_03 = Room(
    'B200.03 - Corridor',
    'B200.02', 'B203LI', 'B204LI', 'B200.04',
    {'dn':None, 'dw':KeyB203(), 'de':KeyB204(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B203')), Carpet(CarpetText('B204'))]
    )

roomB200_04 = Room(
    'B200.04 - Corridor',
    'B200.03', None, None, 'B200.05',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB204LI = Room(
    'B204 - Living room',
    None, 'B200.03', 'B204BA', 'B204KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB204BE = Room(
    'B204 - Bedroom',
    None, 'B204KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB204BA = Room(
    'B204 - Bathroom',
    None, 'B204LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB204KI = Room(
    'B204 - Kitchen',
    'B204LI', None, 'B204BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B205 - B206 ###############################################################
roomB205LI = Room(
    'B205 - Living room',
    None, 'B205BA', 'B200.05', 'B205KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB205BE = Room(
    'B205 - Bedroom',
    None, None, 'B205KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB205BA = Room(
    'B205 - Bathroom',
    None, None, 'B205LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB205KI = Room(
    'B205 - Kitchen',
    'B205LI', 'B205BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_05 = Room(
    'B200.05 - Corridor',
    'B200.04', 'B205LI', 'B206LI', 'B200.06',
    {'dn':None, 'dw':KeyB205(), 'de':KeyB206(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B205')), Carpet(CarpetText('B206'))]
    )

roomB200_06 = Room(
    'B200.06 - Corridor',
    'B200.05', None, None, 'B200.07',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB206LI = Room(
    'B206 - Living room',
    None, 'B200.05', 'B206BA', 'B206KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB206BE = Room(
    'B206 - Bedroom',
    None, 'B206KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB206BA = Room(
    'B206 - Bathroom',
    None, 'B206LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB206KI = Room(
    'B206 - Kitchen',
    'B206LI', None, 'B206BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B207 - B208 ###############################################################
roomB207LI = Room(
    'B207 - Living room',
    None, 'B207BA', 'B200.07', 'B207KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB207BE = Room(
    'B207 - Bedroom',
    None, None, 'B207KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB207BA = Room(
    'B207 - Bathroom',
    None, None, 'B207LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB207KI = Room(
    'B207 - Kitchen',
    'B207LI', 'B207BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_07 = Room(
    'B200.07 - Corridor',
    'B200.06', 'B207LI', 'B208LI', 'B200.08',
    {'dn':None, 'dw':KeyB207(), 'de':KeyB208(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B207')), Carpet(CarpetText('B208'))]
    )

roomB200_08 = Room(
    'B200.08 - Corridor',
    'B200.07', None, None, 'B200.09',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB208LI = Room(
    'B208 - Living room',
    None, 'B200.07', 'B208BA', 'B208KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB208BE = Room(
    'B208 - Bedroom',
    None, 'B208KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB208BA = Room(
    'B208 - Bathroom',
    None, 'B208LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB208KI = Room(
    'B208 - Kitchen',
    'B208LI', None, 'B208BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B209 - B210 ###############################################################
roomB209LI = Room(
    'B209 - Living room',
    None, 'B209BA', 'B200.09', 'B209KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB209BE = Room(
    'B209 - Bedroom',
    None, None, 'B209KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB209BA = Room(
    'B209 - Bathroom',
    None, None, 'B209LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB209KI = Room(
    'B209 - Kitchen',
    'B209LI', 'B209BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_09 = Room(
    'B200.09 - Corridor',
    'B200.08', 'B209LI', 'B210LI', 'B200.10',
    {'dn':None, 'dw':KeyB209(), 'de':KeyB210(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B209')), Carpet(CarpetText('B210'))]
    )

roomB200_10 = Room(
    'B200.10 - Corridor',
    'B200.09', None, None, 'B200.11',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB210LI = Room(
    'B210 - Living room',
    None, 'B200.09', 'B210BA', 'B210KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB210BE = Room(
    'B210 - Bedroom',
    None, 'B210KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB210BA = Room(
    'B210 - Bathroom',
    None, 'B210LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB210KI = Room(
    'B210 - Kitchen',
    'B210LI', None, 'B210BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B200 - Storage room ###############################################################

roomB200_11 = Room(
    'B200.11 - Corridor',
    'B200.10', 'B200.11.1', 'B200SR', 'B200.12',
    {'dn':None, 'dw':None, 'de':KeySRB200(), 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB200_11_1 = Room(
    'B200.11.1 - Corridor',
    None, 'B200.11.2', 'B200.11', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB200_11_2 = Room(
    'B200.11.2 - Corridor',
    None, 'M200.4', 'B200.11.1', None,                               ########################### Mittelweg
    {'dn':None, 'dw':KeySecurityDoorB200(), 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB200SR = Room(
    'B200 - Storage room',
    None, 'B200.11', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     Carton(), Carton(), Carton(), Carton(),
     Carton(), Carton(), Carton(), Carton()]
    )

############################################################### B211 - B212 ###############################################################
roomB211LI = Room(
    'B211 - Living room',
    None, 'B211BA', 'B200.12', 'B211KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB211BE = Room(
    'B211 - Bedroom',
    None, None, 'B211KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB211BA = Room(
    'B211 - Bathroom',
    None, None, 'B211LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB211KI = Room(
    'B211 - Kitchen',
    'B211LI', 'B211BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_12 = Room(
    'B200.12 - Corridor',
    'B200.11', 'B211LI', 'B212LI', 'B200.13',
    {'dn':None, 'dw':KeyB211(), 'de':KeyB212(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B211')), Carpet(CarpetText('B212'))]
    )

roomB200_13 = Room(
    'B200.13 - Corridor',
    'B200.12', None, None, 'B200.14',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB212LI = Room(
    'B212 - Living room',
    None, 'B200.12', 'B212BA', 'B212KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB212BE = Room(
    'B212 - Bedroom',
    None, 'B212KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB212BA = Room(
    'B212 - Bathroom',
    None, 'B212LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB212KI = Room(
    'B212 - Kitchen',
    'B212LI', None, 'B212BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B213 - B214 ###############################################################
roomB213LI = Room(
    'B213 - Living room',
    None, 'B213BA', 'B200.14', 'B213KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB213BE = Room(
    'B213 - Bedroom',
    None, None, 'B213KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB213BA = Room(
    'B213 - Bathroom',
    None, None, 'B213LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB213KI = Room(
    'B213 - Kitchen',
    'B213LI', 'B213BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_14 = Room(
    'B200.14 - Corridor',
    'B200.13', 'B213LI', 'B214LI', 'B200.15',
    {'dn':None, 'dw':KeyB213(), 'de':KeyB214(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B213')), Carpet(CarpetText('B214'))]
    )

roomB200_15 = Room(
    'B200.15 - Corridor',
    'B200.14', None, None, 'B200.16',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB214LI = Room(
    'B214 - Living room',
    None, 'B200.14', 'B214BA', 'B214KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB214BE = Room(
    'B214 - Bedroom',
    None, 'B214KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB214BA = Room(
    'B214 - Bathroom',
    None, 'B214LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB214KI = Room(
    'B214 - Kitchen',
    'B214LI', None, 'B214BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B215 - B216 ###############################################################
roomB215LI = Room(
    'B215 - Living room',
    None, 'B215BA', 'B200.16', 'B215KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB215BE = Room(
    'B215 - Bedroom',
    None, None, 'B215KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB215BA = Room(
    'B215 - Bathroom',
    None, None, 'B215LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB215KI = Room(
    'B215 - Kitchen',
    'B215LI', 'B215BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_16 = Room(
    'B200.16 - Corridor',
    'B200.15', 'B215LI', 'B216LI', 'B200.17',
    {'dn':None, 'dw':KeyB215(), 'de':KeyB216(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B215')), Carpet(CarpetText('B216'))]
    )

roomB200_17 = Room(
    'B200.17 - Corridor',
    'B200.16', None, None, 'B200.18',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB216LI = Room(
    'B216 - Living room',
    None, 'B200.16', 'B216BA', 'B216KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB216BE = Room(
    'B216 - Bedroom',
    None, 'B216KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB216BA = Room(
    'B216 - Bathroom',
    None, 'B216LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB216KI = Room(
    'B216 - Kitchen',
    'B216LI', None, 'B216BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B217 - B218 ###############################################################
roomB217LI = Room(
    'B217 - Living room',
    None, 'B217BA', 'B200.18', 'B217KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB217BE = Room(
    'B217 - Bedroom',
    None, None, 'B217KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB217BA = Room(
    'B217 - Bathroom',
    None, None, 'B217LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB217KI = Room(
    'B217 - Kitchen',
    'B217LI', 'B217BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_18 = Room(
    'B200.18 - Corridor',
    'B200.17', 'B217LI', 'B218LI', 'B200.19',
    {'dn':None, 'dw':KeyB217(), 'de':KeyB218(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B217')), Carpet(CarpetText('B218'))]
    )

roomB200_19 = Room(
    'B200.19 - Corridor',
    'B200.18', None, None, 'B200.20',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB218LI = Room(
    'B218 - Living room',
    None, 'B200.18', 'B218BA', 'B218KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB218BE = Room(
    'B218 - Bedroom',
    None, 'B218KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB218BA = Room(
    'B218 - Bathroom',
    None, 'B218LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB218KI = Room(
    'B218 - Kitchen',
    'B218LI', None, 'B218BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B219 - B220 ###############################################################
roomB219LI = Room(
    'B219 - Living room',
    None, 'B219BA', 'B200.20', 'B219KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB219BE = Room(
    'B219 - Bedroom',
    None, None, 'B219KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB219BA = Room(
    'B219 - Bathroom',
    None, None, 'B219LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB219KI = Room(
    'B219 - Kitchen',
    'B219LI', 'B219BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB200_20 = Room(
    'B200.20 - Corridor',
    'B200.19', 'B219LI', 'B220LI', 'B200.21',
    {'dn':None, 'dw':KeyB219(), 'de':KeyB220(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B219')), Carpet(CarpetText('B220'))]
    )

roomB200_21 = Room(
    'B200.21 - Corridor',
    'B200.20', None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Window(), Painting(), Painting()]
    )

roomB220LI = Room(
    'B220 - Living room',
    None, 'B200.20', 'B220BA', 'B220KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB220BE = Room(
    'B220 - Bedroom',
    None, 'B220KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB220BA = Room(
    'B220 - Bathroom',
    None, 'B220LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB220KI = Room(
    'B220 - Kitchen',
    'B220LI', None, 'B220BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

###########################################################################################################################################
###############################################################    M200    ################################################################
###########################################################################################################################################

roomM200_1 = Room(
    'M200.1 - Corridor',
    None, 'A200.11.2', 'M200.2', None,
    {'dn':None, 'dw':KeySecurityDoorA200(), 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM200_2 = Room(
    'M200.2 - Corridor',
    'M100.2', 'M200.1', 'M200.3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM200_3 = Room(
    'M200.3 - Corridor',
    'M300.3', 'M200.2', 'M200.4', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM200_4 = Room(
    'M200.4 - Corridor',
    None, 'M200.3', 'B200.11.2', None,
    {'dn':None, 'dw':None, 'de':KeySecurityDoorB200(), 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )


###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################


###########################################################################################################################################
###############################################################    A300    ################################################################
###########################################################################################################################################

############################################################### A301 - A302 ###############################################################
roomA301LI = Room(
    'A301 - Living room',
    None, 'A301BA', 'A300.01', 'A301KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA301BE = Room(
    'A301 - Bedroom',
    None, None, 'A301KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA301BA = Room(
    'A301 - Bathroom',
    None, None, 'A301LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA301KI = Room(
    'A301 - Kitchen',
    'A301LI', 'A301BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_01 = Room(
    'A300.01 - Corridor',
    None, 'A301LI', 'A302LI', 'A300.02',
    {'dn':None, 'dw':KeyA301(), 'de':KeyA302(), 'ds':None},
    [Plant(), Plant(), Window(), Carpet(CarpetText('A301')), Carpet(CarpetText('A302'))]
    )

roomA300_02 = Room(
    'A300.02 - Corridor',
    'A300.01', None, None, 'A300.03',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA302LI = Room(
    'A302 - Living room',
    None, 'A300.01', 'A302BA', 'A302KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA302BE = Room(
    'A302 - Bedroom',
    None, 'A302KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA302BA = Room(
    'A302 - Bathroom',
    None, 'A302LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA302KI = Room(
    'A302 - Kitchen',
    'A302LI', None, 'A302BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A303 - A304 ###############################################################
roomA303LI = Room(
    'A303 - Living room',
    None, 'A303BA', 'A300.03', 'A303KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket(),
     Mobile(MobileMessage('''
                          The key for the storage room is under a plant at A300.11.\n
                          In the storage room you will find the key for the security\n
                          door on your floor, can you please hand it in at the reception,\n
                          as you know, at A300.11 go right to M300.02 and the take the\n
                          stairs to M100.02 and then go down to the reception, thanky you.
                          '''))]
    )

roomA303BE = Room(
    'A303 - Bedroom',
    None, None, 'A303KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA303BA = Room(
    'A303 - Bathroom',
    None, None, 'A303LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA303KI = Room(
    'A303 - Kitchen',
    'A303LI', 'A303BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_03 = Room(
    'A300.03 - Corridor',
    'A300.02', 'A303LI', 'A304LI', 'A300.04',
    {'dn':None, 'dw':KeyA303(), 'de':KeyA304(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A303')), Carpet(CarpetText('A304'))]
    )

roomA300_04 = Room(
    'A300.04 - Corridor',
    'A300.03', None, None, 'A300.05',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA304LI = Room(
    'A304 - Living room',
    None, 'A300.03', 'A304BA', 'A304KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA304BE = Room(
    'A304 - Bedroom',
    None, 'A304KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA304BA = Room(
    'A304 - Bathroom',
    None, 'A304LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA304KI = Room(
    'A304 - Kitchen',
    'A304LI', None, 'A304BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A305 - A306 ###############################################################
roomA305LI = Room(
    'A305 - Living room',
    None, 'A305BA', 'A300.05', 'A305KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA305BE = Room(
    'A305 - Bedroom',
    None, None, 'A305KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA305BA = Room(
    'A305 - Bathroom',
    None, None, 'A305LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA305KI = Room(
    'A305 - Kitchen',
    'A305LI', 'A305BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_05 = Room(
    'A300.05 - Corridor',
    'A300.04', 'A305LI', 'A306LI', 'A300.06',
    {'dn':None, 'dw':KeyA305(), 'de':KeyA306(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A305')), Carpet(CarpetText('A306'))]
    )

roomA300_06 = Room(
    'A300.06 - Corridor',
    'A300.05', None, None, 'A300.07',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA306LI = Room(
    'A306 - Living room',
    None, 'A300.05', 'A306BA', 'A306KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA306BE = Room(
    'A306 - Bedroom',
    None, 'A306KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA306BA = Room(
    'A306 - Bathroom',
    None, 'A306LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA306KI = Room(
    'A306 - Kitchen',
    'A306LI', None, 'A306BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A307 - A308 ###############################################################
roomA307LI = Room(
    'A307 - Living room',
    None, 'A307BA', 'A300.07', 'A307KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA307BE = Room(
    'A307 - Bedroom',
    None, None, 'A307KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA307BA = Room(
    'A307 - Bathroom',
    None, None, 'A307LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA307KI = Room(
    'A307 - Kitchen',
    'A307LI', 'A307BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_07 = Room(
    'A300.07 - Corridor',
    'A300.06', 'A307LI', 'A308LI', 'A300.08',
    {'dn':None, 'dw':KeyA307(), 'de':KeyA308(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A307')), Carpet(CarpetText('A308'))]
    )

roomA300_08 = Room(
    'A300.08 - Corridor',
    'A300.07', None, None, 'A300.09',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA308LI = Room(
    'A308 - Living room',
    None, 'A300.07', 'A308BA', 'A308KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA308BE = Room(
    'A308 - Bedroom',
    None, 'A308KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA308BA = Room(
    'A308 - Bathroom',
    None, 'A308LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA308KI = Room(
    'A308 - Kitchen',
    'A308LI', None, 'A308BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket(),
     Birthdaycake(), Gift(), Gift(name='Peter'), Gift(name='Anja'),
     Gift(name='Marc'), Gift(KeyEntrence(), 'Reception-Team'), Gift()]
    )

############################################################### A309 - A310 ###############################################################
roomA309LI = Room(
    'A309 - Living room',
    None, 'A309BA', 'A300.09', 'A309KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA309BE = Room(
    'A309 - Bedroom',
    None, None, 'A309KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA309BA = Room(
    'A309 - Bathroom',
    None, None, 'A309LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA309KI = Room(
    'A309 - Kitchen',
    'A309LI', 'A309BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_09 = Room(
    'A300.09 - Corridor',
    'A300.08', 'A309LI', 'A310LI', 'A300.10',
    {'dn':None, 'dw':KeyA309(), 'de':KeyA310(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A309')), Carpet(CarpetText('A310'))]
    )

roomA300_10 = Room(
    'A300.10 - Corridor',
    'A300.09', None, None, 'A300.11',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA310LI = Room(
    'A310 - Living room',
    None, 'A300.09', 'A310BA', 'A310KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA310BE = Room(
    'A310 - Bedroom',
    None, 'A310KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA310BA = Room(
    'A310 - Bathroom',
    None, 'A310LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA310KI = Room(
    'A310 - Kitchen',
    'A310LI', None, 'A310BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A300 - Storage room ###############################################################

roomA300_11 = Room(
    'A300.11 - Corridor',
    'A300.10', 'A300SR', 'A300.11.1', 'A300.12',
    {'dn':None, 'dw':KeySRA300(), 'de':None, 'ds':None},
    [Plant(), Plant(KeySRA300()), Painting(), Painting()]
    )

roomA300_11_1 = Room(
    'A300.11.1 - Corridor',
    None, 'A300.11', 'A300.11.2', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA300_11_2 = Room(
    'A300.11.2 - Corridor',
    None, 'A300.11.1', 'M300.1', None,                               ########################### Mittelweg
    {'dn':None, 'dw':None, 'de':KeySecurityDoorA300(), 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA300SR = Room(
    'A300 - Storage room',
    None, None, 'A300.11', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     Carton(), Carton(KeySecurityDoorA300()), Carton(), Carton(),
     Carton(), Carton(), Carton(), Carton()]
    )

############################################################### A311 - A312 ###############################################################
roomA311LI = Room(
    'A311 - Living room',
    None, 'A311BA', 'A300.12', 'A311KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA311BE = Room(
    'A311 - Bedroom',
    None, None, 'A311KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA311BA = Room(
    'A311 - Bathroom',
    None, None, 'A311LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA311KI = Room(
    'A311 - Kitchen',
    'A311LI', 'A311BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_12 = Room(
    'A300.12 - Corridor',
    'A300.11', 'A311LI', 'A312LI', 'A300.13',
    {'dn':None, 'dw':KeyA311(), 'de':KeyA312(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A311')), Carpet(CarpetText('A312'))]
    )

roomA300_13 = Room(
    'A300.13 - Corridor',
    'A300.12', None, None, 'A300.14',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA312LI = Room(
    'A312 - Living room',
    None, 'A300.12', 'A312BA', 'A312KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA312BE = Room(
    'A312 - Bedroom',
    None, 'A312KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA312BA = Room(
    'A312 - Bathroom',
    None, 'A312LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA312KI = Room(
    'A312 - Kitchen',
    'A312LI', None, 'A312BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A313 - A314 ###############################################################
roomA313LI = Room(
    'A313 - Living room',
    None, 'A313BA', 'A300.14', 'A313KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA313BE = Room(
    'A313 - Bedroom',
    None, None, 'A313KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA313BA = Room(
    'A313 - Bathroom',
    None, None, 'A313LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA313KI = Room(
    'A313 - Kitchen',
    'A313LI', 'A313BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_14 = Room(
    'A300.14 - Corridor',
    'A300.13', 'A313LI', 'A314LI', 'A300.15',
    {'dn':None, 'dw':KeyA313(), 'de':KeyA314(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A313')), Carpet(CarpetText('A314'))]
    )

roomA300_15 = Room(
    'A300.15 - Corridor',
    'A300.14', None, None, 'A300.16',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA314LI = Room(
    'A314 - Living room',
    None, 'A300.14', 'A314BA', 'A314KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA314BE = Room(
    'A314 - Bedroom',
    None, 'A314KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA314BA = Room(
    'A314 - Bathroom',
    None, 'A314LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA314KI = Room(
    'A314 - Kitchen',
    'A314LI', None, 'A314BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A315 - A316 ###############################################################
roomA315LI = Room(
    'A315 - Living room',
    None, 'A315BA', 'A300.16', 'A315KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA315BE = Room(
    'A315 - Bedroom',
    None, None, 'A315KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA315BA = Room(
    'A315 - Bathroom',
    None, None, 'A315LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA315KI = Room(
    'A315 - Kitchen',
    'A315LI', 'A315BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_16 = Room(
    'A300.16 - Corridor',
    'A300.15', 'A315LI', 'A316LI', 'A300.17',
    {'dn':None, 'dw':KeyA315(), 'de':KeyA316(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A315')), Carpet(CarpetText('A316'))]
    )

roomA300_17 = Room(
    'A300.17 - Corridor',
    'A300.16', None, None, 'A300.18',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA316LI = Room(
    'A316 - Living room',
    None, 'A300.16', 'A316BA', 'A316KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA316BE = Room(
    'A316 - Bedroom',
    None, 'A316KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA316BA = Room(
    'A316 - Bathroom',
    None, 'A316LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA316KI = Room(
    'A316 - Kitchen',
    'A316LI', None, 'A316BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A317 - A318 ###############################################################
roomA317LI = Room(
    'A317 - Living room',
    None, 'A317BA', 'A300.18', 'A317KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA317BE = Room(
    'A317 - Bedroom',
    None, None, 'A317KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA317BA = Room(
    'A317 - Bathroom',
    None, None, 'A317LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA317KI = Room(
    'A317 - Kitchen',
    'A317LI', 'A317BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_18 = Room(
    'A300.18 - Corridor',
    'A300.17', 'A317LI', 'A318LI', 'A300.19',
    {'dn':None, 'dw':KeyA317(), 'de':KeyA318(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A317')), Carpet(CarpetText('A318'))]
    )

roomA300_19 = Room(
    'A300.19 - Corridor',
    'A300.18', None, None, 'A300.20',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomA318LI = Room(
    'A318 - Living room',
    None, 'A300.18', 'A318BA', 'A318KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA318BE = Room(
    'A318 - Bedroom',
    None, 'A318KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA318BA = Room(
    'A318 - Bathroom',
    None, 'A318LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA318KI = Room(
    'A318 - Kitchen',
    'A318LI', None, 'A318BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### A319 - A320 ###############################################################
roomA319LI = Room(
    'A319 - Living room',
    None, 'A319BA', 'A300.20', 'A319KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA319BE = Room(
    'A319 - Bedroom',
    None, None, 'A319KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA319BA = Room(
    'A319 - Bathroom',
    None, None, 'A319LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA319KI = Room(
    'A319 - Kitchen',
    'A319LI', 'A319BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomA300_20 = Room(
    'A300.20 - Corridor',
    'A300.19', 'A319LI', 'A320LI', 'A300.21',
    {'dn':None, 'dw':KeyA319(), 'de':KeyA320(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('A319')), Carpet(CarpetText('A320'))]
    )

roomA300_21 = Room(
    'A300.21 - Corridor',
    'A300.20', None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Window(), Painting(), Painting()]
    )

roomA320LI = Room(
    'A320 - Living room',
    None, 'A300.20', 'A320BA', 'A320KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomA320BE = Room(
    'A320 - Bedroom',
    None, 'A320KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomA320BA = Room(
    'A320 - Bathroom',
    None, 'A320LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomA320KI = Room(
    'A320 - Kitchen',
    'A320LI', None, 'A320BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

###########################################################################################################################################
###############################################################    B300    ################################################################
###########################################################################################################################################



############################################################### A101 - A102 ###############################################################
roomB301LI = Room(
    'B301 - Living room',
    None, 'B301BA', 'B300.01', 'B301KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB301BE = Room(
    'B301 - Bedroom',
    None, None, 'B301KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB301BA = Room(
    'B301 - Bathroom',
    None, None, 'B301LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB301KI = Room(
    'B301 - Kitchen',
    'B301LI', 'B301BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_01 = Room(
    'B300.01 - Corridor',
    None, 'B301LI', 'B302LI', 'B300.02',
    {'dn':None, 'dw':KeyB301(), 'de':KeyB302(), 'ds':None},
    [Plant(), Plant(), Window(), Carpet(CarpetText('B301')), Carpet(CarpetText('B302'))]
    )

roomB300_02 = Room(
    'B300.02 - Corridor',
    'B300.01', None, None, 'B300.03',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB302LI = Room(
    'B302 - Living room',
    None, 'B300.01', 'B302BA', 'B302KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB302BE = Room(
    'B302 - Bedroom',
    None, 'B302KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB302BA = Room(
    'B302 - Bathroom',
    None, 'B302LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB302KI = Room(
    'B302 - Kitchen',
    'B302LI', None, 'B302BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B303 - B304 ###############################################################
roomB303LI = Room(
    'B303 - Living room',
    None, 'B303BA', 'B300.03', 'B303KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB303BE = Room(
    'B303 - Bedroom',
    None, None, 'B303KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB303BA = Room(
    'B303 - Bathroom',
    None, None, 'B303LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB303KI = Room(
    'B303 - Kitchen',
    'B303LI', 'B303BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_03 = Room(
    'B300.03 - Corridor',
    'B300.02', 'B303LI', 'B304LI', 'B300.04',
    {'dn':None, 'dw':KeyB303(), 'de':KeyB304(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B303')), Carpet(CarpetText('B304'))]
    )

roomB300_04 = Room(
    'B300.04 - Corridor',
    'B300.03', None, None, 'B300.05',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB304LI = Room(
    'B304 - Living room',
    None, 'B300.03', 'B304BA', 'B304KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB304BE = Room(
    'B304 - Bedroom',
    None, 'B304KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB304BA = Room(
    'B304 - Bathroom',
    None, 'B304LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB304KI = Room(
    'B304 - Kitchen',
    'B304LI', None, 'B304BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B305 - B306 ###############################################################
roomB305LI = Room(
    'B305 - Living room',
    None, 'B305BA', 'B300.05', 'B305KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(KeyA308()), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB305BE = Room(
    'B305 - Bedroom',
    None, None, 'B305KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB305BA = Room(
    'B305 - Bathroom',
    None, None, 'B305LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB305KI = Room(
    'B305 - Kitchen',
    'B305LI', 'B305BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_05 = Room(
    'B300.05 - Corridor',
    'B300.04', 'B305LI', 'B306LI', 'B300.06',
    {'dn':None, 'dw':KeyB305(), 'de':KeyB306(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B305')), Carpet(CarpetText('B306'))]
    )

roomB300_06 = Room(
    'B300.06 - Corridor',
    'B300.05', None, None, 'B300.07',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB306LI = Room(
    'B306 - Living room',
    None, 'B300.05', 'B306BA', 'B306KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB306BE = Room(
    'B306 - Bedroom',
    None, 'B306KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB306BA = Room(
    'B306 - Bathroom',
    None, 'B306LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB306KI = Room(
    'B306 - Kitchen',
    'B306LI', None, 'B306BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B307 - B308 ###############################################################
roomB307LI = Room(
    'B307 - Living room',
    None, 'B307BA', 'B300.07', 'B307KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB307BE = Room(
    'B307 - Bedroom',
    None, None, 'B307KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB307BA = Room(
    'B307 - Bathroom',
    None, None, 'B307LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB307KI = Room(
    'B307 - Kitchen',
    'B307LI', 'B307BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_07 = Room(
    'B300.07 - Corridor',
    'B300.06', 'B307LI', 'B308LI', 'B300.08',
    {'dn':None, 'dw':KeyB307(), 'de':KeyB308(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B307')), Carpet(CarpetText('B308'))]
    )

roomB300_08 = Room(
    'B300.08 - Corridor',
    'B300.07', None, None, 'B300.09',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB308LI = Room(
    'B308 - Living room',
    None, 'B300.07', 'B308BA', 'B308KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB308BE = Room(
    'B308 - Bedroom',
    None, 'B308KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB308BA = Room(
    'B308 - Bathroom',
    None, 'B308LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB308KI = Room(
    'B308 - Kitchen',
    'B308LI', None, 'B308BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B309 - B310 ###############################################################
roomB309LI = Room(
    'B309 - Living room',
    None, 'B309BA', 'B300.09', 'B309KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB309BE = Room(
    'B309 - Bedroom',
    None, None, 'B309KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB309BA = Room(
    'B309 - Bathroom',
    None, None, 'B309LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB309KI = Room(
    'B309 - Kitchen',
    'B309LI', 'B309BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_09 = Room(
    'B300.09 - Corridor',
    'B300.08', 'B309LI', 'B310LI', 'B300.10',
    {'dn':None, 'dw':KeyB309(), 'de':KeyB310(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B309')), Carpet(CarpetText('B310'))]
    )

roomB300_10 = Room(
    'B300.10 - Corridor',
    'B300.09', None, None, 'B300.11',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB310LI = Room(
    'B310 - Living room',
    None, 'B300.09', 'B310BA', 'B310KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB310BE = Room(
    'B310 - Bedroom',
    None, 'B310KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB310BA = Room(
    'B310 - Bathroom',
    None, 'B310LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB310KI = Room(
    'B310 - Kitchen',
    'B310LI', None, 'B310BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B300 - Storage room ###############################################################

roomB300_11 = Room(
    'B300.11 - Corridor',
    'B300.10', 'B300.11.1', 'B300SR', 'B300.12',
    {'dn':None, 'dw':None, 'de':KeySRB300(), 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB300_11_1 = Room(
    'B300.11.1 - Corridor',
    None, 'B300.11.2', 'B300.11', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB300_11_2 = Room(
    'B300.11.2 - Corridor',
    None, 'M300.4', 'B300.11.1', None,                               ########################### Mittelweg
    {'dn':None, 'dw':KeySecurityDoorB300(), 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB300SR = Room(
    'B300 - Storage room',
    None, 'B300.11', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     StorageShelf(), StorageShelf(), StorageShelf(), StorageShelf(),
     Carton(), Carton(), Carton(), Carton(),
     Carton(), Carton(), Carton(), Carton()]
    )

############################################################### B311 - B312 ###############################################################
roomB311LI = Room(
    'B311 - Living room',
    None, 'B311BA', 'B300.12', 'B311KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB311BE = Room(
    'B311 - Bedroom',
    None, None, 'B311KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB311BA = Room(
    'B311 - Bathroom',
    None, None, 'B311LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB311KI = Room(
    'B311 - Kitchen',
    'B311LI', 'B311BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_12 = Room(
    'B300.12 - Corridor',
    'B300.11', 'B311LI', 'B312LI', 'B300.13',
    {'dn':None, 'dw':KeyB311(), 'de':KeyB312(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B311')), Carpet(CarpetText('B312'))]
    )

roomB300_13 = Room(
    'B300.13 - Corridor',
    'B300.12', None, None, 'B300.14',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB312LI = Room(
    'B312 - Living room',
    None, 'B300.12', 'B312BA', 'B312KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB312BE = Room(
    'B312 - Bedroom',
    None, 'B312KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB312BA = Room(
    'B312 - Bathroom',
    None, 'B312LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB312KI = Room(
    'B312 - Kitchen',
    'B312LI', None, 'B312BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B313 - B314 ###############################################################
roomB313LI = Room(
    'B313 - Living room',
    None, 'B313BA', 'B300.14', 'B313KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB313BE = Room(
    'B313 - Bedroom',
    None, None, 'B313KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB313BA = Room(
    'B313 - Bathroom',
    None, None, 'B313LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB313KI = Room(
    'B313 - Kitchen',
    'B313LI', 'B313BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_14 = Room(
    'B300.14 - Corridor',
    'B300.13', 'B313LI', 'B314LI', 'B300.15',
    {'dn':None, 'dw':KeyB313(), 'de':KeyB314(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B313')), Carpet(CarpetText('B314'))]
    )

roomB300_15 = Room(
    'B300.15 - Corridor',
    'B300.14', None, None, 'B300.16',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB314LI = Room(
    'B314 - Living room',
    None, 'B300.14', 'B314BA', 'B314KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB314BE = Room(
    'B314 - Bedroom',
    None, 'B314KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB314BA = Room(
    'B314 - Bathroom',
    None, 'B314LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB314KI = Room(
    'B314 - Kitchen',
    'B314LI', None, 'B314BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B315 - B316 ###############################################################
roomB315LI = Room(
    'B315 - Living room',
    None, 'B315BA', 'B300.16', 'B315KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB315BE = Room(
    'B315 - Bedroom',
    None, None, 'B315KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB315BA = Room(
    'B315 - Bathroom',
    None, None, 'B315LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB315KI = Room(
    'B315 - Kitchen',
    'B315LI', 'B315BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_16 = Room(
    'B300.16 - Corridor',
    'B300.15', 'B315LI', 'B316LI', 'B300.17',
    {'dn':None, 'dw':KeyB315(), 'de':KeyB316(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B315')), Carpet(CarpetText('B316'))]
    )

roomB300_17 = Room(
    'B300.17 - Corridor',
    'B300.16', None, None, 'B300.18',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB316LI = Room(
    'B316 - Living room',
    None, 'B300.16', 'B316BA', 'B316KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB316BE = Room(
    'B316 - Bedroom',
    None, 'B316KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB316BA = Room(
    'B316 - Bathroom',
    None, 'B316LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB316KI = Room(
    'B316 - Kitchen',
    'B316LI', None, 'B316BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B317 - B318 ###############################################################
roomB317LI = Room(
    'B317 - Living room',
    None, 'B317BA', 'B300.18', 'B317KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB317BE = Room(
    'B317 - Bedroom',
    None, None, 'B317KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB317BA = Room(
    'B317 - Bathroom',
    None, None, 'B317LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB317KI = Room(
    'B317 - Kitchen',
    'B317LI', 'B317BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_18 = Room(
    'B300.18 - Corridor',
    'B300.17', 'B317LI', 'B318LI', 'B300.19',
    {'dn':None, 'dw':KeyB317(), 'de':KeyB318(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B317')), Carpet(CarpetText('B318'))]
    )

roomB300_19 = Room(
    'B300.19 - Corridor',
    'B300.18', None, None, 'B300.20',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Painting(), Painting()]
    )

roomB318LI = Room(
    'B318 - Living room',
    None, 'B300.18', 'B318BA', 'B318KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB318BE = Room(
    'B318 - Bedroom',
    None, 'B318KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB318BA = Room(
    'B318 - Bathroom',
    None, 'B318LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB318KI = Room(
    'B318 - Kitchen',
    'B318LI', None, 'B318BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

############################################################### B319 - B320 ###############################################################
roomB319LI = Room(
    'B319 - Living room',
    None, 'B319BA', 'B300.20', 'B319KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB319BE = Room(
    'B319 - Bedroom',
    None, None, 'B319KI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB319BA = Room(
    'B319 - Bathroom',
    None, None, 'B319LI', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB319KI = Room(
    'B319 - Kitchen',
    'B319LI', 'B319BE', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

roomB300_20 = Room(
    'B300.20 - Corridor',
    'B300.19', 'B319LI', 'B320LI', 'B300.21',
    {'dn':None, 'dw':KeyB319(), 'de':KeyB320(), 'ds':None},
    [Plant(), Plant(), Carpet(CarpetText('B319')), Carpet(CarpetText('B320'))]
    )

roomB300_21 = Room(
    'B300.21 - Corridor',
    'B300.20', None, None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Window(), Painting(), Painting()]
    )

roomB320LI = Room(
    'B320 - Living room',
    None, 'B300.20', 'B320BA', 'B320KI',
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Couch(), TV(), TVTable(), RemoteControl(),
     CoffeeTable(), Armchair(), Armchair(), Painting(),
     Painting(), Plant(), Plant(), Socket()]
    )

roomB320BE = Room(
    'B320 - Bedroom',
    None, 'B320KI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bed(), Bed(), BedsideTable(),
     BedsideTable(), Table(), Chair(), Chair(),
     Plant(), Plant(), Socket(), Socket()]
    )

roomB320BA = Room(
    'B320 - Bathroom',
    None, 'B320LI', None, None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Window(), Bathtub(), Shower(), Toilet(),
     Washbasin(), ToiletPaper(), ToiletPaper(), Mirror()]
    )

roomB320KI = Room(
    'B320 - Kitchen',
    'B320LI', None, 'B320BE', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Fridge(), Stove(), Oven(), KitchenCupboard(),
     KitchenCupboard(), KitchenCupboard(), Table(), Chair(),
     Chair(), Chair(), Chair(), Chair(),
     Chair(), Plant(), Plant(), Socket()]
    )

###########################################################################################################################################
###############################################################    M300    ################################################################
###########################################################################################################################################

roomM300_1 = Room(
    'M300.1 - Corridor',
    None, 'A300.11.2', 'M300.2', None,
    {'dn':None, 'dw':KeySecurityDoorA300(), 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM300_2 = Room(
    'M300.2 - Corridor',
    'M200.2', 'M300.1', 'M300.3', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM300_3 = Room(
    'M300.3 - Corridor',
    None, 'M300.2', 'M300.4', None,
    {'dn':None, 'dw':None, 'de':None, 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )

roomM300_4 = Room(
    'M300.4 - Corridor',
    None, 'M300.3', 'B300.11.2', None,
    {'dn':None, 'dw':None, 'de':KeySecurityDoorB300(), 'ds':None},
    [Plant(), Plant(), Plant(), Plant(),
    Socket(), Painting()]
    )


rooms = {
    # Floor 1
    # A
    'A100.01':roomA100_01, 'A100.02':roomA100_02, 'A101BA':roomA101BA, 'A101BE':roomA101BE, 'A101KI':roomA101KI, 'A101LI':roomA101LI, 'A102BA':roomA102BA, 'A102BE':roomA102BE, 'A102KI':roomA102KI, 'A102LI':roomA102LI, # A101 - A102
    'A100.03':roomA100_03, 'A100.04':roomA100_04, 'A103BA':roomA103BA, 'A103BE':roomA103BE, 'A103KI':roomA103KI, 'A103LI':roomA103LI, 'A104BA':roomA104BA, 'A104BE':roomA104BE, 'A104KI':roomA104KI, 'A104LI':roomA104LI, # A103 - A104
    'A100.05':roomA100_05, 'A100.06':roomA100_06, 'A105BA':roomA105BA, 'A105BE':roomA105BE, 'A105KI':roomA105KI, 'A105LI':roomA105LI, 'A106BA':roomA106BA, 'A106BE':roomA106BE, 'A106KI':roomA106KI, 'A106LI':roomA106LI, # A105 - A106
    'A100.07':roomA100_07, 'A100.08':roomA100_08, 'A107BA':roomA107BA, 'A107BE':roomA107BE, 'A107KI':roomA107KI, 'A107LI':roomA107LI, 'A108BA':roomA108BA, 'A108BE':roomA108BE, 'A108KI':roomA108KI, 'A108LI':roomA108LI, # A107 - A108
    'A100.09':roomA100_09, 'A100.10':roomA100_10, 'A109BA':roomA109BA, 'A109BE':roomA109BE, 'A109KI':roomA109KI, 'A109LI':roomA109LI, 'A110BA':roomA110BA, 'A110BE':roomA110BE, 'A110KI':roomA110KI, 'A110LI':roomA110LI, # A109 - A110
    'A100.11':roomA100_11, 'A100.11.1':roomA100_11_1, 'A100.11.2':roomA100_11_2, 'A100SR':roomA100SR,
    'A100.12':roomA100_12, 'A100.13':roomA100_13, 'A111BA':roomA111BA, 'A111BE':roomA111BE, 'A111KI':roomA111KI, 'A111LI':roomA111LI, 'A112BA':roomA112BA, 'A112BE':roomA112BE, 'A112KI':roomA112KI, 'A112LI':roomA112LI, # A111 - A112
    'A100.14':roomA100_14, 'A100.15':roomA100_15, 'A113BA':roomA113BA, 'A113BE':roomA113BE, 'A113KI':roomA113KI, 'A113LI':roomA113LI, 'A114BA':roomA114BA, 'A114BE':roomA114BE, 'A114KI':roomA114KI, 'A114LI':roomA114LI, # A113 - A114
    'A100.16':roomA100_16, 'A100.17':roomA100_17, 'A115BA':roomA115BA, 'A115BE':roomA115BE, 'A115KI':roomA115KI, 'A115LI':roomA115LI, 'A116BA':roomA116BA, 'A116BE':roomA116BE, 'A116KI':roomA116KI, 'A116LI':roomA116LI, # A115 - A116
    'A100.18':roomA100_18, 'A100.19':roomA100_19, 'A117BA':roomA117BA, 'A117BE':roomA117BE, 'A117KI':roomA117KI, 'A117LI':roomA117LI, 'A118BA':roomA118BA, 'A118BE':roomA118BE, 'A118KI':roomA118KI, 'A118LI':roomA118LI, # A117 - A118
    'A100.20':roomA100_20, 'A100.21':roomA100_21, 'A119BA':roomA119BA, 'A119BE':roomA119BE, 'A119KI':roomA119KI, 'A119LI':roomA119LI, 'A120BA':roomA120BA, 'A120BE':roomA120BE, 'A120KI':roomA120KI, 'A120LI':roomA120LI, # A119 - A120
    # B
    'B100.01':roomB100_01, 'B100.02':roomB100_02, 'B101BA':roomB101BA, 'B101BE':roomB101BE, 'B101KI':roomB101KI, 'B101LI':roomB101LI, 'B102BA':roomB102BA, 'B102BE':roomB102BE, 'B102KI':roomB102KI, 'B102LI':roomB102LI, # B101 - B102
    'B100.03':roomB100_03, 'B100.04':roomB100_04, 'B103BA':roomB103BA, 'B103BE':roomB103BE, 'B103KI':roomB103KI, 'B103LI':roomB103LI, 'B104BA':roomB104BA, 'B104BE':roomB104BE, 'B104KI':roomB104KI, 'B104LI':roomB104LI, # B103 - B104
    'B100.05':roomB100_05, 'B100.06':roomB100_06, 'B105BA':roomB105BA, 'B105BE':roomB105BE, 'B105KI':roomB105KI, 'B105LI':roomB105LI, 'B106BA':roomB106BA, 'B106BE':roomB106BE, 'B106KI':roomB106KI, 'B106LI':roomB106LI, # B105 - B106
    'B100.07':roomB100_07, 'B100.08':roomB100_08, 'B107BA':roomB107BA, 'B107BE':roomB107BE, 'B107KI':roomB107KI, 'B107LI':roomB107LI, 'B108BA':roomB108BA, 'B108BE':roomB108BE, 'B108KI':roomB108KI, 'B108LI':roomB108LI, # B107 - B108
    'B100.09':roomB100_09, 'B100.10':roomB100_10, 'B109BA':roomB109BA, 'B109BE':roomB109BE, 'B109KI':roomB109KI, 'B109LI':roomB109LI, 'B110BA':roomB110BA, 'B110BE':roomB110BE, 'B110KI':roomB110KI, 'B110LI':roomB110LI, # B109 - B110
    'B100.11':roomB100_11, 'B100.11.1':roomB100_11_1, 'B100.11.2':roomB100_11_2, 'B100SR':roomB100SR,
    'B100.12':roomB100_12, 'B100.13':roomB100_13, 'B111BA':roomB111BA, 'B111BE':roomB111BE, 'B111KI':roomB111KI, 'B111LI':roomB111LI, 'B112BA':roomB112BA, 'B112BE':roomB112BE, 'B112KI':roomB112KI, 'B112LI':roomB112LI, # B111 - B112
    'B100.14':roomB100_14, 'B100.15':roomB100_15, 'B113BA':roomB113BA, 'B113BE':roomB113BE, 'B113KI':roomB113KI, 'B113LI':roomB113LI, 'B114BA':roomB114BA, 'B114BE':roomB114BE, 'B114KI':roomB114KI, 'B114LI':roomB114LI, # B113 - B114
    'B100.16':roomB100_16, 'B100.17':roomB100_17, 'B115BA':roomB115BA, 'B115BE':roomB115BE, 'B115KI':roomB115KI, 'B115LI':roomB115LI, 'B116BA':roomB116BA, 'B116BE':roomB116BE, 'B116KI':roomB116KI, 'B116LI':roomB116LI, # B115 - B116
    'B100.18':roomB100_18, 'B100.19':roomB100_19, 'B117BA':roomB117BA, 'B117BE':roomB117BE, 'B117KI':roomB117KI, 'B117LI':roomB117LI, 'B118BA':roomB118BA, 'B118BE':roomB118BE, 'B118KI':roomB118KI, 'B118LI':roomB118LI, # B117 - B118
    'B100.20':roomB100_20, 'B100.21':roomB100_21, 'B119BA':roomB119BA, 'B119BE':roomB119BE, 'B119KI':roomB119KI, 'B119LI':roomB119LI, 'B120BA':roomB120BA, 'B120BE':roomB120BE, 'B120KI':roomB120KI, 'B120LI':roomB120LI, # B119 - B120
    # M
    'M100.1':roomM100_1, 'M100.2':roomM100_2, 'M100.3':roomM100_3, 'M100.4':roomM100_4,
    'KBM100.1':roomKBM100_1, 'KBM100.2':roomKBM100_2, 'RM100':roomRM100,

    # Floor 2
    # A
    'A200.01':roomA200_01, 'A200.02':roomA200_02, 'A201BA':roomA201BA, 'A201BE':roomA201BE, 'A201KI':roomA201KI, 'A201LI':roomA201LI, 'A202BA':roomA202BA, 'A202BE':roomA202BE, 'A202KI':roomA202KI, 'A202LI':roomA202LI, # A101 - A102
    'A200.03':roomA200_03, 'A200.04':roomA200_04, 'A203BA':roomA203BA, 'A203BE':roomA203BE, 'A203KI':roomA203KI, 'A203LI':roomA203LI, 'A204BA':roomA204BA, 'A204BE':roomA204BE, 'A204KI':roomA204KI, 'A204LI':roomA204LI, # A103 - A104
    'A200.05':roomA200_05, 'A200.06':roomA200_06, 'A205BA':roomA205BA, 'A205BE':roomA205BE, 'A205KI':roomA205KI, 'A205LI':roomA205LI, 'A206BA':roomA206BA, 'A206BE':roomA206BE, 'A206KI':roomA206KI, 'A206LI':roomA206LI, # A105 - A106
    'A200.07':roomA200_07, 'A200.08':roomA200_08, 'A207BA':roomA207BA, 'A207BE':roomA207BE, 'A207KI':roomA207KI, 'A207LI':roomA207LI, 'A208BA':roomA208BA, 'A208BE':roomA208BE, 'A208KI':roomA208KI, 'A208LI':roomA208LI, # A107 - A108
    'A200.09':roomA200_09, 'A200.10':roomA200_10, 'A209BA':roomA209BA, 'A209BE':roomA209BE, 'A209KI':roomA209KI, 'A209LI':roomA209LI, 'A210BA':roomA210BA, 'A210BE':roomA210BE, 'A210KI':roomA210KI, 'A210LI':roomA210LI, # A109 - A110
    'A200.11':roomA200_11, 'A200.11.1':roomA200_11_1, 'A200.11.2':roomA200_11_2, 'A200SR':roomA200SR,
    'A200.12':roomA200_12, 'A200.13':roomA200_13, 'A211BA':roomA211BA, 'A211BE':roomA211BE, 'A211KI':roomA211KI, 'A211LI':roomA211LI, 'A212BA':roomA212BA, 'A212BE':roomA212BE, 'A212KI':roomA212KI, 'A212LI':roomA212LI, # A111 - A112
    'A200.14':roomA200_14, 'A200.15':roomA200_15, 'A213BA':roomA213BA, 'A213BE':roomA213BE, 'A213KI':roomA213KI, 'A213LI':roomA213LI, 'A214BA':roomA214BA, 'A214BE':roomA214BE, 'A214KI':roomA214KI, 'A214LI':roomA214LI, # A113 - A114
    'A200.16':roomA200_16, 'A200.17':roomA200_17, 'A215BA':roomA215BA, 'A215BE':roomA215BE, 'A215KI':roomA215KI, 'A215LI':roomA215LI, 'A216BA':roomA216BA, 'A216BE':roomA216BE, 'A216KI':roomA216KI, 'A216LI':roomA216LI, # A115 - A116
    'A200.18':roomA200_18, 'A200.19':roomA200_19, 'A217BA':roomA217BA, 'A217BE':roomA217BE, 'A217KI':roomA217KI, 'A217LI':roomA217LI, 'A218BA':roomA218BA, 'A218BE':roomA218BE, 'A218KI':roomA218KI, 'A218LI':roomA218LI, # A117 - A118
    'A200.20':roomA200_20, 'A200.21':roomA200_21, 'A219BA':roomA219BA, 'A219BE':roomA219BE, 'A219KI':roomA219KI, 'A219LI':roomA219LI, 'A220BA':roomA220BA, 'A220BE':roomA220BE, 'A220KI':roomA220KI, 'A220LI':roomA220LI, # A119 - A120
    # B
    'B200.01':roomB200_01, 'B200.02':roomB200_02, 'B201BA':roomB201BA, 'B201BE':roomB201BE, 'B201KI':roomB201KI, 'B201LI':roomB201LI, 'B202BA':roomB202BA, 'B202BE':roomB202BE, 'B202KI':roomB202KI, 'B202LI':roomB202LI, # B101 - B102
    'B200.03':roomB200_03, 'B200.04':roomB200_04, 'B203BA':roomB203BA, 'B203BE':roomB203BE, 'B203KI':roomB203KI, 'B203LI':roomB203LI, 'B204BA':roomB204BA, 'B204BE':roomB204BE, 'B204KI':roomB204KI, 'B204LI':roomB204LI, # B103 - B104
    'B200.05':roomB200_05, 'B200.06':roomB200_06, 'B205BA':roomB205BA, 'B205BE':roomB205BE, 'B205KI':roomB205KI, 'B205LI':roomB205LI, 'B206BA':roomB206BA, 'B206BE':roomB206BE, 'B206KI':roomB206KI, 'B206LI':roomB206LI, # B105 - B106
    'B200.07':roomB200_07, 'B200.08':roomB200_08, 'B207BA':roomB207BA, 'B207BE':roomB207BE, 'B207KI':roomB207KI, 'B207LI':roomB207LI, 'B208BA':roomB208BA, 'B208BE':roomB208BE, 'B208KI':roomB208KI, 'B208LI':roomB208LI, # B107 - B108
    'B200.09':roomB200_09, 'B200.10':roomB200_10, 'B209BA':roomB209BA, 'B209BE':roomB209BE, 'B209KI':roomB209KI, 'B209LI':roomB209LI, 'B210BA':roomB210BA, 'B210BE':roomB210BE, 'B210KI':roomB210KI, 'B210LI':roomB210LI, # B109 - B110
    'B200.11':roomB200_11, 'B200.11.1':roomB200_11_1, 'B200.11.2':roomB200_11_2, 'B200SR':roomB200SR,
    'B200.12':roomB200_12, 'B200.13':roomB200_13, 'B211BA':roomB211BA, 'B211BE':roomB211BE, 'B211KI':roomB211KI, 'B211LI':roomB211LI, 'B212BA':roomB212BA, 'B212BE':roomB212BE, 'B212KI':roomB212KI, 'B212LI':roomB212LI, # B111 - B112
    'B200.14':roomB200_14, 'B200.15':roomB200_15, 'B213BA':roomB213BA, 'B213BE':roomB213BE, 'B213KI':roomB213KI, 'B213LI':roomB213LI, 'B214BA':roomB214BA, 'B214BE':roomB214BE, 'B214KI':roomB214KI, 'B214LI':roomB214LI, # B113 - B114
    'B200.16':roomB200_16, 'B200.17':roomB200_17, 'B215BA':roomB215BA, 'B215BE':roomB215BE, 'B215KI':roomB215KI, 'B215LI':roomB215LI, 'B216BA':roomB216BA, 'B216BE':roomB216BE, 'B216KI':roomB216KI, 'B216LI':roomB216LI, # B115 - B116
    'B200.18':roomB200_18, 'B200.19':roomB200_19, 'B217BA':roomB217BA, 'B217BE':roomB217BE, 'B217KI':roomB217KI, 'B217LI':roomB217LI, 'B218BA':roomB218BA, 'B218BE':roomB218BE, 'B218KI':roomB218KI, 'B218LI':roomB218LI, # B117 - B118
    'B200.20':roomB200_20, 'B200.21':roomB200_21, 'B219BA':roomB219BA, 'B219BE':roomB219BE, 'B219KI':roomB219KI, 'B219LI':roomB219LI, 'B220BA':roomB220BA, 'B220BE':roomB220BE, 'B220KI':roomB220KI, 'B220LI':roomB220LI, # B119 - B120
    # M
    'M200.1':roomM200_1, 'M200.2':roomM200_2, 'M200.3':roomM200_3, 'M200.4':roomM200_4,

    # Floor 3
    # A
    'A300.01':roomA300_01, 'A300.02':roomA300_02, 'A301BA':roomA301BA, 'A301BE':roomA301BE, 'A301KI':roomA301KI, 'A301LI':roomA301LI, 'A302BA':roomA302BA, 'A302BE':roomA302BE, 'A302KI':roomA302KI, 'A302LI':roomA302LI, # A101 - A102
    'A300.03':roomA300_03, 'A300.04':roomA300_04, 'A303BA':roomA303BA, 'A303BE':roomA303BE, 'A303KI':roomA303KI, 'A303LI':roomA303LI, 'A304BA':roomA304BA, 'A304BE':roomA304BE, 'A304KI':roomA304KI, 'A304LI':roomA304LI, # A103 - A104
    'A300.05':roomA300_05, 'A300.06':roomA300_06, 'A305BA':roomA305BA, 'A305BE':roomA305BE, 'A305KI':roomA305KI, 'A305LI':roomA305LI, 'A306BA':roomA306BA, 'A306BE':roomA306BE, 'A306KI':roomA306KI, 'A306LI':roomA306LI, # A105 - A106
    'A300.07':roomA300_07, 'A300.08':roomA300_08, 'A307BA':roomA307BA, 'A307BE':roomA307BE, 'A307KI':roomA307KI, 'A307LI':roomA307LI, 'A308BA':roomA308BA, 'A308BE':roomA308BE, 'A308KI':roomA308KI, 'A308LI':roomA308LI, # A107 - A108
    'A300.09':roomA300_09, 'A300.10':roomA300_10, 'A309BA':roomA309BA, 'A309BE':roomA309BE, 'A309KI':roomA309KI, 'A309LI':roomA309LI, 'A310BA':roomA310BA, 'A310BE':roomA310BE, 'A310KI':roomA310KI, 'A310LI':roomA310LI, # A109 - A110
    'A300.11':roomA300_11, 'A300.11.1':roomA300_11_1, 'A300.11.2':roomA300_11_2, 'A300SR':roomA300SR,
    'A300.12':roomA300_12, 'A300.13':roomA300_13, 'A311BA':roomA311BA, 'A311BE':roomA311BE, 'A311KI':roomA311KI, 'A311LI':roomA311LI, 'A312BA':roomA312BA, 'A312BE':roomA312BE, 'A312KI':roomA312KI, 'A312LI':roomA312LI, # A111 - A112
    'A300.14':roomA300_14, 'A300.15':roomA300_15, 'A313BA':roomA313BA, 'A313BE':roomA313BE, 'A313KI':roomA313KI, 'A313LI':roomA313LI, 'A314BA':roomA314BA, 'A314BE':roomA314BE, 'A314KI':roomA314KI, 'A314LI':roomA314LI, # A113 - A114
    'A300.16':roomA300_16, 'A300.17':roomA300_17, 'A315BA':roomA315BA, 'A315BE':roomA315BE, 'A315KI':roomA315KI, 'A315LI':roomA315LI, 'A316BA':roomA316BA, 'A316BE':roomA316BE, 'A316KI':roomA316KI, 'A316LI':roomA316LI, # A115 - A116
    'A300.18':roomA300_18, 'A300.19':roomA300_19, 'A317BA':roomA317BA, 'A317BE':roomA317BE, 'A317KI':roomA317KI, 'A317LI':roomA317LI, 'A318BA':roomA318BA, 'A318BE':roomA318BE, 'A318KI':roomA318KI, 'A318LI':roomA318LI, # A117 - A118
    'A300.20':roomA300_20, 'A300.21':roomA300_21, 'A319BA':roomA319BA, 'A319BE':roomA319BE, 'A319KI':roomA319KI, 'A319LI':roomA319LI, 'A320BA':roomA320BA, 'A320BE':roomA320BE, 'A320KI':roomA320KI, 'A320LI':roomA320LI, # A119 - A120
    # B
    'B300.01':roomB300_01, 'B300.02':roomB300_02, 'B301BA':roomB301BA, 'B301BE':roomB301BE, 'B301KI':roomB301KI, 'B301LI':roomB301LI, 'B302BA':roomB302BA, 'B302BE':roomB302BE, 'B302KI':roomB302KI, 'B302LI':roomB302LI, # B101 - B102
    'B300.03':roomB300_03, 'B300.04':roomB300_04, 'B303BA':roomB303BA, 'B303BE':roomB303BE, 'B303KI':roomB303KI, 'B303LI':roomB303LI, 'B304BA':roomB304BA, 'B304BE':roomB304BE, 'B304KI':roomB304KI, 'B304LI':roomB304LI, # B103 - B104
    'B300.05':roomB300_05, 'B300.06':roomB300_06, 'B305BA':roomB305BA, 'B305BE':roomB305BE, 'B305KI':roomB305KI, 'B305LI':roomB305LI, 'B306BA':roomB306BA, 'B306BE':roomB306BE, 'B306KI':roomB306KI, 'B306LI':roomB306LI, # B105 - B106
    'B300.07':roomB300_07, 'B300.08':roomB300_08, 'B307BA':roomB307BA, 'B307BE':roomB307BE, 'B307KI':roomB307KI, 'B307LI':roomB307LI, 'B308BA':roomB308BA, 'B308BE':roomB308BE, 'B308KI':roomB308KI, 'B308LI':roomB308LI, # B107 - B108
    'B300.09':roomB300_09, 'B300.10':roomB300_10, 'B309BA':roomB309BA, 'B309BE':roomB309BE, 'B309KI':roomB309KI, 'B309LI':roomB309LI, 'B310BA':roomB310BA, 'B310BE':roomB310BE, 'B310KI':roomB310KI, 'B310LI':roomB310LI, # B109 - B110
    'B300.11':roomB300_11, 'B300.11.1':roomB300_11_1, 'B300.11.2':roomB300_11_2, 'B300SR':roomB300SR,
    'B300.12':roomB300_12, 'B300.13':roomB300_13, 'B311BA':roomB311BA, 'B311BE':roomB311BE, 'B311KI':roomB311KI, 'B311LI':roomB311LI, 'B312BA':roomB312BA, 'B312BE':roomB312BE, 'B312KI':roomB312KI, 'B312LI':roomB312LI, # B111 - B112
    'B300.14':roomB300_14, 'B300.15':roomB300_15, 'B313BA':roomB313BA, 'B313BE':roomB313BE, 'B313KI':roomB313KI, 'B313LI':roomB313LI, 'B314BA':roomB314BA, 'B314BE':roomB314BE, 'B314KI':roomB314KI, 'B314LI':roomB314LI, # B113 - B114
    'B300.16':roomB300_16, 'B300.17':roomB300_17, 'B315BA':roomB315BA, 'B315BE':roomB315BE, 'B315KI':roomB315KI, 'B315LI':roomB315LI, 'B316BA':roomB316BA, 'B316BE':roomB316BE, 'B316KI':roomB316KI, 'B316LI':roomB316LI, # B115 - B116
    'B300.18':roomB300_18, 'B300.19':roomB300_19, 'B317BA':roomB317BA, 'B317BE':roomB317BE, 'B317KI':roomB317KI, 'B317LI':roomB317LI, 'B318BA':roomB318BA, 'B318BE':roomB318BE, 'B318KI':roomB318KI, 'B318LI':roomB318LI, # B117 - B118
    'B300.20':roomB300_20, 'B300.21':roomB300_21, 'B319BA':roomB319BA, 'B319BE':roomB319BE, 'B319KI':roomB319KI, 'B319LI':roomB319LI, 'B320BA':roomB320BA, 'B320BE':roomB320BE, 'B320KI':roomB320KI, 'B320LI':roomB320LI, # B119 - B120
    # M
    'M300.1':roomM300_1, 'M300.2':roomM300_2, 'M300.3':roomM300_3, 'M300.4':roomM300_4,
}

room = roomA303LI