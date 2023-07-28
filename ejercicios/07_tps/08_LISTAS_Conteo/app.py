import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Diez
Nombre: Natalia
---
TP 01 LISTAS
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

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
        listado_numeros = self.lista

        while True:
            numero_ingresado = prompt(title="Ingreso",prompt="Ingrese un número válido")
            bandera_coma = False
            primero_digito = True
            bandera_valido = True

            if numero_ingresado is None or numero_ingresado == '':
                continue
            else:
                for digito in numero_ingresado:
                    if  digito == '-' and primero_digito == True and len(numero_ingresado) > 1:
                        primero_digito = False
                    elif  digito == '.' and bandera_coma == False:
                        primero_digito = False
                        bandera_coma = True
                    elif digito.isdigit():
                        primero_digito = False
                        continue
                    else:
                        bandera_valido = False
                        print("Error: No es un número")
                        break
                if bandera_valido:
                    numero_ingresado = float(numero_ingresado)
                    break


    def btn_mostrar_estadisticas_on_click(self):
        listado_numeros = self.lista
        flag_primer_negativo = True
        flag_primer_positivo = True
        contador_negativos = 0
        contador_positivos = 0
        contador_ceros = 0
        suma_negativos = 0
        suma_positivos = 0
        print(listado_numeros)

        #For para separar negativos de positivos y colocarlos en listas
        for elemento in listado_numeros:
            if elemento % 10 == 0:
                contador_ceros += 1
            if elemento < 0:
                contador_negativos += 1
                suma_negativos += elemento
                if flag_primer_negativo:
                    minimo_negativo = elemento
                    flag_primer_negativo = False
                elif elemento < minimo_negativo:
                    minimo_negativo = elemento
            elif elemento >= 0:
                contador_positivos += 1
                suma_positivos += elemento
                if flag_primer_positivo:
                    maximo_positivo = elemento
                    flag_primer_positivo = False
                elif elemento > maximo_positivo:
                    maximo_positivo = elemento

        if contador_negativos != 0:
            promedio_negativos = suma_negativos / contador_negativos
            promedio_negativos = round(promedio_negativos, 2)
        else:
            promedio_negativos = 0

        mensaje_salida = f"La cantidad de negativos es: {contador_negativos}"
        mensaje_salida += f"\nLa suma de los negativos es: {suma_negativos}"
        mensaje_salida += f"\nLa cantidad de positivos es: {contador_positivos}"
        mensaje_salida += f"\nLa suma de los positivos es: {suma_positivos}"
        mensaje_salida += f"\nLa cantidad de ceros es de: {contador_ceros}"
        mensaje_salida += f"\nEl número mínimo negativo es: {minimo_negativo}"
        mensaje_salida += f"\nEl máximo número positivo es: {maximo_positivo}"
        mensaje_salida += f"\nEl promedio de los números negativos es: {promedio_negativos}"
        alert(title="Resultados", message=mensaje_salida)

        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
