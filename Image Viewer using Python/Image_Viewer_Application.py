# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:46:14 2021

@author: Tanmoyee
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer Application")
img1= ImageTk.PhotoImage(Image.open('java_logo.png'))
img2= ImageTk.PhotoImage(Image.open('python_logo.png'))
img3= ImageTk.PhotoImage(Image.open('c++_logo.png'))
img4= ImageTk.PhotoImage(Image.open('c_logo.png'))
image_array=[img1,img2,img3,img4]
label_var= Label(image=img1)

def forward(image_number):
    global label_var
    global back_button
    global forward_button
    label_var.grid_forget()
    label_var=Label(image=image_array[image_number-1])
    forward_button=Button(root,text=">>",command= lambda : forward(image_number+1))
    back_button=Button(root,text="<<",command= lambda : backward(image_number-1))
    if image_number==4:
        forward_button=Button(root,text=">>",state=DISABLED)
    label_var.grid(row=0,column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    forward_button.grid(row=1,column=2)

def backward(image_number):
    global label_var
    global back_button
    global forward_button
    label_var.grid_forget()
    label_var=Label(image=image_array[image_number-1])
    forward_button=Button(root,text=">>",command= lambda : forward(image_number+1))
    back_button=Button(root,text="<<",command= lambda : backward(image_number-1))
    if image_number==1:
        back_button=Button(root,text="<<",state=DISABLED)
    label_var.grid(row=0,column=0,columnspan=3)
    back_button.grid(row=1,column=0)
    forward_button.grid(row=1,column=2)

back_button=Button(root,text="<<",command=backward,state=DISABLED)
forward_button=Button(root,text=">>",command= lambda : forward(2))
exit_button= Button(root,text="Exit",command=root.destroy)
label_var.grid(row=0,column=0,columnspan=3)
back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
forward_button.grid(row=1,column=2)
root.mainloop()