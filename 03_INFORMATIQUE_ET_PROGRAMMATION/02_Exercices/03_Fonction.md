# Construction élémentaire : Fonctions

------

## Exercice 1 : Fonction impair( )

1. Ecrire une fonction qui permet de savoir si `nombre` est impair

## Exercice 2 :

```python
def ........ (phrase , lettre) :
	if lettre in phrase :
    	...................
    ........... :
        ...................
```

1. Compléter cette fonction, trouvez lui un nom avec la description suivante :

   Si la lettre *lettre* est dans la phrase *phrase* alors renvoyer Vrai, sinon renvoyer Faux

2. Ecrire un appel de fonction renvoyant Vrai, un autre renvoyant Faux. (Testez la fonction)

## Exercice 3 : 

```python
def mystere(a, b, c, d):
    return (a+b+c+d)/4   
```

1. Que peut faire cette fonction ? Donnez lui un nom approprié.


## Exercice 4 : 

```python 
def plus_grand_que(a,b) :
    if a > b : 
        print(a)
    elif a == b : 
        print(a)
    else :
        print(b)
```

1. Que fait cette fonction ? Que renvoie t'elle ? 
2. Ajoutez une valeur de retour à la fonction (Vous devez modifier la fonction)
3. Ecrire un test permettant de vérifier que la fonction renvoie une valeur

## Exercice 5 :

```python
def orientation(prenom, spe1, spe2, spe3) :
    p = ' en première'
    p1 = 'prendra les spécialités suivantes : '
    p2 = ', '
```

1. Ecrire la suite de la fonction qui renvoie la phrase suivante :
   - "*Votre nom* prendra les spécialités suivantes : *Spécialité 1*, *Spécialité 2*, *Spécialité 3* en première"
2. Ecrire un test de la fonction avec votre nom et vos potentielles spécialités.

## Exercice 6 :

Ecrire une fonction permettant de savoir si un *nombre1* est le diviseur d'un autre nombre (appelé *nombre2*)
