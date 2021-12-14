# Utiliser des lexiques

Dans cette partie, nous verrons comment intégrer des lexiques d'entités nommées à Spacy.

# Intégrer des dates dans Spacy

Par défaut, le moteur de NER de Spacy ne reconnaît pas les dates. Nous allons ici montrer comment ajouter des patrons afin de reconnaîtres des dates au format simple.

Nous reconnaîtrons des dates en minuscule avec une année à 4 chiffres et un jour à 1 ou 2 chiffres.

Vous pouvez lire/lancer le script suivant pour voir comment intégrer des dates à Spacy:

```
python ./test_entity_ruler.py
```

# Limites de l'approche

Cette approche a deux limitations principales :
- elle ne gère que l'ajout d'entités, on ne peut pas en supprimer ;
- on ne peut pas ajouter d'entités qui chevauche une entité existante.

Pour observer ces limitations, nous pouvons étudier deux scripts qui se lancent de la manière suivante :

```
python ./limitation_entity_ruler.py
python ./limitation_matcher.py
```

# Entités nommées imbriquées

Il est malgré tout possible de contourner partiellement la limitation concernant le non-chevauchement des entités.

Le script suivant montre comment faire :

```
python ./multilevel_NER.py
```

Ce script utilise ici un `EntityRuler` pour ajouter un second niveau d'entités nommées, mais le même principe peut être appliqué avec différents modèles appris sur le même corpus.
