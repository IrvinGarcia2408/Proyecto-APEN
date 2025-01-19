class Prueba_11:
    # Variables usadas en BANFE-2
    aciertos = 0

    # Listas auxiliares para evaluar los resultados
    fin = 0
    punto = ['a','c','b','a',['a','b']]
    medio_punto = ['b','','a','b','c']

    # respuestas por refran
    puntos_ganados = [0,0,0,0,0]

    def evaluar_respuesta(self, refran, opcion):
        return self.anotar_aciertos(refran,opcion)

    def anotar_aciertos(self, r, o):
        if r != 5:
            if o == self.punto[r-1]:
                self.evaluar_existencia(r)
                self.aciertos += 1
                self.puntos_ganados[r-1] = 1 
                print(f"Ganamos 1: {self.puntos_ganados[r-1]}")
            elif o == self.medio_punto[r-1]:
                self.evaluar_existencia(r)
                self.aciertos += 0.5
                self.puntos_ganados[r-1] = 0.5
                print(f"Ganamos 2: {self.puntos_ganados[r-1]}")
            else:
                self.aciertos -= self.puntos_ganados[r-1]
                self.puntos_ganados[r-1] = 0
                print(f"Ganamos 3: {self.puntos_ganados[r-1]}")
        else:
            if o == self.punto[r-1][0] or o == self.punto[r-1][1]:
                self.evaluar_existencia(r)
                self.aciertos += 1
                self.puntos_ganados[r-1] = 1 
                print(f"Ganamos 1: {self.puntos_ganados[r-1]}")
            elif o == self.medio_punto[r-1]:
                self.evaluar_existencia(r)
                self.aciertos += 0.5    
                self.puntos_ganados[r-1] = 0.5
                print(f"Ganamos 2: {self.puntos_ganados[r-1]}")
        
    
    def evaluar_existencia(self, r):
        if self.puntos_ganados[r-1] != 0:
            self.aciertos -= self.puntos_ganados[r-1]

    def limpiar_refranes(self):
        self.aciertos = 0
        self.fin = 0
        
        for x in range(len(self.puntos_ganados)):
            self.puntos_ganados[x] = 0