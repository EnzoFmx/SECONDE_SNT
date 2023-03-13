# TP : Modélisation d'un réseau informatique

------

## 1. Présentation :

Ce TP a pour but de construire et simuler quelques actions simples d'un réseau informatique. 

Le logiciel utilisé pour ce travail est Filius, une fiche outils est disponible dans le dossier FICHE_OUTILS

**Pour chaque exercice il est conseillé d'ouvrir un nouveau fichier.**

## Exercice 1 :

1. Créer un réseau de deux ordinateurs (avec deux adresses IP différentes)
2. Faire un ping de la première vers la seconde machine.


## Exercice 2 :

1. Créer un réseau de 6 machines, toutes reliées à un switch. 
2. Passer en mode simulation.

**Pour la suite il faut impérativement passer la vitesse d'exécution à 1%.**

3. Simuler un ping d'une machine vers une autre. Que se passe t'il avant l'envoie du ping ?

4. Expliquer à l'aide d'une recherche internet le protocole ARP.
   - *(Si vous n'avez rien vu, passez en mode conception, puis repasser en simulation (cela réinitialisera la manipulation et le protocole ARP s'effectuera à nouveau))*

## Exercice 3 :

Réaliser les étapes ci-dessous :

1. Créer un réseau contenant 3 ordinateurs et un switch.
2. Attribuer les adresse IP suivantes :

   - 192.168.0.10

   - 192.168.0.11

   - 192.168.0.12
3. Créer un autre réseau (3 ordinateurs et un switch) avec les adresses suivantes :

   - 192.168.1.10

   - 192.168.1.11

   - 192.168.1.12
4. Relier les deux réseaux grâce à un routeur. *(Il faut choisir 3 interfaces ici)*
   - Voici une image de ce que l'on doit obtenir :

![Routage_deux_reseaux.png](./Images/Routage_deux_reseaux.png)

1. Essayer de faire un ping d'une machine du premier réseau vers le second et expliquez ce qu'il se passe.
2. Configurons notre routeur :

   - Dans la section "Général" cocher la case "Routage automatique"
4. Essayer de faire un ping d'une machine du premier réseau vers le second et expliquez ce qu'il se passe.
5. Rajouter un autre réseau composé de 3 ordinateurs et d'un switch. Puis faire en sorte que les 3 réseaux puissent communiquer entre-eux

## Exercice 4 :

Pour cet exercice il est conseiller de réutiliser le réseau de l'exercice 4 (Si vous enregistrez les fichiers, faites en une copie)

1. Suivre les étapes suivantes :

   - Rajouter un ordinateur dans l'un des trois réseaux (Le nommer "Serveur Web")
       - Le rendre accessible depuis les 3 réseaux

   - En mode simulation, ajouter la fonctionnalité Serveur Web dans le nouvel ordinateur puis démarrer le serveur

   - Avec un autre ordinateur du réseau, télécharger navigateur web puis l'ouvrir

   - Rentrer l'adresse IP de votre serveur Web dans la barre de recherche. Que constatez vous ?


## Exercice 5 :

Pour cet exercice il est conseiller de réutiliser le réseau de l'exercice 5

Suivre les étapes suivantes :

- Rajouter un ordinateur dans l'un des trois réseaux (le nommer "Serveur DNS")
    - Le rendre accessible depuis les 3 réseaux
- Ajouter pour chacun des ordinateurs du réseau l'adresse IP du serveur DNS dans le champ "Serveur DNS"
- En mode simulation, ajouter la fonctionnalité Serveur DNS dans votre machine Serveur DNS.
    - Ouvrir le logiciel serveur DNS, puis ajouter le serveur WEB avec comme nom "SNT.com" et comme adresse IP l'adresse de votre Serveur WEB.
- Depuis une machine d'un des réseaux, connectez vous grâce au navigateur WEB sur le site NSI.com
    - Que constatez vous ?
