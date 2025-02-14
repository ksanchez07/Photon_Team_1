import tkinter as tk
from PIL import Image, ImageTk
import subprocess


#import subprocess allows to run server at the same time the photon window is open
#start server in background
server = subprocess.Popen(["python3", "server.py"])
#create root window for splash screen
root = tk.Tk()

# Get screen width and height to resize the image
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#load image
image = Image.open("logo.jpg")
# Resize the image to fit within the screen size
image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

#convert image to a Tkinter-compatible PhotoImage object
photo = ImageTk.PhotoImage(image)

#display image inlabel
label = tk.Label(root, image=photo)
label.pack()

def close_splash():
    root.destroy() #close splash screen
    main_window() #show main window

def main_window():
    window = tk.Tk()
    window.title("Main Application")
    window.geometry("1400x800+100+100")  # Adjust size as needed
    window.resizable(False,False) #make window unresizable, fixed
    window.mainloop()

root.after(3000, close_splash) #close splash screen after 3 seconds

root.mainloop()#run splash screen
    
    
