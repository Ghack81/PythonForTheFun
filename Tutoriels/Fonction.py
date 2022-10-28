def next_year():
    global year
    print("Fin de l'année", year)
    year += 1
    print(("Début de l'année", year))


# variable global récupéré par l'insertion "global year" dans la fonction
year = 2021
next_year()
next_year()
