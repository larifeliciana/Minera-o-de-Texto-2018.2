import nltk
import spacy

def tag(tag):
    tag = tag[1]
    if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
        return 'n'
    elif tag in ['VB', 'VBD', 'VBG', 'VBN','VBP', 'VBZ']:
        return 'v'
    elif tag in ['RB', 'RBR', 'RBS']:
        return 'r'
    else : return 'r'


def lemmas(qt, tokens, stopwords, tipo):
    tokens_stop = tokens
    if stopwords is True:
        tokens_stop = []
        stopwords = open('stopwords.txt', 'r').read()
        for i in tokens:
            if i not in stopwords:
                tokens_stop.append(i)
    tokens = tokens_stop
    lemma = nltk.stem.WordNetLemmatizer()
    tags = nltk.pos_tag(tokens)
    lemmas = [lemma.lemmatize(tokens[x], tipo).lower() for x in range(len(tokens)) if tag(tags[x]) is tipo and tokens[x].isalpha()]
    freq_sub = nltk.FreqDist(lemmas)
    freq_sub = list(freq_sub.items())
    freq_sub = sorted(freq_sub, key=lambda x: x[1], reverse=True)
    return freq_sub[0:qt]

arq = open("Corpus_en_NER.txt", 'r')
stream = arq.read()
tokens = nltk.word_tokenize(stream)


#print(lemmas(20, tokens, False,'n'))
#print(lemmas(20, tokens, False,'v'))
#print(lemmas(20, tokens, True,'n'))
#print(lemmas(20, tokens, True,'v'))
