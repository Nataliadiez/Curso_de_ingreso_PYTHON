

"""
Apellido: Diez
Nombre: Natalia

TP FOR
"""
'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
        """ a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
            cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
            b. Nombre del postulante Jr con menor edad.
            c. Promedio de edades por género.
            d. Tecnologia con mas postulantes (solo hay una).
            e. Porcentaje de postulantes de cada genero.
        """

    def btn_validar_on_click(self):
        POSTULANTES = 10
        contador_postulantes_NB_ASP_o_JS_25_40_Ssr = 0
        nombre_postulante_jr_menor_edad = None
        postulante_jr_menor_edad = 0
        bandera_primer_jr = True
        promedio_edad_F = 0
        promedio_edad_M = 0
        promedio_edad_NB = 0
        contador_tecnologia_JS = 0
        contador_tecnologia_PYTHON = 0
        contador_tecnologia_ASP = 0
        contador_postulantes_F = 0
        contador_postulantes_M = 0
        contador_postulantes_NB = 0
        acumulador_edad_F = 0
        acumulador_edad_M = 0
        acumulador_edad_NB = 0
        
        for i in range(0, POSTULANTES, 1):
            nombre = prompt(title="nombre", prompt="Ingrese su nombre:")
            while nombre is None or nombre == "" or nombre.isdigit():
                nombre = prompt(title="error", prompt="Reingrese su nombre:")

            edad = prompt(title="edad", prompt="Ingrese su edad (mayor a 18):")
            while edad == None or not edad.isdigit() or int(edad) < 18:
                edad = prompt(title="error", prompt="Reingrese su edad (mayor a 18):")
            edad = int(edad)

            genero = prompt(title="genero", prompt="Ingrese su genero (F-M-NB):")
            while genero == None or (genero != "F" and genero != "M" and genero != "NB"):
                genero = prompt(title="genero", prompt="Ingrese un género válido (F-M-NB):")

            tecnologia = prompt(title="tecnologia", prompt="Ingrese su tecnologia (PYTHON - JS - ASP.NET):")
            while tecnologia == None or (tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET"):
                tecnologia = prompt(title="tecnologia", prompt="Ingrese una tecnología válida (PYTHON - JS - ASP.NET):")

            puesto = prompt(title="puesto", prompt="Ingrese su puesto (Jr - Ssr - Sr):")
            while puesto == None or (puesto != "Jr" and puesto != "Ssr" and puesto != "Sr"):
                puesto = prompt(title="puesto", prompt="Reingrese su puesto (Jr - Ssr - Sr):")

            match(genero):
                case "F":
                    contador_postulantes_F += 1
                    acumulador_edad_F += edad
                    pass
                case "M":
                    contador_postulantes_M += 1
                    acumulador_edad_M += edad
                    pass
                case "NB":
                    contador_postulantes_NB += 1
                    acumulador_edad_NB += edad
                    if (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad >= 25 and edad <= 40) and puesto == "Ssr":
                        contador_postulantes_NB_ASP_o_JS_25_40_Ssr += 1
            
            if puesto == "Jr" and (bandera_primer_jr or edad < postulante_jr_menor_edad):  
                nombre_postulante_jr_menor_edad = nombre
                postulante_jr_menor_edad = edad
                bandera_primer_jr = False

            if tecnologia == "ASP.NET":
                contador_tecnologia_PYTHON += 1
            elif tecnologia == "JS":
                contador_tecnologia_JS += 1
            else:
                contador_tecnologia_ASP += 1
        
        if contador_postulantes_F != 0:
            promedio_edad_F = (acumulador_edad_F / contador_postulantes_F)
        if contador_postulantes_M != 0:
            promedio_edad_M = acumulador_edad_M / contador_postulantes_M
        if contador_postulantes_NB != 0:
            promedio_edad_NB = acumulador_edad_NB / contador_postulantes_NB
        
        if contador_tecnologia_ASP > contador_tecnologia_JS and contador_tecnologia_ASP > contador_tecnologia_PYTHON:
            tecnologia_mas_postulada = "ASP.NET"
        elif contador_tecnologia_PYTHON > contador_tecnologia_JS:
            tecnologia_mas_postulada = "PYTHON"
        else:
            tecnologia_mas_postulada = "JS"

        porcentaje_postulantes_F = contador_postulantes_F * 100 / POSTULANTES
        porcentaje_postulantes_M = contador_postulantes_M * 100 / POSTULANTES
        porcentaje_postulantes_NB = contador_postulantes_NB * 100 / POSTULANTES

        """ a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
            cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
            b. Nombre del postulante Jr con menor edad.
            c. Promedio de edades por género.
            d. Tecnologia con mas postulantes (solo hay una).
            e. Porcentaje de postulantes de cada genero. 
        """
        mensaje_salida= f"Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {contador_postulantes_NB_ASP_o_JS_25_40_Ssr}"
        mensaje_salida += f"\nNombre del postulante Jr con menor edad {nombre_postulante_jr_menor_edad}"
        mensaje_salida += f"\nPromedio de edades por género:\n Promedio de edades F: {promedio_edad_F:.2f} \nPromedio de edades M: {promedio_edad_M:.2f}\nPromedio de edades NB: {promedio_edad_NB:.2f}"
        mensaje_salida += f"\nTecnologia con mas postulantes_ {tecnologia_mas_postulada}"
        mensaje_salida += f"\nPorcentaje de postulantes de cada genero:\nPorcentaje F: {porcentaje_postulantes_F}\nPorcentaje M: {porcentaje_postulantes_M}\nPorcentaje NB: {porcentaje_postulantes_NB}"

        print(message=mensaje_salida)
        


            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
