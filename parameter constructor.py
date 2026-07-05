class playlist:
    def __init__(self,name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"playlist '{self.name}' '{self.genre}' is ready!")
    def add_song(self, song):
       self.songs.append(song)
       print(f" '{song}' added to {self.name}")
    def remove_song(self, song):
         if song in self.songs:
            self.songs.remove(song)
            print(f" '{song}' removed")
         else:
              print(f"No songs yet, add some!")
    def del_(self):
         print(f"playlist '{self.name}' has been deleted. Goodbye!")
my_playlist = playlist("roadtrip Mix", "pop")
while True:
      print("\n1. add song  2.Remove song   3. View playlist   4. Quit and delete")
      choice = input("Enter your choice: ")
      if choice == "1":
            song = input("Enter song name: ")
            my_playlist.add_song(song)
      elif choice == "2":
            song = input("Enter song to remove: ")
            my_playlist.remove_song(song)
      elif choice == "3":
            my_playlist.display()
      elif choice == "4":
            del my_playlist
            break
      else :
            print("Invalid choic, enter 1, 2, 3 or 4.")




