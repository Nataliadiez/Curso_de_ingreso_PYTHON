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

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.lista = []

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
        listado_movimientos = self.lista

        while True:
            criptomoneda = prompt(title="moneda", prompt="Ingrese el nombre de la criptomoneda (BTC o ETH)")
            while (criptomoneda is None or criptomoneda == "" or criptomoneda.isdigit()) or (criptomoneda != "BTC" and criptomoneda != "ETH"):
                criptomoneda = prompt(title="moneda", prompt="Elija una criptomoneda vàlida (BTC o ETH)")
            listado_movimientos.append(criptomoneda)

            cantidad_minada = prompt(title="moneda", prompt="Ingrese la cantidad minada")
            while (cantidad_minada is None or not cantidad_minada.isdigit()) or int(cantidad_minada) < 1:
                cantidad_minada = prompt(title="moneda", prompt="Ingrese una cantidad minada válida, mayor a 0")
            cantidad_minada = int(cantidad_minada)
            listado_movimientos.append(cantidad_minada)
            
            cotizacion = prompt(title="moneda", prompt="Ingrese la cotización diaria en USD")
            while (cotizacion is None or not cotizacion.isdigit()) or float(cotizacion) < 0:
                cotizacion = prompt(title="moneda", prompt="Ingrese una cotización válida en USD")
            cotizacion = float(cotizacion)
            listado_movimientos.append(cotizacion)


            continuar = question(title="Continuar", message="¿Desea continuar cargando movimientos?")
            if continuar:
                continue
            else:
                break


    def btn_mostrar_estadisticas_on_click(self):
        listado_movimientos = self.lista
        nombre_criptomoneda_mas_minada = None
        nombre_criptomoneda_mayor_cotizacion = None
        acumulador_minado_BTC = 0
        acumulador_minado_ETH = 0
        acumulador_cotizacion_BTC = 0
        acumulador_cotizacion_ETH = 0
        
        """
        A) Nombre y cantidad de la criptomoneda más minada. Listo
        B) Nombre de la criptomoneda que mayor cotización tuvo. Listo
        C) Cantidad total de ingreso bruto en USD de cada criptomoneda. Listo
        D) Sabiendo que el coste de electricidad para: Listo
            BTC es de un 7% y para ETH es un 4% calcular el ingreso total neto en USD
        """
        for i in range(0, len(listado_movimientos), 3):
            criptomoneda = listado_movimientos[i]
            cantidad_minada = listado_movimientos[i+1]
            cotizacion = listado_movimientos[i+2]
            print(criptomoneda, cantidad_minada, cotizacion)
            match criptomoneda:
                case "BTC":
                    acumulador_minado_BTC += cantidad_minada
                    acumulador_cotizacion_BTC += cotizacion
                case "ETH":
                    acumulador_minado_ETH += cantidad_minada
                    acumulador_cotizacion_ETH += cotizacion
            
        if acumulador_minado_ETH > acumulador_minado_BTC:
            nombre_criptomoneda_mas_minada = "ETH"
            total_minado = acumulador_minado_ETH
        else:
            nombre_criptomoneda_mas_minada = "BTC"
            total_minado = acumulador_minado_BTC

        if acumulador_cotizacion_ETH > acumulador_cotizacion_BTC:
            nombre_criptomoneda_mayor_cotizacion = "ETH"
        else:
            nombre_criptomoneda_mayor_cotizacion = "BTC"
        
        total_ingreso_bruto_USD_BTC = acumulador_minado_BTC * acumulador_cotizacion_BTC
        total_ingreso_bruto_USD_ETH = acumulador_minado_ETH * acumulador_cotizacion_ETH
        total_ingreso_neto_BTC = total_ingreso_bruto_USD_BTC - (total_ingreso_bruto_USD_BTC * 7 / 100)
        total_ingreso_neto_ETH = total_ingreso_bruto_USD_ETH - (total_ingreso_bruto_USD_ETH * 4 / 100)
            
        mensaje_salida = f"Nombre y cantidad de la criptomoneda más minada {nombre_criptomoneda_mas_minada} y la cantidad minada es: {total_minado}"
        mensaje_salida += f"\nNombre de la criptomoneda que mayor cotización tuvo {nombre_criptomoneda_mayor_cotizacion}"
        mensaje_salida += f"\nCantidad total de ingreso bruto en USD de cada criptomoneda\nIngreso bruto BTC: {total_ingreso_bruto_USD_BTC}\nIngreso bruto ETH: {total_ingreso_bruto_USD_ETH}"
        mensaje_salida += f"\nIngreso neto\nIngreso neto BTC: {total_ingreso_neto_BTC}\nIngreso neto ETH {total_ingreso_neto_ETH}"
        print(mensaje_salida) 

        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
