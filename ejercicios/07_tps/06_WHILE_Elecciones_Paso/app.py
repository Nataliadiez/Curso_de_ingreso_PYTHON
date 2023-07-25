
'''
Apellido: Diez
Nombre: Natalia
'''
'''
TP 2 WHILE
'''
'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos YA TA
b. nombre y edad del candidato con menos votos YA TA
c. el promedio de edades de los candidatos YA TA
d. total de votos emitidos. YA TA
Todos los datos se ingresan por prompt y los resultados por consola (print)

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
        flag_votos = True
        contador_candidatos = 0
        total_votos = 0
        total_edades = 0
        
        while True:
            nombre = prompt(title="Nombre", prompt="Ingrese su nombre:")
            edad = prompt(title="Edad", prompt="Ingrese su edad (mayor a 25 años):")
            votos = prompt(title="Votos", prompt="¿Cuántos votos recibió? (no puede ser menor a 0):")

            if nombre != "" or nombre != None and edad != "" or edad != None and votos != "" or votos != None:
                edad = int(edad)
                votos = int(votos)

            if edad < 25:
                alert(title="Error", message="Edad no puede ser menor a 25.\nLos datos no serán grabados.")
                continue
            elif votos < 0:
                alert(title="Error", message="Los votos no pueden ser menor a 0.\nLos datos no serán grabados.")
                continue

            if flag_votos:
                mas_votado = nombre
                menos_votado = nombre
                mas_votos = votos
                menos_votos = votos
                flag_votos = False
                edad_menos_votado = edad
            elif votos > mas_votos:
                mas_votado = nombre
                mas_votos = votos
            elif votos < menos_votos:
                menos_votado = nombre
                menos_votos = votos
                edad_menos_votado = edad

            total_edades += edad
            contador_candidatos += 1
            total_votos += votos

            salida = question(title="Continuar", message="¿Desea continuar agregando candidatos?")
            
            if salida:
                continue
            else:
                break
            
        
        if nombre == "" or nombre == None or edad == "" or edad == None or votos == "" or votos == None:
            alert(title="Error", message="No se pudo realizar la operación.")
        else:
            promedio_edad = total_edades / contador_candidatos
            print(f"Candidato más votado: {mas_votado}\nCandidato menos votado y su edad: {menos_votado} {edad_menos_votado} años.\nPromedio de edades: {round(promedio_edad,2)}\nTotal de votos: {total_votos}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
