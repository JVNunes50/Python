correntista = []
banco = []
extratoA = []

try:
  while True:
    print("Menu")
    print("Digite [1] para inserir correntista:")
    print("Digite [2] para exibir qual correntista teve maior movimentação:")
    print("Digite [3] para exibir a movimentação trimestral de um correntista:")
    print("Digite [4] para exibir relatório financeiro com a movimentação anual total:")
    print("Digite [5] para exibir o lucro para os acionistas")
    
    print("CLIQUE EM QUALQUER TECLA PARA SAIR!")
    opcao = int(input("OPÇÃO: "))

    if(opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5):
      print("FIM!")
      break
      
    elif(opcao == 1):
      nome = str(input("Digite o nome do correntista: ")) #0
      conta = int(input("Digite o numero da conta: ")) #1
      jan = float(input("Digite o valor do mes de Janeiro: ")) #2
      fev = float(input("Digite o valor do mes de Fevereiro: ")) #3
      mar = float(input("Digite o valor do mes de Março: ")) #4
      abr = float(input("Digite o valor do mes de Abril: ")) #5
      mai = float(input("Digite o valor do mes de Maio: ")) #6
      jun = float(input("Digite o valor do mes de Junho: ")) #7
      jul = float(input("Digite o valor do mes de Julho: ")) #8
      ago = float(input("Digite o valor do mes de Agosto: ")) #9
      set = float(input("Digite o valor do mes de Setembro: ")) #10
      out = float(input("Digite o valor do mes de Outubro: ")) #11
      nov = float(input("Digite o valor do mes de Novembro: ")) #12
      dez = float(input("Digite o valor do mes de Dezembro: ")) #13
    
      correntista = [nome, conta, jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez]
      banco.append(correntista)

    elif(opcao == 2):
      extratoA = [sum(correntista[2:]) for correntista in banco]
      maxE = extratoA.index(max(extratoA))

      mExtrato = extratoA[maxE]
      nome = banco[maxE][0]
      conta = banco[maxE][1]
      
      print(f"A maior movimentação anual é de {mExtrato: .2f}: de {nome} {conta}")

    elif (opcao == 3):
      pesquisa_conta = int(input("Digite o numero da conta: "))
      contas = [correntista[1] for correntista in banco]

      try:
        pesq_index = contas.index(pesquisa_conta)
        correntista = banco[pesq_index]

        T1 = sum(correntista[2:5])
        T2 = sum(correntista[5:8])
        T3 = sum(correntista[8:11])
        T4 = sum(correntista[11:14])

        print(f"NOME: {correntista[0]}")
        print(f"CONTA: {correntista[1]}")
        print(f"Valor trimestral:\n"
              f"Trimestre 1: {T1:.2f}\n"
              f"Trimestre 2: {T2:.2f}\n"
              f"Trimestre 3: {T3:.2f}\n"
              f"Trimestre 4: {T4:.2f}\n")
      except:
        print("Conta não encontrada!")
        
    elif(opcao == 4):
      total = [sum(correntista[2:]) for correntista in banco]
      totalA = sum(total)

      print(f"O Relatório Financeiro com a Movimentação Anual é: {totalA: .2f}")

    else:
      total = [sum(correntista[2:]) for correntista in banco]
      totalA = sum(total)
      lucro = totalA * 0.07

      print(f"O lucro para os acionistas é: {lucro: .2f}")
except Exception as ERRO:
  print(f"ERRO: {ERRO}")
