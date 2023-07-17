from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os
import wave
from AudioStego import AudioStego


class LSB_main:
    
    def exit(self, frame):
        frame.destroy()
        
    def lsb_main(self,root):
        root.title('Audio Steganaography')
        root.geometry('700x700')
        root.resizable(width = True, height = True)
        root.config(bg = '#e3f4f1')
        frame = Frame(root)
        frame.grid()

        title = Label(frame, text = 'AUDIO STEGANOGRAPHY')
        title.config(font = ('Arial',28,'bold'), bg = '#e3f4f1')
        title.grid(pady = 10)
        title.grid(row = 1)

        encode = Button(frame, text = "ENCODE", command = lambda:self.lsb_encode_frame1(frame), padx = 14, bg = '#e3f4f1')
        encode.config(font = ('Times new roman', 16), bg = '#e8c1c7')
        encode.grid(row = 2)

        decode = Button(frame, text = "DECODE", command = lambda:self.lsb_decode_frame1(frame), padx = 14, bg = '#e3f4f1')
        decode.config(font = ('Times new roman', 16), bg = '#e8c1c7')
        decode.grid(pady = 12)
        decode.grid(row = 3)

        back0 = Button(frame, text = 'EXIT', command = lambda:[self.exit(root)])
        back0.config(font = ('Times new roman', 16), bg = '#e8c1c7')
        back0.grid(row = 4)

        root.grid_rowconfigure(1, weight = 1)
        root.grid_columnconfigure(0, weight = 1)
        
    def back(self, frame):
        frame.destroy()
        self.lsb_main(root)
        
    def lsb_encode_frame1(self, F):
        F.destroy()
        e_F2 = Frame(root)
        label1 = Label(e_F2, text = 'Select Audio to Hide Text')
        label1.config(font = ('Times new roman', 28, 'bold'), bg = '#e3f4f1')
        label1.grid()

        encode1 = Button(e_F2, text = 'Select', command = lambda:self.lsb_encode_frame2(e_F2))
        encode1.config(font = ('Times new roman', 18), bg = '#e8c1c7')
        encode1.grid()

        back1 = Button(e_F2, text = 'Cancel', command = lambda:LSB_main.back(self, e_F2))
        back1.config(font = ('Times new roman', 18), bg = '#e8c1c7')
        back1.grid(pady = 15)
        back1.grid()
        e_F2.grid()

    def lsb_decode_frame1(self, F):
        F.destroy()
        d_F2 = Frame(root)
        label1 = Label(d_F2, text = 'Select Audio to Retrieve Text')
        label1.config(font = ('Times new roman', 28, 'bold'), bg = '#e3f4f1')
        label1.grid()

        decode1 = Button(d_F2, text = 'Select', command = lambda:self.lsb_decode_frame2(d_F2))
        decode1.config(font = ('Times new roman', 18), bg = '#e8c1c7')
        decode1.grid()

        back1 = Button(d_F2, text = 'Cancel', command = lambda:LSB_main.back(self, d_F2))
        back1.config(font = ('Times new roman', 18), bg = '#e8c1c7')
        back1.grid(pady = 15)
        back1.grid()
        d_F2.grid()

    def lsb_encode_frame2(self, e_F2):
        e_F3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('wav', '*.wav'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("ERROR", "You have selected NOTHING!")
        else:
            filepath = os.path.abspath(myfile)

            img = ImageTk.PhotoImage(Image.open("F:\B.sc CS Notes & Books\Final Year Final Sem\Mini Project [STEGANOGRAPHY]\Steganography\Audio Steganography\wav audio.png"))
            label4 = Label(e_F3, image = img)
            label4.image = img
            label4.grid()
            label3 = Label(e_F3, text = 'Enter the Message')
            label3.config(font = ('Times new roman', 14, 'bold'))
            label3.grid(pady = 15)
            string = Text(e_F3, width = 50, height = 10)
            string.grid()

            back2 = Button(e_F3, text = 'CANCEL', command = lambda:LSB_main.back(self, e_F3))
            back2.config(font = ('TImes new roman', 18), bg = '#e8c1c7')
            back2.grid()
            data = string.get("1.0", "end-1c")
            encode2 = Button(e_F3, text = 'ENCODE', command = lambda:[self.EncodeAudio(filepath,string), LSB_main.back(self,e_F3)])
            encode2.config(font = ('Times new roman', 18), bg = '#e8c1c7')
            encode2.grid(pady = 15)
            encode2.grid()
            e_F3.grid(row = 1)
            e_F2.destroy()

    def lsb_decode_frame2(self, d_F2):
        d_F3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('wav', '*.wav'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("ERROR", "You have selected NOTHING!")
        else:
            filepath = os.path.abspath(myfile)

            img = ImageTk.PhotoImage(Image.open("F:\B.sc CS Notes & Books\Final Year Final Sem\Mini Project [STEGANOGRAPHY]\Steganography\Audio Steganography\wav audio.png"))
            label4 = Label(d_F3, image = img)
            label4.image = img
            label4.grid()
            hidden_data = self.DecodeAudio(filepath)
            label3 = Label(d_F3, text = 'Hidden Data')
            label3.config(font = ('Times new roman', 14, 'bold'))
            label3.grid(pady = 15)
            string = Text(d_F3, width = 50, height = 10)
            string.insert(INSERT, hidden_data)
            string.configure(state = 'disabled')
            string.grid()
            

            back2 = Button(d_F3, text = 'CANCEL', command = lambda:LSB_main.back(self, d_F3))
            back2.config(font = ('TImes new roman', 18), bg = '#e8c1c7')
            back2.grid()
            back2.grid(pady = 15)
            back2.grid()
            d_F3.grid(row = 1)
            d_F2.destroy()

    def DecodeAudio(self, filepath) -> str:
        data = ''
        audioArray = self.ConvertToByteArray(filepath)
        decodedArray = [audioArray[i] & 1 for i in range(len(audioArray))]
        self.audio.close()
        data  = "".join(chr(int("".join(map(str, decodedArray[i:i + 8])), 2)) for i in range(0, len(decodedArray), 8)).split("###")[0]
        return data

    def SaveToLocation(self,audioArray, location):
        dir = os.path.dirname(location)
        self.newAudio = wave.open(dir + "/output-lsb.wav", 'wb')
        self.newAudio.setparams(self.audio.getparams())
        self.newAudio.writeframes(audioArray)
        self.newAudio.close()
        self.audio.close()
        return dir + "/output-lsb.wav"

    def ConvertToByteArray(self, filepath):
        self.audio = wave.open(filepath, mode = "rb")
        return bytearray(list(self.audio.readframes(self.audio.getnframes())))
    
    def EncodeAudio(self, filepath, stringToEncode) -> str:
        data = stringToEncode.get("1.0", "end-1c")
        if(len(data) == 0):
            messagebox.showinfo("Alert", "Kindly enter the text in TextBox")
        else:
            audioArray = self.ConvertToByteArray(filepath)
            stringToEncode = data + int((len(audioArray) - (len(data) * 8 * 8)) / 8) * '#'
            bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in stringToEncode])))
            for i, bit in enumerate(bits):
                audioArray[i] = (audioArray[i] & 254) | bit
            encodedAudio = bytes(audioArray)
            messagebox.showinfo("Success", "Embedding Successful\nFile has been saved to the same directory")
            return self.SaveToLocation(encodedAudio, filepath)



root = Tk()
o = LSB_main()
o.lsb_main(root)
root.mainloop()
