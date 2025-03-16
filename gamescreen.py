from tkinter import *

class GameScreen:
    def __init__(self, players):
        self.root = None
        self.players = players
    def create_widgets(self):
        self.root = Tk()
        self.root.title("Game Screen")
        self.root.configure(background='gray17')
        self.root.geometry("1300x800")

        # update geometry
        self.root.update()

        # calculate dimensions for the frames
        frame_width = int(self.root.winfo_width() * 0.333) 
        frame_height = self.root.winfo_height()

        # red teams frame
        red_frame = LabelFrame(self.root,
                               bg='red4',
                               fg='RosyBrown1',
                               labelanchor="n",
                               height=frame_height,
                               width=frame_width,
                               font=("Courier New", 10, "bold"),
                               text="RED TEAM")
        red_frame.place(x=0, y=0)

        # green teams frame
        green_frame = LabelFrame(self.root,
                                 bg='dark green',
                                 fg='PaleGreen1',
                                 labelanchor="n",
                                 height=frame_height,
                                 width=frame_width,
                                 font=("Courier New", 10, "bold"),
                                 text="GREEN TEAM")
        green_frame.place(x=int(self.root.winfo_width() * 0.666), y=0)
        # add red team names 
        r = 0
        g = 0
        for player in (self.players):
            codename = player.codename
            if player.team == "red":
                player_label = Label(red_frame,
                                    bg='red4',
                                    fg='RosyBrown1',
                                    font=("Courier New", 8),
                                    text=f"{codename}")
                player_label.place(x=10, y=30 + (r * 20))
                r = r + 1 
            else:
                player_label = Label(green_frame,
                                    bg='red4',
                                    fg='RosyBrown1',
                                    font=("Courier New", 8),
                                    text=f"{codename}")
                player_label.place(x=10, y=30 + (g * 20)) 
                g = g + 1

    def run(self):
        self.create_widgets()
        self.root.mainloop()

