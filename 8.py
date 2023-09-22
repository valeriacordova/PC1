hora_ingresada = input("Ingrese la hora: ")

hora,minutos = hora_ingresada.split(":")
if (hora == 7 and minutos >= 0 and minutos <= 59) or (hora == 8 and minutos == 0):
    print("Es hora de desayunar.")
elif (hora == 12 and minutos >= 0 and minutos <= 59) or (hora == 13 and minutos == 0):
    print("Es hora de almorzar.")
elif (hora == 18 and minutos >= 0 and minutos <= 59) or (hora == 19 and minutos == 0):
    print("Es hora de cenar.")