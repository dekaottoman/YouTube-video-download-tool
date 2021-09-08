import tkinter as tk
import os
from tkinter import Button, Label, font
from pytube import YouTube

root = tk.Tk()
root.maxsize(700,400)
root.minsize(700,400)
root.title('Youtube Video Download Tool')

#We get the path to users "Downloads" folder
if os.name == "nt":
    downloads = f"{os.getenv('USERPROFILE')}\\Downloads"
else:
    downloads = f"{os.getenv('HOME')}/Downloads"

#We get the video URL and its title
def get_video():
    url = url_input.get()
    info_label1 = tk.Label(info_frame, text= YouTube(url).title, font=15, bg="#dff9fb")
    info_label1.place(relx=0.036, rely=0.4)
    print(url)

#We use this function to download the High Res. version of the video
def downh():
    url = url_input.get()
    YouTube(url).streams.get_highest_resolution().download(downloads)
    down_label = tk.Label(user_frame, text="Download Done!", width=27, font=25, bg="#22a6b3")
    down_label.place(relx=0.036, rely=0.05)

#We use this function to download the Low Res. version of the video
def downl():
    url = url_input.get()
    YouTube(url).streams.get_lowest_resolution().download(downloads)
    down_label = tk.Label(user_frame, text="Download Done!", width=27, font=25, bg="#22a6b3")
    down_label.place(relx=0.036, rely=0.05)

#We use this function to download the Audio only version of the video
def downa():
    url = url_input.get()
    YouTube(url).streams.get_audio_only().download(downloads)
    down_label = tk.Label(user_frame, text="Download Done!", width=27, font=25, bg="#22a6b3")
    down_label.place(relx=0.036, rely=0.05)

#Info frame is for the part to display the info
canvas = tk.Canvas(root, height=400, width=700, bg="white")
canvas.pack()

info_frame = tk.Frame(root, bg="#dff9fb")
info_frame.place(relheight=0.4, relwidth=1, relx=0, rely=0)

img = tk.PhotoImage(file="yt_logo.png")
yt_label = tk.Label(info_frame, image=img)
yt_label.place(relheight=1, relwidth=0.375 ,relx=0.625, rely=0)

#User frame is the frame for the part of the application the user interacts with
user_frame = tk.Frame(root, bg="#22a6b3")
user_frame.place(relheight=0.4, relwidth=1, relx=0, rely=0.4)

url_input = tk.Entry(root)
canvas.create_window(150,220,window=url_input, width=250, height=25)

down_label = tk.Label(user_frame, text="Enter a URL from YouTube", width=27, font=25, bg="#22a6b3")
down_label.place(relx=0.036, rely=0.05)

vidget_btn = Button(user_frame, text="Click Me !!!" , width=27, font=20, bg="#6ab04c" , fg="white", command=get_video)
vidget_btn.place(relheight=0.3 ,relx=0.036, rely=0.55)

downh_btn = Button(user_frame, text="High Res. Download" , width=27, font=20, bg="#6ab04c", fg="white", command=downh)
downh_btn.place(relx=0.60, rely=0.1)

downl_btn = Button(user_frame, text="Low Res. Download" , width=27, font=20, bg="#6ab04c", fg="white", command=downl)
downl_btn.place(relx=0.6, rely=0.35)

downa_btn = Button(user_frame, text="Audio only Download" , width=27, font=20, bg="#6ab04c", fg="white", command=downa)
downa_btn.place(relx=0.6, rely=0.6)

dekaottoman = tk.Label(root,text="By dekaottoman", font=20, bg="black", fg="white")
dekaottoman.place(relheight=0.2 ,relwidth=1, rely=0.8,relx=0)

root.mainloop()