# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def l():
    from pytube import YouTube
    link=e1.get()
    yt=YouTube(link) 
    dv = yt.streams.get_highest_resolution()
    print('wait')
    dv.download()
    print("finish")
from tkinter import *
w=Tk()
l1=Label(w,text='paste your link here',font=('arial',30))
l1.pack()
e1=Entry(w,font=('arial',15))
e1.pack()
b1=Button(w,text="submit",command=l).pack(anchor='center',ipady=0)
w.mainloop()