#diasPerdidosPorFumar - Recebe uma quantidade de cigarros fumados por dia e a quantidade de anos que fuma, 
# e retorna o total de dias perdidos, sabendo que cada cigarro reduz a vida em 10 minutos.

cigarros = int(input("Cigarros fumados por dia: "))
anos = int(input("Quantidade de anos que fumou: "))

cigarros_fumados = (anos * 365) * cigarros
minutos_perdidos = cigarros_fumados * 10
dias_perdidos = minutos_perdidos / 1440

print("Você perdeu", dias_perdidos, "dias")