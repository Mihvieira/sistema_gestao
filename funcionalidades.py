import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import PIL.Image
import customtkinter as ctk
from PIL import ImageTk, Image
from datetime import datetime, time, timedelta
from tkcalendar import DateEntry, Calendar
from banco_de_dados import BancoDeDados

class Calendario:
    def __init__(self, frame, x, y):
        self.frame = frame
        self.x = x
        self.y = y
        self.data_cal = StringVar(self.frame, Calendar.date.today().strftime("%d/%m/%y"))
        self.criar_calendario()

    def criar_calendario(self):
        self.cal = Calendar(self.frame, date_pattern="dd/mm/yyyy",
                            selectmode='day', font=ctk.CTkFont('Calibri', 16), locale='pt_BR', disableforeground='red',
                            cursor='hand2', background='black', selectbackground='gray', textvariable=self.data_cal)
        self.cal.place(x=self.x, y=self.y)
        print(self.data_cal.get())
        self.cal.bind('<<CalendarSelected>>', self.ver_data_calendario)

    @property
    def ver_data_calendario(self):
        print(self.data_cal.get())
        return self.data_cal.get()

    def config_calendario(self, **kwargs):
        return self.cal.config(**kwargs)

    def criar_evento_calendario(self, nome, dt, tag):
        self.texto = nome
        self.tag = tag
        self.dt = datetime.strptime(dt, '%d/%m/%Y')
        return self.cal.calevent_create(date=self.dt, text=self.texto, tags=self.tag), self.cal.tag_config(self.tag,
                                                                                                           background='blue',
                                                                                                           foreground='black')

    def ver_eventos_calendario(self):
        pass

    def delete_evento(self, evento):
        return self.cal.calevent_remove(evento)


class EntradaData:
    def __init__(self, frame, x, y, data):
        self.frame = frame
        self.x = x
        self.y = y
        self.data = data
        valor = Calendar.date.today().strftime("%d/%m/%Y")
        if self.data is not None:
            self.date_entry = StringVar(self.frame, self.data)
        else:
            self.date_entry = StringVar(self.frame, valor)
        self.dtano = datetime.strptime(self.date_entry.get(), "%d/%m/%Y").year
        self.dtmes = datetime.strptime(self.date_entry.get(), "%d/%m/%Y").month
        self.dtdia = datetime.strptime(self.date_entry.get(), "%d/%m/%Y").day
        self.criar_date_entry()

    def criar_date_entry(self):
        # por padrão o calendário vem com a data do sistema
        self.escolher_data = DateEntry(self.frame, width=12, selectmode='day', year=self.dtano, month=self.dtmes,
                                       day=self.dtdia,
                                       foreground='white', background='darkblue',
                                       borderwidth=2,
                                       date_pattern='dd/mm/Y', font='Calibri', textvariable=self.date_entry)

        self.escolher_data.place(x=self.x, y=self.y)

    def config_date_entry(self, **kwargs):
        return self.escolher_data.config(**kwargs)

    @property
    def ver_date_entry(self):
        return self.date_entry.get()

    def desabilitar_dtentry(self):
        self.escolher_data.configure(state='disable')

    def remover_dateentry(self):
        self.escolher_data.place_forget()


class Entrada:
    def __init__(self, frame, x, y):
        self.frame = frame
        self.x = x
        self.y = y


class Trv:
    def __init__(self, frame, colunas, x, y, table, idbd, **kwargs):
        self.frame = frame
        self.text = colunas
        self.x = x
        self.y = y
        self.table = table
        self.idbd = idbd
        self.criar_treeview()

    def criar_treeview(self):
        # treeview
        self.trv = ttk.Treeview(master=self.frame, columns=self.text, show='headings', height=10)
        self.trv.place(x=self.x, y=self.y)

        for i in self.text:
            self.trv.heading(i, text=i)
            self.trv.column(i, minwidth=0, width=70)

        self.trv.bind('<<TreeviewSelect>>', lambda event: print(self.item_select()))
        self.trv.bind('<Delete>', self.delete_items)

    def barra_rolagem(self, valor):
        if valor == 'vertical':
            self.vsb = ttk.Scrollbar(self.frame, orient="vertical", command=self.trv.yview)
            return self.trv.configure(yscrollcommand=self.vsb.set)
        else:
            self.hsb = ttk.Scrollbar(self.frame, orient="horizontal", command=self.trv.xview)
            return self.trv.configure(xscrollcommand=self.hsb.set)

    def insert_rows(self, valores):
        self.valores = valores
        print(valores)
        for i in self.valores:
            print(i)
            self.trv.insert('', tkinter.END, values=i)

    def item_select(self):
        print(self.trv.selection)
        for i in self.trv.selection():
            return self.trv.item(i)['values']

    def delete_items(self, valor):
        m = messagebox.showwarning(title='', message='Tem certeza que deseja excluir o item selecionado?')
        if m == 'ok':
            selected_item = f'{self.item_select()[0]}'
            print(selected_item)
            selected_item_2 = self.trv.selection()[0]
            print(selected_item_2)
            print(selected_item)

            bd = BancoDeDados()
            query = f'DELETE FROM {self.table} WHERE {self.idbd} = {selected_item}'
            print(query)
            bd.atualizar(query)
            return self.trv.delete(selected_item_2)

        else:
            return None

    def mudar_tamanho_coluna(self, nome_coluna, minwidth, width):
        return self.trv.column(f'{nome_coluna}', minwidth=minwidth, width=width)


class Botao:
    def __init__(self, frame, text, command, x, y):
        self.frame = frame
        self.text = str(text)
        self.command = command
        self.x = x
        self.y = y
        self.criar_botao()

    def criar_botao(self):
        self.botao = ctk.CTkButton(self.frame, text=self.text, fg_color='gray', command=self.command)
        self.botao.place(x=self.x, y=self.y)
        return self.botao

    def configurar_botao(self, **kwargs):
        return self.botao.configure(**kwargs)