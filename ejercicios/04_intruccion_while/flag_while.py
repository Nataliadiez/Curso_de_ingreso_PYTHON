

def btn_comenzar_ingreso_on_click(self):
        es_primer_num = True
        maximo = None
        minimo = None

        while True:
            numero_ingresado = prompt("Numero", "Ingrese un numero:")
            if numero_ingresado is None:
                break
            numero_ingresado = int(numero_ingresado)

            ######### OPCION 1 ##########
            if es_primer_num:
                maximo = numero_ingresado
                minimo = numero_ingresado
                es_primer_num = False

            elif numero_ingresado > maximo:
                maximo = numero_ingresado

            elif numero_ingresado < minimo:
                minimo = numero_ingresado

            ######### OPCION 2 ##########
            if es_primer_num or numero_ingresado > maximo:
                maximo = numero_ingresado

            if es_primer_num or numero_ingresado < minimo:
                minimo = numero_ingresado
                es_primer_num = False

            ######### OPCION 3 ##########
            if maximo == None or numero_ingresado > maximo:
                maximo = numero_ingresado

            if minimo == None or numero_ingresado < minimo:
                minimo = numero_ingresado
