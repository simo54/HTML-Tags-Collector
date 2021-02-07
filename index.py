import requests
import validators
import html.parser
from bs4 import BeautifulSoup
from tkinter import *

# ================ GUI Specifications ================ #
root = Tk()
root.title("Test")
root.geometry("600x300")

##################### FUNCTIONALITIES #####################


def start():
    url = input_url.get()
    validation = validators.url(url)

    if validation == True:
        print('Works')
        f = requests.get(url)
        soup = BeautifulSoup(f.text, 'html.parser')
        print(soup.prettify())
    else:
        print("Please insert a valid URL")


##################### CREATING WIDGETS #####################
button_start = Button(root, text="Start", command=start)
button_quit = Button(root, text="Quit", command=root.quit)
input_url = Entry(root, width=50)

##################### DISPLAYING WIDGETS #####################
button_start.pack()
input_url.pack()
button_quit.pack()

# ================ Runner ================ #
root.mainloop()
