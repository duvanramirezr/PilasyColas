import random

class Estudiante:
    def __init__(self,nombre,codigo):
        self.nombre= nombre
        self.codigo=codigo
    
    
class Cola:
    def __init__(self):
        self.items=[]

    def encolar(self,dato):
        self.items.append(dato)

    def desencolar(self):
        return self.items.pop(0)

    def colaVacia(self):
        return self.items == []

        
def atenderParqueadero(cola):
    for i in range(random.randrange(10)):
        print cola.desencolar().nombre
    
            

col=Cola()
est=Estudiante("Alejandro","201363")
col.encolar(est)
est=Estudiante("Duvan","201362")
col.encolar(est)
est=Estudiante("Pedro","201345")
col.encolar(est)
est=Estudiante("Sandra","201317")
col.encolar(est)
est=Estudiante("Juan","201311")
col.encolar(est)
est=Estudiante("Jose","201329")
col.encolar(est)
est=Estudiante("Miguel","201399")
col.encolar(est)
est=Estudiante("Sara","201388")
col.encolar(est)
est=Estudiante("Ana","201301")
col.encolar(est)
est=Estudiante("Dario","201372")
col.encolar(est)



