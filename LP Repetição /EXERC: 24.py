#Escreva um algoritmo que leia o preço em reais de 50 mercadorias e exiba-as com 5% de reajuste. Entretanto, se o reajuste exceder o teto de R$ 25.50 reais, retirar 2% do preço reajustado.

try:
  for _ in range(50):
    preco = float(input("Digite o preco da mercadoria: "))

    reajuste = preco * 0.05
    
    if(reajuste > 25.50):
      reajuste -= preco * 0.02

    novoPreco = preco + reajuste

    print(f"O preco da mercadoria: {novoPreco: .2f} R$")
  
except Exception as ERRO:
  print(f"Erro: {ERRO}")
