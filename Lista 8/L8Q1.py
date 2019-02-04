from sklearn import feature_extraction
from nltk import tokenize
import json

import pycorenlp

def soma_dic(dic1, dic2):
    x = list(dic1.values())
    y = list(dic2.values())
    dic3 = {}
    for i in range(len(x)):
        dic3.update({i:x[i]+y[i]})
    return dic3
def feature1(data):

    tfidf = feature_extraction.text.TfidfVectorizer(stop_words='english')
    data = tfidf.fit_transform(data).toarray()
    names = (tfidf.get_feature_names())


    soma = {}
    n = 0
    for i in data:
        soma.update({n:sum(i)})
        n = n + 1
    return soma

def feature2(data):

    nlp = pycorenlp.StanfordCoreNLP("http://localhost:9000")
    props = {'annotators': 'dcoref', 'pipelineLanguage': 'en', 'outputFormat': 'json'}
    soma = {}
    tam = []
    n = 0
    for i in data:
        lista = []
        tam.append(len(tokenize.word_tokenize(i)))
        count = 0
        sentence_splitting = nlp.annotate(i, properties=props)
        lista = [i['dep'] for i in sentence_splitting['sentences'][0]['basicDependencies']]
        for j in lista:
            if j == 'nsubj':
                count = count+3
            elif j == 'dobj':
                count = count+2
            else :
                count = count+1

        soma.update({n:count})
        n = n + 1
    return soma, tam

def feature3(data):
    soma1, tam = feature2(data)
    soma = {}

    for i in range(len(soma1)):
        soma.update({i:soma1[i]/tam[i]})
    return soma

#data = ['this is a good movie and maria loves it', 'i really loved this film', 'so good', 'too bad', 'worst film ever', 'i hate it']
#data = 'this is a good movie and maria loves it. I really loved this film. so good. too bad. worst film ever. i hate it'


#print(feature1(data))
#print(feature2(data)[0])
#print(feature3(data))


def criar_resumo(tipo_rank,texto):
    sentencas = tokenize.sent_tokenize(texto)
    tam = 4
    if tipo_rank == 1:
        dic = feature1(sentencas)
    elif tipo_rank == 2:
        dic = feature2(sentencas)[0]
    elif tipo_rank == 3:
        dic = feature3(sentencas)
    elif tipo_rank == 4:
        dic = soma_dic(feature1(sentencas),feature2(sentencas)[0])
    elif tipo_rank == 5:
        dic = soma_dic(feature2(sentencas)[0],feature3(sentencas))
    elif tipo_rank == 6:
        dic = soma_dic(feature1(sentencas),feature3(sentencas))
    elif tipo_rank == 7:
        dic = soma_dic(soma_dic(feature1(sentencas),feature2(sentencas)[0]), feature3(sentencas))

    values = sorted(dic.values(), reverse=True)
    valores  = values[0:tam]

    index = []
    for i in dic.keys():
        if dic[i] in valores:
            index.append(i)
            count = valores.count(dic[i])
            while dic[i] in valores:
                print(valores.index(dic[i]))
                valores.remove(dic[i])

    texto = ""
    print(index)
    for i in index:
        texto = texto + sentencas[i] + "\n"
    print(texto)
    print(values[0:tam])
    return texto, values[0:tam]

data = open('news028.txt', 'r').read()
criar_resumo(7, data)
