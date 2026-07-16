class gallery:
    def __init__(self, name, form):
        self.name = name
        self.form = form
        self.art = []
        print(f"gallery '{self.name}' '{self.form}' is ready!")
    def add_art(self, art):
        self.art.append(art)
        print(f"'{art}' added to '{self.name}'")
    def remove_art(self, art):
        if art in self.art:
            self.art.remove(art)
            print(f"'{art}' removed!")
        else:
            print(f"No art work yet, add some pieces!")
    def del_(self):
        print(f"gallery '{self.name}' has been deleted, bye bye!")
my_gallery = gallery("visual arts", "performing arts")
while True:
    print("\n 1. add artwork  2. delete artwork  3.display artwork  4. quit and delete")
    choice = input("Enter your choice :")
    if choice == "1":
        art = input("Enter art piece :")
        my_gallery.add_art(art)
    elif choice == "2":
        art = input("Enter art piece to remove :")
        my_gallery.remove_art(art)
    elif choice == "3" :
        my_gallery.display()
    elif choice == "4" :
        del my_gallery
        break
    else:
        print("Invalid choice, please enter 1, 2, 3 or 4.")
    