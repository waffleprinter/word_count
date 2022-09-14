# Créé par Jacques-Conrad Calagui-Painchaud, 2022/09/14
# Ce programme va vous demander d'écrire une chaine et retournez le nombre de mots
# TP1

def count_word():
    chain = input("Entrez une chaine:")
    number_of_words = str(len(chain.split(" ")))
    print("Le nombre de mots dans cette chaine est:", number_of_words)

count_word()
