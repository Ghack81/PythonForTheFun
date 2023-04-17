class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

class GestionnaireLivres:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur, annee):
        livre = Livre(titre, auteur, annee)
        self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
        else:
            print("Livres dans la bibliothèque:")
            for livre in self.livres:
                print(f"Titre: {livre.titre}, Auteur: {livre.auteur}, Année: {livre.annee}")

    def chercher_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                print(f"Titre: {livre.titre}, Auteur: {livre.auteur}, Année: {livre.annee}")
                return
        print("Aucun livre avec ce titre n'a été trouvé dans la bibliothèque.")

    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                self.livres.remove(livre)
                print(f"Le livre '{livre.titre}' a été supprimé de la bibliothèque.")
                return
        print("Aucun livre avec ce titre n'a été trouvé dans la bibliothèque.")
