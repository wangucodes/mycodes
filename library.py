books = ["Alice in wonderland", "Wind up chronicle bird", "Crime and punishment", "princess and the peas"]

print("Library book list:", books)
print("Total books:", len(books))
print("First book:", books[0])
print("second book:", books[-1])
print("First three books:", books[:3])
books.append("ariel")
print("After adding a book:", books)
books.remove("Crime and punishment")
print("After removing a book:", books)
books.sort()
print("Books sorted in alphabetical order:", books)
books.reverse()
print("Books in reverse order:", books)
librarian = {
    "name": "Ms.lida",
    "section": "adult section",
    "experience" : "6"
}
print("librarian profile:", librarian)
print("Librarian name:", librarian["name"])
print("Librarian section:", librarian["section"])
print("Experience:", librarian.get("experience"))
librarian["experience"] = 6
print("Updated experience:", librarian)
librarian["email"] = "lida@schoollibrary.com"
print("After addingemail:", librarian)
librarian.pop("section")
print("After removing section:", librarian)
book_ids = [401, 402, 403, 404]
book_names = ["Alice in wonderland", "Wind up chronicle bird", "Crime and punishment", "princess and the peas"]
book_directory = dict(zip(book_ids, book_names))
print("Book directorgy:", book_directory)
print("\n=32")
print("Library organiser summary")
print("\n=32")
print("Available books:", books)
print("Librarian details:", librarian)
print("BookID directory:", book_directory)
print("\n=32")