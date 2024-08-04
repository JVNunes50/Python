import numpy as np

QF = 100
salarioBrut = 0

funcionario = []
empresa = []

for _ in range(QF):
  
  while True:
    try:
      print('MENU')
      print('1: Inserir funcionário')
      print('2: Relatório da taxa de adesão ao Plano de Saúde.')
      print('3: Relatório com os nomes dos funcionários que possuem Plano de Saúde.')
      print('4: Relatório com os cargos dos funcionários que estão acima da média salarial.')
      print('5: Relatório administrativo com o Total da Folha de Pagamento.')
      print('[QUALQUER TECLA]: SAIR')
      opcao = int(input('OPÇÃO: '))
      
      if(opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5):
        break
        
      elif (opcao == 1):
        nome = str(input("digite o nome do funcionario: "))
        cargo = str(input("Digite o cargo: "))
        matricula = np.random.randint(1000, 10000, 1)[0]
        planoS = int(input("Digite o plano de saude (1) para SIM ou (0) para NÃO: "))
        salario = float(input("Digite o salario: "))
        
        funcionario = [nome,cargo, matricula, planoS, salario]
        empresa.append(funcionario)
        salarioBrut += salario
        
      elif(opcao == 2):
        listPlanoS = [funcionario[3] for funcionario in empresa if (funcionario[3] == 1)]
        PFA = sum(listPlanoS) / len(empresa) * 100
        print(f"A taxa de adesão do Plano de Saúde é de {PFA: .2f}%")
        
      elif(opcao == 3):
        listNomes = [funcionario[0] for funcionario in empresa if (funcionario[3] == 1)]
        for index,nome in enumerate (listNomes):
          print(f"Funcionario {index + 1}: {nome}")
          
      elif(opcao == 4):
        tsalario = [funcionario[4] for funcionario in empresa]
        medSalario = sum(tsalario) / len(tsalario)

        funAcimaMed = [funcionario[1] for funcionario in empresa if (funcionario[4] > medSalario)]
        print("Relatório Gerencial: Funcionários com Salário Acima da Média")
        for cargo in funAcimaMed:
          print(f"Cargo: {cargo}")

      else:
        desSalario = 212.54 * sum([funcionario[3] for funcionario in empresa])
        salarioLiq = salarioBrut - desSalario
        print(f"Relatório Administrativo da Folha de Pagamento:")
        print(f"Total da Folha de Pagamento Bruto: R$ {salarioBrut:.2f}")
        print(f"Total da Folha de Pagamento Líquido (desconto do Plano de Saúde): R$ {salarioLiq:.2f}")
    except Exception as ERRO:
      print(f'ERRO: {ERRO}')
