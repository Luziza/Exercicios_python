#precoAluguelCarro - Recebe a quantidade de dias que o carro foi alugado e a quantidade de quilômetros rodados, 
#e retorna o valor a ser pago. 1 dia: 60 reais mais R$ 0,15 por km rodado.

dias = int(input("Insira os dias:"))
km_rodados = int(input("Insira os km:"))

valor = (dias * 60) + (km_rodados * 0.15)

print("R$", valor)