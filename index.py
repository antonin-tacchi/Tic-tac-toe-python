# affiche le plateau de jeu
def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

# programme qui vérifie si un joueur a gagné
def verifier_gagnant(grille):
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != " " or \
           grille[0][i] == grille[1][i] == grille[2][i] != " ":
            return True
    return grille[0][0] == grille[1][1] == grille[2][2] != " " or \
           grille[0][2] == grille[1][1] == grille[2][0] != " "
# programme qui vérifie si le plateau est plein

def morpion():
    grille = [[" "]*3 for _ in range(3)]
    joueur = "X"  # Le joueur commence avec "X"
    
    for tour in range(9):
        afficher_grille(grille)
        ligne, col = map(int, input(f"C'est au tour de {joueur}. Entrez la ligne et la colonne (0, 1 ou 2) : ").split())
        
        while grille[ligne][col] != " ":
            print("Cette case est déjà prise. Essayez encore.")
            ligne, col = map(int, input("Entrez la ligne et la colonne (0, 1 ou 2) : ").split())
        
        grille[ligne][col] = joueur
        
        if verifier_gagnant(grille):
            afficher_grille(grille)
            print(f"Le joueur {joueur} a gagné !")
            return
        
        joueur = "O" if joueur == "X" else "X"
    
    afficher_grille(grille)
    print("Match nul !")

if __name__ == "__main__":
    morpion()