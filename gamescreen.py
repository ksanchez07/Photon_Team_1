from tkinter import *
import socket
import multiprocessing
import threading
from transmission import Transmission


class GameScreen:
    def __init__(self, players):
        self.players = players
        self.red_total = 0
        self.green_total = 0
        self.scores_equal = True
        self.scroll_full = False
       
        
        
        #initializes bind and starts multiprocess for listen function
        self.UDPServerSocketReceive = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocketReceive.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
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
            name = self.players[pointReceiver]["name"]
                
            if message == '53':
                #red base has been hit
                if self.players[pointReceiver]["team"] == "green":
                    self.players[pointReceiver]["points"] += 100
                    self.green_total += 100
                    
                    self.scroll_text.insert(END, f"{name} ", "green")
                    self.scroll_text.insert(END, "hit the ")
                    self.scroll_text.insert(END, "RED BASE\n", "red")
            elif message == '43':
                #green base has been hit
                if self.players[pointReceiver]["team"] == "red":
                    self.players[pointReceiver]["points"] += 100
                    self.red_total += 100

                    self.scroll_text.insert(END, f"{name} ", "red")
                    self.scroll_text.insert(END, "hit the ")
                    self.scroll_text.insert(END, "GREEN BASE\n", "green")
            else:
                name_hit = self.players[message]["name"]
                self.players[pointReceiver]["points"] += 10
                if self.players[pointReceiver]["team"] == "green":
                    self.green_total += 10
                    self.scroll_text.insert(END, f"{name} ", "green")
                    self.scroll_text.insert(END, "hit ")
                    self.scroll_text.insert(END, f"{name_hit}\n", "red")
                else:
                    self.red_total += 10
                    self.scroll_text.insert(END, f"{name} ", "red")
                    self.scroll_text.insert(END, "hit ")
                    self.scroll_text.insert(END, f"{name_hit}\n", "green")

            self.scroll_text.see("end")

            #delete from here
            pointsDisplay = self.players[pointReceiver]["points"]
            nameDisplay = self.players[pointReceiver]["name"]
            print(f"player:{nameDisplay} has scored and now has {pointsDisplay} points")
            #to here after testing

            self.update_points(pointReceiver) 
            if (self.red_total == self.green_total):
                self.scores_equal = True
            elif (self.red_total > self.green_total):
                self.highest = self.r_points_label
                self.high_color = "red"
                self.scores_equal = False
            else:
                self.highest = self.g_points_label
                self.high_color = "green"
                self.scores_equal = False
            
            
            self.UDPClientSocketTransmit.sendto(str.encode(str(message)), serverAddressPort)
            print ('')
    


    def update_points(self, pointReceiver):
        team = self.players[pointReceiver]["team"]
        rank = self.players[pointReceiver]["rank"]
        points = self.players[pointReceiver]["points"]
        if (team == "red"):
            self.r_points_label.configure(text=f"{self.red_total}")
            self.r_display_grid[rank][1].configure(text=f"{points}")
        else:
            self.g_points_label.configure(text=f"{self.green_total}")
            self.g_display_grid[rank][1].configure(text=f"{points}")


    def stop_flash(self):
        self.highest.configure(fg=self.high_color)


    def flash(self):
        if (self.count > 0):
            if (self.scores_equal):
                self.stop_flash()
                pass
            elif (self.highest.cget("fg") == "snow"):
                self.highest.configure(fg=self.high_color)
            else:
                self.highest.configure(fg="snow")
            self.root.after(500, self.flash)
        else:
            self.stop_flash()

        

    def create_widgets(self):
        self.root = Tk()
        self.root.title("Game Screen")
        self.root.configure(background='black')
        self.root.geometry("1200x700")

        #change to 6 minutes (360 secs) when you do the actual timer
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

        self.scroll_text = Text(action_scroll, 
                                bg='gray17', 
                                fg='cyan',
                                bd=0,
                                highlightthickness=0,
                                borderwidth=0, 
                                font=('Courier New', 16, 'bold'))
        self.scroll_text.place(x=5, y=5, width=1000, height=180)
        self.scroll_text.tag_config("red", foreground="red")
        self.scroll_text.tag_config("green", foreground="green")

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
        red_team_label.place(x=190, y=5)

        green_team_label = Label(points_action,
                             bg = 'gray17',
                             fg = 'cyan',
                             font = ('Courier New', 20, 'bold'),
                             text = 'GREEN TEAM')
        green_team_label.place(x=720, y=5)

        red_team_frame = LabelFrame(points_action,
                                bg = 'gray17',
                                bd=0,
                                highlightthickness=0,
                                borderwidth=0,
                                width = 400,
                                height = 280)
        red_team_frame.place(x=70, y=40)
        red_team_frame.grid_propagate(False)
        red_team_frame.columnconfigure(0, weight=1)
        red_team_frame.columnconfigure(1, weight=1)

        green_team_frame = LabelFrame(points_action,
                                  bg = 'gray17',
                                  bd=0,
                                  highlightthickness=0,
                                  borderwidth=0,
                                  width = 400,
                                  height = 280)
        green_team_frame.place(x=610, y=40)
        green_team_frame.grid_propagate(False)
        green_team_frame.columnconfigure(0, weight=1)
        green_team_frame.columnconfigure(1, weight=1)

        self.r_points_label = Label(points_action,
                                bg = 'gray17',
                                fg = 'red',
                                font = ('Courier New', 20, 'bold'),
                                text = '0')
        self.r_points_label.place(x=350, y=5)

        self.g_points_label = Label(points_action,
                                bg = 'gray17',
                                fg = 'green',
                                font = ('Courier New', 20, 'bold'),
                                text = '0')
        self.g_points_label.place(x=900, y=5)

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

        self.highest = self.r_points_label
        self.high_color = "red"
        self.flash()

        self.r_display_grid = []
        self.g_display_grid = []
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

                self.r_display_grid.append([name_label, points_label])
                self.players[player]["rank"] = r
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

                self.g_display_grid.append([name_label, points_label]) 
                self.players[player]["rank"] = g
                g = g + 1

        #self.updatePlayer()     
  
                             

    def return_to_player_entry(self):
        
        from playerentry import PlayerEntry
        self.root.destroy()

        player_entry = PlayerEntry()
        player_entry.run()  # This will open the player entry window
        
    
    def countdown(self):
        if self.count > 0:
            self.count -= 1
            
            if self.count >= 300:
                self.countdown_label.configure(text=f"5:{self.count - 300}")
                if ((self.count - 300) < 10):
                    self.countdown_label.configure(text=f"5:0{self.count - 300}")
            
            elif self.count >= 240:
                self.countdown_label.configure(text=f"4:{self.count - 240}")
                if ((self.count - 240) < 10):
                    self.countdown_label.configure(text=f"4:0{self.count - 240}")
            
            elif self.count >= 180:
                self.countdown_label.configure(text=f"3:{self.count - 180}")
                if ((self.count - 180) < 10):
                    self.countdown_label.configure(text=f"3:0{self.count - 180}")
            
            elif self.count >= 120:
                self.countdown_label.configure(text=f"2:{self.count - 120}")
                if ((self.count - 120) < 10):
                    self.countdown_label.configure(text=f"2:0{self.count - 120}")
            
            elif self.count >= 60:
                self.countdown_label.configure(text=f"1:{self.count - 60}")
                if ((self.count - 60) < 10):
                    self.countdown_label.configure(text=f"1:0{self.count - 60}")
            
            elif self.count >= 10:
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
            self.UDPServerSocketReceive.close()
            self.UDPServerSocketReceive = None  # Reset the socket
            self.show_game_over_screen()
            
    def show_game_over_screen(self):
        # Clear the current window
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg='black')

        # Game over title
        game_over_label = Label(
            self.root,
            text="GAME OVER",
            fg="red",
            bg="black",
            font=("Courier New", 40, "bold")
        )
        game_over_label.pack(pady=50)

        # Final scores title
        final_scores_label = Label(
            self.root,
            text="FINAL SCORES",
            fg="cyan",
            bg="black",
            font=("Courier New", 30, "bold")
        )
        final_scores_label.pack(pady=20)
        # Exit button
        exit_button = Button(
            self.root,
            text="Player Entry",
            command=self.return_to_player_entry,
            bg="gray17",
            fg="white",
            font=("Courier New", 16, "bold"),
            padx=10,
            pady=5
        )
        exit_button.pack(pady=30)
        
    def run(self):
        self.create_widgets()
        self.countdown()
        thread = threading.Thread(target=self.listen, daemon=True)
        thread.start()
        self.root.mainloop()











