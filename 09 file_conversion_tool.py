import tkinter as tk
from tkinter import Canvas, filedialog
from tkinter import font
from PIL import Image

root = tk.Tk()

Canvas1 = tk.Canvas(root, width = 300, height = 250, bg = "azure3", relief = "raised")
Canvas1.pack()

label1 = tk.Label(root,text="file coversion tool", bg = "azure3")
label1.config(font = ("helvatica", 20))
Canvas1.create_window(150,60,window=label1)

def getPNG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browseButton_PNG = tk.Button(text="IMPORT PNG FILE", command= getPNG,bg = 'royalblue', fg='white', font= ("helvetica_JPG",12,font.BOLD) )
Canvas1.create_window(150,140, window = browseButton_PNG)

def convertToJPG():
    global im1
    export_file_path = filedialog.askopenfilename(defaultextension='.jpg')
    im1.save(export_file_path)

saveAsButton_JPG =tk.Button(text="convert PNG to JPG", command= convertToJPG,bg = 'royalblue', fg='white', font= ('helvetica',12,font.BOLD) )
Canvas1.create_window(150,180,window=saveAsButton_JPG)

root.mainloop()