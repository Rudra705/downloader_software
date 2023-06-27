import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as filedialog
import requests
import os

class Downloader:
    def __init__(self):
        self.saveto = ""
        self.window = tk.Tk()
        self.window.title("Python GUI Downloader")
        self.url_label = tk.Label(text ="Enter URL")
        self.textView = tk.Text(self.window, height=10,width=25)
        self.textView.insert(tk.END, "Browse the file where to store, the download file. If you don't browse a folder, by default it will be download in the fold which is having this software.")
        self.textView.pack()
        self.url_label.pack()
        self.url_entry = tk.Entry()
        self.url_entry.pack()
        self.browse_button = tk.Button(text ="Browse", command = self.browse_file)
        self.browse_button.pack()
        self.download_button = tk.Button(text="Download", command = self.download)
        self.download_button.pack()
        self.window.geometry("420x420")
        self.progress_bar = ttk.Progressbar(self.window, orient = "horizontal", maximum=100, length=270,mode="determinate")
        self.progress_bar.pack()
        self.window.mainloop()



    def browse_file(self):
        saveto = filedialog.asksaveasfilename(initialfile=self.url_entry)
        self.textView.delete("1.0", tk.END)
        self.textView.insert(tk.END,f"Your file will be downoaded here {saveto}")
        self.saveto = saveto



    def download(self):
        url  = self.url_entry.get()
        response = requests.get(url)
        total_size_in_bytes = int(response.headers.get("content-length"))
        block_size = 1000
        self.progress_bar["value"] = 0

        fileName = self.url_entry.get().split("/")[-1]
        if self.saveto == "":
            self.saveto = fileName

        self.textView.delete("1.0", tk.END)
        self.textView.insert(tk.END,f"Your file is being downloaded here {self.saveto} \n Thank you for using my software.")
        

        with open(self.saveto, 'wb') as f:
            for data in response.iter_content(block_size):
                
                self.progress_bar["value"] += 100* block_size/total_size_in_bytes
                self.window.update()
                f.write(data)
                print(self.progress_bar["value"])



app = Downloader()