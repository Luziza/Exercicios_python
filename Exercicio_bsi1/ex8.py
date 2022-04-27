#fahrenheitParaCelsius - Recebe uma temperatura em graus Fahrenheit, e retorna a 
# temperatura em graus Celsius.

fahrenheit = float(input("Insira uma temperatura em Fahrenheit: "))

celcius = ((fahrenheit - 32) / 9) * 5

print(celcius)