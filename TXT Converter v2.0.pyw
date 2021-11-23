import os
import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import *
from tkinter import messagebox
from pathlib import Path


root = tk.Tk()

def Comma2Tab():

    root.filename_in =  fd.askopenfilename(initialdir=os.getcwd(),title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    root.filename = Path(root.filename_in)

    if root.filename_in.endswith(".txt"):
        root.filename_out =  fd.asksaveasfilename(initialfile = os.path.basename(root.filename.with_suffix(".tab.txt")), title = "Save file", filetypes = (("txt files","*.txt"),("all files","*.*")),defaultextension = ".txt")

        fin = open(root.filename_in, "r") 
        fout = open(root.filename_out, "w")
        for line in fin:
            new_line = line.replace(',', '\t')
            fout.write(new_line) 
        fin.close()
        fout.close()
        
        root.destroy()


    else: 
        messagebox.showerror("Error!", "Choose a TXT file! Try Again")    

def Tab2Comma():

    root.filename_in =  fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    root.filename = Path(root.filename_in)

    if root.filename_in.endswith(".txt"):
        root.filename_out =  fd.asksaveasfilename(initialfile = os.path.basename(root.filename.with_suffix(".comma.txt")),title = "Save file",filetypes = (("txt files","*.txt"),("all files","*.*")),defaultextension = ".txt")

        fin = open(root.filename_in, "r") 
        fout = open(root.filename_out, "w")
        for line in fin:
            new_line = line.replace('\t', ',')
            fout.write(new_line) 
        fin.close()
        fout.close()

        root.destroy()


    else: 
        messagebox.showerror("Error!", "Choose a TXT file! Try Again") 

def About():
    messagebox.showinfo("ALU DEV TEAM @ 2021", "by nikkpap (nikkpap@gmail.com)")


Title = root.title( "TXT Converter v2")
frame = tk.Frame(root)
frame.pack()

button1 = Button(root, text = "Comma 2 Tab", 
                width = 20, height = 2, 
                bg = "red", fg = "brown", 
                font = ("helvetica", 12, "bold"), 
                command = Comma2Tab) 
    
button1.place(x = 80, y = 60) 
    
button2 = Button(root, text = "Tab 2 Comma", 
                width = 20, height = 2, 
                bg = "orange", fg = "brown", 
                font = ("helvetica", 12, "bold"), 
                command = Tab2Comma) 
    
button2.place(x = 80, y = 150) 



#Menu Bar

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Comma2Tab', command = Comma2Tab)
file.add_command(label = 'Tab2Comma', command = Tab2Comma)
file.add_command(label = 'About', command = About)
file.add_command(label = 'Exit', command = lambda:exit())

menu.add_cascade(label = 'File', menu = file)


root.geometry("360x260+300+200")
root.mainloop()