from tkinter import *
from tkinter.ttk import *
# import startvid
import sys
import tkinter as tk
# import cctvlog
from PIL import ImageTk ,Image
import subprocess, sys
import os
import test_1

# creates a Tk() object
master = Tk()
style = Style()

# sets the geometry of
# main root window
master.geometry("400x400")
master.title('Smart-Vision')
master.configure(background = 'lightblue')
master.attributes("-fullscreen", True)

def exit():
	sys.exit()

def log_window():
	# cctvlog.generate_log()
    pass

def play():
	# opener ="open" if sys.platform == "darwin" else "xdg-open"
	# subprocess.call([opener, 'filename.avi'])
	os.system("open unknown.jpg")
    # pass

style.configure('W.TButton', font =
               ('calibri', 20, 'bold'),
                foreground = 'red')

style.configure('TButton', font =
               ('calibri', 20, 'bold'),
                    borderwidth = '3', foreground = 'green')


label = Label(master, text ="   Welcome to \n Secure-Vision!", font = ('calibri', 40, 'bold'), background = 'lightblue')
label.pack(side = TOP, pady = 40)

# a button widget which will
# open a new window on button click
btn = Button(master,
			text ="Click to Start Surveillance",command=test_1.start_record, style = 'TButton')

btn.pack(pady = 10)


btn1 = Button(master,
			text ="Show Log", command = log_window)

btn1.pack(pady = 10)

btn2 = Button(master,
			text ="Play Video", command = play)

btn2.pack(pady = 10)

btn3 = Button(master,
			text ="Exit", command = exit, style = 'W.TButton')

btn3.pack(pady = 10)

# mainloop, runs infinitely
mainloop()

