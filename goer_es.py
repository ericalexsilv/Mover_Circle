from tkinter import HIDDEN, Canvas, Tk, NORMAL
HEIGHT = 716
WIDTH = 1120
window = Tk()
window.title('Goer ES')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='light blue')
goer = c.create_oval(0, 0, 30, 30, outline='red', state=NORMAL)
c.pack()
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(goer, MID_X, MID_Y)
def move_goer(event):
    if event.keysym == 'Up':
        c.move(goer, 0, -5)
    elif event.keysym == 'Down':
        c.move(goer, 0, 5)
    elif event.keysym == 'Left':
        c.move(goer, -5, 0)
    elif event.keysym == 'Right':
        c.move(goer, 5, 0)
c.bind_all('<Key>', move_goer)

