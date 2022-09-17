# Créé par Jacques-Conrad Calagui-Painchaud
# Créé le 2022/09/14
# Ce programme va retourner le nombre de dans une chaine fourni par l'usager.
# TP1

def count_word():
    chain = input("Entrez une chaine:")
    number_of_words = str(len(chain.split()))
    print(f"Il y a {number_of_words} mots dans cette chaine.")

count_word()
