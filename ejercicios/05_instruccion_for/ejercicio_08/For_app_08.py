import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Apellido: Diez
Nombre: Natalia
---
Ejercicio 08 FOR
"""
'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt(title="numero", prompt="Ingrese un número para saber si es primo o no.")
        numero = int(numero)
        divisores = 0

        for i in range(1, numero, 1):
            if numero % i == 0:
                divisores += 1
            

        if divisores > 2:
            print("No es un número primo")
        else:
            print("Es un número primo")

            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()