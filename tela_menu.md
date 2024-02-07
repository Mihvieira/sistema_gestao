# Painel de opções para o usuário

## Tecnologias utilizadas:
* Python 3.12
  * Customtkinter

### Importando bibliotecas

* Obs. PIL se refere a biblioteca pillow
  
***
import customtkinter as ctk

from tkinter import *

from PIL import Image  
***

### Criando a interface gráfica utilizando classe

*** 
class App(ctk.CTk):
***

***

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen_configuration()
               

    def screen_configuration(self):
        self.geometry('1366x768')
        self.title('Sistema de Gerenciamento de Informações')
        self.maxsize(1366, 768)
        self._set_appearance_mode('dark')
        ctk.set_default_color_theme('blue') 
***

****

if __name__ == '__main__':
    app = App()
    app.mainloop()
    
***

