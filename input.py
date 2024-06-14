nome = input("Digite seu nome: ")
idade = input("Digite sua idade")
idade_formatada = int(idade) # Conversao de string para int
print(type(idade))
idade_futura = idade_formatada + 3


print(f"O nome da pessoa e {nome}, e a idade formatada é {idade}, idade futura{idade_futura}")

