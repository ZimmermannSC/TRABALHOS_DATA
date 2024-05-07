#Crie um DataFrame de exemplo com dados fictícios. 'Nome' 'Idade' 'Departamento' 'Salario'

import pandas as pd

empresa={'Nomes':['Ana','Nicole','Pedro','Joana','Quibe','Uriel','Ezequias','Kesya','Angel','Samuel'],
         'Idade':[19,23,12,34,65,89,15,17,17,18],
         'Departamento':['producao','aprediz','vendedor','producao','producao','aprendiz','repositor','aprendiz','desenvolvedor','vendedor']}


df=pd.DataFrame(empresa)
print(df)
