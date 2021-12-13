# Convertir fichier IOB

Convertir un fichier iob (WikiNER) avec :
- fichier: `aijwikinerfrwp3-sample.iob`
- pipeline Spacy: `fr_core_news_sm`
- dossier de sortie: `docBinsIOB` (doit exister)

```
spacy convert -c iob -s -n 10 -b fr_core_news_sm aijwikinerfrwp3-sample.iob ./docBinsIOB
```

# Convertir fichier CoNLL

Convertir un fichier CoNLL (CoNLL-2003) avec :
- fichier: `aijwikinerfrwp3-sample.conll`
- pipeline Spacy: `fr_core_news_sm`
- dossier de sortie: `docBinsCONLL` (doit exister)

```
spacy convert -c conll -b fr_core_news_sm aijwikinerfrwp3-sample.conll ./docBinsCONLL
```

Le fichier contient déjà des bornes (phrases, documents) lisibles par Spacy, elles seront automatiquement utilisées.
