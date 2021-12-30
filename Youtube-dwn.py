from tkinter import *
from pytube import YouTube
import clipboard

root = Tk()
root.geometry("500x240")
root.resizable(0, 0)
root.title("Enigma-youtube video downloader")
Label(root, text="Youtube Video Downloader", font="arial 20 bold").pack()
yt_link = StringVar()


def _linkPaste():
    t = clipboard.paste()
    yt_link=t


Label(root, text="Youtube linki:", font="arial 15 bold").place(x=160, y=60)
link_enter = Entry(root, width=55, textvariable=yt_link).place(x=32, y=90)
Button(
    root,
    text="Youtube linkini qoy",
    font="arial 10",
    bg="#4A7A8C",
    padx=2,
    command=_linkPaste,
).place(x=370, y=85)


def Downloader():
    Label(root, text="Yükləndi", font="arial 15").place(x=180, y=210)
    url = YouTube(str(yt_link.get()))
    video = (
        url.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
    )
    print(video)
    video.download()
    Label(root, text="Yükləndi", font="arial 15").place(x=180, y=210)


Button(
    root,
    text="Yüklə",
    font="arial 15 bold",
    bg="#4A7A8C",
    padx=2,
    command=Downloader,
).place(x=210, y=150)

root.mainloop()
