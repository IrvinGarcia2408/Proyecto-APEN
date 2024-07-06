# Creación de la clase Prueba
class Prueba_10:
    
    # Listas de cartas tomadas por cada punto
    cartas = [0,0,0,0,0]
    # Lista de castigos obtenidos por cada carta
    castigos = [0,0,0,0,0]

    cartas_puntos = 0
    cartas_castigos = 0

    total_puntos = 0
    total_castigos = 0

    puntuacion = 0
    porcentaje = 0

    terminar = 0
    

    def anotar_carta(self, carta, castigo):
        self.cartas[carta-1] += 1;
        self.cartas_puntos = self.cartas[0]+self.cartas[1]+self.cartas[2]+self.cartas[3]+self.cartas[4]

        self.total_puntos =  self.cartas[0] +  self.cartas[1] * 2 +  self.cartas[2] * 3 +  self.cartas[3] * 4 +  self.cartas[4] * 5
        
        if castigo != 0:
            self.castigos[carta-1] += 1; 
            self.cartas_castigos = self.castigos[0]+self.castigos[1]+self.castigos[2]+self.castigos[3]+self.castigos[4]
            self.total_castigos =  self.castigos[0] * 2 +  self.castigos[1] * 3 +  self.castigos[2] * 5 +  self.castigos[3] * 8 +  self.castigos[4] * 12

        self.puntuacion = self.total_puntos - self.total_castigos
        self.porcentaje = round(((self.cartas[3] + self.cartas[4])/ self.cartas_puntos) * 100, 1)
    
    def limpiar_cartas(self):
        self.cartas = [0,0,0,0,0]
        self.castigos = [0,0,0,0,0]

        self.cartas_puntos = 0
        self.cartas_castigos = 0

        self.total_puntos = 0
        self.total_castigos = 0

        self.puntuacion = 0
        self.porcentaje = 0

        self.terminar = 0

    # Método que ayuda a apagar la prueba
    def apagar(self, fin):
        if fin == 1:
            self.terminar = 1
        
        print(f'Apagar: {fin}')