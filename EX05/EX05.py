import random
def tableau():
    tableau_un = []
    for i in range(15):
        tableau_un.append(random.random())
    print(tableau_un)
    tableau_croissant = []
    tableau_deux = tableau_un[:]
    
    tableau_croissant = []
    
    
    while tableau_deux :
        min_nombre = max(tableau_deux)
        tableau_croissant.append(min_nombre)
        tableau_deux.remove(min_nombre)      

  
    print("Tableau trié par ordre décroissant :", tableau_croissant)
                
        

        
        
tableau()
