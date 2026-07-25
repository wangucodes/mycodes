class pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health
    def show_info(self):
        print(f"pet name: {self.name}")
        print(f"health level: {self.__health}")
    def care_action(self):
        print(f"{self.name} needs general care")
    def set_health(self, new_health):
        if new_health >=0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s healthhas been updated to {new_health}")
        else:
            print(f"Health must be between 0 and 100")
class hedgehog(pet):
    def care_action(self):
        print(f"{self.name} needs a running wheel and morebugs in diet")
class cat(pet):
    def care_action(self):
        print(f"{self.name} needs more rest and matted fur removed ")
class pufferfish(pet):
    def care_action(self):
        print(f"{self.name} needs a bigger tank with filtered water")

hedgehog = hedgehog("silver", 30)
cat = cat("lily", 60)
pufferfish = pufferfish("spike", 10)
pets = [hedgehog, cat, pufferfish]
print("=====My pet healthcare=====")
for pet in pets:
    pet.show_info()
    pet.care_action()
    print()
print("=====Updating pet health=====")
hedgehog.set_health(90)
cat.set_health(85)
pufferfish.set_health(79)
print("=====Final healthcare summary=====")
for pet in pets:
    pet.show_info()
    print()