class Item:
    def __init__(self, name):
        self.name = name

# Keys, Keycards

class GreenKey(Item):
    def __init__(self):
        super().__init__('Grüner Schlüssel')

class GoldenKey(Item):
    def __init__(self):
        super().__init__('Goldener Schlüssel')

class GreenKeycard(Item):
    def __init__(self):
        super().__init__('Grüne Keycard')

class YellowKeycard(Item):
    def __init__(self):
        super().__init__('Gelbe Keycard')

class WhiteKeycard(Item):
    def __init__(self):
        super().__init__('Weiße Keycard')

class BlueKeycard(Item):
    def __init__(self):
        super().__init__('Blaue Keycard')

class RedKeycard(Item):
    def __init__(self):
        super().__init__('Rote Keycard')

# Note

class Note(Item):
    def __init__(self, text):
        super().__init__('Notiz')
        self.text = text

class MobileMessage(Item):
    def __init__(self, text):
        super().__init__('Handy-Nachricht')
        self.text = text

class DiaryEntry(Item):
    def __init__(self, text):
        super().__init__('Tagebuch-Eintrag')
        self.text = text

# SECRET

class SecretText(Item):
    def __init__(self, text):
        super().__init__('Secret')
        self.text = text
        self.type = 'secret'