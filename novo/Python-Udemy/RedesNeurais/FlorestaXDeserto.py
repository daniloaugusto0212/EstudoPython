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
        self.rede = Sequential()

        self.rede.add(Conv2D(64, (3, 3), input_shape=(64, 64, 3), activation='relu'))
        self.rede.add(BatchNormalization())
        self.rede.add(MaxPooling2D(pool_size=(2, 2)))

        self.rede.add(Flatten())

        self.rede.add(Dense(units=100, activation='relu'))
        self.rede.add(Dense(units=100, activation='relu'))
        self.rede.add(Dense(units=1, activation='sigmoid'))

        self.rede.compiler(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        gerador_treinamento = ImageDataGenerator(rescale=1. / 255, rotation_range=7, horizontal_flip=True, shear_range=0.2, heght_shift_range=0.07, zoom_range=0.2)

        gerador_teste = ImageDataGenerator(rescale=1. / 255)

        base_treinamento = gerador_treinamento.flow_from_directory('imagensRede/Treinamento', target_size(64, 64), batch_size=32, class_mode='binary')

        base_teste = gerador_treinamento.flow_from_directory('imagensRede/Teste', target_size=(64, 64), batch_size=32, class_mode='binary')

        self.rede.fit_generator(base_treinamento, steps_per_epoch=20, epochs=3, validaton_data = base_teste, validation_steps = 20)
    
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