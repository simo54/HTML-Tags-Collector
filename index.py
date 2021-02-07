import requests
from tkinter import *

root = Tk()
root.title("Test")
root.geometry("600x300")

##################### CREATING WIDGETS #####################
button_intro = Button(root, text="hello!")
button_quit = Button(root, text="Quit", command=root.quit)

input_url = Entry(root, width=50)

##################### FUNCTIONALITIES #####################


##################### DISPLAYING WIDGETS #####################
button_intro.pack()
button_quit.pack()
input_url.pack()


# ================ Runner ================ #
root.mainloop()
