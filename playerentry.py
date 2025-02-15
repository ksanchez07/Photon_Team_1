import tkinter
from tkinter import *

m = tkinter.Tk(screenName="player entry", baseName="photon", className="photon")
m.geometry("800x600")
m.configure(bg='black')

playerID = None
playerCodename = None

def validate_id(input):
    if input.isdigit() or input == "":
        return True
    else:
        return False

def pushPlayers():
    global playerID, playerCodename
    playerID = playerIdEntry.get()
    playerCodename = playerCodenameEntry.get()
    if not playerID or not playerCodename:
        print("Both entries must be filled")
        return
    print(f"Player ID: {playerID}, Player Codename: {playerCodename}")
    
    playerIdEntry.delete(0, END)
    playerCodenameEntry.delete(0, END)    

validate_id_cmd = m.register(validate_id)

idLabel = Label(m, text="ID")
codename = Label(m, text="Codename")
idLabel.grid(row=0, column=0)
codename.grid(row=0, column=1)

playerIdEntry = Entry(m, validate="key", validatecommand=(validate_id_cmd, '%P'))
playerCodenameEntry = Entry(m)

playerIdEntry.grid(row=1, column=0)
playerCodenameEntry.grid(row=1, column=1)

submitButton = Button(text="Submit", command=pushPlayers)
submitButton.grid(row=2, column=0)

m.mainloop()