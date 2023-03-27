from tkinter import *
import random


window = Tk()

play_zone = Canvas(window, width=600, height=600, bg="white")
score_zone = Canvas(window, width=600, height=100, bg="orange")
play_zone.pack()
score_zone.pack()

colors = ['green', 'red', 'blue', 'orange']
count = 0


def click_on_circle(event):
    global count
    count += 1
    score_zone.delete(ALL)
    score_zone.create_text(80, 30, font='Arial 18', text='Ball')
    score_zone.create_text(180, 30, font='Arial 20', text=str(count))


def ball():
    play_zone.delete(ALL)
    x = random.randint(10, 580)
    y = random.randint(10, 580)
    r = 30
    new_ball = play_zone.create_oval(x, y, x + r, y + r, fill=random.choice(colors), width=0)
    play_zone.tag_bind(new_ball, '<Button-1>', click_on_circle)
    window.after(1500, ball)


ball()

window.mainloop()
