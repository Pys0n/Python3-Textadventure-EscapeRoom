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
        super().__init__('Diary', item, 1)

# SECRET

class Secret(Object):
    def __init__(self, item):
        super().__init__('SECRET', item, 0.5)