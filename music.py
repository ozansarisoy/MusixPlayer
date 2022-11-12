from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer
import customtkinter

#colors
co1 = "#E0FFFF" #cyan
co2 = "#FF6347" #purple
co3 = "#333333" #black
co4 = "#FF6347" #tomato
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk("System")
app.title ("MusixPlayer")
app.geometry('400x300') #352x255
app.configure(background=co1)
app.resizable(width=FALSE, height=FALSE)
app.resizable(width=FALSE, height=FALSE)

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def previous_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing


#frames
left_frame = Frame(app, width=150, height=150, bg=co1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(app, width=550, height=250, bg=co3)
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(app, width=400, height=100, bg=co4)
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

#right frame 
listbox = Listbox(right_frame, selectmode=SINGLE, font=('Arial  9 bold'), width=32, height=10, bg=co3, fg="white")
listbox.grid(row=0, column=0)

w = Scrollbar(right_frame) 
w.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand = w.set)
w.config(command = listbox.yview)

#images

img_1 = Image.open('musixplayericons/music.png')
img_1 = img_1.resize((130, 130))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=130, image=img_1, padx=10, bg=co1)
app_image.place(x=10, y=15)

img_2 = Image.open('musixplayericons/play-button.png')
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, width=40, height=40, image=img_2, padx=10, bg=co1, font=("Ivy 10"), command=play_music)
play_button.place(x=56+28, y=35)

img_3 = Image.open('musixplayericons/backward.png')
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = Button(down_frame, width=40, height=40, image=img_3, padx=10, bg=co1, font=("Ivy 10"), command=previous_music)
prev_button.place(x=10+28, y=35)

img_4 = Image.open('musixplayericons/fast-forward-button.png')
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, width=40, height=40, image=img_4, padx=10, bg=co1, font=("Ivy 10"), command=next_music)
next_button.place(x=102+28, y=35)

img_5 = Image.open('musixplayericons/stop.png')
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, width=40, height=40, image=img_5, padx=10, bg=co1, font=("Ivy 10"), command=pause_music)
pause_button.place(x=148+28, y=35)

img_6 = Image.open('musixplayericons/next-track-button.png')
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(down_frame, width=40, height=40, image=img_6, padx=10, bg=co1, font=("Ivy 10"), command=continue_music)
continue_button.place(x=194+28, y=35)

img_7 = Image.open('musixplayericons/stopbutton.png')
img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(down_frame, width=40, height=40, image=img_7, padx=10, bg=co1, font=("Ivy 10"), command=stop_music)
stop_button.place(x=240+28, y=35)

line = Label(left_frame, width=200, height=1, padx=10, bg=co3) 
line.place(x=0, y=1)

line = Label(left_frame, width=200, height=1, padx=10, bg=co1) 
line.place(x=0, y=3)

running_song =  Label(down_frame, text = "Choose a Song", font=("Ivy 10"), width=44, height=1, padx=10, bg=co1, fg = co3, anchor=NW)
running_song.place(x=0, y=1)


os.chdir(r'E:\VsCode\Projects\MusixPlayer\songs')
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(END, i)

show()

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

app.mainloop()