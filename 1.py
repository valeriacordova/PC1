#Problema 1
nombre = input("Ingresa tu nombre: ")
print(f'Hola {nombre}')

#Problema 2
consumo = float(input("Cuánto fue tu consumo: "))
porcentaje = float(input("Qué porcentaje de propina deseas dejar: "))
propina = consumo*porcentaje/100
print(f'Propina {propina}')

#Problema 3
peso_payaso = 112
peso_muneca = 75
cantidad_payasos = int(input("Ingrese la cantidad de payasos: "))
cantidad_munecas = int(input("Ingrese la cantidad de muñecas: "))
peso_total = peso_payaso*cantidad_payasos+peso_muneca*cantidad_munecas
print(f'El peso total es: {peso_total}')

#Problema 4
n = int(input("Ingrese un número entero: "))
suma = (n*(n+1))/2
print(f'La suma es: {suma}')

#CONDICIONALES
#Problema 5
cantidad = int(input("Cuántos shows has visto en el último año: "))
if cantidad>3:
    True
else: False

#Problema 6
edad = int(input("Ingrese su edad: "))
if edad<4 :
    entrada = 0
elif edad>= 4 and edad<=18:
    entrada = 5
elif edad>18:
    entrada = 10
else:
    print(f'El precio de la entrada es ${entrada}')

#Problema 7
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
print(f'Opciones:')
print(f'1) Suma de los números: ')
print(f'2) Resta de los números: ')
print(f'3) Produto de los números: ')

alternativa = int(input("Seleccione la opcion: "))
if alternativa==1:
    resultado = numero1+numero2
elif alternativa==2:
    resultado = numero1-numero2
elif: alternativa==3:
    resultado=numero1*numero2
else:
    print("La opción es inválida")

print(f'El resultado es {resultado}')

#Problema 8
#Problema 9
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = lista_original[::-1]
print(lista_invertida)
#Problema 10
#Problema 11
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = list(set(lista_original))
lista_procesada
#Problema 12

