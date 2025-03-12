from tkinter import *

class GameScreen:     
    def init(self):
        pass
        
    def create_widgets(self):
        self.root = Tk()
        self.root.title("Game Screen")
        self.root.configure(background='gray17')
        self.root.geometry("1300x800")
        
    def run(self):
        self.create_widgets()
        self.root.mainloop()
    