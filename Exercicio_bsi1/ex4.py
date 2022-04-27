#aumentoSalarial - Recebe um salário e sua porcentagem de aumento, e retorna  o novo salário.

salario = float(input("Insira o seu salario: "))
aumento = float(input("Insira sua porcentagem de aumento: "))

salario_novo = (aumento*salario)/100
soma = salario + salario_novo

print(soma)