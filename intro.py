from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1600x850")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img= Image.open("jarvisfullgui.gif")
    lbl= Label(root)
    lbl.place(x=0,y=0)
    i=0
   # mixer.music.load("")
   # mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img=img.resize((1600,850))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()