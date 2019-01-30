import nltk
def score_global(posicao, sentencas):
    pos =  nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentencas[posicao])))
    ner = [i for i in pos if type(i) is nltk.Tree]
    return 1 + (2*len(ner))/(len(sentencas)+(1- (posicao)/len(sentencas)))


def summarizador(stream):
    sentencas = nltk.sent_tokenize(stream)

    print(len(sentencas))
    scores = {}
    for i in range(len(sentencas)):
        scores.update({i:score_global(i, sentencas)})
    scores = sorted(scores, key=scores.get, reverse=True)
    tam = int(len(sentencas) * 0.3)

    return scores[:tam]

lista = [open('news1.txt','r').read(), open('news2.txt','r').read(), open('news3.txt','r').read(), open('news4.txt','r').read(),open('news5.txt','r').read()]


string = ""
for x in lista:
      z = nltk.sent_tokenize(x)
      summarizar = sorted(summarizador(x))
      for i in summarizar:
          string = string + z[i]
      string = (string) + "\n\n\n\n"

x = open("saida1.txt",'w')
x.writelines(string)
x.close()