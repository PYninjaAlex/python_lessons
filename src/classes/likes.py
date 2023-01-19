from tkinter import *
from tkinter import ttk

likes = 0
def click_button():
    global likes
    if likes == 0:
        likes += 1
    else:
        likes -= 1
    btn["text"] = f"Likes {likes}"


root = Tk()
root.title("Likes")
root.geometry("250x150")

btn = ttk.Button(text="Like", command=click_button)
btn.pack()

root.mainloop()
