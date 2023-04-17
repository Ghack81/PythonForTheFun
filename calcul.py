import tkinter as tk

# Fonction pour mettre à jour l'affichage de la calculatrice
def update_display(text):
    display.delete(1.0, tk.END)
    display.insert(tk.END, text)

# Fonction pour gérer les clics sur les boutons numériques
def on_digit_click(digit):
    current_expression = display.get(1.0, tk.END).strip()
    update_display(current_expression + str(digit))

# Fonction pour gérer les clics sur les boutons d'opération
def on_operator_click(operator):
    current_expression = display.get(1.0, tk.END).strip()
    update_display(current_expression + operator)

# Fonction pour gérer le clic sur le bouton égal
def on_equal_click():
    current_expression = display.get(1.0, tk.END).strip()
    try:
        # Évalue l'expression mathématique et met à jour l'affichage
        result = eval(current_expression)
        update_display(result)
    except Exception as e:
        update_display("Erreur")

# Fonction pour gérer le clic sur le bouton C (Clear)
def on_clear_click():
    update_display("")

# Crée une fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Crée un widget Text pour afficher les chiffres et les résultats
display = tk.Text(root, height=2, state=tk.DISABLED)
display.grid(row=0, column=0, columnspan=4)

# Crée les boutons numériques
for i in range(9):
    button = tk.Button(root, text=str(i+1), command=lambda i=i: on_digit_click(i+1))
    button.grid(row=1 + i // 3, column=i % 3)

# Crée le bouton zéro
button = tk.Button(root, text="0", command=lambda: on_digit_click(0))
button.grid(row=4, column=1)

# Crée les boutons d'opération
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(root, text=operator, command=lambda operator=operator: on_operator_click(operator))
    button.grid(row=1 + i, column=3)

# Crée le bouton égal
button = tk.Button(root, text="=", command=on_equal_click)
button.grid(row=4, column=0)

# Crée le bouton Clear
button = tk.Button(root, text="C", command=on_clear_click)
button.grid(row=4, column=2)

# Lance la boucle principale de l'interface graphique
root.mainloop()
