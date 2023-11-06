import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytlink = str(link.get())
        youtubeobject = YouTube(ytlink)
        video = youtubeobject.streams.get_highest_resolution()
        video.download('~/download')
    except Exception as e:
        finishLabel.configure(text=e, text_color="red")
    finishLabel.configure(text="Downloaded", text_color="Green")


customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("820x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert Your YouTube Link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)
app.mainloop()
