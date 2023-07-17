from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
import os
import sys

class Stegno:

    def exit(self, frame):
        root.destroy()
        
    def main(self,root):
        root.title('Steganography')
        root.geometry('700x700')
        root.resizable(height = True, width = True)
        root.config(bg = '#e3f4f1')
        frame = Frame(root)
        frame.grid()

        title = Label(frame, text = 'STEGANOGRAPHY')
        title.config(font = ('Arial',28, 'bold'), bg = '#e3f4f1')
        title.grid(pady = 10)
        title.grid(row = 1)

        label1 = Label(frame, text = 'Select The Method You Want To Use')
        label1.config(font = ('Arial', 28, 'bold'), bg = "#e3f4f1")
        label1.grid(pady = 12)
        label1.grid(row = 2)

        IMGS = Button(frame, text = 'USING IMAGE', command = lambda:os.system('Image_Steganography.py'))
        IMGS.config(font = ('Times new roman', 16), bg = '#e8c1c7')
        IMGS.grid(row = 3)

        AUDS = Button(frame, text = 'USING AUDIO', command = lambda:os.system('Audio_Steganography_Using_LSB.py'))
        AUDS.config(font = ('Times new roman', 16), bg = '#e8c1c7')
        AUDS.grid(pady = 14)
        AUDS.grid(row = 4)

        exit1 = Button(frame, text = 'EXIT', command = lambda:[self.exit(root), sys.exit()])
        exit1.config(font = ('Times new roman', 16), bg = "#e8c1c7")
        exit1.grid(row = 5)

        root.grid_rowconfigure(1, weight = 1)
        root.grid_columnconfigure(0, weight = 1)

root = Tk()
s = Stegno()
s.main(root)
root.mainloop()
