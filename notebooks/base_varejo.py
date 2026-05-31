print('Hello World!')

# Importando as bibliotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os dados
df = pd.read_csv('Data/Base Varejo.csv', sep=';')

# Visualizando as primeiras linhas do dataset
print(df.head())

# Verificando números de registros
print(df.shape)

# Verificando colunas
print(df.columns)

# Verificando o tipo de dados
print(df.dtypes)

# Verificando valores nulos por coluna
nulos_por_coluna = df.isnull().sum()
print(nulos_por_coluna)
print(df.isnull().sum())

# Verificando porcentagem de valores nulos por coluna
pct = round(nulos_por_coluna / len(df) * 100, 2)
print(pd.DataFrame({'Nulos': nulos_por_coluna, '% Nulos': pct}))

# Substituindo usando estruturas condicionais
if "categoria" in df.columns:
    df['categoria'] = df['categoria'].fillna('Sem categoria')

# Usando condicional para preencher valores nulos 
if "valor" in df.columns:
    df['valor'] = df['valor'].fillna(df['valor'].mean())

# Eliminando colunas com valores nulos
colunas_para_eliminar = ['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13']
df = df.drop(columns=colunas_para_eliminar, errors='ignore')
print(f'Colunas eliminadas: {colunas_para_eliminar}')

# Verificando duplicatas
total_duplicatas = df.duplicated().sum()
print(f'Total de registros duplicados: {total_duplicatas}')

# Encontrando e eliminando duplicatas
df_sem_duplicatas = df.drop_duplicates()
print(f'Total de registros após eliminar duplicatas: {df_sem_duplicatas.shape[0]}')


# Codigo de conversão para Datatime
if 'DATA' in df.columns:
    df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')
    print('Coluna "DATA" convertida para datetime.')

# Gerando estatísticas descritivas básicas para colunas de números de filhos
if 'CL_FHL' in df.columns:
    print(df['CL_FHL'].describe())

media_fhl = df['CL_FHL'].mean()
print(f'Média de filhos: {media_fhl}')
mediana_fhl = df['CL_FHL'].median()
print(f'Mediana de filhos: {mediana_fhl}')
desvio_padrao_fhl = df['CL_FHL'].std()
print(f'Desvio padrão de filhos: {desvio_padrao_fhl}')
moda_fhl = df['CL_FHL'].mode()[0]
print(f'Moda de filhos: {moda_fhl}')
min_fhl = df['CL_FHL'].min()
print(f'Mínimo de filhos: {min_fhl}')
max_fhl = df['CL_FHL'].max()
print(f'Máximo de filhos: {max_fhl}')


# Explorando padrões de agrupamento
colunas_para_agrupamento = ['PR_CAT', 'PR_NOME']
agrupamento = df.groupby(colunas_para_agrupamento).size().reset_index(name='Contagem')
agrupamento.sort_values(by='Contagem', ascending=False)
print(agrupamento.head(10))

