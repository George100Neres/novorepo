
"""
Desenvolver um programa que conte quantas vogais (a, e, i, o, u) existem
em uma palavra fornecida pelo usuário. 

Implementam uma função que receba uma palavra qualquer (string) como entrada.
O programa deve imprimir o número total de vogais na palavra.

Soliticação de Entrada

 *Implementem a solicitação de entrada de uma palavra (string)

 Contagem de Vogais

  *Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
  * Veirifique se cada caractere é uma vogal (a, e, i, o, u)e conte-as.
  *Imprima o numero total de vogais na palavra.
"""
print("Bem vindo a calculadora de vogais da Squad 4!")
palavra = str(input("Qual a palavra que você quer contar as vogais: "))

contador = 0 
vogais = "AEIOUaeiou"
for caracter in palavra:
    if caracter in vogais:
        contador += 1

print(f"O número de vogais na palavra é {contador}")
