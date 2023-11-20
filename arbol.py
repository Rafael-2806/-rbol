class Cola:
    def __init__(self):
        self.lista = []
    
    def vacia(self):
        return len(self.lista) == 0
    
    def poner(self,elemento):
        self.lista.append(elemento)

    def quitar(self):
        return self.lista.pop(0)


    
    

class Arbol(object):
    """Clase nodo árbol."""
    
    def __init__(self, info, iz=None, de=None):
        """Crea un nodo con la información cargada."""
        self.izq = iz
        self.der = de
        self.info = info
    def insertar_nodo(raiz, dato, compara=None):
        """Inserta un dato al árbol."""
        if compara==None:
            if raiz is None:
                raiz = Arbol(dato)
            elif dato < raiz.info:
                raiz.izq = Arbol.insertar_nodo(raiz.izq, dato)
            elif dato >= raiz.info:
                raiz.der = Arbol.insertar_nodo(raiz.der, dato)
        else:
            if raiz is None:
                raiz = Arbol(dato)
            elif compara(dato, raiz.info)<0: # #negativo es menor  q la raiz y lo inserto en el arbol izquierda 
                raiz.izq = Arbol.insertar_nodo(raiz.izq, dato, compara)
            elif compara(dato,raiz.info)>=0: #positivo es mayor o igual q la raiz y lo inserto en el arbol derecho
                raiz.der = Arbol.insertar_nodo(raiz.der, dato, compara)
        return raiz
    def arbol_vacio(raiz):
        """Devuelve true si el árbol está vacío."""
        return raiz is None

    def reemplazar(raiz):
        """Determina el nodo que reemplazará al que se elimina."""
        aux = None
        if raiz.der is None:
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = Arbol.reemplazar(raiz.der)
        return raiz, aux

    def eliminar_nodo(raiz, clave, compara=None):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        x = None
        if compara==None:
            if raiz is not None:
                if clave < raiz.info:
                    raiz.izq, x = Arbol.eliminar_nodo(raiz.izq, clave)
                elif clave > raiz.info:
                    raiz.der, x = Arbol.eliminar_nodo(raiz.der, clave)
                else:
                    x = raiz.info
                    if raiz.izq is None:
                        raiz = raiz.der
                    elif raiz.der is None:
                        raiz = raiz.izq
                    else:
                        raiz.izq, aux = Arbol.reemplazar(raiz.izq)
                        raiz.info = aux.info
        else:
            if raiz is not None:
                if compara(clave, raiz.info)<0:
                    raiz.izq, x = Arbol.eliminar_nodo(raiz.izq, clave, compara)
                elif compara(clave, raiz.info)>0:
                    raiz.der, x = Arbol.eliminar_nodo(raiz.der, clave, compara)
                else:
                    x = raiz.info
                    if raiz.izq is None:
                        raiz = raiz.der
                    elif raiz.der is None:
                        raiz = raiz.izq
                    else:
                        raiz.izq, aux = Arbol.reemplazar(raiz.izq)
                        raiz.info = aux.info
        return raiz, x
    
    def buscar(raiz, clave,compara=None):
        """Devuelve la dirección del elemento buscado."""
        pos = None
        if compara==None:
            if raiz is not None:
                if raiz.info == clave:
                    pos = raiz
                elif clave < raiz.info:
                    pos = Arbol.buscar(raiz.izq, clave)
                else:
                    pos = Arbol.buscar(raiz.der, clave)
        else:
            if raiz is not None:
                if compara(raiz.info,clave)==0:
                    pos = raiz
                elif compara(clave, raiz.info)<1:
                    pos = Arbol.buscar(raiz.izq, clave, compara)
                else:
                    pos = Arbol.buscar(raiz.der, clave, compara)
        return pos

    def por_nivel(raiz):
        """Realiza el barrido por nivel del árbol."""
        pendientes = Cola()
        pendientes.poner(raiz)
        while not pendientes.vacia():
            nodo = pendientes.quitar()
            print(nodo.info)
            if nodo.izq is not None:
                pendientes.poner(nodo.izq)
            if nodo.der is not None:
                pendientes.poner(nodo.der)
    def inorden(raiz):
        """Realiza el barrido inorden del árbol."""
        if raiz is not None:
            Arbol.inorden(raiz.izq)
            print(raiz.info)
            Arbol.inorden(raiz.der)

    def preorden(raiz):
        """Realiza el barrido preorden del árbol."""
        if raiz is not None:
            print(raiz.info)
            Arbol.preorden(raiz.izq)
            Arbol.preorden(raiz.der)

    def postorden(raiz):
        """Realiza el barrido postorden del árbol."""
        if raiz is not None:
            Arbol.postorden(raiz.izq)
            Arbol.postorden(raiz.der)
            print(raiz.info)
            
    def pintar(arbol, nivel=0):
        if not Arbol.arbol_vacio(arbol):
            Arbol.pintar(arbol.der,nivel + 1)
            print(" "*nivel*5,arbol.info)
            Arbol.pintar(arbol.izq, nivel+1)   
    
    def generar(lista,comparador):
        a= None
        for i in lista:
            a=Arbol.insertar_nodo(a,i,comparador)

        return a
    
    def filtrar(arbol,filtro):
        """Realiza el barrido inorden del árbol."""
        if arbol is not None:
            Arbol.inorden(arbol.izq,filtro)
            if filtro(arbol.info):
                print(arbol.info)
            Arbol.inorden(arbol.der,filtro        