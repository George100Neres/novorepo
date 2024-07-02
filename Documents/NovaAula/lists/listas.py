# Criando a tupla com 5 dados
minha_tupla = (1, 2, 3, 4, 5)
print("Tupla:", minha_tupla)

# Convertendo a tupla para uma lista
minha_lista = list(minha_tupla)
print("Lista após conversão:", minha_lista)

# Inserindo 2 dados extras à lista
minha_lista.append(6)
minha_lista.append(7)
print("Lista após inserção de 2 dados extras:", minha_lista)

# Removendo o primeiro dado da lista
minha_lista.pop(0)
print("Lista após remoção do primeiro dado:", minha_lista)

# Removendo o último dado da lista
minha_lista.pop()
print("Lista após remoção do último dado:", minha_lista)

# Imprimindo o primeiro dado da lista
print("Primeiro dado da lista:", minha_lista[0])

# Imprimindo a quantidade de dados da lista
print("Quantidade de dados na lista:", len(minha_lista))

# Criando um dicionário com Nome, Idade e Profissão
meu_dicionario = {
    "Nome": "João",
    "Idade": 30,
    "Profissão": "Engenheiro"
}
print("Dicionário:", meu_dicionario)

# Imprimindo o valor contido na chave Nome do dicionário
print("Valor da chave 'Nome':", meu_dicionario["Nome"])