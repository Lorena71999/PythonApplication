from datetime import datetime

import speech_recognition as sr
from translate import Translator
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import timeit





def browseFiles():

    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

    label_file_explorer=tk.Label(text="File Opened: " + filename,fg = "#424874", bg = "#e3cdc1",font = ("BlackChancery", 11)).pack(pady = 20)
window = Tk()
label1 = tk.Label(window, text="Hello!", fg="#424874", bg="#e3cdc1", width=580, font=("Ubuntu", 26)).pack()
label2 = tk.Label(window, text="Welcome to ForTrans!", fg = "#424874", bg = "#e3cdc1", width = 400, font=("Montserrat", 26)).pack(padx = 10, pady = 10)
s = ttk.Style()
s.configure('.', background='#e3cdc1')
s.configure('.',font=("Montserrat", 19))
s.configure('.', foreground='#424874')

button_explore = Button(window,text="Browse Audio File",command=browseFiles, fg="#424874", bg="#e3cdc1",font = ("Montserrat", 16)).pack(padx = 10, pady = 30)
ttk.Label(window, text="Select the Language :",font=("Montserrat", 14)).pack( padx=10, pady=10)

n = tk.StringVar()
choose = ttk.Combobox(window, width=30,textvariable=n,foreground="#424874")

choose['values'] = ('romanian',
                          'albanian',
                          'amharic',
                          'arabic',
                          'armenian',
                          'basque',
                          'belarusian',
                          'bengali',
                          'bulgarian',
                          'catalan',
                          'croatian',
                          'greek',
                          'hungarian',
                          'croatian',
                          'danish',
                          'estonian',
                          'filipino',
                          'french',
                          'turkish',
                          'russian',
                          'norwegian',
                          'urdu'
                          )

choose.pack()
choose.current(1)

def clicked():

   global mylabel
   path = filename
   start_path = path.find('.') + 1
   end_path = int(len(path))
   format = path[start_path:end_path]


   if (format != "wav"):
       audio_file = AudioSegment.from_file(path, format)
       path1 = path[0:path.find('.')] + ".wav"
       audio_file.export(path1, format="wav")
       path = path1

   with sr.AudioFile(path) as source:
       r = sr.Recognizer()
       audio = r.record(source)
       text = r.recognize_google(audio)
       mylabel = Label(window, fg="#424874", bg="#e3cdc1", font=40,text="The text from the Audio file is: " + text).pack()
       translation = Translator(to_lang=choose.get())
       t = translation.translate(text)
       label3 =  Label(window, fg="#424874", bg="#e3cdc1", font=40, text="The  translated text  is:  "+  t).pack()

a = timeit.timeit()
btn = tk.Button(window, text="Translate", command=clicked, fg="#424874", bg="#e3cdc1", padx=20, pady=20,font=("Montserrat", 20)).pack(padx=20, pady=20)
b = timeit.timeit()

print (b-a)
window.geometry('600x700')
window.title("Aplicatii multimedia")
window.configure(bg="#e3cdc1")

button_exit = Button(window,text="Exit",command=exit,fg="#424874", bg="#e3cdc1",font = ("Montserrat", 15)).pack(padx = 20,pady = 10)

window.mainloop()
