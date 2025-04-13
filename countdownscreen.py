import time
from tkinter import *
from PIL import Image, ImageTk
from gamescreen import GameScreen
from transmission import Transmission
from player import Player
import pygame
import random

class CountdownScreen:  
    #not sure what to put in init so its just passing so i can use self   
    pygame.mixer.init()
    def __init__(self, players):
        self.players = players
        
    #creates the screen
    def create_widgets(self):
        self.root = Tk()
        self.root.title("Countdown Screen")
        self.root.configure(background='gray17')
        self.root.geometry("1300x800")
        self.count = 30

        #load the background image
        self.bg_image = Image.open("background.png")
        self.bg_image = self.bg_image.resize((1300,800), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        #set background label
        self.bg_label = Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth = 1, relheight = 1)

        #create countdown label
        self.countdown_label = Label(self.root, text=str(self.count), font=("Arial", 50, "bold"), fg="white", bg="black") #font size/color of countdown
        self.countdown_label.place(relx=0.5, rely=0.5, anchor="center") #centers label
        
    #countdown but it only prints in terminal right now, i added this to 
    #finish my part of when countdown finishes it goes to the game screen
    def countdown(self):
        if self.count > 0:
            if self.count == 15:
                tracks = [
                    "track1.mp3", 
                    "track2.mp3", 
                    "track3.mp3", 
                    "track4.mp3", 
                    "track5.mp3", 
                    "track6.mp3", 
                    "track7.mp3", 
                    "track8.mp3"
                ]
                selectedTrack = random.choice(tracks)
                pygame.mixer.music.load(selectedTrack)
                pygame.mixer.music.play(-1)    
            self.countdown_label.config(text=str(self.count))
            delay = 1000
            if self.count <= 5:
                delay = 1500

            self.count -= 1
            self.root.after(delay, self.countdown)            
        else:
            #time is up
            #pause for a second
            self.initialize_game()

    #whenever countdown finished it closes this page and opens game screen
    def initialize_game(self):
        self.root.destroy()
        game_screen = GameScreen(self.players)
        game_screen.run() 


    #runs windowscreen
    def run(self):
        self.create_widgets()
        self.countdown()
        self.root.mainloop()
    
