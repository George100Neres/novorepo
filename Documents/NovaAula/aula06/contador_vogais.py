
entrada = str(input(" Informe qual palavra voce queira pra cotabilizar as vogais "))

cont_vog = 0
vogais = "AEIOUaeiou"


for caracter in entrada:
    if caracter in vogais:
     cont_vog += 1

print(f"A Quantidade total de vogais que contem na palavra {entrada} sao: {cont_vog}")


