class ArtGallery:
    def __init__(self, gallery_name, gallery_location):
        self.gallery_name = gallery_name
        self.gallery_location = gallery_location
        self.artworks = []
        print(f"\nWelcome to {self.gallery_name}!!")
        print(f"location : {self.location}" )
        print(f"art gallery is ready!")
    def add_artworks(self, artwork):
        self.artworks.append(artwork) 
        print(f"'{artwork}' has successfully been added!")
    def remove_artworks(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' has successfully been removed!")
        else :
            print(f"'{artwork}' was not found in gallery...")
    def display_artworks(self) :
        print(f"\n---{self.gallery_name} Art collection---")
        if self.artworks :
            for number, artwork in enumerate(self.artworks, 1):
                print(f"{number} . {artwork}")
            else:
                print("No artworks have been added yet")
    def __del__(self):
        print(f"\nClosing {self.gallery_name}. Thank you for managing the collection!")
Gallery = ArtGallery("creative art gallery" , "Bengaluru")
while True:
    print("\n=========ART GALLERY=========")
    print("1. Add artwork")
    print("2. Remove artwork")
    print("3. Display art collection")
    print("4. Quit")
    print("===================================")
    choice = input("Enter your choice :")
    if choice == "1" :
        artwork_name = input("Enter artwork to be added :")
        Gallery.add_artwork(artwork_name)
    elif choice == "2":
        artwork_name = input("Enter artwork to remove :")
        Gallery.remove_artwork(artwork_name)
    elif choice == "3":
        Gallery.display_artworks()
    elif choice == "4" :
        print("Quiting art gallery")
        del Gallery
        break
    else:
        print("Invalid choice,please enter number from 1 to 4.")

