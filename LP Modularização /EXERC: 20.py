'''
Faça uma função em Python que calcule o contracheque de um funcionário. Essa função receberá como
parâmetros:
● Salário Bruto (R$)
● Número de Dependentes: Esposa + Filhos;
E, retornará da função:
● Salário Líquido (R$)
● Total de Descontos (R$)
Conforme as regras a seguir:
DESCONTOS:
● INSS: 11% do Salário Bruto;
● Plano de Saúde: 2% do Salário Bruto;
BENEFÍCIOS:
● Vale Alimentação: R: Salário Mínimo + 5% do Salário Bruto por dependente.
'''

def salario(salB, numD):

  salM = 1412
  
  INSS = salB * 0.11
  PS = salB * 0.02
  VA = salM + (0.05 * salB * numD)

  totalD = INSS + PS

  salL = salB - (INSS + PS)

  return totalD, salL, VA

#CÉLULA (main)
try:
  salB = float(input("Digite o seu Salário Bruto (R$): "))
  numD = int(input("Digite o número de dependentes: Esposa + Filhos: "))
  
  totalD, salL, VA = salario(salB, numD)
  
  print(f"Seu salario liquido é: {salL} R$")
  print(f"Seu total de desconto é: {totalD} R$")
  
  print("BENEFÍCIOS:")
  print(f"Seu vale alimentação é: {VA} R$")

except Exception as ERRO:
  print(f"Erro: {ERRO}")
