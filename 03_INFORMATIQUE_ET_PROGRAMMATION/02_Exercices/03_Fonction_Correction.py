def impair(nombre):
    if (nombre % 2) == 0 :
        est_impair = False
    else :
        est_impair = True
    return est_impair

def lettre_dans_phrase(lettre,phrase) :
    if lettre in phrase :
        return True
    else :
        return False

def moyenne(a,b,c,d):
    return (a+b+c+d)/4