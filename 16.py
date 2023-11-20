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
            Arbol.filtrar(arbol.izq,filtro)
            if filtro(arbol.info):
                print(arbol.info)
            Arbol.filtrar(arbol.der,filtro)      

class Pokemon:
    
    def __init__(self,nombre, numero=0,tipos=[], debilidad=""):
        self.nombre=nombre
        self.numero=numero
        self.tipos=tipos
        self.debilidad=debilidad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Numero: {self.numero}, Tipos: {self.tipos}, debilidad: {self.debilidad}"
        
    def gana(poke1,poke2): #Si tipo de poke 1 es debilidad de poke 2 gana
        for i in poke1.tipos:
            if i == poke2.debilidad:
                return True #si algun tipo es la debilidad de poke 2
        return False #si el tipo no esta en la debilidad de poke 2
    

pokemons_info = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": ["Planta", "Veneno"], "debilidad": "Psíquico"},
    {"nombre": "Ivysaur", "numero": 2, "tipos": ["Planta", "Veneno"], "debilidad": "Psíquico"},
    {"nombre": "Venusaur", "numero": 3, "tipos": ["Planta", "Veneno"], "debilidad": "Psíquico"},
    {"nombre": "Charmander", "numero": 4, "tipos": ["Fuego"], "debilidad": "Agua"},
    {"nombre": "Charmeleon", "numero": 5, "tipos": ["Fuego"], "debilidad": "Agua"},
    {"nombre": "Charizard", "numero": 6, "tipos": ["Fuego", "Volador"], "debilidad": "Agua"},
    {"nombre": "Squirtle", "numero": 7, "tipos": ["Agua"], "debilidad": "Planta"},
    {"nombre": "Wartortle", "numero": 8, "tipos": ["Agua"], "debilidad": "Planta"},
    {"nombre": "Blastoise", "numero": 9, "tipos": ["Agua"], "debilidad": "Planta"},
    {"nombre": "Pikachu", "numero": 25, "tipos": ["Eléctrico"], "debilidad": "Tierra"},
    {"nombre": "Raichu", "numero": 26, "tipos": ["Eléctrico"], "debilidad": "Tierra"},
    {"nombre": "Jigglypuff", "numero": 39, "tipos": ["Normal", "Hada"], "debilidad": "Acero"},
    {"nombre": "Wigglytuff", "numero": 40, "tipos": ["Normal", "Hada"], "debilidad": "Acero"},
    {"nombre": "Psyduck", "numero": 54, "tipos": ["Agua"], "debilidad": "Planta"},
    {"nombre": "Golduck", "numero": 55, "tipos": ["Agua"], "debilidad": "Planta"},
    {"nombre": "Machop", "numero": 66, "tipos": ["Lucha"], "debilidad": "Psíquico"},
    {"nombre": "Machoke", "numero": 67, "tipos": ["Lucha"], "debilidad": "Psíquico"},
    {"nombre": "Machamp", "numero": 68, "tipos": ["Lucha"], "debilidad": "Psíquico"},
    {"nombre": "Gyarados", "numero": 130, "tipos": ["Agua", "Volador"], "debilidad": "Eléctrico"},
    {"nombre": "Vaporeon", "numero": 134, "tipos": ["Agua"], "debilidad": "Planta"},
    {"nombre": "Jolteon", "numero": 135, "tipos": ["Eléctrico"], "debilidad": "Tierra"},
    {"nombre": "Flareon", "numero": 136, "tipos": ["Fuego"], "debilidad": "Agua"},
    {"nombre": "Snorlax", "numero": 143, "tipos": ["Normal"], "debilidad": "Lucha"},
    {"nombre": "Dragonite", "numero": 149, "tipos": ["Dragón", "Volador"], "debilidad": "Hielo"},
    {"nombre": "Mewtwo", "numero": 150, "tipos": ["Psíquico"], "debilidad": "Siniestro"},
    {"nombre": "Mew", "numero": 151, "tipos": ["Psíquico"], "debilidad": "Siniestro"},
    {"nombre": "Tyranitar", "numero": 248, "tipos": ["Roca", "Siniestro"], "debilidad": "Lucha"},
    {"nombre": "Blaziken", "numero": 257, "tipos": ["Fuego", "Lucha"], "debilidad": "Agua"},
    {"nombre": "Gardevoir", "numero": 282, "tipos": ["Psíquico", "Hada"], "debilidad": "Acero"},
]
    
poke_lista=[]
    
for p in pokemons_info:
    poke_lista.append(Pokemon(p["nombre"],p["numero"],p["tipos"],p["debilidad"]))
    
#crea arbol por oden de nombre, tipo y numero
# comparadores por nombre y por color sable -1 si es mas pequeño 0 igual 1 mayor. lambda hace una funcion pero si poner nombre
comparaNombre=lambda x,y: -1 if x.nombre<y.nombre else 0 if x.nombre==y.nombre else 1
comparaNumero=lambda x,y: -1 if x.numero<y.numero else 0 if x.numero==y.numero else 1
comparaTipo=lambda x,y: -1 if x.tipos[0]<y.tipos[0] else 0 if x.tipos[0]==y.tipos[0] else 1  #sepone[0] por que es un diccionario

indice_nombre= Arbol.generar(poke_lista,comparaNombre)
indice_numero= Arbol.generar(poke_lista,comparaNumero)
indice_tipo= Arbol.generar(poke_lista,comparaTipo)
    
Arbol.pintar(indice_nombre)
#Buscar por nombre
nombre=input("nombre del pokemon ")
arbol_pokemon= Arbol.buscar(indice_nombre,Pokemon(nombre),comparaNombre)
print(arbol_pokemon)

if arbol_pokemon != None:
    pokemon=arbol_pokemon.info
    print(pokemon, "gana a: ")
    #me va a sacar todos los que gana el que busco
    Arbol.filtrar(indice_nombre, lambda x:Pokemon.gana(pokemon, x))
#busqueda por proximidad
nombre_filtrar=input("primeras leetras del nombre de pokemon")
Arbol.filtrar(indice_nombre, lambda x: x.nombre.startswith(nombre_filtrar)) # si el nombre del pokemon contiene las primeras letras 

