import os
import requests
import PIL.ImageTk
import PIL.Image
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import json
import pygame


class GUI:

    def __init__(self,raiz:Tk) -> None:
        self.raiz = raiz
        self.raiz.iconbitmap('GUI/icons/play.ico')
        self.raiz.geometry("700x400")
        
        raiz.rowconfigure(0,weight=1)
        raiz.columnconfigure(0,weight=1)
        
        #Main Principal
        mainframe = ttk.Frame(raiz)
        mainframe.grid(row=0,column=0,sticky=NSEW)
        mainframe.rowconfigure(1, weight=1)
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)
        
        
        #Contenedor Del Panel(Informacion Musica), Barra(Play,Pause,etc) y Lista(Canciones a Reporducir)
        container_info = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        container_info.grid(row=0,column=0, sticky=NSEW)
        
        label_nombre = ttk.Label(container_info, text='Nombre: ')
        label_artista = ttk.Label(container_info, text='Artista: ')
        label_ruta = ttk.Label(container_info, text='Ruta: : ')
        label_genero = ttk.Label(container_info, text='Genero: : ')
        label_ano = ttk.Label(container_info, text='Lanzamiento: ')
        
        
        label_nombre.grid(row=0, column=0, sticky=NSEW)
        label_artista.grid(row=1, column=0, sticky=NSEW)
        label_ruta.grid(row=2, column=0, sticky=NSEW)
        label_genero.grid(row=3, column=0, sticky=NSEW)
        label_ano.grid(row=4, column=0, sticky=NSEW)
        
        Container_button_upload_list = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        Container_button_upload_list.grid(row=0,column=1, sticky=NSEW)
        
        Button_upload_list = ttk.Button(Container_button_upload_list,text="Upload List")
        Button_upload_list.grid(row=1,column=1,sticky=NSEW)
        
        Container_button_upload_list.columnconfigure(1,weight=1)
        Container_button_upload_list.rowconfigure(1,weight=1)
        
        #Lista(Canciones a Reporducir)
        container_lista = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        container_lista.grid(row=1,column=1, sticky=NSEW)
        
        
        label_Lista = ttk.Label(container_lista, text='Lista de Reproduccion: ')
        label_Lista.grid(row=0, column=0, sticky=NSEW)
        
        #Contenedor Boton Salir
        Container_button_exit = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        Container_button_exit.grid(row=2,column=1, sticky=NSEW)
        
        Button_exit = ttk.Button(Container_button_exit,text="Exit")
        Button_exit.grid(row=1,column=1,sticky=NSEW)
        
        Container_button_exit.columnconfigure(1,weight=1)
        
        
        #Panel Imagen Musica
        container_multimedia = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        self.imagen = ttk.Label(container_multimedia, text='Imagen')
        self.setImage('GUI/icons/multimedia.png')
        
        
        container_multimedia.grid(row=1,column=0,sticky=NSEW)
        self.imagen.grid(row=0,column=0,sticky=NSEW)
        
        
        #Barra(Play,Pause,etc)
        container_buttons = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        container_buttons.grid(row=2,column=0,sticky=NSEW)
        
        play = ttk.Button(container_buttons,text='Play')
        stop = ttk.Button(container_buttons,text='Stop')
        pause = ttk.Button(container_buttons,text='Pause')
        previus = ttk.Button(container_buttons,text='Previus')
        next = ttk.Button(container_buttons,text="Next")
         
        play.grid(row=1,column=1,sticky=EW)
        stop.grid(row=1,column=2,sticky=EW)
        pause.grid(row=1,column=3,sticky=EW)
        previus.grid(row=1,column=4,sticky=EW)
        next.grid(row=1,column=5,sticky=EW)
        
        container_buttons.columnconfigure(1,weight=1)
        container_buttons.columnconfigure(2,weight=1)
        container_buttons.columnconfigure(3,weight=1)
        container_buttons.columnconfigure(4,weight=1)
        container_buttons.columnconfigure(5,weight=1)
        
        
    def setImage(self,route):
        self.img = PIL.ImageTk.PhotoImage(PIL.Image.open(route).resize((600,600)))
        self.imagen['image'] = self.img

        


        
        



        
        
        

        






       
       



