from tkinter import messagebox,filedialog,Tk,StringVar
from urllib.request import urlopen,HTTPError,URLError
import _thread
from main import *

import os


fln = ""
filesize = ""

def initDownload(url,download_progress,download_percentage):
    furl= url.get()
    target = urlopen(furl)
    meta = target.info()
    filesize = float(meta['Content-Length'])
    filesize_mb = round((filesize/1024/1024),2)
    downloaded = 0
    chunks = 1024 * 5
    with open(fln,"wb") as f:
        while True:
            parts = target.read(chunks)
            if not parts:
                messagebox.showinfo("Download complete","Your Download has been finished succesfully")
                break
            downloaded += chunks
            download_progress.set(str(downloaded) + "MB /" +str(filesize_mb)+"MB")
            download_percentage.set(round(((downloaded/filesize)*100),2) +"%")
            f.write(parts)
        f.close()


def startDownload(filename):
    global fln
    fln = filedialog.asksaveasfilename(iniitialdir=os.chdir("D:\DM\downloads"),title="Save File",filetypes=(("All Files","*.*"),))
    filename.set(os.path.basename(fln)) 
    _thread.start_new_thread(initDownload,())



def select_all(ent):
    ent.tag_add("sel","1.0","end")
    ent.tag_config("sel",background="white",foreground="ocean-blue")

def exitApp():
    if messagebox.askyesno("Exit Program!","Are you sure you want to exit the program") is False:
        return False
    exit()
