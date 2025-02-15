from tkinter import * 
import tkinter as tk
import subprocess

#localIp = "127.0.0.1"
#import subprocess allows to run server at the same time the photon window is open
server = subprocess.Popen(["python3", "server.py"])

window = tk.Tk()
window.title = ("Photon")


 #add button, when pressed call changeIP()
#button = Button(window, text="Select Network", command=changeIP)
#button.pack()


window.mainloop()

    
    



