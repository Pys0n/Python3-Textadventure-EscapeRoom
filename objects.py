class Object:
    def __init__(self, name, item, steps_per_s):
        self.name = name
        self.item = item
        self.steps_per_s = steps_per_s    # int in sec

class Book(Object):
    def __init__(self, item=None):
        super().__init__('Buch', item, 10)

class Bookpile(Object):
    def __init__(self, item=None):
        super().__init__('Bücherstapel', item, 2)

class Rubbishbin(Object):
    def __init__(self, item=None):
        super().__init__('Mülleimer', item, 5)

class Shelf(Object):
    def __init__(self, item=None):
        super().__init__('Regal', item, 5)

class Plant(Object):
    def __init__(self, item=None):
        super().__init__('Pflanze', item, 5)

class Table(Object):
    def __init__(self, item=None):
        super().__init__('Tisch', item, 3.3)

class Wardrobe(Object):
    def __init__(self, item=None):
        super().__init__('Kleiderschrank', item, 2)

class Bed(Object):
    def __init__(self, item=None):
        super().__init__('Bett', item, 2)

class Chair(Object):
    def __init__(self, item=None):
        super().__init__('Stuhl', item, 2.5)

class Fridge(Object):
    def __init__(self, item=None):
        super().__init__('Kühlschrank', item, 2.5)

class Socket(Object):
    def __init__(self, item=None):
        super().__init__('Steckdose', item, 5)

class Window(Object):
    def __init__(self, item=None):
        super().__init__('Fenster', item, 5)

class Mobile(Object):
    def __init__(self, item=None):
        super().__init__('Handy', item, 10)

class Computer(Object):
    def __init__(self, item=None):
        super().__init__('Computer', item, 5)

class Notebook(Object):
    def __init__(self, item=None):
        super().__init__('Laptop', item, 5)

class Paper(Object):
    def __init__(self, item=None):
        super().__init__('Papier', item, 100)

class Pen(Object):
    def __init__(self, item=None):
        super().__init__('Stift', item, 50)

class Painting(Object):
    def __init__(self, item=None):
        super().__init__('Gemälde', item, 10)

class Toilet(Object):
    def __init__(self, item=None):
        super().__init__('Toilette', item, 3.3)

class Diary(Object):
    def __init__(self, item=None):
        super().__init__('Tagebuch', item, 1)

# SECRET

class Secret(Object):
    def __init__(self, item):
        super().__init__('SECRET', item, 0.5)