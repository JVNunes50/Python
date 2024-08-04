import numpy as np
dataset5 = np.load("C:/Users/João Vitor/Desktop/Python/datasets/dataset5.npy")

try:
  print("Lista de atletas:")
  for indice, atleta in enumerate(dataset5[:1000]):
    print(f"Nº {indice + 1}")
    print(f"Matrículas: {atleta[0]}")
    print(f"Natação: {atleta[1]}")
    print(f"Corrida: {atleta[2]}")
    print(f"Ciclismo: {atleta[3]}")
    print("==================================================================\n")

  natacao = dataset5[:1000, 1]
  corrida = dataset5[:1000, 2]
  ciclismo = dataset5[:1000, 3]

  mediaNat = np.mean(natacao)
  mediaCor = np.mean(corrida)
  mediaCic = np.mean(ciclismo)

  mediaGer = np.mean([mediaNat, mediaCor, mediaCic])
  print("============ Média de Tempo por Modalidade e Geral ===============")
  print(f"A Média de Tempo da Natação é {mediaNat: .1f}")
  print(f"A Média de Tempo da Corrida é {mediaCor: .1f}")
  print(f"A Média de Tempo do Ciclismo é {mediaCic: .1f}")
  print(f"A Média de Tempo Geral é {mediaGer: .1f}")
  print("==================================================================\n")

  vencedorNat = np.argmin(natacao)
  lanternaNat = np.argmax(natacao)

  vencedorCor = np.argmin(corrida)
  lanternaCor = np.argmax(corrida)

  vencedorCic = np.argmin(ciclismo)
  lanternaCic = np.argmax(ciclismo)

  geral = (natacao + corrida + ciclismo) / 3

  vencedorGer = np.argmin(geral)
  lanternaGer = np.argmax(geral)

  print("========= Vencedor e do Lanterna por Modalidade e Geral ==========")
  print(f"Vencedor da Natação: {dataset5[vencedorNat, 0]}")
  print(f"Lanterna da Natação: {dataset5[lanternaNat, 0]}\n")

  print(f"Vencedor da Corrida: {dataset5[vencedorCor, 0]}")
  print(f"Lanterna da Corrida: {dataset5[lanternaCor, 0]}\n")

  print(f"Vencedor da Ciclismo: {dataset5[vencedorCic, 0]}")
  print(f"Lanterna da Ciclismo: {dataset5[lanternaCic, 0]}\n")

  print(f"Vencedor Geral: {dataset5[vencedorGer, 0]}")
  print(f"Lanterna Geral: {dataset5[lanternaGer, 0]}")
  print("==================================================================\n")

  abaxioMedNat = np.sum(natacao <= mediaNat)
  abaxioMedCor = np.sum(corrida <= mediaCor)
  abaxioMedCic = np.sum(ciclismo <= mediaCic)
  abaxioMedGer = np.sum(geral <= mediaGer)

  matricula = dataset5[:1000, 0]
  totalAtletas = len(matricula)

  perAbaxioMedNat = (abaxioMedNat / totalAtletas) * 100
  perAbaxioMedCor = (abaxioMedCor / totalAtletas) * 100
  perAbaxioMedCic = (abaxioMedCic / totalAtletas) * 100
  perabaxioMedGer = (abaxioMedGer / totalAtletas) * 100

  print("======= Atletas abaixo dos tempos médios por Modalidade e Geral ========")
  print(f"Natação {abaxioMedNat} atletas: {perAbaxioMedNat: .1f}%")
  print(f"Corrida {abaxioMedCor} atletas: {perAbaxioMedCor: .1f}%")
  print(f"Ciclismo {abaxioMedCic} atleats: {perAbaxioMedCic: .1f}%")
  print(f"Geral {abaxioMedGer} atleats: {perabaxioMedGer: .1f}%")
  print("========================================================================\n")

  topGer = (mediaNat + mediaCor + mediaCic) / 3

  mvp = np.argsort(topGer)[::-1]

  print("==================== Lista dos 5 melhores atletas ======================")
  for i in range(min(5, len(mvp))):
    indiceAtleta = mvp[i]
    atleta = dataset5[indiceAtleta]
    print(f"Matrícula: {atleta[0]}, Natação: {atleta[1]}, Corrida: {atleta[2]}, Ciclismo: {atleta[3]}")
  print("========================================================================\n")


  while True:
    MIN = np.min(dataset5[:1000, 0])
    MAX = np.max(dataset5[:1000, 0])
    matEsc = input(f"Digite a matrícula do atleta entre [{MIN:.0f}, {MAX:.0f}] ou 'sair' para encerrar: ")

    if matEsc.lower() == "sair":
      print("Encerrando o programa...")
      break
    elif int(matEsc) < MIN or int(matEsc) > MAX:
      print(f"ERRO: Digite uma matrícula entre [{MIN:.0f}, {MAX:.0f}]")
    else:

      for atleta in dataset5[:1000]:
        if str(atleta[0]) == matEsc:
          print("Dados do atleta:")
          print(f"Matrícula: {atleta[0]}")
          print(f"Natação: {atleta[1]}")
          print(f"Corrida: {atleta[2]}")
          print(f"Ciclismo: {atleta[3]}")
          break
      else:
        print(f"Atleta com matrícula {matEsc} não encontrado.")

except Exception as ERRO:
    print(f"Erro: {ERRO}")
