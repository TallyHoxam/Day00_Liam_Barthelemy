def armstrong(nombre):
    nombre_chaine = str(nombre)
    addition = 0
    for numero in nombre_chaine :
        addition += int(numero) * int(numero) * int(numero)
    if addition == nombre:
        print(nombre , " est un nombre d'Armstrong")
    else:
        print(addition)
        print("non ce n'est pas un nombre d'Amstrong")
              
