from utils import text_similarity, lemmatize, stop_words, tokenize
from pprint import pprint
import json

def database():
    json_file = open("data\\index.json", "r", encoding="utf-8")
    titles = [
        i["Title"]
        for i in json.load(json_file)
    ]

    tokenize_titles = [tokenize(sent.lower()) for sent in titles]
    clean_titles = [stop_words(tok) for tok in tokenize_titles]

    lemmatize_titles = [
        (idx, " ".join([lemmatize(word) for word in toks]))
        for idx, toks in enumerate(clean_titles)
    ]

    unique_strings = set()
    return list(filter(lambda x: x[1] not in unique_strings and not unique_strings.add(x[1]), lemmatize_titles))

def clean_sentence(text):
    toks = tokenize(text.lower())
    clean_toks = stop_words(toks)
    return " ".join([lemmatize(word) for word in clean_toks])

list_of_titles = database()
def color_rank(text):
    results = text_similarity(clean_sentence(text), list_of_titles)
    indexes = [i["index"] for i in results]

    json_file = open("data\\index.json", "r", encoding="utf-8")
    content = json.load(json_file)

    return [content[i] for i in indexes]

if __name__ == "__main__":
    text = "how to reply to an insult"
    results = color_rank(text)

    print("SEARCH QUERY:", text)
    pprint(results)
