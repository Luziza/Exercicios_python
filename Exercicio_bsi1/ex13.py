#salarioLiquido - Recebe quanto ganha por hora e quantas horas trabalho ao mês, e retorna o salário líquido.
#    Descontos:
#    - INSS é 8% do salário bruto
#    - IR é 11% do salário bruto
#    - Sindicato é 5% do salário bruto.


salario_hora = float(input("Insira o salário recebido por hora: "))
horas = float(input("Insira quantas horas trabalha: "))

salario = (salario_hora * horas) * 30

inss = (salario * 8) / 100
ir = (salario * 11) / 100
sindicato = (salario * 5) / 100

salario_liquido = salario - (inss + ir + sindicato)

print(salario_liquido)