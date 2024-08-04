import numpy as np

agenda = []

try:
  while True:
    print("1: Inserir dados.")
    print("2: Pesquisar um contato pelo Nome.")
    opcao = int(input("Digite a opção: "))

    if(opcao != 1 and opcao != 2):
      break

    elif(opcao == 1):
      nome = str(input("Digite o nome: "))
      email = str(input("Digite o email: "))
      whatss = int(input("Digite o WhatsApp: "))

      contato = [nome, email, whatss]
      agenda.append(contato)
      
    elif(opcao == 2):
      pesqContato = str(input("Digite um nome para pesquisar: "))
      contatos = (contatos[0] for contatos in agenda)
      
      try:
        pesqIndex = list(contatos).index(pesqContato)
        contato = agenda[pesqIndex]

        print(f"Nome: {contato[0]}")
        print(f"Email: {contato[1]}")
        print(f"WhatsApp: {contato[2]}")
      except:
        print("Contato não encontrado!")
        
except Exception as ERRO:
  print(f"Erro: {ERRO}")
