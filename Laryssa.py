#Crie um DataFrame de exemplo com dados fictícios. 'Nome' 'Idade' 'Departamento' 'Salario'

import pandas as pd

empresa={'Nomes':['Ana','Nicole','Pedro','Joana','Quibe','Uriel','Ezequias','Kesya','Angel','Samuel'],
         'Idade':[19,23,12,34,65,89,15,17,17,18],
         'Departamento':['producao','aprediz','vendedor','producao','producao','aprendiz','repositor','aprendiz','desenvolvedor','vendedor'],
         'Salario':[1300,800,1200,1300,1300,800,1900,900,3200,1200]}


df=pd.DataFrame(empresa)
print(df)


#Exiba as primeiras linhas do DataFrame usando head() para entender a estrutura dos dados.

print(df.head())


#Utilize info() para obter informações sobre as colunas e tipos de dados.

print(df.info())

#Selecione uma ou várias colunas específicas do DataFrame.

colunas_selecionadas = df[['Nomes', 'Departamento']]

print(colunas_selecionadas)


#Crie uma nova coluna calculada com base em valores existentes.



#Crie um gráfico de linhas para visualizar uma tendência ao longo do tempo.

