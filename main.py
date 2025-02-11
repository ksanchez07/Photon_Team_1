import tkinter as tk
import subprocess


#import subprocess allows to run server at the same time the photon window is open
server = subprocess.Popen(["python3", "server.py"])
window = tk.Tk()
window.title = ("Photon")


window.mainloop()

    
    



