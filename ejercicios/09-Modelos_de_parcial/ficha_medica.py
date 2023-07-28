import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Diez
Nombre: Natalia
---
Ejercicio de parcial 1:

Se pide cargar la ficha médica para 11 jugadores de fútbol.
Se solicita Nombre, Edad, Peso(ej: 60.5kg) y Altura(ej: 1.65mt).
A) Nombre del jugador más joven.
B) El peso del jugador más alto.
C) Promedio de altura del equipo.
D) Promedio de peso del equipo.
E) Cantidad de jugadores que superen el promedio de altura y de peso del equipo.
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
    Se pide cargar la ficha médica para 11 jugadores de fútbol.
    Se solicita Nombre, Edad, Peso(ej: 60.5kg) y Altura(ej: 1.65mt).
    A) Nombre del jugador más joven. LISTO
    B) El peso del jugador más alto. LISTO
    C) Promedio de altura del equipo. LISTO
    D) Promedio de peso del equipo. LISTO
    E) Cantidad de jugadores que superen el promedio de altura y de peso del equipo. 
    """
    
    def btn_comenzar_ingreso_on_click(self):
        JUGADORES = 3
        lista_peso_jugadores = []
        lista_altura_jugadores = []
        nombre_jugador_mas_joven = 0
        edad_jugador_mas_joven = 0
        altura_jugador_mas_alto = 0
        peso_jugador_mas_alto = 0
        acumulador_altura = 0
        acumulador_peso = 0
        contador_jugadores_mas_altura = 0
        contador_jugadores_mas_peso = 0

        for i in range(0, JUGADORES, 1):
            nombre = prompt(title="nombre", prompt="Ingrese su nombre")
            while nombre == "" or nombre == None or nombre.isdigit():
                nombre = prompt(title="nombre", prompt="Reingrese su nombre")
            
            edad = prompt(title="edad", prompt="Ingrese su edad")
            while edad == "" or edad == None or not edad.isdigit():
                edad = prompt(title="edad", prompt="Reingrese su edad")
            edad = int(edad)
            
            peso = prompt(title="peso", prompt="Ingrese su peso (en kg)")
            while peso == "" or peso == None:
                peso = prompt(title="peso", prompt="Reingrese su peso (en kg)")
            peso = float(peso)

            altura = prompt(title="altura", prompt="Ingrese su altura (en metros)")
            while altura == "" or altura == None:
                altura = prompt(title="altura", prompt="Reingrese su altura (en metros)")
            altura = float(altura)

            lista_peso_jugadores.append(peso)

            print(nombre, edad, peso, altura)
            acumulador_altura += altura
            acumulador_peso += peso

            if i == 0 or edad < edad_jugador_mas_joven:
                nombre_jugador_mas_joven = nombre
                edad_jugador_mas_joven = edad
            if i == 0 or altura > altura_jugador_mas_alto:
                altura_jugador_mas_alto = altura
                peso_jugador_mas_alto = peso

        promedio_altura_equipo = acumulador_altura / JUGADORES
        promedio_peso_equipo = acumulador_peso / JUGADORES

        """ for i in range(0, JUGADORES, 1):
            for elemento in lista_altura_jugadores:
        """
        
        

        

        mensaje_salida = f"Nombre del jugador más joven: {nombre_jugador_mas_joven}"
        mensaje_salida += f"\nPeso del jugador más alto: {peso_jugador_mas_alto}"
        mensaje_salida += f"\nPromedio de altura del equipo: {promedio_altura_equipo:.2f}"
        mensaje_salida += f"\nPromedio de peso del equipo: {promedio_peso_equipo:.2f}"
        mensaje_salida += f"\nCantidad de jugadores que superen el promedio de altura y de peso del equipo {contador_jugadores_mas_altura_mas_peso}"
        alert(title="Resultados", message=mensaje_salida)


        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
