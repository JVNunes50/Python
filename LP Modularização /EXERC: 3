#Criar duas funções e seus protótipos que calculam a Combinação e o Arranjo de n elementos combinados p a p. Após isso, na célula do programa principal, 
use as funções criadas várias vezes e exiba o resultado da Combinação e do Arranjo enquanto os valores lidos do usuário: n e p estiverem corretos. Sabe-se que:

def combinacao(n, p):
  if 0 <= p <= n:
    return fatorial(n) / (fatorial(p) * fatorial(n - p))
  else:
    return "'p' e 'n' devem ser >= '0' e 'n' deve ser >= 'p'"

def arranjo(n, p):
  if 0 <= p <= n:
    return fatorial(n) / fatorial(n - p)
  else:
    return "'p' e 'n' devem ser >= '0' e 'n' deve ser >= 'p'"

def fatorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * fatorial(num - 1)

#CÉLULA (main)
try:
  n = int(input("Digite o valor de n: "))
  p = int(input("Digite o valor de p: "))
  
  print(f"Combinação de {n} elementos tomados {p} a {p}: {combinacao(n, p)}")
  print(f"Arranjo de {n} elementos tomados {p} a {p}: {arranjo(n, p)}")
  
except Exception as ERRO:
  print(f"Erro: {ERRO}")
