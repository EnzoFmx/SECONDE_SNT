# Affectation et conditions

------

## 1. Affectation :

Ecrire les instructions suivantes dans la console :

```python
>>> a = 5
>>> b = 7
>>> a
>>> b
>>> a = b
>>> a
>>> b
```

1. Expliquer ce qu'il s'est passé avec les valeurs a et b ici.

Ecrire à la suite :

```python
>>> c = 6
>>> d = 8
>>> e = 6
>>> c == d
>>> c == e
```

2. Que s'est-il passé ici? A quoi peut correspondre l'opérateur '=='

## 2. Conditions :

Une condition permet d'exécuter ou non des lignes de code. Ce type de cas peut s'apparenter à une situation de la vie quotidienne.

Par exemple :

- Si j'ai plus de 18 ans
  - Je peut avoir mon permis de conduire
- Sinon
  - Je ne peux pas avoir mon permis de conduire

Ce type de condition peut s'écrire en python, par exemple :

```python
# Une variable appelée age permet de stocker un age
age = 16
if age > 18 :
    print('Je peux avoir mon permis de conduire')
else :
    print('Je ne peux pas avoir mon permis de conduire')
```

Plusieurs choses sont à noter ici :

- Après un **if** on écrit une condition (age > 18) le résultat de cette condition est soit vrai, soit faux.
  - Dans le cas ou c'est Vrai, on affiche grâce à la fonction `print( )` la phrase 'Je peux avoir mon permis de conduire'
- Après un **else** (sinon) on n'écrit pas de condition
  - Dans ce cas on affiche 'Je ne peux pas avoir mon permis de conduire'

**A la fin du mot clé IF et ELSE, il y a toujours `:`**

**De plus, les lignes de code à exécuter selon la condition sont indentées (elles sont décalées). Thonny, Edupython fait cette indentation automatiquement. Sinon il faut appuyer sur la touche `TAB` du clavier.**

### 2. 1. Exercices d'application :

Exercice 0 : Copier coller le code du dessus et tester avec différentes valeur afin d'avoir les différents affichages.

Exercice 1 : Décrire la situation suivante en python

> Bob est arrivé 15ème à son tournoi en ligne.
> Si il est dans les 20 premiers
>     Alors afficher `"Vous remportez une récompense"`
> Sinon
>     afficher `"Vous ne gagnez rien"`

a. Proposez une valeur pour la quelle la phrase `Vous ne gagnez rien` s'affiche.

Exercice 2 :

```python
#Partie 1 :
note = 16
if note > 14 :
	print('Bien')
if note > 12 :
	print('Assez bien')
if note > 10 : 
	print('Insuffisant')


# Partie 2 :  
note = 16
if note > 14 :
	print('Très bien')
elif note > 12 :
	print('Bien')
elif note > 10 : 
	print('Assez bien')
else :
    print('Insuffisant')
```

1. Faire un copier collé de la partie 1, qu'affiche t'il avec une note égale à 13. 
2. En s'aidant de la partie 2, à quoi peut servir le mot clé `elif`
3. Dans quel cas affichons nous "Insuffisant" (pour la partie 2)

