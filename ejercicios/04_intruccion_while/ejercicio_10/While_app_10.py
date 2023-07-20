import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Natalia 
apellido: Diez
---
Ejercicio: While_app_010
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos YA TA
    La suma acumulada de los positivos YA TA
    Cantidad de números positivos ingresados YA TA
    Cantidad de números negativos ingresados YA TA
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos YA TA

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0 
        contador_negativos = 0
        ceros = 0
        diferencia_positivos_negativos = 0
        
        while True:
            numeros = prompt(title="Ingreso", prompt="Ingrese números (cancelar para salir):")
            if numeros == None or numeros == "":
                break
            numeros = int(numeros)
            if numeros >= 0:
                suma_positivos += numeros
                contador_positivos += 1
            elif numeros < 0:
                suma_negativos += numeros
                contador_negativos += 1

            if numeros % 10 == 0:
                ceros += 1

        if contador_positivos > contador_negativos:
            diferencia_positivos_negativos = contador_positivos - contador_negativos
        elif contador_positivos < contador_negativos:
            diferencia_positivos_negativos = contador_negativos - contador_positivos

        title = "Resultado"
        message = "Total números positivos: {0}\nSuma números positivos: {1}\nTotal números negativos: {2}\nSuma números negativos: {3}\nDiferencia cantidad de números positivos y negativos: {4}\nTotal números con ceros: {5}".format(contador_positivos, suma_positivos, contador_negativos, suma_negativos, diferencia_positivos_negativos, ceros)
        alert(title, message)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
