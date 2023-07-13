import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	Para el departamento de Pinturas:
	A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados con un mensaje concatenado 
        (0 °F − 32) × 5/9 = -17,78 °C

    B.	Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        (0 °C × 9/5) + 32 = 32 °F

    
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Temperatura °C")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_temperatura_c = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_c.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Temperatura °F")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_temperatura_f = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_f.grid(row=1, column=1)

        self.btn_convertir_c_f = customtkinter.CTkButton(master=self, text="Convertir °C a °F", command=self.btn_convertir_c_f_on_click)
        self.btn_convertir_c_f.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_convertir_f_c = customtkinter.CTkButton(master=self, text="Convertir °F a °C", command=self.btn_convertir_f_c_on_click)
        self.btn_convertir_f_c.grid(row=4, pady=10, columnspan=2, sticky="nsew")
    
    def btn_convertir_c_f_on_click(self):

        temperatura_centigrados = self.txt_temperatura_c.get()
        temperatura_centigrados_float = float(temperatura_centigrados)
        centigrado_a_farenheit = (temperatura_centigrados_float * (9/5)) + 32
        

        alert(title = "Resultado", message = "El resultado de "+ temperatura_centigrados + "C° a F° es: " + "{:.2f}".format(centigrado_a_farenheit))


    def btn_convertir_f_c_on_click(self):
        temperatura_farenheit = self.txt_temperatura_f.get()
        temperatura_farenheit_float = float(temperatura_farenheit)
        farenheit_a_centigrados = (temperatura_farenheit_float - 32) * 5/9

        alert(title = "Resultado", message = "El resultado de " + temperatura_farenheit + "F° a C° es: " + "{:.2f}".format(farenheit_a_centigrados))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()