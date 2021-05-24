from tkinter import *
from PIL import ImageTk, Image
from pytube import YouTube
from moviepy.editor import *


root = Tk()
root.geometry('700x450')
root.resizable(0,0)
root.title('YouTube Downloader')

Label(root, text = 'YouTube Video Downloader', font = 'arial 20 bold').pack()

link = StringVar(root)

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x=265, y=60)
link_enter = Entry(root, width = 70, textvariable = link).place(x=130, y=90)

#image = Image.open('youtube.png')
#image = image.resize((100, 100), Image.ANTIALIAS)
#new_image = ImageTk.PhotoImage(image)
#Label(root, image = new_image).place(x=50, y=400)


def Downloader():
	url = YouTube(str(link.get()))
	video = url.streams.first()
	video.download()
	Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x=270, y=210)
	Label(root, text = 'You just downloaded: ' + url.title, font = 'arial 13').place(x=32, y=250)
	Label(root, text = 'Having: ' + str(url.views) + ' views', font = 'arial 13').place(x=32, y=275)
	Label(root, text = 'Having: ' + str(url.length) + ' seconds', font = 'arial 13').place(x=32, y=300)
	Label(root, text = 'Posted on: ' + str(url.publish_date), font = 'arial 13').place(x=32, y=325)

Button(root, text = 'DOWNLOAD', font = 'arial 15 bold', bg = 'red', padx = 2, command = Downloader).place(x=275, y=150)

root.mainloop()