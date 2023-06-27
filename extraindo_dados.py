from dados_repos import DadosReposiotrios

amazon_repo = DadosReposiotrios('amzn')
lingu_mais_usadas_amzn = amazon_repo.cria_df_linguagens()

netflix_repo = DadosReposiotrios('netflix')
lingu_mais_usadas_netflix = netflix_repo.cria_df_linguagens()

#Salvando os dados
lingu_mais_usadas_amzn.to_csv('dados/linguages_amzn.csv')
lingu_mais_usadas_netflix.to_csv('dados/linguages_netflix.csv')