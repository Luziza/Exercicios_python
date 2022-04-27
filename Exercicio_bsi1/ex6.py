#diasParaSegundos - Recebe uma data em dias com horas, minutos e segundos, e retorna a data em segundos.

dias = int(input("Insira os dias:"))
horas = float(input("Insira as horas:"))
minutos = float(input("Insira os minutos:"))
segundos = float(input("Insira os segundos:"))

dias_segundos = dias * 86400
horas_segundos = (horas * 60)* 60
minutos_segundos = minutos * 60

print(dias_segundos + horas_segundos + minutos_segundos + segundos)