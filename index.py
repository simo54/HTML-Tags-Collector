import requests
import validators
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
        f = requests.get(url)
        soup = BeautifulSoup(f.text, 'html.parser')
        rawtagsList = []
        for tag in soup.find_all():
            rawtagsList.append(tag.name)

        cleanList = list(dict.fromkeys(rawtagsList))

        for uniqueTag in cleanList:
            tagLabelName = uniqueTag
            labelTags = Label(root, text=tagLabelName)
            labelTags.pack()
    else:
        print("Please insert a valid URL")


##################### CREATING WIDGETS #####################

button_start = Button(root, text="Start", padx=10, pady=5, command=start)
button_quit = Button(root, text="Quit", padx=10, pady=5, command=root.quit)
input_url = Entry(root, width=70)

##################### DISPLAYING WIDGETS #####################

button_start.pack()
input_url.pack()
button_quit.pack()

# ================ Runner ================ #

root.mainloop()
