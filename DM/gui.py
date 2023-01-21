from tkinter import messagebox,filedialog
from tkinter import *
import os
from main import select,Download,close

root = Tk()

root.geometry("400x400")
root.title("Download Manager V 1.0")
root.resizable(False,False)

url = StringVar()
filename = StringVar()
download_progress = StringVar()
download_percentage = StringVar()


wrapper = LabelFrame(root,text="File URL")
wrapper.pack(fill="both",expand="yes",padx=10,pady=10)

wrapper2 = LabelFrame(root,text="Download Information")
wrapper2.pack(fill="both",expand="yes",padx=10,pady=10)

lbl = Label(wrapper,text="Download URL")
lbl.grid(row=0,column=0,padx=10,pady=10)

ent = Entry(wrapper,textvariable=url)
ent.grid(row=0,column=1,padx=5,pady=10)

data = ""
def paste_select(e1):
    global data
    e1.insert(data)

cop = Button(wrapper,text="paste link",command=lambda:paste_select(ent))
cop.grid(row=0,column=2)

btn = Button(wrapper,text="Download",command=Download(filename=filename))
btn.grid(row=0,column=3,padx=5,pady=10)


lbl2 = Label(wrapper2,text="File: ")
lbl2.grid(row=0,column=0,padx=10,pady=10)

lbl3 = Label(wrapper2,textvariable=filename)
lbl3.grid(row=0,column=1,padx=10,pady=10)

#show progress
lbl4 = Label(wrapper2,text="Download Progress")
lbl4.grid(row=1,column=0,padx=10,pady=10)

lbl5 = Label(wrapper2,textvariable=download_progress)
lbl5.grid(row=1,column=1,padx=10,pady=10)

lbl6 = Label(wrapper2,text="Download Percentage")
lbl6.grid(row=2,column=0,padx=10,pady=10)
 
lbl7 = Label(wrapper2,textvariable=download_percentage)
lbl7.grid(row=2,column=1,padx=10,pady=10)

Button(wrapper2,text="Exit Downloader",command=close()).grid(row=3,column=0,padx=10,pady=10)


root.mainloop()