from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Enigma-youtube video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()


Label(root, text = 'Youtube linki:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader(): 
    Label(root, text = 'Yükləndi', font = 'arial 15').place(x= 180 , y = 210)     
    url =YouTube(str(link.get()))
    video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    print(video)
    video.download()
    Label(root, text = 'Yükləndi', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'Yüklə', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()