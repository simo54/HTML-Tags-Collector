import requests
import validators
from bs4 import BeautifulSoup
from tkinter import messagebox, Tk, Label, Button, Entry, Frame

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
        i_grid = 5
        for uniqueTag in cleanList:
            # tagLabelName = uniqueTag
            # labelTags = Label(root, text=uniqueTag)
            # labelTags.pack()
            boxText.insert(0, uniqueTag + ", ")

    else:
        print("Please insert a valid URL")


def popup():
    messagebox.showinfo(
        "Credits", "This script can be used/modified/implemented/tested with a free license use. \n\nAuthor: simo54 => https://github.com/simo54")

##################### CREATING WIDGETS #####################


button_start = Button(root, text="Start", padx=10, pady=5, command=start)
button_quit = Button(root, text="Quit", padx=10, pady=5, command=root.quit)
input_url = Entry(root, width=70)
button_credits = Button(root, text="Credits", padx=10, pady=5, command=popup)
boxText = Entry(root, width=70)

##################### DISPLAYING WIDGETS #####################

button_start.pack()
input_url.pack()
button_quit.pack()
button_credits.pack()
boxText.pack()

# ================ Runner ================ #

root.mainloop()
