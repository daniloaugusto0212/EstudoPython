from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

class Interface():
    
    def Captura(self):
        self.filename = askopenfilename()

        self.image = Image.open(self.filename)

        self.photo = ImageTk.PhotoImage(self.image)

        label = Label(self.root, image=self.photo).grid(row=1, column=0, padx=15, pady=5, rowspan=3)


    
    def Treinamento(self):
        pass
    
    def ClassificarImagens(self):
        pass
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Classificador de imagens')
        
        Button(self.root, text='Selecione a imagem', command=self.Captura).grid(row=0, column=0, pady=5)
        Button(self.root, text='Treinar rede', command=self.Treinamento, width=10, height=2).grid(row=0, column=1)
        Button(self.root, text='Classificar', command=self.ClassificarImagens, width=10, height=2).grid(row=1, column=1)
        self.root.mainloop()
        
Interface()