class Prueba_2:
    
    # Variables usadas en BANFE-2
    aciertos = 0
    perseveraciones = 0

    # Listas auxiliares para evaluar los resultados
    vecinos = [0,0,0,0,0,0,0,0]
    figuras = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # Contador auxiliar
    cont_clicks = 0

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

    # Variable que no afecta a la lógica, pero se usa en la vista
    terminar = 0

    # Método que permite seleccionar la figura que fue seleecionada
    def seleccionar(self, figura):
        if figura == "ardilla":
            self.evaluar_clicks('ardilla',1)

        elif figura == "avion":
            self.evaluar_clicks('avion',2)

        elif figura == "bicicleta":
            self.evaluar_clicks('bicicleta',3)  
            
        elif figura == "pluma":
            self.evaluar_clicks('pluma',4)

        elif figura == "caballo":
            self.evaluar_clicks('caballo',5)  

        elif figura == "calceta":
            self.evaluar_clicks('calceta',6)

        elif figura == "casa":                                            
            self.evaluar_clicks('casa',7)

        elif figura == "cepillo":
            self.evaluar_clicks('cepillo',8)

        elif figura == "cinturon":
            self.evaluar_clicks('cinturon',9)

        elif figura == "foco":
            self.evaluar_clicks('foco',10)

        elif figura == "guitarra":
            self.evaluar_clicks('guitarra',11)

        elif figura == "hacha":
            self.evaluar_clicks('hacha',12)

        elif figura == "hormiga":
            self.evaluar_clicks('hormiga',13)
        
        elif figura == "mano":
            self.evaluar_clicks('mano',14)

        elif figura == "manzana":
            self.evaluar_clicks('manzana',15)

        elif figura == "martillo":
            self.evaluar_clicks('martillo',16)

        elif figura == "mesa":
            self.evaluar_clicks('mesa',17)

        elif figura == "pantalon":
            self.evaluar_clicks('pantalon',18)

        elif figura == "pez":
            self.evaluar_clicks('pez',19)

        elif figura == "platano":
            self.evaluar_clicks('platano',20)

        elif figura == "saco":
            self.evaluar_clicks('saco',21)

        elif figura == "gato":
            self.evaluar_clicks('gato',22)

        elif figura == "jarra":
            self.evaluar_clicks('jarra',23)

        elif figura == "carro":
            self.evaluar_clicks('carro',24)

        elif figura == "estufa":
            self.evaluar_clicks('estufa',25)                

    # Método que comprueba los vecinos que tiene cada figura
    def comprobar_vecinos(self, figura):
        if figura == 1:
            self.evaluar_figura(
                self.vecinos[0] != 1,
                'ardilla',
                figura
            )
        elif figura == 2:
            self.evaluar_figura(
                self.vecinos[0] != 2 and self.vecinos[1] != 2,
                'avion',
                figura
            )
        elif figura == 3:
            self.evaluar_figura(
                self.vecinos[0] != 3 and self.vecinos[1] != 3 and self.vecinos[2] != 3 and self.vecinos[4] != 3,
                'bicicleta',
                figura
            )        
        elif figura == 4:
            self.evaluar_figura(
                self.vecinos[0] != 4 and self.vecinos[1] != 4 and self.vecinos[2] != 4 and self.vecinos[4] != 4,
                'pluma',
                figura
            )        
        elif figura == 5:
            self.evaluar_figura(
                self.vecinos[0] != 5 and self.vecinos[2] != 5 and self.vecinos[4] != 5,
                'caballo',
                figura
            )        
        elif figura == 6:
            self.evaluar_figura(
                self.vecinos[0] != 6 and self.vecinos[1] != 6 and self.vecinos[2] != 6 and self.vecinos[7] != 6,
                'calceta',
                figura
            )        
        elif figura == 7:                                            
            self.evaluar_figura(
                self.vecinos[0] != 7 and self.vecinos[1] != 7 and self.vecinos[2] != 7 and self.vecinos[7] != 7,
                'casa',
                figura
            )        
        elif figura == 8:
            self.evaluar_figura(
                self.vecinos[0] != 8 and self.vecinos[1] != 8 and self.vecinos[2] != 8 and self.vecinos[3] != 8 and self.vecinos[7] != 8,
                'cepillo',
                figura
            )                
        elif figura == 9:
            self.evaluar_figura(
                self.vecinos[0] != 9 and self.vecinos[1] != 9 and self.vecinos[2] != 9 and self.vecinos[3] != 9,
                'cinturon',
                figura
            )        
        elif figura == 10:
            self.evaluar_figura(
                self.vecinos[1] != 10 and self.vecinos[2] != 10 and self.vecinos[3] != 10,
                'foco',
                figura
            )        
        elif figura == 11:
            self.evaluar_figura(
                self.vecinos[0] != 11 and self.vecinos[3] != 11 and self.vecinos[4] != 11 and self.vecinos[6] != 11,
                'guitarra',
                figura
            )        
        elif figura == 12:
            self.evaluar_figura(
                self.vecinos[0] != 12 and self.vecinos[1] != 12 and self.vecinos[2] != 12 and self.vecinos[3] != 12,
                'hacha',
                figura
            )        
        elif figura == 13:
            self.evaluar_figura(
                self.vecinos[0] != 13 and self.vecinos[1] != 13 and self.vecinos[2] != 13 and self.vecinos[3] != 13 and self.vecinos[4] != 13 and self.vecinos[5] != 13 and self.vecinos[6] != 13,
                'hormiga',
                figura
            )                
        elif figura == 14:
            self.evaluar_figura(
                self.vecinos[0] != 14 and self.vecinos[1] != 14 and self.vecinos[2] != 14 and self.vecinos[3] != 14 and self.vecinos[4] != 14 and self.vecinos[5] != 14,
                'mano',
                figura
            )        
        elif figura == 15:
            self.evaluar_figura(
                self.vecinos[1] != 15 and self.vecinos[2] != 15 and self.vecinos[4] != 15,
                'manzana',
                figura
            )        
        elif figura == 16:
            self.evaluar_figura(
                self.vecinos[0] != 16 and self.vecinos[3] != 16 and self.vecinos[4] != 16 and self.vecinos[5] != 16,
                'martillo',
                figura
            )        
        elif figura == 17:
            self.evaluar_figura(
                self.vecinos[0] != 17 and self.vecinos[1] != 17 and self.vecinos[2] != 17 and self.vecinos[3] != 17 and self.vecinos[5] != 17 and self.vecinos[6] != 17,
                'mesa',
                figura
            )        
        elif figura == 18:
            self.evaluar_figura(
                self.vecinos[0] != 18 and self.vecinos[1] != 18 and self.vecinos[2] != 18 and self.vecinos[3] != 18 and self.vecinos[5] != 18 and self.vecinos[6] != 18,
                'pantalon',
                figura
            )                
        elif figura == 19:
            self.evaluar_figura(
                self.vecinos[0] != 3 and self.vecinos[1] != 3 and self.vecinos[2] != 3 and self.vecinos[3] != 19 and self.vecinos[4] != 19 and self.vecinos[5] != 19 and self.vecinos[6] != 19 and self.vecinos[7] != 19,
                'pez',
                figura
            )         
        elif figura == 20:
            self.evaluar_figura(
                self.vecinos[1] != 20 and self.vecinos[2] != 20 and self.vecinos[4] != 20 and self.vecinos[7] != 20,
                'platano',
                figura
            )        
        elif figura == 21:
            self.evaluar_figura(
                self.vecinos[3] != 21 and self.vecinos[5] != 21,
                'saco',
                figura
            )        
        elif figura == 22:
            self.evaluar_figura(
                self.vecinos[2] != 22 and self.vecinos[3] != 22 and self.vecinos[4] != 22 and self.vecinos[5] != 22 and self.vecinos[6] != 22,
                'gato',
                figura
            )        
        elif figura == 23:
            self.evaluar_figura(
                self.vecinos[3] != 23 and self.vecinos[4] != 23 and self.vecinos[5] != 23 and self.vecinos[6] != 23 and self.vecinos[7] != 23,
                'jarra',
                figura
            )                
        elif figura == 24:
            self.evaluar_figura(
                self.vecinos[2] != 24 and self.vecinos[3] != 24 and self.vecinos[4] != 24 and self.vecinos[6] != 24 and self.vecinos[7] != 24,
                'carro',
                figura
            )        
        elif figura == 25:
            self.evaluar_figura(
                self.vecinos[4] != 25 and self.vecinos[7] != 25,
                'estufa',
                figura
            )                                            
    
    # Método que evalua los clicks que se han dado a lo largo de la prueba
    def evaluar_clicks(self, figura_pers, figura):
        print(f'Clicks: {self.cont_clicks}')
        if self.cont_clicks < 12:
            self.comprobar_vecinos(figura)
            self.anotar_vecinos(figura)
            self.cont_clicks += 1
        else:
            print('Andamos despues de 12')
            self.condicion_evaluar(figura_pers,figura)

    # Método que evalua si una figura es vecina de la figura anteriormente seleccionada 
    def evaluar_figura(self, condicion_vecinos, figura_pers, figura):
        if(condicion_vecinos):
            print("No hay vecinos")
            self.condicion_evaluar(figura_pers, figura)
        else:
            print("Incorrecto")
            self.figuras_pers[figura_pers] = 1
            self.figuras[figura-1] = 1

    # Método que evalua si la figura ya ha sido seleccionada anteriormente 
    def condicion_evaluar(self, figura_pers, figura):
        if(self.figuras_pers[figura_pers] == 1):
            self.perseveraciones += 1

        else:
            self.figuras[figura-1] = 1
            self.aciertos += 1
            self.figuras_pers[figura_pers] = 1

    # Método que anota los vecinos de cada figura
    def anotar_vecinos(self, figura):
        if figura == 1:
            self.almacenar_lista(figura)
        elif figura == 2:
            self.almacenar_lista(figura)
        elif figura == 3:
            self.almacenar_lista(figura)
        elif figura == 4:
            self.almacenar_lista(figura)
        elif figura == 5:
            self.almacenar_lista(figura)
        elif figura == 6:
            self.almacenar_lista(figura)    
        elif figura == 7:
            self.almacenar_lista(figura)
        elif figura == 8:
            self.almacenar_lista(figura)
        elif figura == 9:
            self.almacenar_lista(figura)
        elif figura == 10:
            self.almacenar_lista(figura)
        elif figura == 11:
            self.almacenar_lista(figura)
        elif figura == 12:
            self.almacenar_lista(figura)
        elif figura == 13:
            self.almacenar_lista(figura)
        elif figura == 14:
            self.almacenar_lista(figura)
        elif figura == 15:
            self.almacenar_lista(figura)
        elif figura == 16:
            self.almacenar_lista(figura)
        elif figura == 17:
            self.almacenar_lista(figura)
        elif figura == 18:
            self.almacenar_lista(figura)
        elif figura == 19:
            self.almacenar_lista(figura)
        elif figura == 20:
            self.almacenar_lista(figura)
        elif figura == 21:
            self.almacenar_lista(figura)
        elif figura == 22:
            self.almacenar_lista(figura)
        elif figura == 23:
            self.almacenar_lista(figura)
        elif figura == 24:
            self.almacenar_lista(figura)
        elif figura == 25:
            self.almacenar_lista(figura)
    
    # Método que almacena los vecinos de la figura seleccionada
    def almacenar_lista(self, figura):
    
        pos_vec = (
            (2,7,6,0,0,0,0,0),
            (1,6,7,8,3,0,0,0),
            (2,7,8,9,4,0,0,0),
            (3,8,9,10,5,0,0,0),
            (4,9,10,0,0,0,0,0),
            (1,2,7,12,11,0,0,0),
            (1,2,3,8,13,12,11,6),
            (2,3,4,9,14,13,12,7),
            (3,4,5,10,15,14,13,8),
            (5,4,9,14,15,0,0,0),
            (6,7,12,17,16,0,0,0),
            (6,7,8,11,13,16,17,18),
            (7,8,9,12,14,17,18,19),
            (8,9,10,13,15,18,19,20),
            (9,10,12,19,20,0,0,0),
            (11,12,17,21,22,0,0,0),
            (11,12,13,16,18,21,22,23),
            (12,13,14,17,19,22,23,24),
            (13,14,15,18,20,23,24,25),
            (14,15,19,24,25,0,0,0),
            (16,17,22,0,0,0,0,0),
            (16,17,18,21,23,0,0,0),
            (17,18,19,22,24,0,0,0),
            (18,19,20,23,25,0,0,0),
            (19,20,24,0,0,0,0,0)
        )

        for x in range(0,8):
            self.vecinos[x] = pos_vec[figura-1][x]

    # Método que limpia las variables 
    def limpiar_variables(self):
        self.aciertos = 0
        self.perseveraciones = 0
        self.cont_clicks = 0
        self.terminar = 0

        for key in self.figuras_pers: 
            self.figuras_pers[key] = 0
        
        for x in range(0,8):
            self.vecinos[x] = 0

        for x in range(0,25):
            self.figuras[x] = 0
    
    # Método que calcula las omisiones 
    def calcular_omisiones(self):
        omisiones = 0

        for x in range(0,25):
            if self.figuras[x] == 0:
                omisiones += 1
        return omisiones
    
    # Método que ayuda a apagar la prueba
    def apagar(self, fin):
        if fin == 1:
            self.terminar = 1
        
        print(f'Apagar: {fin}')