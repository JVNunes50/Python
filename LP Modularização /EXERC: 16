'''
Faça um programa Python modularizado que:
(i) Tenha uma função que calcule e retorne a área de um círculo de raio R;
(ii) Tenha outra função que calcule e retorne o volume do cilindro reto.
A função de (ii) deve usar a função de (i).
O raio e a altura de um cilindro devem ser lidos do teclado na célula do programa principal.
Obs.: Área do círculo: A = π . r2
Volume do Cilindro: Área do Círculo da Base vezes a Altura.
'''

def areaC(raio):
  
  area = 3.14 * (raio ** 2)

  return area

def volumeC(altura, raio):
  
  area = areaC(raio)
  
  volume = area * altura

  return volume

try:
  raio = float(input("Digite o raio: "))
  altura = float(input("Digite a altura: "))

  volume = volumeC(altura, raio)
  area = areaC(raio)
  
  print(f"A área de um círculo: {area: .2f}")
  print(f"O volume do cilindro reto: {volume: .2f}")
  
except Exception as ERRO:
  print(f"Erro: {ERRO}")
