from abc import ABC, abstractmethod
class instrument(ABC):
    def __init__(self, name, category):
        self.name= name
        self.category = category
    def display_info(self):
        print(f"Instrument name : {self.name}")
        print(f"Category : {self.category}")
    @abstractmethod
    def play_sound(self):
        pass
class violin(instrument):
    def __init__(self, name, category, strings):
        super().__init__(name, category)
        self.strings = strings
    def play_sound(self):
        print(f"{self.name} has {self.strings} strings and sounds like :strum strum!")
class piano(instrument):
    def __init__(self, name, category):
        super().__init__(name, category)
        self.piano_type  = piano_type
    def play_sound(self):
        print(f"{self.name} is a {self.piano_type} and sounds like : ting ting!")
instrument_1 = violin("Modern violin", "string instrument", 4)
instrument_2 = piano("Grand piano", "hybrid instrument", "large piano")
print("=====Music Instrument Sound Show=====")

instrument_1.display_info()
instrument_1.play_sound()

print()

instrument_2.display_info()
instrument_2.play_sound()

print()