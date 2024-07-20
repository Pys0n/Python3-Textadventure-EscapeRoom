class Object:
    def __init__(self, name, item, steps_per_s):
        self.name = name
        self.item = item
        self.steps_per_s = steps_per_s    # int in sec

class Book(Object):
    def __init__(self, item=None):
        super().__init__('Book', item, 10)

class Bookpile(Object):
    def __init__(self, item=None):
        super().__init__('Bookpile', item, 2)

class Rubbishbin(Object):
    def __init__(self, item=None):
        super().__init__('Trash Bin', item, 5)

class Shelf(Object):
    def __init__(self, item=None):
        super().__init__('Shelf', item, 5)

class Plant(Object):
    def __init__(self, item=None):
        super().__init__('Plant', item, 5)

class Table(Object):
    def __init__(self, item=None):
        super().__init__('Table', item, 3.3)

class Wardrobe(Object):
    def __init__(self, item=None):
        super().__init__('Wardrobe', item, 2)

class Bed(Object):
    def __init__(self, item=None):
        super().__init__('Bed', item, 2)

class Chair(Object):
    def __init__(self, item=None):
        super().__init__('Chair', item, 2.5)

class Fridge(Object):
    def __init__(self, item=None):
        super().__init__('Fridge', item, 2.5)

class Socket(Object):
    def __init__(self, item=None):
        super().__init__('Socket', item, 5)

class Window(Object):
    def __init__(self, item=None):
        super().__init__('Window', item, 5)

class Mobile(Object):
    def __init__(self, item=None):
        super().__init__('Smartphone', item, 10)

class Computer(Object):
    def __init__(self, item=None):
        super().__init__('Computer', item, 5)

class Notebook(Object):
    def __init__(self, item=None):
        super().__init__('Notebook', item, 5)

class Paper(Object):
    def __init__(self, item=None):
        super().__init__('Paper', item, 100)

class Pen(Object):
    def __init__(self, item=None):
        super().__init__('Pen', item, 50)

class Painting(Object):
    def __init__(self, item=None):
        super().__init__('Painting', item, 10)

class Toilet(Object):
    def __init__(self, item=None):
        super().__init__('Toilet', item, 3.3)

class Diary(Object):
    def __init__(self, item=None):
        super().__init__('Diary', item, 2)

class BedsideTable(Object):
    def __init__(self, item=None):
        super().__init__('Bedside table', item, 3.3)

class Couch(Object):
    def __init__(self, item=None):
        super().__init__('Couch', item, 2)

class TV(Object):
    def __init__(self, item=None):
        super().__init__('TV', item, 4)

class TVTable(Object):
    def __init__(self, item=None):
        super().__init__('TV-Table', item, 3.3)

class RemoteControl(Object):
    def __init__(self, item=None):
        super().__init__('Remote control', item, 10)

class CoffeeTable(Object):
    def __init__(self, item=None):
        super().__init__('Coffee table', item, 3.3)

class Armchair(Object):
    def __init__(self, item=None):
        super().__init__('Armchair', item, 3.3)

class Bathtub(Object):
    def __init__(self, item=None):
        super().__init__('Bathtub', item, 3.3)

class Shower(Object):
    def __init__(self, item=None):
        super().__init__('Shower', item, 3.3)

class Washbasin(Object):
    def __init__(self, item=None):
        super().__init__('Washbasin', item, 5)

class ToiletPaper(Object):
    def __init__(self, item=None):
        super().__init__('Toilet paper', item, 5)

class Towel(Object):
    def __init__(self, item=None):
        super().__init__('Towel', item, 5)

class Mirror(Object):
    def __init__(self, item=None):
        super().__init__('Mirror', item, 5)

class Stove(Object):
    def __init__(self, item=None):
        super().__init__('Stove', item, 5)

class Oven(Object):
    def __init__(self, item=None):
        super().__init__('Oven', item, 2)

class KitchenCupboard(Object):
    def __init__(self, item=None):
        super().__init__('Kitchen cupboard', item, 2)

class Carpet(Object):
    def __init__(self, item=None):
        super().__init__('Carpet', item, 2)

class Carton(Object):
    def __init__(self, item=None):
        super().__init__('Carton', item, 3.3)

class StorageShelf(Object):
    def __init__(self, item=None):
        super().__init__('Storage shelf', item, 2)

class KeyHook(Object):
    def __init__(self, item=None):
        super().__init__('Key hook', item, 100)
        if item != None:
            self.name = 'Key hook: '+item.name

class PC(Object):
    def __init__(self, item=None):
        super().__init__('PC', item, 5)

class Birthdaycake(Object):
    def __init__(self, item=None):
        super().__init__('Birthday cake', item, 5)

class Bar(Object):
    def __init__(self, item=None):
        super().__init__('Bar', item, 2)

class Gift(Object):
    def __init__(self, item=None, name=None):
        super().__init__('Gift', item, 5)
        if name != None:
            self.name = 'Gift from '+name

# SECRET

class Secret(Object):
    def __init__(self, item):
        super().__init__('SECRET', item, 0.5)