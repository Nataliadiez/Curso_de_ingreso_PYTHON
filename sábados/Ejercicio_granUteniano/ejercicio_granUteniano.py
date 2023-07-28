import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

""" 
Nombre: Natalia
Apellido: Diez 
---
El gran Uteniano

"""

""" 
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes 
y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y 
Marina no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:
Nombre del votante
Edad del votante (debe ser mayor a 13)
Género del votante (Masculino, Femenino, Otro)
El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:
El promedio de edad de las votantes de género Femenino 
Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
Nombre del votante más joven qué votó a Gianni.
Nombre de cada participante y porcentaje de los votos qué recibió.
El nombre del participante que debe dejar la casa (El que tiene más votos)


"""



class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="Gran Uteniano", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Votar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #Inicialización de variables
        flag_mas_joven = True
        votantes_femenino = 0
        votantes_masculino = 0
        edades_femenino = 0
        edad_mas_joven = 0
        votos_gianni = 0
        votos_giovanni = 0
        votos_facundo = 0

#MODIFICAR ESTE EJERCICIO PARA PODER PONER UN WHILE POR CADA VALIDACIÓN
        while True:
            nombre_votante = prompt(title="nombre", prompt="Ingrese su nombre:")
            if nombre_votante == "" or nombre_votante == None:
                alert(title="Error", message="Debe rellenar el campo nombre")
                continue

            edad_votante = prompt(title="edad", prompt="Ingrese su edad (mayor a 13 años):")
            if edad_votante == "" or edad_votante == None:
                alert(title="Error", message="Debe rellenar el campo edad")
                continue
            else:
                edad_votante = int(edad_votante)
                
            if edad_votante < 14:
                alert(title="Error", message="Debe ser mayor a 13 años.")
                continue

            genero_votante = prompt(title="género", prompt="Ingrese su género (Masculino, Femenino, Otro):")
            if genero_votante == "" or genero_votante == None:
                alert(title="Error", message="Debe rellenar el campo género") 
                continue
            elif genero_votante != "Masculino" and genero_votante != "Femenino" and genero_votante != "Otro":
                alert(title="Error", message="Debe elegir un género entre Femenino, Masculino u Otro.")
                continue

            participante_votado = prompt(title="voto", prompt="Ingrese el participante en placa que desea votar\nGiovanni, Gianni, Facundo:")
            if participante_votado == "" or participante_votado == None:
                alert(title="Error", message="Debe rellenar el campo participante")
                continue
            elif participante_votado != "Giovanni" and participante_votado != "Gianni" and participante_votado != "Facundo":
                alert(title="Error", message="Debe elegir un participante en placa")
                continue
            

            #participante masculino entre 25 y 40 años que vote a Giovanni o Facundo
            if genero_votante == "Femenino":
                edades_femenino += edad_votante
                votantes_femenino += 1
            elif genero_votante == "Masculino" and edad_votante >= 25 and edad_votante <= 40 and participante_votado == "Giovanni" or participante_votado == "Facundo":
                votantes_masculino += 1

            #Participante más joven que vota a Gianni
            if flag_mas_joven and participante_votado == "Gianni":
                edad_mas_joven = edad_votante
                nombre_mas_joven = nombre_votante
                flag_mas_joven = False
            elif edad_votante < edad_mas_joven and participante_votado == "Gianni":
                edad_mas_joven = edad_votante
                nombre_mas_joven = nombre_votante
            else:
                nombre_mas_joven = ""
                
            #Votos de cada participante
            if participante_votado == "Gianni":
                votos_gianni += 1
            elif participante_votado == "Giovanni":
                votos_giovanni += 1
            else:
                votos_facundo += 1

            print(participante_votado)

            #Salida o continuación del bucle
            continuar = question(title="Continuar", message="¿Desea continuar cargando votos?")
            if continuar:
                continue
            else:
                break
        
        
        #promedio votantes femeninos
        if votantes_femenino != 0:
            promedio_edades_femenino = edades_femenino / votantes_femenino
        else:
            promedio_edades_femenino = 0

        #porcentaje votos a cada participante
        total_votos = votos_gianni + votos_facundo + votos_giovanni
        porcentaje_gianni = votos_gianni / total_votos * 100
        porcentaje_giovanni = votos_giovanni / total_votos * 100
        porcentaje_facundo = votos_facundo / total_votos * 100

        #quién abandona la casa
        if votos_facundo > votos_gianni and votos_facundo > votos_giovanni:
            abandona_la_casa = "Facundo"
        elif votos_gianni > votos_facundo and votos_gianni > votos_giovanni:
            abandona_la_casa = "Gianni"
        elif votos_giovanni > votos_gianni and votos_giovanni > votos_facundo:
            abandona_la_casa = "Giovanni"
        else: 
            abandona_la_casa = "Nadie abandona la casa, es empate"

        #Salida por alert
        mensaje1 = "Cantidad de votantes masculinos entre 25 y 40 años que votaron a Giovanni y Facundo: {0}".format(votantes_masculino)
        mensaje2 = "\nPromedio de la edad de las mujeres votantes: {0:.2f}".format(promedio_edades_femenino)
        mensaje3 = "\nEl votante más joven que votó a Gianni es: {0}".format(nombre_mas_joven)
        mensaje4 = "\nPorcentaje de votos: Gianni {0:.2f}% Giovanni {1:.2f}% Facundo {2:.2f}%".format(porcentaje_gianni, porcentaje_giovanni, porcentaje_facundo)
        mensaje5 = "\nEl participante que debe abandonar la casa es: {0}".format(abandona_la_casa)
        alert(title="Resultados", message=mensaje1+mensaje2+mensaje3+mensaje4+mensaje5)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
