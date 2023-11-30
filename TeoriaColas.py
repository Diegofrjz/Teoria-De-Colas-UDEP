#1. Tipo de Llegada del Sistema
print("1. TIPOS DE LLEGADA DEL SISTEMA:")
Tipos_de_llegada = '''
M: Distribucion de Poisson/Distribuccion exponencial
D: Constante
G: Cualquiera
'''
print(Tipos_de_llegada)
Llegada = input("seleccione el tipo de llegada: ")

#2. Tipos de salida del sistema
print("2. TIPOS DE SALIDA DEL SISTEMA:")
Tipos_de_salida = '''
M: Distribucion de Poisson/Distribuccion exponencial
D: Constante
Ek: Distribucion de Erlang
G: Cualquiera
'''
print(Tipos_de_salida)
Salida = input("seleccione el tipo de salida: ")

#3. Cantidad de servidores en el sistema
print("3. CANTIDAD DE SERVIDORES EN EL SISTEMA:")
Tipos_de_servidores = '''
1: Un solo Servidor
s: Más de un servidor
infinitos: infinitos servidores
'''
print(Tipos_de_servidores)
Servidores = input("Seleccione la alternativa: ")

#4. Tipo de disciplina en el sistema
print("4. TIPO DE DISCIPLINA EN EL SISTEMA:")
Tipos_de_disciplina = '''
DG: Disciplina General
'''
print(Tipos_de_disciplina)
Disciplina = input("Ingrese el tipo de disciplina del concierto: ")

#5. Cantidad de clientes máxima en el sistema
print("5. CANTIDAD DE CLIENTES MAXIMA EN EL SISTEMA:")
Tipos_de_clientes = '''
M: limitado a M clientes en el sistema
M': una fraccion de clientes no entra por el tamaño de cola
s: limitado al numero de servidores
infinitos: Infinitos clientes en el sistema
'''
print(Tipos_de_clientes)
Linea = input("Ingrese la alternativa que se adecue: ")

#6. Cantidad máxima de poblacion
print("6. CANTIDAD MAXIMA DE POBLACION:")
Tipos_de_poblacion = '''
M: Finita poblacion
infinitos: Infinitoa poblacion
'''
print(Tipos_de_poblacion)
Poblacion = input("Ingrese el tamaño maximo de la poblacion: ")

ARRAY = [Llegada,Salida, Servidores, Disciplina, Linea, Poblacion]
print(ARRAY)
