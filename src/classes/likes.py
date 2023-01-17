from tkinter import *
from tkinter import ttk

count = 0
def click_button():
    global count
    if count == 0:
        count += 1
    else:
        count -= 1
    btn["text"] = f"Likes {count}"


root = Tk()
root.title("Likes")
root.geometry("250x150")

while True:
    btn = ttk.Button(text="Like", command=click_button)
    btn.pack()

    root.mainloop()
