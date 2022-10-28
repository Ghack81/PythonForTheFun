#  Program to calculate the factorial of a positive integer:

n = int(input('Tapez un nombre et sa factorielle sera imprimée : '))

if n < 0:
    raise ValueError('Vous devez saisir un entier non négatif')

factorial = 1
for i in range(2, n + 1):
    factorial *= i

print(factorial)