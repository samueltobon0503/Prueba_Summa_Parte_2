'''1. Dada un arreglo de enteros, devuelva los índices de los dos números de modo que se
sume un número específico.
Nota: Asuma que en cada entrada se tendrá exactamente una solución, y no puede usar el
mismo elemento dos veces.

Ejemplo:
Números = [2, 7, 11, 15]
Suma objetivo = 9
retorna [0, 1]'''

#Solucion a punto 1 parte 2

#Definicion de entradas
'''lista = [6,2,1,6,5,8]
objetivo = 9

# Funcion con 2 ciclos for para hacer las combinaciones posibles de sumas para el resultado esperado
#Recide una lista y el objetivo de suma
#Se toma la longitud de la lista para realizar correctamente el ciclo
def suma(lista, objetivo):
    for i in range(len(lista)):
        # Comenzar desde i + 1 en el segundo ciclo para evitar combinaciones repetidas y auto-sumas
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                return [i, j]

#Se llama la funcion y se pasan los 2 argumentos
r = suma(lista,objetivo)
print(r)'''

'''Un sistema de información cuenta con tres agentes (A, B y C) cada agente cumple con dos
funcionalidades:
Funcionalidad 1: Obtener media
- Definir la función getMedia(Lista de números reales)  valor de retorno: número
real
- Agente A: Obtener la media aritmética o promedio
- Agente B: Obtener media armónica

- Agente C: Obtener mediana
Si la cantidad de datos es impar, la mediana es el valor que queda en la mitad al
ordenar los datos de menor a mayor.
Si la cantidad de datos es par, la mediana es el promedio de los dos valores que
quedan al centro al ordenar los datos de menor a mayor.'''

#Definicion de entradas
'''agentes = [36, 45, 71]

#Funcion para sacar la media de los agentes A, B, C la cual recibe una lista
def getMedia(lista):
    #Se opera con la suma de los valores para un posterior retorno de la media
    suma = sum(lista)
    return suma/len(lista)

# Se llama la funcion y se le pasa el argumento de la lista de los agentes

print(f'La media es: {getMedia(agentes)}')

#Funcion para sacar la media armonica de los agentes A, B, C la cual recibe una lista
def getMediaArmonica (lista):
    # Se opera con la division por 1 y suma de los valores para un posterior retorno de la media armonica
    n = len(lista)
    divididos = []
    for i in lista:
        aux = 1/i
        divididos.append(aux)
    suma= sum(divididos)
    return n/suma

# Se llama la funcion y se le pasa el argumento de la lista de los agentes
print(f'La media armonica es: {getMediaArmonica(agentes)}')

#Se crea la funcion para sacar la mediana
def getMediana(lista):
    lista.sort()
    n = len(lista)
#Determinar si es par o no para sacar la sea la mediana unica o con dos datos
    if n % 2 != 0:
        n = n//2
        int(n)
        mediana = lista[n]
    elif n % 2 == 0:
        n = n // 2
        m1 = n
        m2 = n - 1
        mediana = [m1,m2]
    return mediana

# Se llama la funcion y se le pasa el argumento de la lista de los agentes
print(f'La mediana es: {getMediana(agentes)}')'''

'''Funcionalidad 2: Escalera
- Definir función getStaircase(número entero)  valor de retorno: cadena de texto
- Agente A:
La base y altura son ambas iguales a n. Se dibuja usando el símbolo # símbolos y
espacios. La última línea no va precedida de ningún espacio. Escriba un programa
que imprima una escalera de tamaño n. Formato de entrada: Un único entero, n,
que denota el tamaño de la escalera.
Restricciones: 0 &lt; n &lt; 100. La escalera debe estar alineada a la derecha.'''

'''escalones = 4
def getStairCase(num):
    new = ""
    cadena = ""
    for i in range(num) :
        new = new +"#"
        cadena = cadena + new + '\n'
    return cadena

#Condicion numerica y llamar la funcion
if 0 < escalones < 100:
    staircase = getStairCase(escalones)
    print(staircase)
else:
    print("El tamaño de la escalera debe estar dentro del rango permitido.")'''

'''- Agente B:
La cima y altura son ambas iguales a n. Se dibuja usando el símbolo # símbolos y
espacios. La primera línea no va precedida de ningún espacio. Escriba un programa
que imprima una escalera de tamaño n. Formato de entrada: Un único entero, n,
que denota el tamaño de la escalera.
Restricciones: 0 &lt; n &lt; 100. La escalera debe estar alineada a la derecha.'''


'''#Crear la funcion para imprimir la escalera de numerales
def getStairCase2(num):
    cadena = ""
    #Ciclo for para imprimir la cadena invertida
    for i in range(num, 0, -1):
        new = "#" * i
        cadena += new + '\n'
    return cadena
#Condicion numerica y llamar la funcion
if 0 < escalones < 100:
    staircase = getStairCase2(escalones)
    print(staircase)
else:
    print("El tamaño de la escalera debe estar dentro del rango permitido.")'''