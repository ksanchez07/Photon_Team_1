from tkinter import *
import socket
import multiprocessing
import threading
from transmission import Transmission


class GameScreen:
    def __init__(self, players):
        self.players = players
        
       
        
        
        #initializes bind and starts multiprocess for listen function
        self.UDPServerSocketReceive = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        
        with open("network.txt", "r") as file:
            localIp = file.read()

        clientAddressPort   = (localIp, 7501)
        self.UDPServerSocketReceive.bind(clientAddressPort)
        #process = multiprocessing.Process(target=self.listen)
        #process.start()
        

    def listen(self):
        bufferSize  = 1024
        with open("network.txt", "r") as file:
            localIp = file.read()

        serverAddressPort   = (localIp, 7500)

        #starting game
        transmission = Transmission()
        transmission.transmit(202, 7500)

        received_data = ' '
        while received_data != '202':
            received_data, address = self.UDPServerSocketReceive.recvfrom(bufferSize)
            received_data = received_data.decode('utf-8')
            print ("Received from traffic generator: " + received_data)
            player_hit = received_data.split(":")
            message = player_hit[1]
            

            #finding the row with person who's hardware id got the points and
            #adds the points to them
            pointReceiver = player_hit[0]          
            
                
            if message == '53':
                #red base has been hit
                if self.players[pointReceiver]["team"] == "green":
                    self.players[pointReceiver]["name"] = "B" + self.players[pointReceiver]["name"]
                    self.players[pointReceiver]["points"] += 100
            elif message == '43':
                #green base has been hit
                if self.players[pointReceiver]["team"] == "red":
                    self.players[pointReceiver]["name"] = "B" + self.players[pointReceiver]["name"]
                    self.players[pointReceiver]["points"] += 100
            else:
                self.players[pointReceiver]["points"] += 10


            #delete from here
            pointsDisplay = self.players[pointReceiver]["points"]
            nameDisplay = self.players[pointReceiver]["name"]
            print(f"player:{nameDisplay} has scored and now has {pointsDisplay} points")
            #to here after testing
                    

            
            self.UDPClientSocketTransmit.sendto(str.encode(str(message)), serverAddressPort)
            print ('')
    


    def create_widgets(self):
        self.root = Tk()
        self.root.title("Game Screen")
        self.root.configure(background='black')
        self.root.geometry("1200x700")

        #change to 6 minutes when you do the actual timer
        self.count = 60

        # update geometry
        self.root.update()

        points_action = LabelFrame(self.root,
                               bg = 'gray17',
                               width = 1100,
                               height = 600,
                               highlightbackground = "cyan",
                               highlightthickness =  4)

        points_action.place(x=50, y=50)

        action_scroll = LabelFrame(points_action,
                               bg = 'gray17',
                               width = 1080,
                               height = 200,
                               highlightbackground = "cyan",
                               highlightthickness = 4)
    
        action_scroll.place(x=5, y=340)

        action_label = Label(points_action,
                         bg = 'gray17',
                         fg = 'cyan',
                         font = ('Courier New', 16, 'bold'),
                         text = 'CURRENT GAME ACTION')
        action_label.place(x=810, y=330)

        red_team_label = Label(points_action,
                           bg = 'gray17',
                           fg = 'cyan',
                           font = ('Courier New', 20, 'bold'),
                           text = 'RED TEAM')
        red_team_label.place(x=200, y=5)

        green_team_label = Label(points_action,
                             bg = 'gray17',
                             fg = 'cyan',
                             font = ('Courier New', 20, 'bold'),
                             text = 'GREEN TEAM')
        green_team_label.place(x=720, y=5)

        red_team_frame = LabelFrame(points_action,
                                bg = 'gray17',
                                width = 400,
                                height = 280)
        red_team_frame.place(x=70, y=40)
        red_team_frame.grid_propagate(False)
        red_team_frame.columnconfigure(0, weight=1)
        red_team_frame.columnconfigure(1, weight=1)

        green_team_frame = LabelFrame(points_action,
                                  bg = 'gray17',
                                  width = 400,
                                  height = 280)
        green_team_frame.place(x=610, y=40)
        green_team_frame.grid_propagate(False)
        green_team_frame.columnconfigure(0, weight=1)
        green_team_frame.columnconfigure(1, weight=1)

        red_total_points = Label(points_action,
                                bg = 'gray17',
                                fg = 'red',
                                font = ('Courier New', 20, 'bold'),
                                text = '0')
        red_total_points.place(x=350, y=5)

        green_total_points = Label(points_action,
                                bg = 'gray17',
                                fg = 'green',
                                font = ('Courier New', 20, 'bold'),
                                text = '0')
        green_total_points.place(x=900, y=5)

        time_left_label = Label(points_action,
                                bg = 'gray17',
                                fg = 'cyan',
                                font = ('Courier New', 20, 'bold'),
                                text = 'TIME REMAINING:')
        time_left_label.place(x=740, y=550)

        self.countdown_label = Label(points_action,
                                bg = 'gray17',
                                fg = 'cyan',
                                font = ('Courier New', 20, 'bold'),
                                text = '6:00')
        self.countdown_label.place(x=1000, y=550)

        r = 0
        g = 0
        for player in (self.players):
            codename = self.players[player]["name"]
            print(codename)
            if self.players[player]["team"] == "red":
                name_label = Label(red_team_frame,
                                bg='gray17',
                                fg='red',
                                font=("Courier New", 16, 'bold'),
                                text=f"{codename}")
                name_label.grid(row=r, column=0, sticky='w')

                points_label = Label(red_team_frame,
                                bg = 'gray17',
                                fg='red',
                                font=("Courier New", 16, 'bold'),
                                text = "0")
                points_label.grid(row=r, column=1, sticky='e')
                #player.ranking = r
                r = r + 1 
            else:
                name_label = Label(green_team_frame,
                                bg='gray17',
                                fg='green',
                                font=("Courier New", 16, 'bold'),
                                text=f"{codename}")
                name_label.grid(row=g, column=0, sticky='w')

                points_label = Label(green_team_frame,
                                bg='gray17',
                                fg='green',
                                font=("Courier New", 16, 'bold'),
                                text = "0")
                points_label.grid(row=g, column=1, sticky='e') 
                g = g + 1

        #self.updatePlayer()     
  
                             

    def return_to_player_entry(self):
        return
    
    def countdown(self):
        if self.count > 0:
            self.count -= 1

            if self.count >= 10:
                self.countdown_label.configure(text=f"0:{self.count}")
            else:
                self.countdown_label.configure(text=f"0:0{self.count}")
            
            print(self.count)
            self.root.after(1000, self.countdown)
        else:
            #transmitting the code 3 times
            transmission = Transmission()
            transmission.transmit(221, 7500)
            transmission.transmit(221, 7500)
            transmission.transmit(221, 7500)

    def run(self):
        self.create_widgets()
        self.countdown()
        thread = threading.Thread(target=self.listen, daemon=True)
        thread.start()
        self.root.mainloop()


