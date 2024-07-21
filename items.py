class Item:
    def __init__(self, name):
        self.name = name

# Keys, Keycards

class GreenKey(Item):
    def __init__(self):
        super().__init__('Green Key')

class GoldenKey(Item):
    def __init__(self):
        super().__init__('Golden Key')

class GreenKeycard(Item):
    def __init__(self):
        super().__init__('Green Keycard')

class YellowKeycard(Item):
    def __init__(self):
        super().__init__('Yellow Keycard')

class WhiteKeycard(Item):
    def __init__(self):
        super().__init__('White Keycard')

class BlueKeycard(Item):
    def __init__(self):
        super().__init__('Blue Keycard')

class RedKeycard(Item):
    def __init__(self):
        super().__init__('Red Keycard')

# Note

class Note(Item):
    def __init__(self, text):
        super().__init__('Note')
        self.text = text

class MobileMessage(Item):
    def __init__(self, text):
        super().__init__('Smartphone-Message')
        self.text = text

class DiaryEntry(Item):
    def __init__(self, text):
        super().__init__('Diary-Entry')
        self.text = text

class CarpetText(Item):
    def __init__(self, text):
        super().__init__('Carpet-Text')
        self.text = text

class BreakingNews(Item):
    def __init__(self, text):
        super().__init__('Breaking News')
        self.text = text
    
    def reloadText(self, text):
        self.text = text

# SECRET

class SecretText(Item):
    def __init__(self, text):
        super().__init__('Secret')
        self.text = text
        self.type = 'secret'