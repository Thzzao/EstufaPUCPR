import random
from time import time
from tkinter import W

#Camada de Abstração de Hardware 

def aquecedor (estado: str):
    if estado == 'on':
        print ('Aquecedor LIGADO')
    else:
        print('Aquecedor DESLIGADO')


def controleTemp ( estado: str):
    if estado == 'on':
        print ('Controle de Temperatura AUTO')
    else:
        print ('Controle de Temperatura MANU')


def temperaturaDips1 ():
    return random.randrange (0,60)    

def temperaturaDips2():
    return random.randrange (0,60)
