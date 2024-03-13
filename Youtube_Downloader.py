from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import time
import pynput.keyboard
import threading
import subprocess, smtplib


def download_video():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        yd = yt.streams.get_highest_resolution()
        title = yt.title
        yd.download()
        messagebox.showinfo(title="Info ", message=f"Download Complete!\n{title}\nTotal size : {round((yd.filesize / 1024) / 1024, 1)} MB")
    except Exception as e:
        messagebox.showinfo(title="Error ", message="Error" + str(e))

def audio():

    link = url_entry.get()
    try:
        yt = YouTube(link)
        title = yt.title
        yd = yt.streams.get_audio_only()
        yd.download()
        messagebox.showinfo(title="Info ", message=f"Download Complete!\n{title}\nTotal size : {round((yd.filesize / 1024) / 1024, 1)} MB")
    except Exception as e:
        messagebox.showinfo(title="Error ", message="Error" + str(e))



# Create the main window
window = Tk()
window.title("YouTube Downloader")
window.config(padx=50, pady=30, bg="#E5E5F5")

# Create the URL entry field
title = Label(text="Youtube Download By R3b00t !", bg="#E5E5F5", font=("Georgia", 15, "bold"))
title.grid(column=0, columnspan= 3, row=0)
url_label = Label(text="Video URL:", bg="#E5E5F5")
url_label.grid(column=0, row=1,pady=40)
url_entry = Entry(width=50)
url_entry.grid(column=1, columnspan=2, row=1)


# Create the download button
download_button = Button(text="Video", width=10,  command=download_video)
download_button.grid(column=1, row=2)
download_audio = Button(text="Audio",  width=10, command=audio)
download_audio.grid(column=2, row=2)

# Create a label to show the download status
# status_label = Label(window, text="Status : ", bg="#E5E5F5")
# status_label.grid(column=0, columnspan=3, row=3, pady=25)

# Start the GUI main loop


window.mainloop()
