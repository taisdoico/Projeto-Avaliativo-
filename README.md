 Documento para README

Este relatório mostra as funções e métodos para o trabalho de limpeza desenvolvido, análise estatística e extração de dados que foram fornecidos diretamente do repositório Kaggle carregados através das bibliotecas: "pandas", "numpy", "matplotlib.pyplot" e "seaborn".


 1. Estrutura do Pipeline de Dados

 A importação foi feita mantendo a estrutura original, permitindo saber o tamanho da base de dados antes de aplicar as correções necessárias.
 Verifiquei valores nulos por coluna, verifiquei a porcentagem e criei uma condicional para achar categorias vazias e preenchê-las com o texto "Sem Categoria". Deletei as colunas fantasmas que vieram vazias usando o comando "df.drop(errors='ignore')".
 Usei o "df.drop_duplicates(inplace=True)" para apagar linhas repetidas e não distorcer o relatório causando inconsistências.
 Identifiquei a coluna "DATA" e usei o "pd.to_datetime() para corrigir, e o uso do "errors='coerce" para o caso de ter alguma data com texto errado.
 Na coluna de filhos ("CL_FHL"), usei as funções ".mean()", ".median()", ".mode()" e ".std()", que trouxeram a média, a mediana, a moda e o desvio padrão de quantos filhos os clientes têm.
 Para o agrupamento, apliquei o método #.groupby()" juntando as categorias "PR_CAT" e "PR_NOME". O comando ".size().reset_index()" gerou uma tabela organizada mostrando a quantidade de produtos dentro da categoria.


 2. Alguns Insights que tive nessa EAD

 O tratamento condicional garantiu que nenhum produto ficasse sem classificação. Ao preencher os nulos com "Sem Categoria", o código evitou a perda dessas linhas de vendas e organizou a tabela.
 O agrupamento revelou quais produtos específicos lideram o volume de saídas em cada categoria. Esse dado mostra quais itens têm maior giro no estoque físico, ajudando na decisão de reposição de mercadorias.
 As funções estatísticas aplicadas na coluna "CL_FHL" mostraram o comportamento dos compradores, identificando a média e a quantidade mais frequente de filhos por cliente.
 Transformamos a coluna de data de texto para o formato de data real do Python. Isso organiza as informações em ordem cronológica e ajuda o sistema a entender os dias e meses certinhos das vendas, deixando tudo pronto caso a gente queira olhar quais meses vendem mais no futuro.
