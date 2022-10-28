import statistics 
from random import shuffle
# Exemple de calcule de moyenne
notes = [
    8, 12, 16,
    9, 4, 15,
    14, 16
]
print(notes)
shuffle(notes)
print(notes)
# module : statistics avec "mean" -> moyen qui peut être importer
# de 'from statistic import mean' en retirant statistic dans "result"
result = statistics.mean(notes)
print("La moyenne des éléves est de {}".format(result))