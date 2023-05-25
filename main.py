import tkinter as tk
import downloader as downloader

root = tk.Tk()

root.geometry("500x200")
root.title("Youtube Video Downloader")
root.config(bg="skyblue")

#Widgets
welcome_label = tk.Label(root,text="WELCOME HERE", font=("Arial",25),bg=("skyblue"))
inst_label = tk.Label(root,text="Paste your video link here", font=("Arial",20),bg=("skyblue"))
link = tk.Entry(root)
button = tk.Button(root, text="Download")

#Packs

welcome_label.pack()
inst_label.pack(pady=10)
link.pack(pady=10, fill="x")
button.pack()

if __name__ == '__main__':
    root.mainloop()

