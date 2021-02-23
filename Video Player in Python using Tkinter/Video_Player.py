# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:17:37 2021

@author: Tanmoyee
"""

import tkinter as tk
import os

root=tk.Tk()
root.geometry("450x420")

f=tk.Frame(root, borderwidth=1, relief="groove")
label_menu=tk.Label(f,text="Related Videos",font=("Helvetica",18,"bold"),fg="black",bg="rosybrown")
label_menu.pack(pady=5)
f.pack(pady=5)

list_box=tk.Listbox(root,width=35,height=12,font=("Times",15,"italic"),bg="wheat")
list_box.pack()

def mediaplay(event):
    if list_box.curselection():
        file=list_box.curselection()[0]
        os.startfile(list_box.get(file))
for file in os.listdir():
    if file.endswith(".mp4"):
        list_box.insert(0,file)
        
start_button=tk.Button(root, text="Play",font=("Arial",14),bg="Tan")
start_button.pack(fill='x',expand='no')
start_button.bind("<ButtonPress-1>",mediaplay)

def top():
    root.destroy()
    
exit_button=tk.Button(root, text="Exit",font=("Arial",14),bg="Tan",command=top)
exit_button.pack(fill='x',expand='no')

root.mainloop()