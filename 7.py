#Problema 7
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

