
"""
Crie um Dataframe com os seguintes dados:

 Nome, idade e cidade. Sendo 3 pessoas moradoras de Recife, 2 de Salvador, 1 de São Pualo
 e 1 de Manaus

 Depois, filtre os dados para exibir na tela apenas os moradores do Recife.

"""
import pandas as pd

dados = {
    "Nome": ["Matheus", "Michelle", "Renato Taca Fogo", "Viviane", "Diego", "Amigo Javeiro"],
    "Idade": [20, 18, 40, 25, 31, 60],
    "Cidade":["Salvador", "Recife", "Recife", "Recife", "Manaus", "Manaus"] 
}

df = pd.DataFrame(data=dados)

# Filtro dos dados dos Moradores de Recife 
df_recife = df[df["Cidade"] == "Recife"]


print(df_recife)
    