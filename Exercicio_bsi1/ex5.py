#precoComDesconto - Recebe um preço e sua porcentagem de desconto, e retorna o novo preço.

preco = float(input("Insira o preço: "))
desconto = float(input("Insira sua porcentagem de desconto: "))

desconto = (desconto*preco)/100
preco_novo = preco - desconto

print(preco_novo)