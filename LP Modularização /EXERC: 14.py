'''
Crie uma função e seu protótipo que receba a hora de entrada e saída de um estacionamento e retorne o tempo de permanência e total a pagar. Na célula do programa principal o usuário informa:
Hora de entrada (HH:MM): Exemplo: 13:37
Hora de saída (HH:MM): Exemplo: 18:41 (Menus)
-------------------------------------------------------------------------------
Diferença: (HH:MM): Exemplo: 04:64 → 5 Horas de permanência no estacionamento.

Preço: R$ 7.00 por hora.
'''
def estacionamento(horasEnt, horasSai, preco = 7):
  entrada = int(horasEnt[:2]) * 3600 + int(horasEnt[3:]) * 60
  saida = int(horasSai[:2]) * 3600 + int(horasSai[3:]) * 60

  temp = saida - entrada

  horas = temp // 3600
  min = (temp % 3600) // 60

  if(min > 59):
    horas += 1

  pagar = preco * horas

  diferenca_formatada = "{:02}:{:02}".format(horas, min)

  return diferenca_formatada, pagar


#CÉLULA (main)
try:
  horasEnt = (input("Horas de entrada HH:MM: "))
  horasSai = (input("Horas de entrada HH:MM: "))
  
  permanencia, pagamento = estacionamento(horasEnt, horasSai)
  
  print(f"Tempo permanecido: {permanencia}")
  print(f"Valor a pagar: {pagamento}R$")

except Exception as ERRO:
  print(f"Erro: {ERRO}")
