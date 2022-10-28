#Les classes - Introduction
#Convention PEP8

class Voiture:

    #pass
    def __init__(self, p_couleur, p_marque, p_vitesse = 0):#self pour avoir la référence à l'objet en question
        #self suivis de l'attibut que l'on veut
        self.couleur = p_couleur
        self.marque  = p_marque
        self.vitesse = p_vitesse 
    #Créer une première méthode
    def accelerer(self, p_vitesse):
        self.vitesse += p_vitesse
    #Créer une dexième méthode
    def freiner(self, p_vitesse):
        self.vitesse -= p_vitesse
        if self.vitesse < 0:
            self.vitesse = 0
 
#Deux Instances de la classe Voiture
voiture_bleu = Voiture('rouge', 'BMW', 20)     #on vient créer un objet voiture
voiture_rouge = Voiture('bleu', 'Peugeot')     #on créer un deuxième objet

#Afficher au final nos objets créés
print(voiture_bleu.couleur)
print(voiture_bleu.marque)
print(voiture_bleu.vitesse)
print('-'*8)
print(voiture_rouge.couleur)
print(voiture_rouge.marque)
print(voiture_rouge.vitesse)
print('-'*8)
print(voiture_bleu.vitesse)
voiture_bleu.accelerer(20)
print(voiture_bleu.vitesse)
voiture_bleu.freiner(10)
print(voiture_bleu.vitesse)
voiture_bleu.freiner(50)
print(voiture_bleu.vitesse)

#Test 
x = int(input( "your value: " ))
if x > 3 : print( "Big" )
elif x == 3 : print( "Medium" )
else : print( "Small" )

