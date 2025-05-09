import os



def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')

def opcao_invalida():
    os.system('cls')
    print("opção invalida\n")
    input("digite uma tecla para voltar para o menu")
    main()



# minha lista 
restaurantes=[]
#post
def cadastrar_restaurante():
     print("cadastro de novos restaurantes")
     nome_do_restaurante=input("digite o nome do restaurante que deseja cadastrar:")
     restaurantes.append(nome_do_restaurante)
     print(f"o restaurante  {nome_do_restaurante} cadastrado com sucesso\n")
     input("digite uma tecla para voltar para menu")
     main()
#get All
def Listar_restaurantes():
     for restaurante in restaurantes:
          print(f"{restaurante}")
     
     input("digite uma tecla para voltar para menu")
     main()
     
    


def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))

            if opcao_escolhida == 1:
                cadastrar_restaurante()
            elif opcao_escolhida == 2:
                 Listar_restaurantes()
            elif opcao_escolhida == 3:
                  print('Ativar restaurante')
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()

      except ValueError:
            opcao_invalida()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()