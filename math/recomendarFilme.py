# FUNÇÃO PARA RECOMEDAR FILME
def recomendar_filmes(usuarios):
    recomendar_filmes = []
    teste = []
    user = int(input("qual usuário?"))
    filmesAssistidos = usuarios[user]['filmes']
    generosPreferidos = usuarios[user]['generos']
    for usuarios[user]['filmes'] in filmes.keys():
        if filmes.keys(1) not in usuarios[user]['filmes']:
            recomendar_filmes.append(filmes.keys)
    print(recomendar_filmes)







# DADOS DO USUÁRIO (DICIONARIO ONDE A CHAVE É O ID DO USUÁRIO E O VALOR É UM DICIONÁRIO COM OS CONJUNTOS DE FILMES E GENEROS)

usuarios = {
    1: {'filmes': {'A', 'B', 'C', 'D'}, 'generos': {'Ação', 'Aventura', 'Comédia'}},
    2: {'filme': {'B', 'D', 'E', 'F'}, 'generos': {'Drama', 'Romance', 'Ação'}}
}

# DADOS DOS FILMES DISPONÍVEIS (DICIONARIO ONDE A CHAVE É O ID DO FILME E O VALOR É O CONJUNTO DE GENEROS)

filmes = {
    'A': {'Ação', 'Aventura'},
    'B': {'Comédia', 'Ação'},
    'C': {'Drama'},
    'D': {'Ação', 'Aventura'},
    'E': {'Drama', 'Romance'},
    'F': {'Comédia', 'Romance'}
}

print(recomendar_filmes(usuarios))
