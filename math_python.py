#Une parabole
#Création d'une fonction personnelle basée sur l'équation : y = x2 + 10
#Vous allez me dire que l'on a déjà fait.
#C'est vrai mais cette fois j'emploie dans le code la fonction native pow(x,n) : élève x à la puissance n.

def  parabole(x):
    y = pow(x,2) + 10
    return y

print(parabole(-10))