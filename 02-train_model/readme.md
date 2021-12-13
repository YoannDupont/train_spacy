# Créer le fichier de configuration

## Générer une configuration de base avec un gabarit (template)

On va ici générer des modèles qu'on va pouvoir apprendre et utiliser rapidement. S'il faut une meilleure qualité, il faudra changer des paramètres.

Aller sur : https://spacy.io/usage/training#quickstart

Et dans le menu :
- language => French
- components => ner
- hardware => cpu
- Optimize for => efficiency

Télécharger le fichier (icône en bas à droite de l'extrait (snippet).

Dans un terminal, lancer :

```
python -m spacy init fill-config base_config.cfg config.cfg
```

## Donner les fichiers pour l'apprentissage

Deux possibilités :
1. donner les fichiers dans le fichier de configuration `config.cfg`
2. donner les fichiers en arguments du script d'entraînement

Pour la solution 1. il faut modifier les lignes suivantes du fichier `config.cfg` :

```
[paths]
train = <chemin-vers-train.spacy>
dev = <chemin-vers-dev.spacy>
```

Il est à noter que modifier `config.cfg` ne fait que donner des valeurs par défaut. Il est toujours possible de les changer via la solution 2.

# Apprendre un modèle

En supposant que les fichiers train et dev donnés dans `config.cfg` sont les bons et qu'on veut stocker les résultats dans le dossier `spacy_retrained` :

```
spacy train config.cfg -o spacy_retrained
```

En supposant qu'on souhaite modifier les fichiers train et dev donnés dans `config.cfg` et qu'on veut stocker les résultats dans le dossier `spacy_retrained`.
Les chemins donnés sont les fichiers générés à partir du IOB dans `01-prepare_data`.

```
spacy train config.cfg -o spacy_retrained --paths.train ../01-prepare_data/docBinsCONLL/aijwikinerfrwp3-sample.spacy --paths.dev ../01-prepare_data/docBinsCONLL/aijwikinerfrwp3-sample.spacy
```

L'entraînement donnera deux dossiers :
- `spacy_retrained/model-last` le modèle de la dernière itération
- `spacy_retrained/model-best` le modèle ayant eu le meilleur score sur le dev

# Utiliser un modèle entraîné

Il est alors possible de charger un pipeline entraîné en donnant le chemin vers son dossier.

