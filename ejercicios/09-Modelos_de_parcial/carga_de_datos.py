import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Diez
Nombre: Natalia
---
Ejercicio de parcial 3: 

En una carga indefinida de datos (hasta que el usuario quiera) se desea llevar a cabo el registro diario de una granja de minería en Bitcoin y Ethereum.
Se requieren los siguientes datos:
Nombre de la criptomoneda (VALIDAR EL INGRESO solo de BTC o ETH).
Cantidad de BTC o ETH minado ese día - Número positivo.
Cotización diaria en USD - Número positivo inclusive 0.
INFORMAR
A) Nombre y cantidad de la criptomoneda más minada.
B) Nombre de la criptomoneda que mayor cotización tuvo.
C) Cantidad total de ingreso bruto en USD de cada criptomoneda.
D) Sabiendo que el coste de electricidad para:

BTC es de un 7% y para ETH es un 4% calcular el ingreso total neto en USD.

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    """ 
    Nombre de la criptomoneda (VALIDAR EL INGRESO solo de BTC o ETH).
    Cantidad de BTC o ETH minado ese día - Número positivo.
    Cotización diaria en USD - Número positivo inclusive 0.
    INFORMAR
    A) Nombre y cantidad de la criptomoneda más minada. Listo
    B) Nombre de la criptomoneda que mayor cotización tuvo. Listo
    C) Cantidad total de ingreso bruto en USD de cada criptomoneda. Listo
    D) Sabiendo que el coste de electricidad para:

    BTC es de un 7% y para ETH es un 4% calcular el ingreso total neto en USD. 
    """
    
    def btn_comenzar_ingreso_on_click(self):
        nombre_criptomoneda = prompt(title="moneda", prompt="Ingrese el nombre de la moneda")
        while nombre_criptomoneda == "" or nombre_criptomoneda == None:
            nombre_criptomoneda = prompt(title="moneda", prompt="Ingrese el nombre de la moneda")



        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
