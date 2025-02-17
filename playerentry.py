import tkinter

from tkinter import *

import socket

import subprocess





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

      all_entries = self.red_entries + self.green_entries
      for player_id_entry, player_codename_entry, team in all_entries:
        
        player_id = player_id_entry.get()
        player_codename = player_codename_entry.get()
        if(player_id != "" and player_codename != ""):
          if (player_id and not player_codename) or (player_codename and not player_id):
            print(f"Both entries must be filled for {team} team")
            continue
        
          if player_codename:
            player_codename = player_codename + "_" + team

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
        
          msgFromClient = str(str(player_id) + ":" + str(player_codename))
          bytesToSend = str.encode(msgFromClient)
          #sending the information to ther server
          UPDClientSocket.sendto(bytesToSend, trafficAddressPort)

          player_id_entry.delete(0, END)
          player_codename_entry.delete(0, END) 



    def create_widgets(self):  
      validate_id_cmd = self.m.register(self.validate_id)

      red_label = Label(self.m, text="Red Team", fg="red", bg="black")
      red_label.grid(row=0, column=1, columnspan=2)

      green_label = Label(self.m, text="Green Team", fg="green", bg="black")
      green_label.grid(row=0, column=4, columnspan=2)

      red_id_header = Label(self.m, text="ID", fg="red", bg="black")
      red_codename_header = Label(self.m, text="Codename", fg="red", bg="black")
      red_id_header.grid(row=1, column=1)
      red_codename_header.grid(row=1, column=2)

      green_id_header = Label(self.m, text="ID", fg="green", bg="black")
      green_codename_header = Label(self.m, text="Codename", fg="green", bg="black")
      green_id_header.grid(row=1, column=4)
      green_codename_header.grid(row=1, column=5)

      self.red_entries = []
      self.green_entries = []

      for i in range(20):

        
        red_id_label = Label(self.m, text=f"{i}", fg="red", bg="black")
        red_id_label.grid(row=i+2, column=0)

        red_id_entry = Entry(self.m, validate="key", validatecommand=(validate_id_cmd, '%P'))
        red_codename_entry = Entry(self.m)
        red_id_entry.grid(row=i+2, column=1)
        red_codename_entry.grid(row=i+2, column=2)
        self.red_entries.append((red_id_entry, red_codename_entry, "red"))

        green_id_label = Label(self.m, text=f"{i}", fg="green", bg="black")
        green_id_label.grid(row=i+2, column=3)
        
        green_id_entry = Entry(self.m, validate="key", validatecommand=(validate_id_cmd, '%P'))
        green_codename_entry = Entry(self.m)
        green_id_entry.grid(row=i+2, column=4)
        green_codename_entry.grid(row=i+2, column=5)

        self.green_entries.append((green_id_entry, green_codename_entry, "green"))
      
      submit_button = Button(self.m, text="Submit Players", command=self.pushPlayers)
      submit_button.grid(row=22, column=1, columnspan=5)

      

      self.button = Button(self.m, text="Input Network Address", command=self.show_entry_field, font=("Arial", 20))

      self.button.place(x=200, y=555)



        # Create an Entry widget (hidden initially)

      self.entry_field = Entry(self.m, font=("Arial", 20), bg='white')

        

        # Variable to store captured text

      self.captured_text = ""



    def show_entry_field(self):

        # Pack the Entry widget to show it when the button is clicked

        self.entry_field.place(x=550, y=560)

        self.entry_field.focus()  # Set focus on the entry field

        self.entry_field.bind('<Return>', self.capture_text)       



    def capture_text(self, event):

        self.captured_text = self.entry_field.get()  # Get the text from the Entry widget

        print(f"Using IP: {self.captured_text}")  # Process or use the text as needed

        with open("network.txt", "w") as file:

            file.write(self.captured_text)
        #import subprocess allows to run server at the same time the photon window is open
        #start server in background
        self.server = subprocess.Popen(["python3", "server.py"])
        # Hide the Entry widget after capturing the text
      
        self.entry_field.grid_forget()



    

    def run(self):

	    self.m.mainloop()