import tkinter
from tkinter import *


class PlayerEntry:
    def __init__(self):
        #self.playerID = None
        #self.playerCodename = None
        self.m = tkinter.Tk(screenName="player entry", baseName="photon", className="photon")
        self.m.geometry("1400x800+100+100")
        self.m.configure(bg='black')
        self.create_widgets()

    def validate_id(self, input):
      if input.isdigit() or input == "":
            return True
      else:
            return False

    def pushPlayers(self):
      global playerID, playerCodename
      #playerID = playerIdEntry.get()
      #playerCodename = playerCodenameEntry.get()
      if not playerID or not playerCodename:
        print("Both entries must be filled")
        return
      #print(f"Player ID: {playerID}, Player Codename: {playerCodename}")

      self.playerIdEntry.delete(0, END)
      self.playerCodenameEntry.delete(0, END) 

    def create_widgets(self):  
      validate_id_cmd = self.m.register(self.validate_id)

      idLabel = Label(self.m, text="ID")
      codename = Label(self.m, text="Codename")
      idLabel.grid(row=0, column=0)
      codename.grid(row=0, column=1)

      self.playerIdEntry = Entry(self.m, validate="key", validatecommand=(validate_id_cmd, '%P'))
      self.playerCodenameEntry = Entry(self.m)

      self.playerIdEntry.grid(row=1, column=0)
      self.playerCodenameEntry.grid(row=1, column=1)

      submitButton = Button(self.m, text="Submit", command=self.pushPlayers)
      submitButton.grid(row=2, column=0)
    
    def run(self):
        self.m.mainloop()
