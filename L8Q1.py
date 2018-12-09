from sklearn import feature_extraction
from nltk import tokenize
import json
import L2
import pycorenlp

def feature1(data):
    tfidf = feature_extraction.text.TfidfVectorizer(stop_words='english')
    data = tfidf.fit_transform(data).toarray()
    names = (tfidf.get_feature_names())
    print(names)
    soma = []
    for i in data:
        soma.append(sum(i))
    return soma

def feature2(data):

    nlp = pycorenlp.StanfordCoreNLP("http://localhost:9000")
    props = {'annotators': 'dcoref', 'pipelineLanguage': 'en', 'outputFormat': 'json'}
    soma = []
    tam = []
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

        soma.append(count)
    return soma, tam

def feature3(data):
    soma1, tam = feature2(data)
    soma = [soma1[i]/tam[i] for i in range(len(soma1))]
    return soma

data = ['this is a good movie and maria loves it', 'i really loved this film', 'so good', 'too bad', 'worst film ever', 'i hate it']

print(feature2(data))


