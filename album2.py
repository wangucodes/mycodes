from tkinter import *
from tkinter import messagebox
from PIL import Image, imageTK
window = Tk()
window.title("my photo album")
window.geometry("450x500")
window.config(bg="lavendar")
title_label = Label(
    window,
    text = "my photo album",
    font = ("arial", 20, "bold"),
    fg = "white",
    bg = "purple",
    width = 25
)
title_label.pack(pady=15)
image_file = Image.open("images.jpeg")
image_file = image_file.resize(300, 200)
photo = imageTK.photoImage(image_file)
image_file = Label(window, image=photo, bg ="lavendar")
def show_reaction():
    messagebox.showinfo(
        "photo reaction"
        "This is a beautiful memory"
    )
def open_photo_details():
    details_window = Toplevel(window)
    details_window.title("photo details")
    details_window.geometry("350x250")
    details_window.config(bg = "lightyellow")
    heading = Label(
        details_window,
        text = "photo details",
        font = ("arial", 16, "bold"),
        bg = "lightyellow",
        fg = "purple"
    )
    heading.pack(pady=15)
    details = Label(
        details_window, 
        text = "photo name: my favourite memory\n"
        "category: personal album\n"
        "description: a special photo saved in my album.",
        font = ("arial", 11),
        bg = "lightyellow",
        justify = "left"
    )
    details.pack(pady=10)
    close_button = Button(
        details_window,
        text = "close",
        bg = "purple",
        fg = "white",
        command = details_window.destroy
    )
    close_button.pack(pady=15)
reaction_button = Button(
    window,
    text = "react to photo",
    font=("arial", 12, "bold"),
    bg ="blue",
    fg = "white",
    command = show_reaction
)
reaction_button.pack(pady=10)
details_button = Button(
    window,
    text = "view photo details",
    font = ("arial", 12, "bold"),
    bg = "green",
    fg = "white",
    command = open_photo_details
)
details_button.pack(pady=10)
window.mainloop()
