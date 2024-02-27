# POO EXERCICE

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nombre_de_personne = 3
    
liste_personne = []

for i in range(nombre_de_personne):
    nom = input(f"nom de la personne {i+1} : ")
    liste_personne.append(Personne(nom))

for personne in liste_personne:
    personne.SePresenter()