from main import *
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox, ttk
from banco_de_dados import *


class Agenda(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(width=1360, height=718, fg_color='#fafcd4')
        self.tabela = 'tarefas'
        self.calendario = None
        self.calendario_agenda()

        self.dtI = None
        self.dtF = None
        self.display()

    def atualizar_dados_agenda(self):
        bd = BancoDeDados()
        query = f'SELECT nome, DataInicio, DataFinal, TagLocal FROM {self.tabela}'
        a = bd.consulta_bd(query)
        print(a)
        for n, di, df, tl in a:
            self.calendario.criar_evento_calendario(n, di, tl)
            self.calendario.criar_evento_calendario(n, df, tl)
            df = datetime.strptime(df, "%d/%m/%Y")
            di = datetime.strptime(di, "%d/%m/%Y")
            diff = (df - di).days
            print(diff)
            for i in range(diff):
                dt = di + timedelta(days=i)
                dt = dt.strftime("%d/%m/%Y")
                print(dt)
                self.calendario.criar_evento_calendario(n, dt, tl)

    def calendario_agenda(self):

        self.btn_atualizar_agenda = ctk.CTkButton(self, text='Atualizar Dados', fg_color='gray',
                                                  command=self.atualizar_dados_agenda)
        self.btn_atualizar_agenda.place(x=800, y=90)

        self.calendario = Calendario(self, 800, 140)

    def display(self):
        self.lb_titulo1 = ctk.CTkLabel(self, text='Pesquise ou delete Compromissos', text_color='black',
                                       font=('Calibri bold', 14))
        self.lb_titulo1.place(x=40, y=60)

        self.lb_data_agenda = ctk.CTkLabel(self, text='Entre:', text_color='black',
                                           font=('Calibri bold', 14))
        self.lb_data_agenda.place(x=40, y=90)

        self.data_agenda_inicio = EntradaData(self, 115, 90, None)
        self.dtI = self.data_agenda_inicio.ver_date_entry

        self.data_agenda_fim = EntradaData(self, 260, 90, None)
        self.dtF = self.data_agenda_fim.ver_date_entry

        self.btn_pesquisar_agenda = Botao(self, 'Pesquisar', self.show_events_display, 410, 90)

        self.btn_incluir_agenda = Botao(self, 'Incluir', self.criar_evento, 100, 500)

        self.btn_editar_agenda = Botao(self, 'Editar', self.editar_evento, 100, 540)

        
        # criando treeview para visualização dos compromissos
        colunas = ('Id', 'DInicio', 'DFim', 'Nome', 'Hora', 'Tag', 'Subtag')

        self.table_agenda = Trv(self, colunas, 100, 140, 'tarefas', 'idTarefa')
        self.table_agenda.barra_rolagem('vertical')
        self.table_agenda.barra_rolagem('horizontal')
        self.table_agenda.mudar_tamanho_coluna('Nome', 0, 120)
        self.table_agenda.mudar_tamanho_coluna('Id', 0, 20)
        self.table_agenda.mudar_tamanho_coluna('Hora', 0, 50)
        self.table_agenda.mudar_tamanho_coluna('Tag', 0, 50)


    def incluir_evento(self):
        rstate = self.rbotao._check_state
        self.ne = self.nome_evento_incluir.get()
        self.t = self.tag_incluir.get()
        self.dt_inicio = self.data_incluir_inicio.ver_date_entry
        self.hora = self.hora_evento_incluir.get()
        self.subtag1 = 'Null'
        self.dt_fim = self.data_incluir_fim.ver_date_entry
        print('ok1')
        # validação de dados
        if self.subtag_incluir.get() != '':
            print('ok2')
            self.subtag1 = self.subtag_incluir.get()
        print(self.subtag1)

        if rstate == True:
            print('ok4')
            self.dt_fim = self.dt_inicio
            print('ok5')
        print(self.date_fim)

        # Criando Tarefa - BD
        try:

            bd = BancoDeDados()
            print('ok7')
            valor = f'INSERT INTO {self.tabela} (nome, DataInicio, DataFinal, hora, tagLocal, subtag) VALUES ("{self.ne}", "{self.dt_inicio}", "{self.dt_fim}", "{self.hora}", "{self.t}", "{self.subtag1}");'
            print(valor)
            print('ok8')
            bd.inserir_dados(valor)
            print('ok82')
            messagebox.showinfo(title='Agenda', message='Dados inseridos com sucesso!')
            print('ok9')
            self.frame_taskday.place_forget()
            print('ok10')
            self.btn_incluir_agenda.configurar_botao(fg_color='gray')

        except:
            messagebox.showerror(title='Agenda', message='Erro! Tente Novamente!')

    def editar_evento(self):
        try:
            self.btn_editar_agenda.configurar_botao(fg_color='green')
            a = self.table_agenda.item_select()
            print(a)
            self.id_ed = a[0]
            self.dt_inicio_ed = a[1]
            self.dt_fim_ed = a[2]
            self.nome_ed = a[3]
            self.hora_ed = a[4]
            self.t_ed = a[5]
            self.subtag_ed = a[6]
            print('ok1')
            self.editar_evento_agenda()
            print('ok2')
            self.lb_id = ctk.CTkLabel(self.frame_taskday, text=f'Id: {self.id_ed}', text_color='black',
                                      font=('Calibri bold', 14))
            self.lb_id.place(x=260, y=130)

            self.btn_ok_incluir.configurar_botao(command=self.alterar_evento)

        except:
            messagebox.showerror(title='Agenda', message='Selecione um evento')


    def show_events_display(self):
        self.date_inicio = self.data_agenda_inicio.ver_date_entry
        self.date_fim = self.data_agenda_fim.ver_date_entry
        print(self.date_inicio, self.date_fim)
        bd = BancoDeDados()
        query = f'SELECT * FROM {self.tabela} WHERE DataInicio between "{self.date_inicio}" AND "{self.date_fim}"'
        a = bd.consulta_bd(query)
        return self.table_agenda.insert_rows(a)

    def criar_evento(self):
        self.btn_incluir_agenda.configurar_botao(fg_color='green')
        self.form_task_incluir()
        self.btn_ok_incluir.configurar_botao(command=self.incluir_evento)

    def frame_form_task(self):
        self.frame_taskday = ctk.CTkFrame(self, width=500, height=200)
        self.frame_taskday.place(x=300, y=410)

        self.lb_dti = ctk.CTkLabel(self.frame_taskday, text='Data de Início', text_color='black',
                                   font=ctk.CTkFont('Calibri bold', 14))
        self.lb_dti.place(x=20, y=30)

        self.lb_dtf = ctk.CTkLabel(self.frame_taskday, text='Data de Fim', text_color='black',
                                   font=ctk.CTkFont('Calibri bold', 14))
        self.lb_dtf.place(x=250, y=30)

        self.rbotao = ctk.CTkCheckBox(self.frame_taskday, text='Datas Iguais?', command=self.entradas_de_datas)
        self.rbotao.place(x=250, y=5)

        self.lb_nome = ctk.CTkLabel(self.frame_taskday, text='Nome', text_color='black',
                                    font=ctk.CTkFont('Calibri bold', 14))
        self.lb_nome.place(x=20, y=65)

        self.lb_h = ctk.CTkLabel(self.frame_taskday, text='Hora', text_color='black',
                                 font=('Calibri bold', 14))
        self.lb_h.place(x=190, y=65)

        self.lb_t = ctk.CTkLabel(self.frame_taskday, text='Tag', text_color='black',
                                 font=ctk.CTkFont('Calibri bold', 14))
        self.lb_t.place(x=340, y=65)

        self.lb_sub = ctk.CTkLabel(self.frame_taskday, text='SubTag', text_color='black',
                                   font=ctk.CTkFont('Calibri bold', 14))
        self.lb_sub.place(x=20, y=100)

        self.btn_ok_incluir = Botao(self.frame_taskday, 'OK', None, 20, 160)
        self.btn_ok_incluir.configurar_botao(fg_color='green')


    def form_task_incluir(self):
        self.frame_form_task()
        #Variáveis incluir
        self.date_inicio_incluir = self.data_agenda_inicio.ver_date_entry
        self.date_fim_incluir = self.data_agenda_fim.ver_date_entry
        self.nome_evento_incluir = StringVar()
        self.hora_evento_incluir = StringVar()
        self.subtag_incluir = StringVar()


        self.data_incluir_inicio = EntradaData(self.frame_taskday, 110, 30, self.date_inicio_incluir)

        self.data_incluir_fim = EntradaData(self.frame_taskday, 330, 30, self.date_fim_incluir)

        self.nome_incluir = ctk.CTkEntry(self.frame_taskday, width=100, font=ctk.CTkFont('Calibri'), fg_color='white',
                                         textvariable=self.nome_evento_incluir)
        self.nome_incluir.place(x=70, y=65)

        self.hora_incluir = ctk.CTkEntry(self.frame_taskday, width=100, font=ctk.CTkFont('Calibri'),
                                         textvariable=self.hora_evento_incluir, fg_color='white', )
        self.hora_incluir.place(x=230, y=65)

        self.tag_incluir = ctk.CTkComboBox(self.frame_taskday, width=90, font=ctk.CTkFont('Calibri'), fg_color='white', values=['Eventos', 'Aluguéis', 'Vendas', 'Pagamentos', 'Compras'])
        self.tag_incluir.place(x=370, y=65)

        self.tag_sub = ctk.CTkEntry(self.frame_taskday, width=120, font=ctk.CTkFont('Calibri'), fg_color='white',
                                           textvariable=self.subtag_incluir)
        self.tag_sub.place(x=70, y=100)


    def editar_evento_agenda(self):
        self.frame_form_task()
        # Variáveis editar 

        try:

            self.nome_evento_ed = StringVar(self.frame_taskday, f'{self.nome_ed}')
            self.hora_evento_ed = StringVar(self.frame_taskday, f'{self.hora_ed}')
            self.subtag_ed_2 = StringVar(self.frame_taskday, f'{self.subtag_ed}')
            print('1')
            self.data_ed_inicio = EntradaData(self.frame_taskday, 110, 30, self.dt_inicio_ed)

            self.data_ed_fim = EntradaData(self.frame_taskday, 330, 30, self.dt_fim_ed)
            print('2')
            self.nome_ed = ctk.CTkEntry(self.frame_taskday, width=100, font=ctk.CTkFont('Calibri'), fg_color='white',
                                        textvariable=self.nome_evento_ed)
            self.nome_ed.place(x=70, y=65)

            self.hora_ed = ctk.CTkEntry(self.frame_taskday, width=100, font=ctk.CTkFont('Calibri'),
                                        textvariable=self.hora_evento_ed, fg_color='white')
            self.hora_ed.place(x=230, y=65)

            self.tag_ed = ctk.CTkComboBox(self.frame_taskday, width=90, font=ctk.CTkFont('Calibri'), fg_color='white',
                                               values=['Eventos', 'Aluguéis', 'Vendas', 'Pagamentos', 'Compras'])
            self.tag_ed.set(f'{self.t_ed}')
            self.tag_ed.place(x=370, y=65)

            self.tag_sub_ed = ctk.CTkEntry(self.frame_taskday, width=120, font=ctk.CTkFont('Calibri'), fg_color='white',
                                           textvariable=self.subtag_ed_2)
            self.tag_sub_ed.place(x=70, y=100)
            print(3)

        except:
            messagebox.showerror(title='Agenda', message='Selecione um evento')

    def entradas_de_datas(self):
        rstate = self.rbotao._check_state
        print(rstate)
        if rstate == False:
            self.data_incluir_fim.config_date_entry(state='enable')
        else:
            self.date_fim = self.data_incluir_inicio.ver_date_entry
            print(self.date_fim)
            return self.date_fim, self.data_incluir_fim.desabilitar_dtentry()

    def alterar_evento(self):
        self.subtag1 = 'Null'
        if self.subtag_ed_2.get() != '':
            print('ok2')
            self.subtag1 = self.subtag_ed_2.get()
        print(self.subtag1)
        try:
            atualizar = (f'UPDATE {self.tabela} SET nome="{self.nome_evento_ed.get()}", hora="{self.hora_evento_ed.get()}", '
                         f'DataInicio="{self.data_ed_inicio.ver_date_entry
                         }", DataFinal="{self.data_ed_fim.ver_date_entry}", tagLocal="{self.tag_ed.get()}", '
                         f'subtag="{self.subtag1}" WHERE idTarefa = {self.id_ed};')
            print(atualizar)
            bd = BancoDeDados()
            bd.atualizar(atualizar)
            messagebox.showinfo(title='Agenda', message='Dados Atualizados com sucesso!')
            self.frame_taskday.place_forget()

        except:
            messagebox.showerror(title='Agenda', message='Preencha todos os campos!')

