import tkinter


root = tkinter.Tk()  # объект главного окна
root.geometry("600x600")


def change_image():
    image_font.destroy()
    button1.destroy()
    image_font2 = tkinter.Label(root, image=font2)
    image_font2.pack()


label1 = tkinter.Label(text="Привет")
label1.pack()

font = tkinter.PhotoImage(file='cat.png')

font2 = tkinter.PhotoImage(file='rainbow.png')
image_font = tkinter.Label(root, image=font)
image_font.pack()

button1 = tkinter.Button(text="НАЖМИ", command=change_image)
button1.pack()

root.mainloop()  # главный цикл событий