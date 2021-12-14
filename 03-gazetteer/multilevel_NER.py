import spacy

# Trois pipelines pour avoir un traitement "optimal" :
#     - faire tous les prétraitements ;
#     - appliquer le modèle entraîné d'entités nommées ;
#     - appliquer un lexique.
# Note : fonctionne de manière similaire pour lancer des modèles entraînés sur le même corpus
nlp0 = spacy.load("fr_core_news_sm", exclude=["parser", "ner"]) # aspect "syntaxique" (mots, lemmes, etc.)
nlp1 = spacy.load("fr_core_news_sm", exclude=['tok2vec', 'morphologizer', 'attribute_ruler', 'lemmatizer', 'parser']) # uniquement la NER de Spacy
nlp2 = spacy.load("fr_core_news_sm", exclude=['tok2vec', 'morphologizer', 'attribute_ruler', 'lemmatizer', 'parser', 'ner']) # uniquement le EntityRuler (ajouté après)

patterns = [{"label": "ORG", "pattern": "parquet de Créteil"}]
REN = nlp2.add_pipe("entity_ruler")
REN.add_patterns(patterns)

with open("fichier.txt", encoding="utf-8") as input_stream:
    text = input_stream.read()

doc0 = nlp0(text)
doc1 = nlp1(doc0.copy())
doc2 = nlp2(doc0.copy())
for ent in doc1.ents:
    print(ent, ent.label_, ent.start, ent.end)
for ent in doc2.ents:
    print(ent, ent.label_, ent.start, ent.end)
