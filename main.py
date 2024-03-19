import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import PIL.Image
import customtkinter as ctk
from PIL import ImageTk, Image
from datetime import datetime, time, timedelta
from tkcalendar import DateEntry, Calendar
from funcionalidades import *
from Agenda_calendario import *
from Login import *
from Produtos import *
from Cadastro import *
from Alugueis_Vendas import *
from eventos import *
from pagamentos_rh import *
from banco_de_dados import BancoDeDados


class Janela(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.screen_configuration()
        self.toplevel_window = None
        self.show_inicial_screen()
        # Executar janela
        self.mainloop()

    def show_login(self):
        self.login = Login(self)
        self.login.pack(expand=True, fill='both')

    def show_inicial_screen(self):
        self.inicial_screen = InicialScren(self)
        self.inicial_screen.pack(expand=True, fill='both')

    def screen_configuration(self):
        self.geometry('1366x768')
        self.title('Sistema de Gerenciamento de Informações')
        self.maxsize(1366, 768)
        self._set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')


class InicialScren(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.username_loguin = 'Mirelly'

        # criando frame menu
        self.frame_menu = ctk.CTkFrame(self, width=50, height=768, fg_color='#0d1316', bg_color='black')
        self.frame_menu.place(x=0, y=0)

        # criando frame cima
        self.frame_título = ctk.CTkFrame(self, width=1360, height=50, fg_color='#0d1316', bg_color='black')
        self.frame_título.place(x=50, y=0)

        # criando frame meio
        self.frame_options = ctk.CTkFrame(self, width=1360, height=718, fg_color='white')
        self.frame_options.place(x=50, y=55)

        self.menu_widgets()
        self.options_widgets()

    def menu_widgets(self):
        self.img_logo = ctk.CTkImage(PIL.Image.open('Images/logo1.png'), size=(50, 50))
        self.img_home = ctk.CTkImage(PIL.Image.open('Images/home.png'))
        self.img_graph = ctk.CTkImage(PIL.Image.open('Images/monitoring.png'))
        self.img_acount = ctk.CTkImage(PIL.Image.open('Images/account_box.png'))
        self.img_group = ctk.CTkImage(PIL.Image.open('Images/group_add.png'))
        self.img_pesquisa = ctk.CTkImage(PIL.Image.open('Images/search.png'))

        self.lb_logo = ctk.CTkLabel(self.frame_menu, image=self.img_logo, text='')
        self.lb_logo.place(x=0, y=10)

        self.btn_home = ctk.CTkButton(self.frame_menu, image=self.img_home, text='', width=30, fg_color='white',
                                      command=self.home)
        self.btn_home.place(x=8, y=450)
        self.btn_graph = ctk.CTkButton(self.frame_menu, image=self.img_graph, text='', width=30, fg_color='white',
                                       command=self.dashboard)
        self.btn_graph.place(x=8, y=500)
        self.btn_acount = ctk.CTkButton(self.frame_menu, image=self.img_acount, text='', width=30, fg_color='white',
                                        command=self.conta_box)
        self.btn_acount.place(x=8, y=550)
        self.btn_group = ctk.CTkButton(self.frame_menu, image=self.img_group, text='', width=30, fg_color='white',
                                       command=self.add_user)
        self.btn_group.place(x=8, y=600)

        self.lb_nome = ctk.CTkLabel(self.frame_título, text=f'Olá {self.username_loguin}.', text_color='white',
                                    font=('Calibri bold', 20))
        self.lb_nome.place(x=50, y=20)
        self.entry_pesquisa = ctk.CTkEntry(self.frame_título, width=300, placeholder_text='Pesquise aqui..',
                                           border_color='#f56e8a')
        self.entry_pesquisa.place(x=899, y=18)

        self.btn_pesquisa = ctk.CTkButton(self.frame_título, image=self.img_pesquisa, text='', width=60,
                                          fg_color='white')
        self.btn_pesquisa.place(x=1200, y=18)

    def home(self):
        self.inicial_screen = InicialScren(self)
        self.inicial_screen.pack(expand=True, fill='both')

    def dashboard(self):
        pass

    def conta_box(self):
        pass

    def add_user(self):
        pass

    def options_widgets(self):
        # imagem botão subframes
        self.img_add = ctk.CTkImage(PIL.Image.open('Images/icons8-adicionar-30.png'))
        self.btn_add1 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Cadastro', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT, command=self.abrir_cadastro)
        self.btn_add1.place(x=100, y=90)

        self.btn_add2 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Agenda', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT, command=self.abrir_agenda)
        self.btn_add2.place(x=400, y=90)

        self.btn_add3 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Eventos', width=230,
                                      height=200, fg_color='pink', bg_color='pink', text_color='black',
                                      font=('Verdana bold', 22), compound=RIGHT, command=self.abrir_evento)
        self.btn_add3.place(x=700, y=90)

        self.btn_add4 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Produtos', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT, command=self.abrir_produtos)
        self.btn_add4.place(x=1000, y=90)

        self.btn_add5 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Clientes', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT, command=self.abrir_clientes)
        self.btn_add5.place(x=100, y=390)

        self.btn_add6 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Vendas', width=230,
                                      height=200, fg_color='pink', bg_color='pink', text_color='black',
                                      font=('Verdana bold', 22), compound=RIGHT, command=self.abrir_vendas)
        self.btn_add6.place(x=400, y=390)

        self.btn_add7 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Alugueis', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT, command=self.abrir_pagamentos)
        self.btn_add7.place(x=700, y=390)

        self.btn_add8 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Pagamentos', width=230,
                                      height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT, command=self.abrir_rh)
        self.btn_add8.place(x=1000, y=390)

    def clean_options(self):
        self.frame_options.place_forget()

    def abrir_cadastro(self):
        self.clean_options()
        self.cadastro = Cadastro(self)
        self.cadastro.place(x=50, y=55)

    def abrir_agenda(self):
        self.clean_options()
        self.agenda = Agenda(self)
        self.agenda.place(x=50, y=55)

    def abrir_evento(self):
        self.clean_options()
        self.evento = Eventos(self)
        self.evento.place(x=50, y=55)

    def abrir_produtos(self):
        self.clean_options()
        self.produto = Produtos(self)
        self.produto.place(x=50, y=55)

    def abrir_pagamentos(self):
        self.clean_options()
        self.pagamentos = Pagamentos(self)
        self.pagamentos.place(x=50, y=55)

    def abrir_vendas(self):
        self.clean_options()
        self.vendas = Vendas(self)
        self.vendas.place(x=50, y=55)

    def abrir_clientes(self):
        self.clean_options()
        self.clientes = Clientes(self)
        self.clientes.place(x=50, y=55)

    def abrir_rh(self):
        self.clean_options()
        self.rh = RH(self)
        self.rh.place(x=50, y=55)


if __name__ == '__main__':
    app = Janela()
