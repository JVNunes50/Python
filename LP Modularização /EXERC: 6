#Crie uma função que calcule o IMC (Índice de Massa Corpórea) de uma pessoa com base na sua idade, massa e sexo conforme tabela. 
Na célula do programa principal, use a função e exiba o IMC de 100 entrevistados (um por um).

def IMC(sexo, massa, altura):

  resultado = 0

  if(sexo == 1):
    IMCF = (0.95 * massa) / (altura ** 2)
    resultado = IMCF
  else:
    IMCM = (1.05 * massa) / (altura ** 2)
    resultado = IMCM
  
  return resultado

try:
  for _ in range(100):
    
    while True:
      sexo = int(input("Digite para (1) Feminino ou (2) Masculino: "))
      if(sexo not in (1, 2)):
        print("Opcao invalida!")
        continue
      break
      
    while True:
      massa = float(input("Digite sua massa em KG: "))
      if(massa <= 0):
        print("Dados invalidos!")
        continue
      break
      
    while True:
      altura = float(input("Digite sua altura em METROS: "))
      if(altura <= 0):
        print("Dados invalidos!")
        continue
      break
        
    resultado = IMC(sexo, massa, altura)

    print(f"Seu IMC: {resultado: .2f}")    
  
except Exception as ERRO:
  print(f"Erro: {ERRO}")
