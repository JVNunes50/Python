#Escrever um algoritmo modularizado em Python que leia o preço de uma mercadoria e exiba o preço na tela o preço reajustado de X%. 
O usuário escolherá para reajuste, (1): Acréscimo ou (2): Desconto para o reajuste de X %. Na célula do programa principal, use a função várias vezes, criando um Menu para o usuário.

def mercadoria(preco, reajuste):
  ajuste = preco * reajuste / 100

  reajusteA = preco + ajuste
  reajusteD = preco - ajuste

  return reajusteA, reajusteD

#CÉLULA (main)
try:
  print("MENU")
  
  while True:
    
    reajusteT = int(input("Digite (0) Sair, (1) Acréscimo ou (2) Desconto: "))
    
    if(reajusteT == 0):
      print("Fim do programa!")
      break
    elif(reajusteT not in [0,1,2]):
      print("Opção invalida!")
    else:
      reajuste = float(input("Digite o reajuste em (%): "))
      preco = float(input("Digite o preco da mercadoria: "))
  
      novoPA, novoPD = mercadoria(preco, reajuste)
  
      if(reajusteT == 1):
        print(f"O reajsute foi de: {novoPA: .1f}")
      elif(reajusteT == 2):
        print(f"O reajsute foi de: {novoPD: .1f}")
  
except Exception as ERRO:
  print(f"Erro: {ERRO}")
