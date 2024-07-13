import customtkinter
import tkinter
from tkinter import *
from combined import a
from server2 import startserver
def server():
    startserver()
def getimg():
    canvas = tkinter.Canvas(root, width = 250, height = 250)
    canvas.pack()
    label=customtkinter.CTkLabel(master=root,text="Encrypted Image")
    label.pack(pady=2,padx=2)
    img = tkinter.PhotoImage(file="ReceivedImage1.png")
    img=img.subsample(2)
    canvas.create_image(0,0, anchor=tkinter.NW, image=img)
    root.mainloop()
def dec():
    a()
    
    canvas = tkinter.Canvas(root, width = 250, height = 250)
    canvas.pack()
    label=customtkinter.CTkLabel(master=root,text="Decrypted Image")
    label.pack(pady=2,padx=2)
    im = tkinter.PhotoImage(file="ReceivedImage1CombinedDecrypted.png")
    im=im.subsample(2)
    canvas.create_image(0,0, anchor=tkinter.NW, image=im)
    root.mainloop()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.geometry("800x800")  
def x():
    
    
    button=customtkinter.CTkButton(master=root,text="Start the server",command=startserver)
    button.pack(pady=10,padx=10)
    label=customtkinter.CTkLabel(master=root,text="Encrypted Image")
    label.pack(pady=2,padx=2)
    # canvas = tkinter.Canvas(root, width = 250, height = 250)
    # canvas.pack()
    button=customtkinter.CTkButton(master=root,text="Get ency",command=getimg)
    button.pack(pady=10,padx=10)
    # img = tkinter.PhotoImage(file="ReceivedImage3.png")
    # img=img.subsample(2)
    # canvas.create_image(0,0, anchor=tkinter.NW, image=img)
    button=customtkinter.CTkButton(master=root,text="Decrypt image",command=dec)
    button.pack(pady=10,padx=10)
    root.mainloop()
    
x()