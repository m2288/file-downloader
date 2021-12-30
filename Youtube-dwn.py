from tkinter import *
from pytube import YouTube
import clipboard

root = Tk()
root.geometry("500x240")
root.resizable(0, 0)
root.title("Enigma-youtube video downloader")
Label(root, text="Youtube Video Downloader", font="arial 20 bold").pack()

yt_link = StringVar()

Label(root, text="Youtube linki:", font="arial 15 bold").place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=yt_link).place(x=32, y=90)

t = clipboard.paste()

if t is not None:
    Label(root, text=("Link yaddaşa köçürülüb."), font="arial 11").place(x=150, y=120)


def Downloader():
    if t is not None:
        url = YouTube(str(t))
    else:
        url = YouTube(str(yt_link.get()))
    print(type(yt_link.get()))
    video = (
        url.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
    )
    print(video)
    video.download()
    Label(root, text="Yükləndi", font="arial 15").place(x=210, y=120)


Button(
    root,
    text="Yüklə",
    font="arial 15 bold",
    bg="#4A7A8C",
    padx=2,
    command=Downloader,
).place(x=210, y=150)


root.mainloop()
