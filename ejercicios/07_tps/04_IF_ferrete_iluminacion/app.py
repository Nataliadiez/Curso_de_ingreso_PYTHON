import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        PRECIO = 800
        DESCUENTO_50 = 50
        DESCUENTO_40 = 40
        DESCUENTO_30 = 30
        DESCUENTO_25 = 25
        DESCUENTO_20 = 20
        DESCUENTO_15 = 15
        DESCUENTO_10 = 10
        DESCUENTO_5 = 5
        porcentaje_descuento = 0
        total = 0

        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()

        cantidad_int = int(cantidad)
        argentina_luz = marca == "ArgentinaLuz"
        felipe_lamparas = marca == "FelipeLamparas"


        if(cantidad_int >= 6):
            porcentaje_descuento = DESCUENTO_50
        elif(cantidad_int == 5):
            if (argentina_luz):
                porcentaje_descuento = DESCUENTO_40
            else:
                porcentaje_descuento = DESCUENTO_30
        elif(cantidad_int == 4):
            if(argentina_luz or felipe_lamparas):
                porcentaje_descuento = DESCUENTO_25
            else:
                porcentaje_descuento = DESCUENTO_20
        elif (cantidad_int == 3):
            if(argentina_luz):
                porcentaje_descuento = DESCUENTO_15
            elif(felipe_lamparas):
                porcentaje_descuento = DESCUENTO_10
            else:
                porcentaje_descuento = DESCUENTO_5
        
        total = (PRECIO - (PRECIO *  porcentaje_descuento / 100)) * cantidad_int

        if (total >= 4000):
            porcentaje_descuento += DESCUENTO_5
            total = (PRECIO - (PRECIO *  (porcentaje_descuento) / 100)) * cantidad_int

        porcentaje_descuento_str = str(porcentaje_descuento)
        total_str = str(total)

        alert(title = "Final", message = "Cantidad de lámparas: " + cantidad + "\nMarca: " + marca + "\nDescuento: %" + porcentaje_descuento_str + "\nSaldo final: $" + total_str)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()