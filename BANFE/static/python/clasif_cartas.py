# Creación de la clase Carta
class Carta:
    def __init__(self, color, forma, numero):
        self.forma = forma
        self.color = color
        self.numero = numero

# Creación de la clase Prueba
class Prueba_6:

    # Variables usadas en BANFE-2
    aciertos = 0
    errores = 0
    perseveraciones = 0
    err_mant = 0
    pers_dif = 0

    # contador de aciertos auxiliar
    cont_ac = 0

    # Banderas usadas para controlar el los errores y perseveraciones de la prueba
    ban_pers = False
    ban_color = False
    ban_num = False
    ban_forma = False
    ban_x = False

    # Banderas para errores de perserverseveraciones
    error_forma = False
    error_color = False
    error_num = False
    error_x = False
    incorrecto = True

    # Diccionario con valores de la baraja de cartas
    baraja_cartas = {
        1: ("Azul", "Cuadrado", 1),
        2: ("Marron", "Rombo", 2),
        3: ("Celeste", "Pentagono", 3),
        4: ("Rojo", "Hexagono", 4),
        5: ("Azul", "Rombo", 1),
        6: ("Marron", "Cuadrado", 2),
        7: ("Celeste", "Hexagono", 3),
        8: ("Rojo", "Rombo", 4),
        9: ("Azul", "Hexagono", 1),
        10: ("Marron", "Pentagono", 2),
        11: ("Celeste", "Rombo", 3),
        12: ("Rojo", "Cuadrado", 4),
        13: ("Azul", "Pentagono", 1),
        14: ("Marron", "Hexagono", 2),
        15: ("Celeste", "Cuadrado", 3),
        16: ("Rojo", "Pentagono", 4),
        17: ("Celeste", "Hexagono", 1),
        18: ("Rojo", "Pentagono", 2),
        19: ("Azul", "Cuadrado", 3),
        20: ("Marron", "Rombo", 4),
        21: ("Celeste", "Rombo", 1),
        22: ("Rojo", "Hexagono", 2),
        23: ("Azul", "Pentagono", 3),
        24: ("Marron", "Cuadrado", 4),
        25: ("Celeste", "Pentagono", 1),
        26: ("Rojo", "Cuadrado", 2),
        27: ("Azul", "Rombo", 3),
        28: ("Marron", "Hexagono", 4),
        29: ("Celeste", "Cuadrado", 1),
        30: ("Rojo", "Rombo", 2),
        31: ("Azul", "Hexagono", 3),
        32: ("Marron", "Pentagono", 4),
        33: ("Marron", "Hexagono", 1),
        34: ("Azul", "Rombo", 2),
        35: ("Rojo", "Pentagono", 3),
        36: ("Celeste", "Cuadrado", 4),
        37: ("Marron", "Rombo", 1),
        38: ("Azul", "Hexagono", 2),
        39: ("Rojo", "Cuadrado", 3),
        40: ("Celeste", "Pentagono", 4),
        41: ("Marron", "Cuadrado", 1),
        42: ("Azul", "Pentagono", 2),
        43: ("Rojo", "Rombo", 3),
        44: ("Celeste", "Hexagono", 4),
        45: ("Marron", "Pentagono", 1),
        46: ("Azul", "Cuadrado", 2),
        47: ("Rojo", "Hexagono", 3),
        48: ("Celeste", "Rombo", 4),
        49: ("Rojo", "Hexagono", 1),
        50: ("Celeste", "Pentagono", 2),
        51: ("Marron", "Rombo", 3),
        52: ("Azul", "Cuadrado", 4),
        53: ("Rojo", "Pentagono", 1),
        54: ("Celeste", "Hexagono", 2),
        55: ("Marron", "Cuadrado", 3),
        56: ("Azul", "Rombo", 4),
        57: ("Rojo", "Rombo", 1),
        58: ("Celeste", "Cuadrado", 2),
        59: ("Marron", "Hexagono", 3),
        60: ("Azul", "Pentagono", 4),
        61: ("Rojo", "Cuadrado", 1),
        62: ("Celeste", "Rombo", 2),
        63: ("Marron", "Pentagono", 3),
        64: ("Azul", "Hexagono", 4)
    }

    # Creación de las cartas clasificadoras y la pila
    c1 = Carta("Celeste", "Cuadrado", 1)
    c2 = Carta("Rojo", "Hexagono", 2)
    c3 = Carta("Marron", "Rombo", 3)
    c4 = Carta("Azul", "Pentagono", 4)

    pila = Carta("Negro", "Círculo", 0)
    
    def limpiar_prueba(self):
        self.aciertos = self.errores = self.perseveraciones = self.err_mant = self.pers_dif = self.cont_ac = 0
        self.ban_color = self.ban_forma = self.ban_num = self.ban_x = self.ban_pers = False
        self.error_color = self.error_forma = self.error_num = self.error_x = False
        self.incorrecto = False
    
    # Método que asigna los valores de la carta que se tomó de la pila
    def asignar_valores(self, carta):
        print(f'Tarjeta tomada: {carta}')
        if carta < 65:
            mano = self.baraja_cartas[carta]

            self.pila.color = mano[0]
            self.pila.forma = mano[1]
            self.pila.numero = mano[2]

            # -> Aquí mandamos mensaje de incorrecto
            self.incorrecto = False            

    # Método que determinar los criterios de clasificación
    def evaluar_criterio(self):
        if self.aciertos < 10 or self.aciertos > 49:
            print("Evaluando color")
            return "color"
        elif self.aciertos < 20 or (self.aciertos > 29 and self.aciertos < 40):
            print("Evaluando forma")
            return "forma"
        else:
            print("Evaluando número")
            return "numero"
    
    # Método que determina el criterio de comparación
    def determinar_criterio(self, carta):
        if self.evaluar_criterio() == "color":
            self.comparar_pila_color(carta)
        elif self.evaluar_criterio() == "forma":
            self.comparar_pila_forma(carta)
        else:
            self.comparar_pila_numero(carta)

    # Método principal que evalua la respuesta dada por el usuario
    def evaluar_respuesta(self, lugar):
        if lugar == "A":
            self.determinar_criterio(self.c1)
        elif lugar == "B":
            self.determinar_criterio(self.c2)
        elif lugar == "C":
            self.determinar_criterio(self.c3)
        else:
            self.determinar_criterio(self.c4)

    # Método que cambia el valor de las banderas de la prueba
    def cambiar_banderas(self, banderas, flag):
        valor = False
        if flag == 1:
            valor = True
        for bandera in banderas:
            if bandera == "ban_num":
                self.ban_num = valor
            elif bandera == "ban_forma":
                self.ban_forma = valor
            elif bandera == "ban_color":
                self.ban_color = valor
            else:
                self.ban_x = valor

    # Método que cambia el valor de los errores de la prueba
    def cambiar_errores(self, errores):
        for error in errores:
            if error == "error_num":
                self.error_num = True
            elif error == "error_forma":
                self.error_forma = True
            elif error == "error_color":
                self.error_color = True
            else:
                self.error_x = True

    # Método que determina el tipo de error realizado
    def evaluar_error(self, condicion_banderas, banderas, errores, condicion_aciertos, condicion_errores, error, ban_err):
        if self.ban_pers and condicion_banderas:
            # -> Aquí mandamos mensaje de incorrecto
            self.incorrecto = True
            # Entramos a una perseveración
            print("Perseveración")
            self.perseveraciones += 1
            self.cambiar_banderas(banderas, 0)
        else:
            if self.cont_ac >= 3 and condicion_aciertos:        
                 # -> Aquí mandamos mensaje de incorrecto
                self.incorrecto = True       
                # Error de mantenimiento
                print("Error de mantenimiento")
                self.err_mant += 1
            else:
                if condicion_errores:       
                    # -> Aquí mandamos mensaje de incorrecto
                    self.incorrecto = True                      
                    # Perseveración diferida
                    print("Perseveración diferida")
                    self.pers_dif += 1
                else:
                    # Error
                    self.incorrecto = True   
                    print("Error")
                    self.cambiar_errores(errores)
                    self.errores += 1
            self.anotar_error(error, ban_err)

    # Método que anota los aciertos obtenidos en cada movimiento
    def anotar_acierto(self, valor):
        self.aciertos += 1
        self.ban_pers = False
        self.cont_ac += 1
        self.ban_x = self.error_x = False
        self.incorrecto = False

        if valor == "color":
            self.ban_num = self.ban_forma = False
            self.error_num = self.error_forma = False
        elif valor == "forma":
            self.ban_num = self.ban_color = False
            self.error_num = self.error_color = False
        else:
            self.ban_color = self.ban_forma = False
            self.error_color = self.error_forma = False

    # Método que anota los errores ocurridos en cada movimiento
    def anotar_error(self, error, flags):
        self.cont_ac = 0
        self.ban_pers = True
        # -> Aquí mandamos mensaje de incorrecto
        self.incorrecto = True
        print(f"Error encontrado: {self.incorrecto}")
        
        if error == "C2":  # Coinciden 2
            self.cambiar_banderas(flags, 1)
            self.ban_x = False
        elif error == "CN":  # Coincide con número
            self.ban_num = True
            self.cambiar_banderas(flags, 0)
        elif error == "CF":  # Coincide con forma
            self.ban_forma = True
            self.cambiar_banderas(flags, 0)
        elif error == "CC":  # Coincide con color
            self.ban_color = True
            self.cambiar_banderas(flags, 0)
        else:
            self.ban_x = True
            self.cambiar_banderas(flags, 0)
            
    # Método que compara el movimiento cuando el criterio es color
    def comparar_pila_color(self, carta):
        # Condición que reinicia el contador de aciertos al llegar a 10
        if self.cont_ac == 10:
            self.cont_ac = 0

        # Evalúa que la carta coincida con al menos una propiedad de clasificación
        if self.pila.color == carta.color or self.pila.forma == carta.forma or self.pila.numero == carta.numero:
            if self.pila.color == carta.color and self.pila.forma == carta.forma and self.pila.numero == carta.numero:
                # Coincide con forma, número y color
                print("Coincide con las 3")
                self.anotar_acierto("color")
            elif self.pila.color == carta.color and self.pila.numero == carta.numero:
                # Coincide con número y color
                print("Coincide con color y numero")
                self.anotar_acierto("color")
            elif self.pila.color == carta.color and self.pila.forma == carta.forma:
                # Coincide con color y forma
                print("Coincide con color y forma")
                self.anotar_acierto("color")
            elif self.pila.color == carta.color:
                # Coincide con color
                print("Coincide con color")
                self.anotar_acierto("color")
            elif self.pila.forma == carta.forma and self.pila.numero == carta.numero:
                # Error: Coincide con forma y número
                print("Coincide con forma y número")
                self.evaluar_error(
                    self.ban_num or self.ban_forma,
                    ["ban_x"],
                    ["error_num", "error_forma"],
                    self.aciertos != 20 and self.aciertos != 30 and self.aciertos != 40 and self.aciertos != 50,
                    self.error_num and self.error_forma and self.error_x,
                    "C2",
                    ["ban_num", "ban_forma"])
            elif self.pila.numero == carta.numero:
                # Error: Coincide con número
                print("Coincide con número")
                self.evaluar_error(
                    self.ban_num,
                    ["ban_x", "ban_forma"],
                    ["error_num"],
                    self.aciertos != 30 and self.aciertos != 50,
                    (self.error_num and self.error_forma and self.error_x) or (
                        self.error_num and self.error_forma) or (self.error_num and self.error_x),
                    "CN",
                    ["ban_forma", "ban_x"])
            else:
                # Error: Coincide con forma
                print("Coincide con forma")
                self.evaluar_error(
                    self.ban_forma,
                    ["ban_x", "ban_num"],
                    ["error_forma"],
                    self.aciertos != 20 and self.aciertos != 40,
                    (self.error_num and self.error_forma and self.error_x) or (
                        self.error_num and self.error_forma) or (self.error_forma and self.error_x),
                    "CF",
                    ["ban_x", "ban_num"])
        else:
            # Error: No hay coincidencias
            print("No hay coincidencias")
            self.evaluar_error(
                self.ban_x,
                ["ban_num", "ban_forma"],
                ["error_x"],
                self.aciertos != 20 and self.aciertos != 30 and self.aciertos != 40 and self.aciertos != 50,
                (self.error_num and self.error_forma and self.error_x) or (
                    self.error_x and self.error_forma) or (self.error_num and self.error_x),
                "NC",
                ["ban_num", "ban_forma"])

    # Método que compara el movimiento cuando el criterio es forma
    def comparar_pila_forma(self, carta):
        # Condición que reinicia el contador de aciertos al llegar a 10
        if self.cont_ac == 10:
            self.cont_ac = 0

        # Evalúa que la carta coincida con al menos una propiedad de clasificación
        if self.pila.color == carta.color or self.pila.forma == carta.forma or self.pila.numero == carta.numero:
            if self.pila.color == carta.color and self.pila.forma == carta.forma and self.pila.numero == carta.numero:
                # Coincide con forma color, forma y número
                self.anotar_acierto("forma")
            elif self.pila.forma == carta.forma and self.pila.numero == carta.numero:
                # Coinciden forma y número
                self.anotar_acierto("forma")
            elif self.pila.forma == carta.forma and self.pila.color == carta.color:
                # Coinciden forma y color
                self.anotar_acierto("forma")
            elif self.pila.forma == carta.forma:
                # Coincide forma
                self.anotar_acierto("forma")
            elif self.pila.color == carta.color and self.pila.numero == carta.numero:
                # Error: Coincide con color y número
                self.evaluar_error(
                    self.ban_color or self.ban_num,
                    ["ban_x"],
                    ["error_num", "error_color"],
                    self.aciertos != 10 and self.aciertos != 60 and self.aciertos != 30 and self.aciertos != 50,
                    self.error_num and self.error_color and self.error_x,
                    "C2",
                    ["ban_num", "ban_color"]
                )
            elif self.pila.color == carta.color:
                # Error: Coincide con color
                self.evaluar_error(
                    self.ban_color,
                    ["ban_x", "ban_num"],
                    ["error_color"],
                    self.aciertos != 10 and self.aciertos != 60,
                    (self.error_num and self.error_color and self.error_x) or (
                        self.error_num and self.error_color) or (self.error_color and self.error_x),
                    "CC",
                    ["ban_x", "ban_num"],
                )
            else:
                # Error: Coincide con número
                self.evaluar_error(
                    self.ban_num,
                    ["ban_x", "ban_color"],
                    ["error_num"],
                    self.aciertos != 30 and self.aciertos != 50,
                    (self.error_num and self.error_color and self.error_x) or (
                        self.error_num and self.error_color) or (self.error_num and self.error_x),
                    "CN",
                    ["ban_x", "ban_color"]
                )

        else:
            # Error: No hay coincidencias
            self.evaluar_error(
                self.ban_x,
                ["ban_num", "ban_color"],
                ["error_x"],
                self.aciertos != 10 and self.aciertos != 60 and self.aciertos != 30 and self.aciertos != 50,
                (self.error_num and self.error_color and self.error_x) or (
                    self.error_x and self.error_color) or (self.error_num and self.error_x),
                "NC",
                ["ban_num", "ban_color"]
            )

    # Método que compara el movimiento cuando el criterio es número
    def comparar_pila_numero(self, carta):
        if self.cont_ac == 10:
            self.cont_ac = 0
        # Evalúa que la carta coincida con al menos una propiedad de clasificación
        if self.pila.color == carta.color or self.pila.forma == carta.forma or self.pila.numero == carta.numero:
            if self.pila.color == carta.color and self.pila.forma == carta.forma and self.pila.numero == carta.numero:
                # Coincide con forma, color y numero
                self.anotar_acierto("numero")
            elif self.pila.color == carta.color and self.pila.numero == carta.numero:
                # Coincide con color y número
                self.anotar_acierto("numero")
            elif self.pila.forma == carta.forma and self.pila.numero == carta.numero:
                # Coincide con forma y número
                self.anotar_acierto("numero")
            elif self.pila.numero == carta.numero:
                # Coincide con número
                self.anotar_acierto("numero")
            elif self.pila.forma == carta.forma and self.pila.color == carta.color:
                # Error: Coincide con forma y número
                print("Coincide con forma y color")
                self.evaluar_error(
                    self.ban_color or self.ban_forma,
                    ["ban_x"],
                    ["error_color", "error_forma"],
                    self.aciertos != 10 and self.aciertos != 20 and self.aciertos != 40 and self.aciertos != 60,
                    self.error_color and self.error_forma and self.error_x,
                    "C2",
                    ["ban_color", "ban_forma"])
            elif self.pila.numero == carta.numero:
                # Error: Coincide con color
                print("Coincide con color")
                self.evaluar_error(
                    self.ban_color,
                    ["ban_x", "ban_forma"],
                    ["error_color"],
                    self.aciertos != 10 and self.aciertos != 60,
                    (self.error_color and self.error_forma and self.error_x) or (
                        self.error_color and self.error_forma) or (self.error_color and self.error_x),
                    "CC",
                    ["ban_forma", "ban_x"])
            else:
                # Error: Coincide con forma
                print("Coincide con forma")
                self.evaluar_error(
                    self.ban_forma,
                    ["ban_x", "ban_color"],
                    ["error_forma"],
                    self.aciertos != 20 and self.aciertos != 40,
                    (self.error_color and self.error_forma and self.error_x) or (
                        self.error_color and self.error_forma) or (self.error_forma and self.error_x),
                    "CF",
                    ["ban_x", "ban_color"])
        else:
            # Error: No hay coincidencias
            print("No hay coincidencias")
            self.evaluar_error(
                self.ban_x,
                ["ban_color", "ban_forma"],
                ["error_x"],
                self.aciertos != 10 and self.aciertos != 20 and self.aciertos != 40 and self.aciertos != 60,
                (self.error_color and self.error_forma and self.error_x) or (
                    self.error_x and self.error_forma) or (self.error_color and self.error_x),
                "NC",
                ["ban_color", "ban_forma"])