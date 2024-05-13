def longueur(chaine):
    nombre = 0
    while chaine != "":
        chaine = chaine[1:]
        
        nombre += 1
    return nombre
    
