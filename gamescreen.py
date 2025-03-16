from tkinter import *

class GameScreen:
    def __init__(self, red_entries, green_entries):
        self.root = None
        self.red_entries = red_entries
        self.green_entries = green_entries
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
        for i, row in (self.red_entries):
            codename = row[2].get()
            player_label = Label(red_frame,
                                 bg='red4',
                                 fg='RosyBrown1',
                                 font=("Courier New", 8),
                                 text=f"{codename}")
            player_label.place(x=10, y=30 + (i * 20)) 
        # add green team names
        for i, row in (self.green_entries):
            codename = row[2].get()
            player_label = Label(green_frame,
                                 bg='red4',
                                 fg='RosyBrown1',
                                 font=("Courier New", 8),
                                 text=f"{codename}")
            player_label.place(x=10, y=30 + (i * 20)) 

    def run(self):
        self.create_widgets()
        self.root.mainloop()
