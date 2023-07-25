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

    """ Luego calcular:
        a. La suma acumulada de los negativos
        b. La suma acumulada de los positivos
        c. Cantidad de números positivos ingresados
        d. Cantidad de números negativos ingresados
        e. Cantidad de ceros
        f. El minimo de los negativos
        g. El maximo de los positivos
        h. El promedio de los negativos """
    
    def btn_comenzar_ingreso_on_click(self):
        listado_numeros = self.lista

        while True:
            numeros_ingresados = prompt(title="Números", prompt="Ingrese un número")
            bandera_coma = False
            primero_digito = True
            bandera_valido = True

            if numeros_ingresados is None or numeros_ingresados == '':
                continue
            else:
                for digito in numeros_ingresados:
                    if digito == '-' and primero_digito == True and len(numeros_ingresados) > 1:
                        primero_digito = False
                    elif digito == '.' and bandera_coma == False:
                        primero_digito = False
                        bandera_coma = True
                    elif digito.isdigit():
                        primero_digito = False
                        continue
                    else:
                        bandera_valido = False
                        print("No es un numero")
                        break
                if bandera_valido:
                    break

            numeros_ingresados = float(numeros_ingresados)
            print(numeros_ingresados)

            listado_numeros.append(numeros_ingresados)

            continuar = question(title="Continuar", message="¿Continuar ingresando números?")
            if continuar:
                continue
            else:
                break

        print(listado_numeros)

    def btn_mostrar_estadisticas_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
