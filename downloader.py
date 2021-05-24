from tkinter import *
from PIL import ImageTk, Image
from pytube import YouTube


display_window = Tk()
display_window.geometry('700x450')
display_window.resizable(0,0)
display_window.title('YouTube Downloader')

Label(display_window, text = 'YouTube Video Downloader', font = 'arial 20 bold').pack()

link = StringVar()

Label(display_window, text = 'Paste Link Here:', font = 'arial 15 bold').place(x=265, y=60)
link_enter = Entry(display_window, width = 70, textvariable = link).place(x=130, y=90)

#image = Image.open('youtube.png')
#image = image.resize((100, 100), Image.ANTIALIAS)
#new_image = ImageTk.PhotoImage(image)
#Label(display_window, image = new_image).place(x=50, y=400)

def Downloader():
	url = YouTube(str(link.get()))
	video = url.streams.first()
	video.download()
	Label(display_window, text = 'DOWNLOADED', font = 'arial 15').place(x=270, y=210)
	Label(display_window, text = 'You just downloaded: ' + url.title, font = 'arial 13').place(x=32, y=250)
	Label(display_window, text = 'Having: ' + str(url.views) + ' views', font = 'arial 13').place(x=32, y=275)
	Label(display_window, text = 'Having: ' + str(url.length) + ' seconds', font = 'arial 13').place(x=32, y=300)
	Label(display_window, text = 'Posted on: ' + str(url.publish_date), font = 'arial 13').place(x=32, y=325)

Button(display_window, text = 'DOWNLOAD', font = 'arial 15 bold', bg = 'red', padx = 2, command = Downloader).place(x=275, y=150)

display_window.mainloop()