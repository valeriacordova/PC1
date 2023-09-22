edad = int(input("Ingrese su edad: "))
if edad < 4 :
    entrada = 0
elif edad>= 4 and edad<=18:
    entrada = 5
elif edad>18:
    entrada = 10
else:
    print(f'El precio de la entrada es {entrada:,}')