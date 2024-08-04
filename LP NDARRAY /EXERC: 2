import numpy as np
dataset2 = np.load("C:/Users/João Vitor/Desktop/Python/datasets/dataset2.npy")

try:
  print("Lista dos entrevistados: ")
  for indice, entrevistados in enumerate(dataset2):
    print(f"Nº {indice + 1}:")
    print(f"Codigo: {entrevistados[0]}")
    print(f"Massa: {entrevistados[1]: .2f} QUILOGRAMAS")
    print(f"Altura: {entrevistados[2]: .2f} METROS")
    print(f"CLASSIFICAÇÃO: {entrevistados[3]}")

    dataset2[:,4] = dataset2[:,1] / (dataset2[:,2] ** 2)
    print(f"IMC: {entrevistados[4]: .1f}")
    print("==================================================================\n")

  altura = dataset2[:,2]

  alturaDec = np.sort(altura)[::-1]
  topEntre = alturaDec[:200]
  media = np.mean(topEntre)

  print("=============================== Altura média dos 200 entrevistados mais altos ===============================")
  print(f"A altura média dos 200 entrevistados mais altos é {media: .2f} metros")
  print("=============================================================================================================\n")

  classif = dataset2[:,3]

  NumSedentarios = np.sum(classif)
  NumNSedentarios = len(classif) - NumSedentarios

  totalEntrevistados = len(classif)

  sedentarios = (NumSedentarios / totalEntrevistados) * 100
  nSedentarios = (NumNSedentarios / totalEntrevistados) * 100

  print("=========================== Sedentários e não sedentários =================================")
  print(f"Número de entrevistados sedentários: {NumSedentarios}")
  print(f"Número de entrevistados não sedentários: {NumNSedentarios}")
  print(f"Percentual de entrevistados sedentários: {sedentarios: .2f}%")
  print(f"Percentual de entrevistados não sedentários: {nSedentarios: .2f}%")
  print("===========================================================================================\n")

  imc = dataset2[:, 4]
  imcSaudaveis = (imc >= 18.5) & (imc <= 25)

  numSaudaveis = np.sum(imcSaudaveis)
  totalEntrevistados = len(imc)

  saudaveis = (numSaudaveis / totalEntrevistados) * 100

  print("========================================== IMC ============================================")
  print(f"Número absoluto de entrevistados saudáveis (IMC entre 18.5 e 25.0): {numSaudaveis}")
  print(f"Percentual de entrevistados saudáveis (IMC entre 18.5 e 25.0): {saudaveis: .2f}%")
  print("===========================================================================================\n")

  classif = dataset2[:, 3]
  imc = dataset2[:, 4]

  classifNSeden = classif == 0
  classifSeden = classif == 1

  medNSeden = np.mean(classifNSeden)
  medSeden = np.mean(classifSeden)

  print("================= Média do IMC entre os sedentários e não sedentários =====================")
  print(f"A média do IMC entre os entrevistados sedentários é {medSeden: .2f}")
  print(f"A média do IMC entre os entrevistados não sedentários é {medNSeden: .2f}")
  print("===========================================================================================\n")

  classif = dataset2[:, 3]
  imc = dataset2[:, 4]

  imcNSaudaveis = (imc < 18.5) | (imc > 25)

  imcPior = np.where(imc)
  imcDec = np.argsort (imc)[::-1]
  topImc = imcDec[:100]

  print("=================== 100 entrevistados com os piores índices de IMC ========================\n")
  print(f'Os códigos (índices) dos 100 entrevistados com os piores índices de IMC são:\n{topImc}')
  print("===========================================================================================\n")

except Exception as ERRO:
    print(f"ERRO: {ERRO}")
