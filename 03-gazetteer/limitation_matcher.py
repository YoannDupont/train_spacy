import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span


def add_org(matcher, doc, i, matches):
    """Get the current match and create tuple of entity label, start and end.
    Append entity to the doc's entity. (Don't overwrite doc.ents!)
    """
    match_id, start, end = matches[i]
    entity = Span(doc, start, end, label="ORG")
    doc.ents += (entity,)
    print(entity.text)


nlp = spacy.load("fr_core_news_sm", exclude=["parser"])

pattern = [{"LOWER": "parquet"}, {"ORTH": "de"}, {"ORTH": "Créteil"}]
matcher = Matcher(nlp.vocab)
matcher.add("m1", [pattern], on_match=add_org)

with open("fichier.txt", encoding="utf-8") as input_stream:
    text = input_stream.read()

doc = nlp(text)
for ent in doc.ents:
    print(ent, ent.label_)
print()
print()

matches = matcher(doc)
for ent in doc.ents:
    print(ent, ent.label_)
print(nlp.pipe_names)
