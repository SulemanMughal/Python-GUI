import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
from tkinter.ttk import *

music_player = tkr.Tk()
#Set the resizable property False
music_player.resizable(False, False)
music_player.title("Music Player")
music_player.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold",  selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()
Button1 = Button(music_player,  text="PLAY", command=play)
Button2 = Button(music_player,  text="STOP", command=stop)

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")

play_list.pack(fill="both", expand="yes")
music_player.mainloop()