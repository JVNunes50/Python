#Escrever um algoritmo que leia vários números reais (um por um) e exiba, em porcentagem, a quantidade de positivos e de negativos lidos. Pare o programa quando o usuário digitar ZERO.

POS = 0
NEG = 0

try:
  while True:
    NUM = int(input("Digite um numero positivo ou negativo ou digite [0] para encerrar o programa: "))
    if(NUM == 0):
      break
    elif(NUM > 0):
      POS += 1
    else:
      NEG += 1
    TNUM = POS + NEG
    
  print(f"Numeros positivos digitados: {POS / TNUM * 100}%")
  print(f"Numeros negativos digitados: {NEG / TNUM * 100}%")
  
except Exception as ERRO:
  print(f"Erro: {ERRO}")
