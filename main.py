import tkinter as tk
from tkinter import ttk
import threading
from pytube import YouTube

#root config
root = tk.Tk()
root.geometry("500x200")
root.title("Youtube Video Downloader")
root.config(bg="skyblue")

#Progress bar setting
def progress_set(percentage):
    progress['value']=percentage


def progress_displaying(stream,chunk,bytes_remaining):
    size=stream.filesize
    progression = size-bytes_remaining
    percentage= float((100/size) * progression)
    progress_set(percentage)

#downloading with pytube
def download(link):
    yt = YouTube(link,on_progress_callback=progress_displaying)
    stream = yt.streams.filter(progressive=True).filter(res="720p").first()
    stream.download(output_path="./videos")

#Widgets
welcome_label = tk.Label(root,text="WELCOME HERE", font=("Arial",25),bg=("skyblue"))
inst_label = tk.Label(root,text="Paste your video link here", font=("Arial",20),bg=("skyblue"))
link = tk.Entry(root)
button = tk.Button(root, text="Download",command= lambda : threading.Thread(target=download,args=(link.get(),)).start())
progress = ttk.Progressbar(root, orient="horizontal",mode='determinate', length=300)

#Packs
welcome_label.pack()
inst_label.pack(pady=10)
link.pack(pady=10, fill="x")
button.pack()
progress.pack(pady=10)

if __name__ == '__main__':
    threading.Thread(target=root.mainloop()).start()

