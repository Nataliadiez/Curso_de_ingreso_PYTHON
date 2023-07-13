import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter
import threading
import time

'''
Enunciado:
Al presionar el botón INICIAR se debe mostrar un mensaje de bienvenida "Bienvenidos a la UTN FRA" cada 3 segundos. 

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Iniciar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
        def saludo ():
            alert(title = "Saludo", message = "Bienvenidos a la UTN FRA")
        
        timer = threading.Timer(3, saludo)
        timer.start()
        
        
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()