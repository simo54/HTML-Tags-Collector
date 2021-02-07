from tkinter import *

root = Tk()

button_intro = Button(root, text="hello!")
button_quit = Button(root, text="Quit", command=root.quit)

button_intro.pack()
button_quit.pack()

root.mainloop()
