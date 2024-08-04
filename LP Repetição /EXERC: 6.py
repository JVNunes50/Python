'''
Escreva um algoritmo que leia o salário em reais (R$) de 1000 clientes de um shopping e exiba na tela, em porcentagem, a divisão dos clientes por tipo: A, B ou C, conforme a seguir:
✓ A: Maior ou igual a 15 Salários Mínimos ou
✓ B: Menor que 15 Salários Mínimos ou maior ou igual a 5 Salários Mínimos ou
✓ C: Menor que 5 Salários Mínimos.
Declarar o Salário Mínimo (SM: R$ 998.05).
'''

salm = 998.05
Ta = 0
Tb = 0
Tc = 0

try:
  for _ in range(1000):
    while True:
      sal = float(input("Digite o seu salario: "))
      if(sal < salm):
        print("O salario esta menor que o salario minimo!")
      else:
        break
        
    if(sal >= salm * 15):
      Ta += 1
    elif(sal < salm * 15 and sal >= salm * 5):
      Tb += 1
    else:
      Tc += 1

  total = Ta + Tb + Tc

  print(f"Clientes tipo A: {(Ta / total) * 100:.2f}%")
  print(f"Clientes tipo B: {(Tb / total) * 100:.2f}%")
  print(f"Clientes tipo C: {(Tc / total) * 100:.2f}%")

except Exception as ERRO:
  print(f"Erro: {ERRO}")
