import spacy

nlp = spacy.load("spacy_retrained/model-best")

text = "France: arrivée du présiden Jean Dupont."

for entity in nlp(text).ents:
    print(entity.start, entity.end, entity.label_, entity)
