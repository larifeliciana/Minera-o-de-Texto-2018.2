import nltk
from L2 import tag
import matplotlib.pyplot as plt
import spacy

########################################################################################
#8
def pipeline(stream):
    tokens = nltk.word_tokenize(stream)
    sentences = nltk.sent_tokenize(stream)
    stemmer = nltk.stem.SnowballStemmer("english")
    stems = [stemmer.stem(x) for x in tokens]
    lemma = nltk.stem.WordNetLemmatizer()
    tags = nltk.pos_tag(tokens)
    lemmas = [lemma.lemmatize(x, tag(tags[tokens.index(x)])) for x in tokens]

    return tokens, sentences, stems, lemmas, tags

stream = open('texto_en.txt', 'r').read()
tokens, sentences, stems, lemmas, tags = pipeline(stream)
palavras = [x for x in tokens if x.isalpha()]
stemmes = [y for y in stems if y.isalpha()]
print(lemmas)
########################################################################################
#A
"""print("A)"+str(len(palavras)))

########################################################################################
#B
print("B)"+str(len(set(stemmes))))


########################################################################################
#C
print("C)"+str(len(sentences)))
print("C)"+str(len(tokens)/len(sentences)))

########################################################################################
#E
tags = [x[1] for x in tags]
freqTag = (nltk.FreqDist(tags))
freqTag = (sorted(list(freqTag.items()), key = lambda x:x[1], reverse=True))
x = [i[1] for i in freqTag if i[0].isalpha()]
y = [i[0] for i in freqTag if i[0].isalpha()]
plt.bar(y, x)
plt.title("E)")
plt.show()
# AS CLASSES GRAMÁTICAIS MAIS FREQUENTES 'NN', 'IN', 'DT', 'NNS', 'VB', 'JJ', 'NNP', 'TO'   

#######################################################################################
#F
freq = nltk.FreqDist(stemmes)
plt.bar(freq.keys(), freq.values())
plt.show()"""
# AS MAIS FREQUENTE SÃO AS PREPOSIÇÕES e DETERMINANTES (QUE REFERENCIAM SUBSTANTIVOS) COMO POR EXEMPLO

