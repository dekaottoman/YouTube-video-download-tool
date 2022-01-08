import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from yt import download_mp4, download_mp3, get_info


root = tk.Tk()
root.minsize(300,486)
root.maxsize(300,486)
root.title("YT Video Download")
icon = tk.PhotoImage("icon.ico")
root.iconbitmap(icon)

def pop_up(msg:str):
    win = tk.Toplevel()
    win.wm_title("For you!")
    win.maxsize(243,150)
    win.minsize(243,150)
    win.iconbitmap(icon)

    l = tk.Label(win, text=msg)
    l.place(relwidth=1, relheight=0.2, rely=0.25, relx=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.place(relwidth=0.5, relheight=0.2, rely=0.5, relx=0.25)

def download_vid():
    try:
        url = url_input.get()
        if len(url) > 0:
            time_taken = download_mp4(url)
            pop_up("Download Complete.")
        else:
            pop_up("Please enter URL.")
    except:
        pop_up("Please check your URL.")

def download_audio():
    pop_up("Not implemented yet.")

def info():
    try:
        url = url_input.get()
        if len(url) > 0:
            info = get_info(url)
            win = tk.Toplevel()
            win.wm_title("Video Info")
            win.maxsize(243,150)
            win.minsize(243,150)
            win.iconbitmap(icon)

            l = tk.Label(win, text=str(info[0]))
            l.place(relwidth=1, relheight=0.12, rely=0.15, relx=0)

            l = tk.Label(win, text="View Count : " + str(info[2]))
            l.place(relwidth=1, relheight=0.12, rely=0.3, relx=0)

            l = tk.Label(win, text="Length : " + str(info[1]))
            l.place(relwidth=1, relheight=0.12, rely=0.45, relx=0)

            b = ttk.Button(win, text="Okay", command=win.destroy)
            b.place(relwidth=0.5, relheight=0.2, rely=0.65, relx=0.25)
        else:
            pop_up("Please enter URL.")
    except:
        pop_up("Please check your URL.")

canvas = tk.Canvas(root, width=300, height=486, bg="#f0f0f0")
canvas.pack()

img = tk.PhotoImage(file="github.png")
qr = tk.Label(root, image=img)
qr.place(relwidth=0.7, relheight=0.4 , rely=0, relx=0.15)

url_input = ttk.Entry(root)
canvas.create_window(150,200, window=url_input,width=250,height=35)

download_btn = ttk.Button(root, text="Download Video", command=download_vid)
download_btn.place(relwidth=0.7,relheight=0.12,relx=0.15,rely=0.47)

download_btn = ttk.Button(root, text="Download Audio", command=download_audio)
download_btn.place(relwidth=0.7,relheight=0.12,relx=0.15,rely=0.62)

download_btn = ttk.Button(root, text="Display Info", command=info)
download_btn.place(relwidth=0.7,relheight=0.12,relx=0.15,rely=0.77)

attr_label = tk.Label(root, text="by dekaottoman", bg="#576574", fg="#ffffff")
attr_label.place(relwidth=1, relheight=0.07, relx=0,rely=0.93)

root.mainloop()