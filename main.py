from tkinter import * 
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

#localIp = "127.0.0.1"
#import subprocess allows to run server at the same time the photon window is open
#start server in background
server = subprocess.Popen(["python3", "server.py"])
window = tk.Tk()
window.title = ("Photon")


window.mainloop()

root.after(3000, close_splash) #close splash screen after 3 seconds

root.mainloop()#run splash screen
    
    
