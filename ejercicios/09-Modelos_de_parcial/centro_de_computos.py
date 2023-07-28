import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Diez
Nombre: Natalia
---
Ejercicio de parcial 2: 

Centro de cómputos

Ingresar el nombre de los 5 candidatos a presidente de Berlinberlin,  la edad de cada uno y la cantidad de votos que sacó en las elecciones.
Informar: 
a) el candidato con más votos
b) el candidato con menos votos
c) el promedio de edades de los candidatos
d) total de votos emitidos

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
    a) el candidato con más votos LISTO
    b) el candidato con menos votos LISTO
    c) el promedio de edades de los candidatos
    d) total de votos emitidos 
    """
    def btn_comenzar_ingreso_on_click(self):
        CANDIDATOS = 5
        nombre_candidato_mas_votos = None
        candidato_mas_votos = 0
        nombre_candidato_menos_votos = None
        candidato_menos_votos = 0
        total_votos_emitidos = 0
        acumulador_edades = 0

        for i in range(0, CANDIDATOS, 1):
            nombre = prompt(title="nombre", prompt="Ingrese su nombre")
            while nombre == None or nombre == "" or nombre.isdigit():
                nombre = prompt(title="nombre", prompt="Reigrese su nombre")

            edad = prompt(title="edad", prompt="Ingrese su edad")
            while edad == None or edad == "" or not edad.isdigit():
                edad = prompt(title="edad", prompt="Reigrese su edad")
            edad = int(edad)

            cantidad_votos = prompt(title="cantidad_votos", prompt="Ingrese su cantidad_votos")
            while cantidad_votos == None or cantidad_votos == "" or not cantidad_votos.isdigit():
                cantidad_votos = prompt(title="cantidad_votos", prompt="Reigrese su cantidad_votos")
            cantidad_votos = int(cantidad_votos)
            print(nombre, edad, cantidad_votos)
            
            acumulador_edades += edad
            total_votos_emitidos += cantidad_votos

            if i == 0 or cantidad_votos > candidato_mas_votos:
                nombre_candidato_mas_votos = nombre
                candidato_mas_votos = cantidad_votos

            if i == 0 or cantidad_votos < candidato_menos_votos:
                nombre_candidato_menos_votos = nombre
                candidato_menos_votos = cantidad_votos

        promedio_edades = acumulador_edades / CANDIDATOS

        mensaje_salida = f"Candidato con más votos: {nombre_candidato_mas_votos}"
        mensaje_salida += f"\nCandidato con menos votos: {nombre_candidato_menos_votos}"
        mensaje_salida += f"\nPromedio de edades de los candidatos: {promedio_edades:.2f}"
        mensaje_salida += f"\nTotal de votos emitidos: {total_votos_emitidos}"
        alert(title="Resultados", message=mensaje_salida)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
