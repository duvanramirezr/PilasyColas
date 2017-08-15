class Pila:
    def __init__(self):
        self.items=[]

    def apilar(self,dato):
        self.items.append(dato)

    def desapilar(self):
        return self.items.pop()

    def pilaVacia(self):
        return self.items == []


class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der

def evaluar(arbol):
    if arbol.valor=="+":
        return evaluar(arbol.izq)+evaluar(arbol.der)
    if arbol.valor=="-":
        return evaluar(arbol.izq)-evaluar(arbol.der)
    if arbol.valor=="*":
        return evaluar(arbol.izq)*evaluar(arbol.der)
    if arbol.valor=="/":
        return evaluar(arbol.izq)/ evaluar(arbol.der)
    return int(arbol.valor)


def armarArbol(pila):
    auxPila=Pila()
    izq, der, valor
    while not len (pila):
        valor=pila.pop(0)
        if valor in "+-*/":
            der= auxPila.desapilar()
            izq=auxPila.desapilar()
            else:
                auxPila.apilar(Nodo(valor))
                
            
        
  
posord= raw_input("ingrese la cadena")
posord ="5 2 2 * - 10 2 / +"
pilaCad=posord.split(" ")
otraPila=Pila()


               
