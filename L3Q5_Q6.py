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




def probabilidade(dicionario, ngram, unigramas):
    if ngram is 1:
        N = sum([i for i in dicionario.values()])
    else:
        uni = {}
        for x in unigramas.keys():

            lista = []
            for i in dicionario.keys():
                if i[0] is x:
                 lista.append(dicionario[i])
            uni.update({x:sum(lista)})


    prob = {}
    lista =[]


    for i in dicionario:
        if ngram is 2:
            N = uni[i[0]]

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
dicionario = vocabulario(tokens, 2)
prob = probabilidade(dicionario,2, vocabulario(tokens,1))



#####E
def calcular(frase,ngram, tokens):

    dicionario = vocabulario(tokens, ngram)
    prob = probabilidade(dicionario, ngram, vocabulario(tokens, 1))
    return frase_probabilidade(prob, frase, ngram)


#frase = "eu li uma má notícia ontem"
#print(calcular(frase, 1, tokens))

