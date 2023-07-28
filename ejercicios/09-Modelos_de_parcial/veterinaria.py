import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Diez
Nombre: Natalia
---
Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario quiera 
(se limita a 1 perrito por ingreso), se les pide: 
1-nombre, 
2-precio de la consulta (validar entre 500 y 2500$) 
3-raza: (validar entre caniche, ovejero, siberiano), 
4-edad (validar 0 a 15) y 
5-peso (entre 25 y 40 kilos) 

determinar:
el nombre y el peso del perro con más peso
el porcentaje de razas
la facturación en bruto de la veterinaria
si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos
si el mismo perro tiene múltiples ingresos se le hacen estos descuentos:
2 ingresos 15% 
3 a 5 ingresos 35%

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.lista = []

    
    def btn_comenzar_ingreso_on_click(self):
        pass

    def btn_mostrar_estadisticas_on_click(self):
        pass

        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
