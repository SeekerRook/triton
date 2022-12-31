#!/usr/bin/python3
from os import system
import tkinter as tk
import triton as tr
import tritongraph as trg
# import tritonlog as trl
window = tk.Tk()

tb = tk.Text(window,height=10,width=60)

def Load():
    loadingsign = tk.Label(window,text="Loading...")


    res = tr.run()        
    tb.insert(tk.INSERT,res)
def log():
    system("./tritonlog.sh")

window.title = ("TRITON  Mutual Funds Monitor")
# window.geometry("780x640")
window.minsize(550, 450)

btn = tk.Button(window,text="Load Values ",command=Load)
graph = tk.Button(window,text="Show Graph",command=trg.show)
log = tk.Button(window,text="Open Log File",command=log)
btn.place(y = 50,x= 100)
graph.place(y = 50,x= 400)
log.place(y = 50,x= 300)
tb.place(y = 100,x= 50)
# Load()
window.iconphoto(True,tk.PhotoImage(file='triton-logo-icon_white.png'))
window.wait_visibility()
# Load()
window.mainloop()
