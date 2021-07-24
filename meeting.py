import webbrowser as web
import pyautogui as key
from tkinter import*
import time
import tkinter.messagebox as tmsg







r=Tk()
r.title("teacher login")
tk=tmsg.showinfo("meetings","This may take some time so be patient")
def exit():
    quit()
j=IntVar()
var=StringVar()
var.set("Radio")
def meet():

    time.sleep(j.get()*60)
    web.open_new_tab("https://meet.google.com")
    time.sleep(40)
    key.click(x=121,y=538)
    time.sleep(2)
    if var.get()=="late":
        key.click(x=121,y=538)
        time.sleep(1)
        key.click(x=660,y=457)
    elif var.get()=="instant":
        key.click(x=156,y=587)    
Label(r,text="Time to build google meet in minutes").grid(row=0,column=0)
n=Entry(bg="light green", textvariable=j).grid(row=1,column=0)
choice=Radiobutton(r,text="create meeting for later",value="late",variable=var).grid(row=2,column=0)
choiced=Radiobutton(r,text="Start instant meeting",value="instant",variable=var).grid(row=3,column=0)
build=Button(r,text="BUILD",bg="light blue", fg="yellow",command=meet).grid(row=4,column=0)
quit=Button(r,text="Quit",bg="red",fg="white",command=exit).grid(row=5,column=0)


r.mainloop()