#    ************************************
#        STEGANOGRAPHY MINI PROJECT
#    ************************************

#Importing Modules
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os

class IMG_Stegno:
    output_image_size = 0

    def exit(self, frame):
        frame.destroy()

    # Main Frame code

    def main(self, root):
        root.title('Image Steganography')
        root.geometry('700x700')
        root.resizable(width = True, height = True)
        root.config(bg = '#e3f4f1')
        frame = Frame(root)
        frame.grid()
    
        title = Label(frame,text = 'Image Steganography')
        title.config(font = ('Arial',28,'bold'),bg = '#e3f4f1')
        title.grid(pady = 10)
        title.grid(row = 1)

        encode  = Button(frame,text="ENCODE", command = lambda:self.encode_frame1(frame), padx = 14, bg = '#e3f4f1')
        encode.config(font = ('Times new  roman',16), bg = '#e8c1c7')
        encode.grid(row = 2)
        decode  = Button(frame,text = "DECODE", command = lambda:self.decode_frame1(frame), padx = 14, bg = '#e3f4f1')
        decode.config(font = ('Times new  roman',16), bg = '#e8c1c7')
        decode.grid(pady = 12)
        decode.grid(row = 3)

        back0 = Button(frame, text = 'BACK', command = lambda:[self.exit(root)])
        back0.config(font = ('Times new roman', 16), bg = '#e8c1c7')
        back0.grid(row = 4)

        root.grid_rowconfigure(1, weight = 1)
        root.grid_columnconfigure(0, weight = 1)

    # Back function to loop back to main screen

    def back(self,frame):
        frame.destroy()
        self.main(root)

    # Frame for Encode Page

    def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root)
        label1 = Label(F2, text = 'Select Image to hide text')
        label1.config(font = ('Arial',28,'bold'), bg = '#e3f4f1')
        label1.grid()
    
        button_bws = Button(F2, text = 'Select', command = lambda:self.encode_frame2(F2))
        button_bws.config(font=('Times new roman',18), bg = '#e8c1c7')
        button_bws.grid()
        button_back = Button(F2, text = 'Cancel', command = lambda:IMG_Stegno.back(self,F2))
        button_back.config(font=('Times new roman',18), bg = '#e8c1c7')
        button_back.grid(pady = 15)
        button_back.grid()
        F2.grid()

    #Frame for Decode Page
    
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text = 'Select Image with hidden text')
        label1.config(font = ('Arial',28,'bold'), bg = '#e3f4f1')
        label1.grid()
    
        button_bws = Button(d_f2, text = 'Select', command = lambda:self.decode_frame2(d_f2))
        button_bws.config(font=('Times new roman',18), bg = '#e8c1c7')
        button_bws.grid()
        button_back = Button(d_f2, text = 'Cancel', command = lambda:IMG_Stegno.back(self,d_f2))
        button_back.config(font=('Times new roman',18), bg = '#e8c1c7')
        button_back.grid(pady = 15)
        button_back.grid()
        d_f2.grid()

    # Function to Encode Image

    def encode_frame2(self,e_F2):
        e_pg = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'), ('jpeg', '*.jpeg'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected Nothing!")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_image)
            label3 = Label(e_pg, text = 'Selected Image')
            label3.config(font=('Times new roman', 14, 'bold'))
            label3.grid()
            board = Label(e_pg, image = img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            label2 = Label(e_pg, text = 'Enter the message')
            label2.config(font=('Times new roman',14,'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width = 50, height = 10)
            text_a.grid()
            encode_button = Button(e_pg, text = 'Cancel', command = lambda:IMG_Stegno.back(self,e_pg))
            encode_button.config(font=('Times new  roman',18), bg = '#e8c1c7')
            data = text_a.get("1.0", "end-1c")
            button_back = Button(e_pg, text = 'Encode', command = lambda : [self.enc_fun(text_a, my_img), IMG_Stegno.back(self,e_pg)])
            button_back.config(font = ('Times new roman',18), bg = '#e8c1c7')
            button_back.grid(pady = 15)
            encode_button.grid()
            e_pg.grid(row = 1)
            e_F2.destroy()

    # Function to Decode Image

    def decode_frame2(self,d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error","You have selected Nothing!")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(my_image)
            label4 = Label(d_F3, text = 'Selected Image: ')
            label4.config(font=('Times new roman', 14, 'bold'))
            label4.grid()
            board = Label(d_F3, image = img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            label2 = Label(d_F3, text = 'Hidden data is: ')
            label2.config(font = ('Times new roman', 14, 'bold'))
            label2.grid(pady = 10)
            text_a = Text(d_F3, width = 50, height = 10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state = 'disabled')
            text_a.grid()
            button_back = Button(d_F3, text = 'Cancel', command = lambda:self.frame_3(d_F3))
            button_back.config(font = ('Times new roman', 14), bg = '#e8c1c7')
            button_back.grid(pady = 15)
            button_back.grid()
            d_F3.grid(row = 1)
            d_F2.destroy()

    # Function to Decode Data

    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data
            
    # Function to Generate Data

    def generate_Data(self,data):
        # List of binary codes of given data
        new_data = []
        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data

    # Function to Modify the Pixels of Image

    def modify_Pix(self, pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            for j in range(0,8):
                if (dataList[i][j]=='0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1
                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                   pix[j] -= 1
            if (i == dataLen-1):
                if(pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if(pix[-1] % 2 != 0):
                    pix[-1] -= 1
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    # Function to Enter the data Pixels in Images

    def encode_enc(self, newImg, data):
        w = newImg.size[0]
        (x,y) = (0,0)
        for pixel in self.modify_Pix(newImg.getdata(),data):
            #Putting modified pixxels in the New Image
            newImg.putpixel((x,y), pixel)
            if(x == w-1):
                x=0
                y+=1
            else:
                x+=1

    #Function to Enter Hidden Text

    def enc_fun(self, text_a, myImg):
        data = text_a.get("1.0", "end-1c")
        if(len(data) == 0):
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myImg.filename))
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes = ([('png','*.png')]), defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved in the same directory")

    def frame_3(self,frame):
        frame.destroy()
        self.main(root)

# GUI Loop

root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()
