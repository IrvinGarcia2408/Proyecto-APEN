class Prueba_14:
    # Variables usadas en BANFE-2
    sustituciones = 0
    error_orden = 0
    perseveraciones = 0

    # Diccionario para anotar figuras perseveradas
    figuras_pers = {
        "casa": 0,
        "pantalon": 0,
        "martillo": 0,
        "cinturon": 0,

        "mano": 0,
        "avion": 0,
        "mesa": 0,
        "calceta": 0,
        "manzana": 0,
        
        "hormiga": 0,
        "guitarra": 0,
        "ardilla": 0,
        "foco": 0,
        "platano": 0,
        "hacha": 0,                        

        "pez": 0,
        "pluma": 0,
        "bicicleta": 0,        

        "caballo": 0,
        "cepillo": 0,
        "saco": 0,        
        "gato": 0,
        "jarra": 0,
        "carro": 0,        
        "estufa": 0
    }

    aciertos = 0
    nivel = 0
    figura = 1
    fin = 0

    reiniciar = "apagado"

    # Método principal que responde al View
    def comparar(self, nombre,f,l):
        self.figura = f
        self.nivel = l

        if self.nivel == 1:
            # casa - pantalon - martillo - cinturon
            self.evaluar_nivel1(self.figura,nombre)
        elif self.nivel == 2:
            # mano - avion - mesa - calceta - manzana
            self.evaluar_nivel2(self.figura,nombre)
        elif self.nivel == 3:
            # hormiga - guitarra - ardilla - foco - platano - hacha
            self.evaluar_nivel3(self.figura,nombre)
        elif self.nivel == 4:
            # foco - pez - pluma - casa - bicicleta - cinturon - calceta
            self.evaluar_nivel4(self.figura,nombre)
    
    # Método que evalua las perseveraciones y errores de orden
    def evaluar_perseveracion(self, orden, nombre):
        if self.figuras_pers[nombre] == 1:
            self.perseveraciones += 1
        else:
            self.figuras_pers[nombre] = 1    
        if orden == 0:
            self.error_orden += 1        

    # Método que evalua los valores del nivel 1
    def evaluar_nivel1(self, figura, nombre):
        print(figura)
        if figura == 1:
            if nombre == "casa" or nombre == "pantalon" or nombre == "martillo" or nombre == "cinturon":
                if nombre == "casa":
                    self.figuras_pers["casa"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1
                print(f"No la encontre {self.sustituciones}")
        elif figura == 2:   
            if nombre == "casa" or nombre == "pantalon" or nombre == "martillo" or nombre == "cinturon":
                if nombre == "pantalon":
                    self.figuras_pers["pantalon"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                
                print(f"No la encontre {self.sustituciones}")
        elif figura == 3:
            if nombre == "casa" or nombre == "pantalon" or nombre == "martillo" or nombre == "cinturon":
                if nombre == "martillo":
                    self.figuras_pers["martillo"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1             
        elif figura == 4:
            if nombre == "casa" or nombre == "pantalon" or nombre == "martillo" or nombre == "cinturon":
                if nombre == "cinturon":
                    self.figuras_pers["cinturon"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1   
        else:
            if nombre == "casa" or nombre == "pantalon" or nombre == "martillo" or nombre == "cinturon":
                self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                   

    # Método que evalua los valores del nivel 2
    def evaluar_nivel2(self, figura, nombre):
        if figura == 1:
            if nombre == "mano" or nombre == "avion" or nombre == "mesa" or nombre == "calceta" or nombre == "manzana":
                if nombre == "mano":
                    self.figuras_pers["mano"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                    
                print(f'Estoy en {self.figuras_pers[nombre]}')
        elif figura == 2:   
            if nombre == "mano" or nombre == "avion" or nombre == "mesa" or nombre == "calceta" or nombre == "manzana":
                if nombre == "avion":
                    self.figuras_pers["avion"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                
        elif figura == 3:
            if nombre == "mano" or nombre == "avion" or nombre == "mesa" or nombre == "calceta" or nombre == "manzana":
                if nombre == "mesa":
                    self.figuras_pers["mesa"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1             
        elif figura == 4:
            if nombre == "mano" or nombre == "avion" or nombre == "mesa" or nombre == "calceta" or nombre == "manzana":
                if nombre == "calceta":
                    self.figuras_pers["calceta"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1   
        elif figura == 5:
            if nombre == "mano" or nombre == "avion" or nombre == "mesa" or nombre == "calceta" or nombre == "manzana":
                if nombre == "manzana":
                    self.figuras_pers["manzana"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1   
        else:
            if nombre == "mano" or nombre == "avion" or nombre == "mesa" or nombre == "calceta" or nombre == "manzana":
                self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1               

    # Método que evalua los valores del nivel 3
    def evaluar_nivel3(self, figura, nombre):
        if figura == 1:
            if nombre == "hormiga" or nombre == "guitarra" or nombre == "ardilla" or nombre == "foco" or nombre == "platano" or nombre == "hacha":
                if nombre == "hormiga":
                    self.figuras_pers["hormiga"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1
        elif figura == 2:   
            if nombre == "hormiga" or nombre == "guitarra" or nombre == "ardilla" or nombre == "foco" or nombre == "platano" or nombre == "hacha":
                if nombre == "guitarra":
                    self.figuras_pers["guitarra"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                
        elif figura == 3:
            if nombre == "hormiga" or nombre == "guitarra" or nombre == "ardilla" or nombre == "foco" or nombre == "platano" or nombre == "hacha":
                if nombre == "ardilla":
                    self.figuras_pers["ardilla"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1             
        elif figura == 4:
            if nombre == "hormiga" or nombre == "guitarra" or nombre == "ardilla" or nombre == "foco" or nombre == "platano" or nombre == "hacha":
                if nombre == "foco":
                    self.figuras_pers["foco"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1   
        elif figura == 5:
            if nombre == "hormiga" or nombre == "guitarra" or nombre == "ardilla" or nombre == "foco" or nombre == "platano" or nombre == "hacha":
                if nombre == "platano":
                    self.figuras_pers["platano"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1   
        elif figura == 6:
            if nombre == "hormiga" or nombre == "guitarra" or nombre == "ardilla" or nombre == "foco" or nombre == "platano" or nombre == "hacha":
                if nombre == "hacha":
                    self.figuras_pers["hacha"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                   
        else:
            if nombre == "hormiga" or nombre == "guitarra" or nombre == "ardilla" or nombre == "foco" or nombre == "platano" or nombre == "hacha":
                self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                

    # Método que evalua los valores del nivel 4
    def evaluar_nivel4(self, figura, nombre):
        if figura == 1:
            if nombre == "foco" or nombre == "pez" or nombre == "pluma" or nombre == "casa" or nombre == "bicicleta" or nombre == "cinturon" or nombre == "calceta":
                if nombre == "foco":
                    self.figuras_pers["foco"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1
        elif figura == 2:   
            if nombre == "foco" or nombre == "pez" or nombre == "pluma" or nombre == "casa" or nombre == "bicicleta" or nombre == "cinturon" or nombre == "calceta":
                if nombre == "pez":
                    self.figuras_pers["pez"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                
        elif figura == 3:
            if nombre == "foco" or nombre == "pez" or nombre == "pluma" or nombre == "casa" or nombre == "bicicleta" or nombre == "cinturon" or nombre == "calceta":
                if nombre == "pluma":
                    self.figuras_pers["pluma"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1             
        elif figura == 4:
            if nombre == "foco" or nombre == "pez" or nombre == "pluma" or nombre == "casa" or nombre == "bicicleta" or nombre == "cinturon" or nombre == "calceta":
                if nombre == "casa":
                    self.figuras_pers["casa"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1   
        elif figura == 5:
            if nombre == "foco" or nombre == "pez" or nombre == "pluma" or nombre == "casa" or nombre == "bicicleta" or nombre == "cinturon" or nombre == "calceta":
                if nombre == "bicicleta":
                    self.figuras_pers["bicicleta"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1   
        elif figura == 6:
            if nombre == "foco" or nombre == "pez" or nombre == "pluma" or nombre == "casa" or nombre == "bicicleta" or nombre == "cinturon" or nombre == "calceta":
                if nombre == "cinturon":
                    self.figuras_pers["cinturon"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1   
        elif figura == 7:
            if nombre == "foco" or nombre == "pez" or nombre == "pluma" or nombre == "casa" or nombre == "bicicleta" or nombre == "cinturon" or nombre == "calceta":
                if nombre == "calceta":
                    self.figuras_pers["calceta"] = 1
                    self.aciertos += 1
                else:
                    self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                                
        else:
            if nombre == "foco" or nombre == "pez" or nombre == "pluma" or nombre == "casa" or nombre == "bicicleta" or nombre == "cinturon" or nombre == "calceta":
                self.evaluar_perseveracion(0,nombre)
            else:
                self.evaluar_perseveracion(1,nombre)
                self.sustituciones += 1                

    # Método que revisa el nivel máximo alcanzado
    def secuencia_maxima(self):
        if (self.nivel == 1 and self.aciertos == 4) or (self.nivel == 2 and self.aciertos == 5) or (self.nivel == 3 and self.aciertos == 6) or (self.nivel == 4 and self.aciertos == 7):
            return self.nivel
        else:
            return self.nivel - 1

    # Método que limpia las variables de la prueba
    def limpiar_variables(self):
        self.aciertos = 0
        self.nivel = 0
        self.figura = 0
        self.fin = 0

        self.sustituciones = 0
        self.error_orden = 0
        self.perseveraciones = 0

        for key in self.figuras_pers:
            self.figuras_pers[key] = 0
        
