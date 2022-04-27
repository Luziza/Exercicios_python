#tempoDistancia - Recebe uma distância e a velocidade de movimentação, 
# e retorna as horas que seriam gastas para percorrer em linha reta.

distancia = float(input("Insira uma distancia: "))
velocidade = float(input("Insira uma velocidade: "))

tempo = distancia/velocidade

print(tempo)