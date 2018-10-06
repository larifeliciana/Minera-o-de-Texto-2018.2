import nltk
import math
import os
def carregar(pasta):
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    lista = []
    for i in caminhos:
        review = open(i, 'r')
        lista.append(review.read())
    return lista

def vocabulario(tokens, ngram):
    if ngram is 2:
        tokens1 = [nltk.ngrams(i, 2) for i in tokens]
        tokens = tokens1
    voc = {}
    for i in tokens:
        for x in i:
            if x not in voc:
                voc.update({x:1})
            else:
                voc[x] = voc[x]+1
    return voc




def probabilidade(dicionario):
    N = sum([i for i in dicionario.values()])
    prob = {}
    for i in dicionario:
        prob.update({i: (dicionario[i]) /(N)})
    return prob

def frase_probabilidade(dicionario, frase, ngram):
    N = dicionario[sorted(dicionario, key=dicionario.get)[0]]

    frase = nltk.word_tokenize(frase)
    if ngram is 2:
        frase = nltk.ngrams(frase, 2)
    prob = 1
    for i in frase:
        if i in dicionario.keys():
            y = dicionario[i]
            x = (dicionario[i])
            prob = prob +  math.log(x)

        else: prob = prob + math.log(N)

    return math.exp(prob)

noticias = carregar("Noticias")
######A
sentencas = [nltk.sent_tokenize(i) for i in noticias]

######B
lower = [i.lower() for i in noticias]

#####C
tokens = [nltk.word_tokenize(i) for i in lower]

#####D
dicionario = vocabulario(tokens, 1)
prob = probabilidade(dicionario)



#####E
x = (frase_probabilidade(prob, "asudahsd asuidahsi asiduahsuid aiushdaiusd asuhaus aushuas",1))
print(x)
y = frase_probabilidade(prob, 'Uma boa notícia sobre algo.',1)
print(y)
