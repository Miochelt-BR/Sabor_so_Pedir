print("ℴ𝓁𝒶 𝓈ℯ𝒿𝒶 𝒷ℯ𝓂 𝓋𝒾𝓃𝒹ℴ 𝒶𝓅𝓅 𝒮𝒶𝒷ℴ𝓇 ℯ́ 𝒮ℴ 𝒫ℯ𝒹𝒾𝓇\n")
print("1.cadastrar restaurante")
print("2.Listar  restaurante")
print("3.Ativar restaurante")
print("4.Sair\n")

#criando as funcoes 
def finalizando_app():
     print("Volte logo")

opcao_escolhida=int(input("escolha  a opção:"))
print(f"voçÊ escolheu a opção {opcao_escolhida}")

if opcao_escolhida==1:
      print("pode cadastrar o restaurante desejado")
  
elif  opcao_escolhida==2:
      print("Bem vindo a lista de restaurantes ")

elif  opcao_escolhida==3:
      print("pode atualizar seu restaurante")
else:
     finalizando_app()



