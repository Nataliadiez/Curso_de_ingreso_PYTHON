import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Natalia 
apellido: Diez
---
Ejercicio: While_app_05
---
Enunciado:
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas) 
En caso no coincidir con ninguna de las letras, volverla a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        letra = prompt(title="Letra", prompt="Ingrese una letra (u/t/n): ")
        letra_mayus = letra.capitalize()
        utn = letra_mayus == "U" or letra_mayus == "T" or letra_mayus == "N"
        while(not utn):
            letra = prompt(title="Letra", prompt="Ingrese una letra válida (u/t/n): ")
            letra_mayus = letra.capitalize()
            utn = letra_mayus == "U" or letra_mayus == "T" or letra_mayus == "N"
        
        if utn:
            alert("Correcto", f"La letra ingresada es: {letra_mayus}")
        else:
            alert("Error", f"La letra ingresada es: {letra_mayus}")
        
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()