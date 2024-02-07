# Tela inicial com as opções disponíveis para o usuário

 ## Imagens
 * Os ícones utilizados foram encontrados nos sites: [Google Fonts](https://fonts.google.com/icons) e [icons](https://icons8.com.br/icons)
 * O modelo de logo foi encontrado no aplicativo [Canvas](https://www.canva.com/pt_br/)

### Importando bibliotecas

* Obs. PIL se refere a biblioteca pillow
  
***
import customtkinter as ctk

from tkinter import *

from PIL import Image  
***

### Criando a interface gráfica utilizando classe

```
class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen_configuration()
               

    def screen_configuration(self):
        self.geometry('1366x768')
        self.title('Sistema de Gerenciamento de Informações')
        self.resizable(False, False)
        self._set_appearance_mode('dark')
        ctk.set_default_color_theme('blue') 

if __name__ == '__main__':
    app = App()
    app.mainloop()
    
```
 Com isso teremos a seguinte tela:
![tela_inicio](https://github.com/Mihvieira/sistema_gestao/assets/136247614/61207ae3-5414-42c9-8c66-0cd5b43b0028)

Agora passaremos a criar a tela de início

```
    def menu(self):  # definindo nova janela
        
        self.username_loguin = 'Admin'

        # criando frame menu
        self.frame_menu = ctk.CTkFrame(self, width=50, height=768, fg_color='#0d1316', bg_color='black')
        self.frame_menu.grid(row=0, column=0, rowspan=1, pady=0, padx=0, sticky="nsew")

        self.img_logo = ctk.CTkImage(Image.open('logo1.png'), size=(50, 50))
        self.img_home = ctk.CTkImage(Image.open('home.png'))
        self.img_graph = ctk.CTkImage(Image.open('monitoring.png'))
        self.img_acount = ctk.CTkImage(Image.open('account_box.png'))
        self.img_group = ctk.CTkImage(Image.open('group_add.png'))

        self.lb_logo = ctk.CTkLabel(self.frame_menu, image=self.img_logo, text='')
        self.lb_logo.place(x=0, y=10)

        self.btn_home = ctk.CTkButton(self.frame_menu, image=self.img_home, text='', width=30, fg_color='white',
                                      command=self.menu)
        self.btn_home.place(x=8, y=450)
        self.btn_graph = ctk.CTkButton(self.frame_menu, image=self.img_graph, text='', width=30, fg_color='white')
        self.btn_graph.place(x=8, y=500)
        self.btn_acount = ctk.CTkButton(self.frame_menu, image=self.img_acount, text='', width=30, fg_color='white')
        self.btn_acount.place(x=8, y=550)
        self.btn_group = ctk.CTkButton(self.frame_menu, image=self.img_group, text='', width=30, fg_color='white')
        self.btn_group.place(x=8, y=600)

        # criando frame cima
        self.frame_título = ctk.CTkFrame(self, width=1360, height=50, fg_color='#0d1316', bg_color='black')
        self.frame_título.place(x=50, y=0)
        self.lb_nome = ctk.CTkLabel(self.frame_título, text=f'Olá {self.username_loguin}.', text_color='white',
                                    font=('Calibri bold', 20))
        self.lb_nome.place(x=50, y=20)
        self.entry_pesquisa = ctk.CTkEntry(self.frame_título, width=300, placeholder_text='Pesquise aqui..',
                                           border_color='#f56e8a')
        self.entry_pesquisa.place(x=899, y=20)
        self.img_pesquisa = ctk.CTkImage(Image.open('search.png'))
        self.btn_pesquisa = ctk.CTkButton(self.frame_título, image=self.img_pesquisa, text='', width=60,
                                          fg_color='white')
        self.btn_pesquisa.place(x=1200, y=20)

        # criando frame meio
        self.frame_options = ctk.CTkFrame(self, width=1360, height=718, fg_color='white')
        self.frame_options.place(x=50, y=55)

        # imagem botão subframes
        self.img_add = ctk.CTkImage(Image.open('icons8-adicionar-30.png'))
        self.btn_add1 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Cadastro', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT, command=self.abrir_cadastro)
        self.btn_add1.place(x=100, y=90)

        self.btn_add2 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Agenda', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT)
        self.btn_add2.place(x=400, y=90)

        self.btn_add3 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Fluxos\n de Trabalho', width=230,
                                      height=200, fg_color='pink', bg_color='pink', text_color='black',
                                      font=('Verdana bold', 22), compound=RIGHT)
        self.btn_add3.place(x=700, y=90)

        self.btn_add4 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Produtos', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT)
        self.btn_add4.place(x=1000, y=90)

        self.btn_add5 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Clientes', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT)
        self.btn_add5.place(x=100, y=390)

        self.btn_add6 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Recursos\n Humanos', width=230,
                                      height=200, fg_color='pink', bg_color='pink', text_color='black',
                                      font=('Verdana bold', 22), compound=RIGHT)
        self.btn_add6.place(x=400, y=390)

        self.btn_add7 = ctk.CTkButton(self.frame_options, image=self.img_add, text='Pagamentos', width=230, height=200,
                                      fg_color='pink', bg_color='pink', text_color='black', font=('Verdana bold', 22),
                                      compound=RIGHT)
        self.btn_add7.place(x=700, y=390)
```

Após criada a função é preciso inseri-la no início da classe:

```
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen_configuration()
        self.menu()
```

Tudo pronto! A tela final ficaria dessa forma:

![image](https://github.com/Mihvieira/sistema_gestao/assets/136247614/f7e6c7cb-acfb-4075-9177-b968fa2efa44)


### Outras informações

Os botões possuem como padrão a cor azul, no momento em que o mouse está sobre ele, porém é possível alterar a cor acrescentando o seguinte parâmetro:
```
hover_color='green'
```
ou, além do nome da cor é possível adicionar o código da cor
```
hover_color= '#0d1316'
```




 


