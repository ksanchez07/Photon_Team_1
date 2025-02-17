import tkinter

from tkinter import *

import socket





class PlayerEntry:

    

    def __init__(self):

        #self.playerID = None

        #self.playerCodename = None

        self.m = tkinter.Tk()

        self.m.title("Entry Terminal")

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

      if not self.playerIdEntry or not self.playerCodenameEntry:

        print("Both entries must be filled")

        return

      #print(f"Player ID: {playerID}, Player Codename: {playerCodename}")



      #UPD Socket code to send the player entries to server



      #reading the ip from text file and setting it to localIp

      with open("network.txt", "r") as file:

        localIp = file.read()



      #the server we are sending the information to

      #if it says network is being used changed the port(7501) here and on server to a different number,

      #use the same number for both files though

      trafficAddressPort = (localIp, 7501)

      bufferSize = 1024



      #creating client side socket

      UPDClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

      #inputting player information

      print(self.playerCodenameEntry)

      msgFromClient = str(str(self.playerIdEntry.get()) + ":" + str(self.playerCodenameEntry.get()))

      bytesToSend = str.encode(msgFromClient)

      #sending the information to ther server

      UPDClientSocket.sendto(bytesToSend, trafficAddressPort)



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

      

      self.button = Button(self.m, text="Enter Player Information", command=self.show_entry_field, font=("Arial", 20))

      self.button.grid(row=3, column=0)



        # Create an Entry widget (hidden initially)

      self.entry_field = Entry(self.m, font=("Arial", 20), bg='white')

        

        # Variable to store captured text

      self.captured_text = ""



    def show_entry_field(self):

        # Pack the Entry widget to show it when the button is clicked

        self.entry_field.grid(row=3, column=0)

        self.entry_field.focus()  # Set focus on the entry field

        self.entry_field.bind('<Return>', self.capture_text)       



    def capture_text(self, event):

        self.captured_text = self.entry_field.get()  # Get the text from the Entry widget

        print(f"User entered: {self.captured_text}")  # Process or use the text as needed

        with open("network.txt", "w") as file:

            file.write(self.captured_text)

        # Hide the Entry widget after capturing the text

        self.entry_field.grid_forget()



    

    def run(self):

	    self.m.mainloop()
