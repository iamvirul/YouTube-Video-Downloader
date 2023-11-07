import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        youtube_url = str(link.get())
        youtube_object = YouTube(youtube_url, on_progress_callback=on_progress)
        video = youtube_object.streams.get_highest_resolution()
        title.configure(text=youtube_object.title, text_color='white')
        finishLabel.configure(text="")
        video.download('~/download')
        finishLabel.configure(text="Downloaded", text_color="Green")
    except Exception as e:
        finishLabel.configure(text=e, text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_remaining = total_size - bytes_remaining
    percentage_of_complete = bytes_remaining / total_size * 100
    per = str(int(percentage_of_complete))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    progressBar.set(float(percentage_of_complete) / 100)
    

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

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400, height=5)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)
app.mainloop()
