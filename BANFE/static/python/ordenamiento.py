class Prueba_3:
    # Variables usadas en BANFE-2
    num_ensayo = [0,0,0]
    error_orden = [0,0,0]
    perseveraciones = [0,0,0]
    intrusiones = [0,0,0]

    # Tuplas auxiliares ordenadas
    tupla_1 = ('arbol','eco','iman','oso','uva')
    tupla_2 = ('beso','casa','dedo','faro','goma','joya')
    tupla_3 = ('ajo','bata','carro','dado','edad','feo','gota')

    palabras = ['','','','','','','','','','']

    lista1_pers = [0,0,0,0,0]
    lista2_pers = [0,0,0,0,0,0]
    lista3_pers = [0,0,0,0,0,0,0]

    # Variable auxiliar
    aciertos = [0,0,0]
    estado = -1
    palabra_anterior = "";

    reiniciar = 0

    # Método principal que invoca Views
    def comparar_palabra(self, palabra,orden,lista):
        if self.existe_palabra(lista,palabra):
            self.esta_orden(lista,palabra,orden)
        else:
            ban_intrusion = False
            
            for x in self.palabras:
                if palabra.lower() == x:
                    # Este if se va si solo es Perseveracion y no error de orden
                    if self.palabra_anterior > palabra.lower():
                        self.error_orden[lista-1] += 1
                        print("Error de orden")
                   
                    self.perseveraciones[lista-1] += 1
                    self.palabra_anterior = palabra.lower()
                    ban_intrusion = True
            
            if not ban_intrusion:
                if self.palabra_anterior > palabra.lower():
                    self.error_orden[lista-1] += 1
                    print("Error de orden")
                self.intrusiones[lista-1] += 1
                self.palabras.append(palabra.lower())
                self.palabra_anterior = palabra.lower()
                print("Intrusion")
    
    # Mëtodo que comprueba si la palabra recibida existe
    def existe_palabra(self, l,p):
        seeker = False

        if l == 1:
            tupla = self.tupla_1
        elif l == 2:
            tupla = self.tupla_2
        else:
            tupla = self.tupla_3
        
        for x in tupla:
            if p == x:
                seeker = True
        
        return seeker
    
    # Método que comprueba si la palabra está en orden
    def esta_orden(self,l,p,o):
        if l == 1:
            tupla = self.tupla_1
            lista = self.lista1_pers
            lim_ac = 5
        elif l == 2:
            tupla = self.tupla_2
            lista = self.lista2_pers
            lim_ac = 6
        else:
            tupla = self.tupla_3
            lista = self.lista3_pers
            lim_ac = 7

        if self.buscar_perseveraciones(p,l):
            self.perseveraciones[l-1] += 1
            print("Perseveración")
        else:
            if o <= lim_ac:
                if tupla[o-1] == p:
                    self.aciertos[l-1] += 1
                    lista[tupla.index(p)] = p
                    self.palabra_anterior = p
                    print("Acierto")
                else:
                    if self.palabra_anterior != "":
                        if self.palabra_anterior > p:
                            lista[tupla.index(p)] = p
                            self.error_orden[l-1] += 1
                            self.palabra_anterior = p
                            print("Error de orden")
                        else:
                            lista[tupla.index(p)] = p
                            self.palabra_anterior = p
                    else:
                        lista[tupla.index(p)] = p
                        self.palabra_anterior = p
            else:
                if self.palabra_anterior > p:
                    lista[tupla.index(p)] = p 
                    self.error_orden[l-1] += 1
                    print("Error de orden")
                else:
                    lista[tupla.index(p)] = p
                    self.palabra_anterior = p

    # Método comprueba si la palabra dada la había dicho anteriormente en el ensayo
    def buscar_perseveraciones(self,p,l):
        cont = 0

        if l == 1:
            lista = self.lista1_pers
        elif l == 2:
            lista = self.lista2_pers
        else:
            lista = self.lista3_pers
        
        for x in lista:
            if p == x:

                cont += 1
        
        if cont >= 1:
            return True
        else:
            return False
    
    # Método comprueba si el ensayo fue correcto o incorrecto
    def comprobar_ensayo(self,l):
        self.num_ensayo[l-1] += 1
        self.palabra_anterior = ""
        
        if l == 1:
            if self.aciertos[l-1] == 5:
                self.estado = 0
                self.lista1_pers = [0,0,0,0,0]
                return 0
            else:
                self.estado = 1
                self.aciertos[l-1] = 0
                self.lista1_pers = [0,0,0,0,0]     
                if self.num_ensayo[0] == 5:
                    self.num_ensayo[0] = 0           
                return 1
        elif l == 2:
            if self.aciertos[l-1] == 6:
                self.estado = 0
                self.aciertos[l-1] = 0
                self.lista2_pers = [0,0,0,0,0,0]      
                return 0
            else:
                self.estado = 1
                self.aciertos[l-1] = 0
                self.lista2_pers = [0,0,0,0,0,0]   
                if self.num_ensayo[1] == 5:
                    self.num_ensayo[1] = 0                       
                return 1
        else:
            if self.aciertos[l-1] == 7:
                self.estado = 0
                self.aciertos[l-1] = 0
                self.lista3_pers = [0,0,0,0,0,0,0]                     
                return 0
            else:
                self.estado = 1
                self.aciertos[l-1] = 0
                self.lista3_pers = [0,0,0,0,0,0,0]   
                if self.num_ensayo[2] == 5:
                    self.num_ensayo[2] = 0                                      
                return 1

    # Método que limpia las variables usadas
    def limpiar_ordenamiento(self):
        self.num_ensayo = [0,0,0]
        self.error_orden = [0,0,0]       
        self.perseveraciones = [0,0,0]
        self.intrusiones = [0,0,0]

        self.palabras = ['','','','','','','','','','']

        self.lista1_pers = [0,0,0,0,0]
        self.lista2_pers = [0,0,0,0,0,0]
        self.lista3_pers = [0,0,0,0,0,0,0]

        self.aciertos = [0,0,0]
        self.estado = -1
        self.palabra_anterior = "";

        self.reiniciar = 0