#Programa para resolver tablas de verdad.

nLetras = 0

while nLetras < 1 or nLetras > 3:
    nLetras = int(input("Cantidad de letras: "))
    if nLetras < 1 or nLetras > 3:
        print("Cantidad de letras invalidas, ingrese un número entre 1 y 3")

nReglones = 2 ** nLetras

p = []
q = []
r = []

#Lista P
for i in range(int(nReglones / 2)):
    p.append('V')
    p.append('F')

#Lista Q
for i in range(int(nReglones / 4)):
    q.append('V')
    q.append('V')
    q.append('F')
    q.append('F')

#Lista R
for i in range(int(nReglones / 8)):
    r.append('V')
    r.append('V')
    r.append('V')
    r.append('V')
    r.append('F')
    r.append('F')
    r.append('F')
    r.append('F')

def listaVertical(lista):
    for item_lista in zip(lista):
        print(item_lista)

#Opone el valor de verdad
def negacion(lista):

    lista_resultado = []
    for i in range(len(lista)):

        if lista[i] == 'V':
            lista_resultado.append('F')
        else:
            lista_resultado.append('V')

    return(lista_resultado)

#Verdadera en el caso V-V
def conjuncion(lista1, lista2):

    lista_resultado = []
    for i in range(len(lista1)):    
        if lista1[i] == 'V' and lista2[i] == 'V':
            lista_resultado.append('V')
        else:
            lista_resultado.append('F')

    return lista_resultado

#Verdadera menos en el caso F-F
def disyuncion_in(lista1, lista2):

    lista_resultado = []
    for i in range(len(lista1)):    
        if lista1[i] == 'F' and lista2[i] == 'F':
            lista_resultado.append('F')
        else:
            lista_resultado.append('V')

    return lista_resultado

#Verdadera cuando son distintas
def disyuncion_ex(lista1, lista2):

    lista_resultado = []
    for i in range(len(lista1)):    
        if lista1[i] != lista2[i]:
            lista_resultado.append('V')
        else:
            lista_resultado.append('F')

    return lista_resultado

#Verdadera menos en el caso V-F
def condicional(lista1, lista2):

    lista_resultado = []
    for i in range(len(lista1)):    
        if lista1[i] == 'V' and lista2[i] == 'F':
            lista_resultado.append('F')
        else:
            lista_resultado.append('V')

    return lista_resultado

#Verdadera cuando son iguales
def bicondicional(lista1, lista2):

    lista_resultado = []
    for i in range(len(lista1)):    
        if lista1[i] == lista2[i]:
            lista_resultado.append('V')
        else:
            lista_resultado.append('F')

    return lista_resultado

#Relaciones Logicas
def relaciones_logicas(lista1, lista2):

    #Implicación
    implicacion = 0
    for i in range(len(lista1)):
        if lista1[i] == 'V' and lista2[i] != 'F':
            implicacion += 1
        
    if implicacion == len(lista1):
        print("La lista 1 implica a la lista 2.")

    #Equivalencia
    equivalencia = 0
    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            equivalencia += 1
        
    if equivalencia == len(lista1):
        print("La lista 1 es equivalente a la lista 2.")

    #Contrariedad
    contrariedad = 0
    for i in range(len(lista1)):
        if lista1[i] == 'V' and lista2[i] != 'V':
            contrariedad += 1
        
    if contrariedad == len(lista1):
        print("La lista 1 es contraria a la lista 2.")

    #Subcontrariedad
    subcontrariedad = 0
    for i in range(len(lista1)):
        if lista1[i] == 'F' and lista2[i] != 'F':
            subcontrariedad += 1
        
    if subcontrariedad == len(lista1):
        print("La lista 1 es subcontraria a la lista 2.")

    #Contradictoriedad
    contradictoriedad = 0
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            contradictoriedad += 1
        
    if contradictoriedad == len(lista1):
        print("La lista 1 es contradictoria a la lista 2.")

relaciones_logicas(p, p)