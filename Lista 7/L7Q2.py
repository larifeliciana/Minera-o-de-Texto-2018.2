import L3Q5_Q6 as data
import spacy
from gensim.models import Word2Vec

nlp = spacy.load('en')
#23
n = open('rt-polarity.neg', 'r')
p = open('rt-polarity.pos', 'r')
neg = []
pos = []
for i in range(1000):
    x = nlp(n.readline())
    y = nlp(p.readline())
    neg.append([str(token).lower() for token in x if (not token.is_stop) and (not token.is_punct) and token is not '\n' ])
    pos.append([str(token).lower() for token in y if (not token.is_stop) and (not token.is_punct) ])

treino =  neg+pos


model = Word2Vec(treino)

model.train(treino, total_examples=len(treino), epochs=10)

w = 'bad'

x = model.wv.most_similar(w)
print(x)