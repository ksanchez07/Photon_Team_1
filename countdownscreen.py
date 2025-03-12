import time
from tkinter import *
from gamescreen import GameScreen


class CountdownScreen:  
    #not sure what to put in init so its just passing so i can use self   
    def init(self):
        pass
        
    #creates the screen
    def create_widgets(self):
        self.root = Tk()
        self.root.title("Countdown Screen")
        self.root.configure(background='gray17')
        self.root.geometry("1300x800")
        self.count = 30
        
    #countdown but it only prints in terminal right now, i added this to 
    #finish my part of when countdown finishes it goes to the game screen
    def countdown(self):
        if self.count > 0:
            self.count -= 1
            print(self.count)
            self.root.after(1000, self.countdown)
        else:
            #time is up
            #pause for a second
            self.initialize_game()

    #whenever countdown finished it closes this page and opens game screen
    def initialize_game(self):
        self.root.destroy()
        game_screen = GameScreen()
        game_screen.run() 


    #runs windowscreen
    def run(self):
        self.create_widgets()
        self.countdown()
        self.root.mainloop()
    
