
# Constura um script para verificar se o usuario tem uma idade maior que 18 anos

idade = int(input(" Digite a sua idade"))


if idade > 18:
    print("Individuo possui idade minima para dirigir")
elif idade >= 17 and idade <= 18:
    print("Individuo tem entre 17 e 18 anos e ainda Não está apto para dirigir")
else:
     print("Individuo nao possui idade minima para dirigir")