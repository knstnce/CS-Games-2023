# Challenge de conversion de devise - CSGames 2023

## Contexte

La confiance dans les banques étant ébranlée et la coopération entre les nouveaux habitants nécessaire, le comité a décidé que toute monnaie devait être acceptée et convertie automatiquement et gratuitement. Il s'agit de garantir l'égalité et de faciliter les transactions pour avoir une continuité dans l'économie.

## Résumé

Vous et votre équipe devez créer un programme permettant une conversion rapide et facile des devises. Ce programme comprendra une interface graphique pour permettre aux utilisateurs d'interagir facilement et de voir la conversion de diverses devises différentes. Vous devrez utiliser une API pour obtenir la valeur actuelle des différentes devises, puis convertir la devise sélectionnée par l'utilisateur en d'autres devises.

## Valeur de la compétition

`500 points`

## Tâches

Ce programme doit être écrit en **Python**

### Interface utilisateur

Pour cette portion du projet, **vouz devez utiliser tkinter library** : [tkinter](https://docs.python.org/3/library/tkinter.html)

- Créer une fenêtre pour l'interface graphique de l'application (30 points)
- Ajouter un logo (10 points)
- Utiliser une police personnalisée (10 points)
- Avoir un en-tête (10 points)
- Autoriser un utilisateur à sélectionner une devise source et cible dans une liste (40 points)
- Ajouter une fonction pour permettre à un utilisateur d'afficher un plus grand nombre de devises cibles pour une consultation facile (30 points)
- Intégration du thème *Atlantis* (20 points)
- Conception générale et présentation (80 points)

### API

Vous devez utiliser **ExchangeRate API** pour la conversion des devises régulières : [ExchangeRate API](https://www.exchangerate-api.com/)

- Utilisez l'API ExchangeRate pour obtenir des informations sur les devises (20 points)
- Créer une fonction qui permet d'obtenir les codes des devises (30 points)
- Créer une fonction qui permet la conversion de devise (30 points)

#### Cryptocurrency

Les crypto-monnaies ont pris beaucoup d'importance après que les riches ont trahi l'humanité et que les banques ont fermé. Inclure un moyen de convertir les crypto-monnaies. Vous pouvez utiliser l'API de votre choix pour cela, mais nous vous recommandons [CoinAPI](https://www.coinapi.io/). Attention, le niveau gratuit est limité à 100 transactions par clé.

- Utilisez une API pour obtenir la valeur de différentes crypto-monnaies (20 points)
- Autoriser les utilisateurs à convertir entre différentes crypto-monnaies (20 points)
- Autoriser les utilisateurs à convertir entre monnaies ordinaires et crypto (60 points)

### Générale

- Le projet fonctionne sans modifications (20 points)
- Le code est propre et commenté (20 points)
- Coder conformément aux pratiques standards et en suivant le guide de style de Python (20 points)
- Fournissez un README avec des instructions claires sur la façon d'exécuter et d'utiliser votre programme (30 points)
