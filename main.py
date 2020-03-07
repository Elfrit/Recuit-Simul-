def recuitSimule(f,S,T):
    # F la fonction , S = Solution initiale, T température pouvant être traduit par le degré de précision 
    while T>0 : #à 0 la "meilleur solution" doit être trouvée
        Sp = random() #voisin de S
        for i in range (S):
            d = f(Sp)-F(S) #Chercher un delta qu'on devra comparer
            if CritMetropolis(d,T): #Si f(Sp) est inferieur à f(S) ou sp est une valeur interessante 
                S = Sp; #S devient la valeur la plus interessante
                nbMove += 1
            coeff = i/nbMove
            T = t*coeff
    return S
def critMetropolis(d,T): #ou T>=0
    if (d<=0):
        return true
    else:
        if (exp(-d/T<=0):
            return true
        return false
