import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

nlp = spacy.load("fr_core_news_sm", exclude=["parser"])

patterns = [
    {
        "label": "DATE",
        "pattern": [{"shape": "d"}, {"shape": "xxxx"}, {"shape": "dddd"}]
    },
    {
        "label": "DATE",
        "pattern": [{"shape": "dd"}, {"shape": "xxxx"}, {"shape": "dddd"}]
    },
]
NER_rules = nlp.add_pipe("entity_ruler")
NER_rules.add_patterns(patterns)

with open("fichier.txt", encoding="utf-8") as input_stream:
    text = input_stream.read()

doc = nlp(text)
for ent in doc.ents:
    print(ent, ent.label_)
