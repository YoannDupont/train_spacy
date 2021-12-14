import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

nlp = spacy.load("fr_core_news_sm", exclude=["parser"])

patterns = [{"label": "ORG", "pattern": "parquet de"}]
NER_rules = nlp.add_pipe("entity_ruler")
NER_rules.add_patterns(patterns)

with open("fichier.txt", encoding="utf-8") as input_stream:
    text = input_stream.read()

doc = nlp(text)
for ent in doc.ents:
    print(ent, ent.label_)
print()
print()

for ent in doc.ents:
    print(ent, ent.label_)
print(nlp.pipe_names)
