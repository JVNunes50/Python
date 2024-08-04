'''
Escreva um algoritmo que leia de 10.000 habitantes de uma pequena cidade se está empregado ou não e exiba em porcentagem a quantidade de empregados e desempregados desta pequena cidade.
'''
POP = 0
SIM = 0
NAO = 0
try:
  for _ in range(10000):
    
    print("MENU")
    print("Você está empregado?")
    
    while True:
      RESPOSTA = int(input("Digite [1] para SIM ou [0] para NÃO: "))
      if RESPOSTA in (1 , 0):
        break
      else:
        print('ERRO: Dados de entrada. Escolha de novo.')
        
    if(RESPOSTA == 1):
      SIM += 1
    else:
      NAO += 1
    POP += 1
  
  print(f"Porcentagem de empregados {SIM / POP * 100: .1f}%")
  print(f"Porcentagem de desempregados {NAO / POP * 100: .1f}%")
  
except Exception as ERRO:
  print(f"Erro: {ERRO}")
