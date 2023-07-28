

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
        
    def btn_validar_on_click(self): 
        #inicialización de contadores, flags y acumuladores
        bandera_jr_menor_edad = True
        edades_femeninas = 0
        edades_masculinas = 0
        edades_no_binarias = 0
        edad_postulante_menor = 0
        nombre_postulante_menor = None
        postulantes_femeninos = 0
        postulantes_masculinos = 0
        postulantes_no_binarios = 0       
        tecnologia_python = 0
        tecnologia_asp = 0
        tecnologia_js = 0
        postulantes_NB_Ssr = 0 # tal vez sería mejor nombrarla postulantes_NB_ASP_ssr_3045
        contador_postulantes = 0

        for _ in iter(int, 1):
            #Entrada y validación de campos vacíos y de información válida
            #Transformar todo a for porque sólo son 10 postulantes
            nombre = prompt(title="nombre", prompt="Ingrese su nombre:")
            if nombre == "" or nombre == None:
                alert(title="Error", message="Debe llenar el campo de nombre")
                continue

            edad = prompt(title="edad", prompt="Ingrese su edad (mayor de edad):")
            if edad == "" or edad == None:
                alert(title="Error", message="Debe llenar el campo de edad")
                continue
            else:
                edad = int(edad)
            if edad < 18:
                alert(title="Error", message="La edad ingresada debe ser mayor a 18 años.")
                continue

            genero = prompt(title="género", prompt="Ingrese su género (F-M-NB):")
            if genero == "" or genero == None:
                alert(title="Error", message="Debe llenar el campo de genero")
                continue
            elif genero != "F" and genero != "M" and genero != "NB":
                alert(title="Error", message="Ingrese un género válido (M - F - NB)")
                continue

            tecnologia = prompt(title="tecnología", prompt="Ingrese su tecnología (PYTHON - JS - ASP.NET):")
            if tecnologia == "" or tecnologia == None:
                alert(title="Error", message="Debe llenar el campo de tecnología")
                continue
            elif tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                alert(title="Error", message="Ingrese una tecnología válida (PYTHON - JS - ASP.NET)")
                continue

            puesto = prompt(title="puesto", prompt="Ingrese su puesto (Jr - Ssr - Sr):")
            if puesto == "" or puesto == None:
                alert(title="Error", message="Debe llenar el campo de puesto")
                continue
            elif puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                alert(title="Error", message="Ingrese una tecnología válida (PYTHON - JS - ASP.NET)")
                continue
            
            #validación de postulantes no binarios
            if genero == "NB" and edad >= 25 and edad <= 40 and puesto == "Ssr" and tecnologia == "JS" or tecnologia == "ASP.NET": #El or siempre debe ir al final
                postulantes_NB_Ssr += 1

            #validación postulante Jr de menor edad
            if bandera_jr_menor_edad and puesto == "Jr":
                edad_postulante_menor = edad
                nombre_postulante_menor = nombre
                bandera_jr_menor_edad = False
            elif edad < edad_postulante_menor:
                edad_postulante_menor = edad
                nombre_postulante_menor = nombre

            #total de edades femeninas y masculinas
            if genero == "F":
                edades_femeninas += edad
                postulantes_femeninos += 1
            elif genero == "M":
                edades_masculinas += edad
                postulantes_masculinos += 1
            else:
                edades_no_binarias += edad
                postulantes_no_binarios += 1

            #Tecnología más utilizada
            if tecnologia == "JS":
                tecnologia_js += 1
            elif tecnologia == "ASP.NET":
                tecnologia_asp += 1
            else:
                tecnologia_python += 1

            #Total de postulantes
            contador_postulantes += 1

            #print de testeo de datos ingresados
            print(nombre, edad, genero, tecnologia, puesto)
            
            #salida del for
            continuar = question(title="Continuar", message="¿Desea continuar cargando datos?")
            if continuar:
                continue
            else:
                break
        
        #promedio de edades
        if postulantes_masculinos != 0 and postulantes_femeninos != 0 and postulantes_no_binarios != 0:
            promedio_edad_masculina = edades_masculinas / postulantes_masculinos
            promedio_edad_femenina = edades_femeninas / postulantes_femeninos
            promedio_edad_no_binario = edades_no_binarias / postulantes_no_binarios
        
        #porcentaje de postulantes de cada género
        porcentaje_masculino = postulantes_masculinos / contador_postulantes * 100
        porcentaje_femenino = postulantes_femeninos / contador_postulantes * 100
        porcentaje_no_binario = postulantes_no_binarios / contador_postulantes * 100

        #Tecnología más utilizada
        if tecnologia_asp > tecnologia_js and tecnologia_asp > tecnologia_python:
            tecnologia_mas_postulada = "ASP.NET"
        elif tecnologia_python > tecnologia_asp and tecnologia_python > tecnologia_js:
            tecnologia_mas_postulada = "PYTHON"
        else:
            tecnologia_mas_postulada = "JS"
        

        mensaje1 = "Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS {0}".format(postulantes_NB_Ssr)
        mensaje2 = "\nNombre del postulante Jr con menor edad {0}".format(nombre_postulante_menor)
        mensaje3 = "\nPromedio de edad género femenino {0:.2f}".format(promedio_edad_femenina)
        mensaje4 = "\nPromedio de edad género masculino {0:.2f}".format(promedio_edad_masculina)
        mensaje5 = "\nPromedio de edad género no binario {0:.2f}".format(promedio_edad_no_binario)
        mensaje6 = "\nTecnologia con mas postulantes {0}".format(tecnologia_mas_postulada)
        mensaje7 = "\n Porcentaje de postulantes de género masculino {0:.2f}".format(porcentaje_masculino)
        mensaje8 = "\n Porcentaje de postulantes de género femenino {0:.2f}".format(porcentaje_femenino)
        mensaje9 = "\n Porcentaje de postulantes de género no binario{0:.2f}".format(porcentaje_no_binario)

        print(mensaje1+mensaje2+mensaje3+mensaje4+mensaje5+mensaje6+mensaje7+mensaje8+mensaje9)


        


            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
