import nltk
import matplotlib.pyplot as plt
from nltk.corpus import brown
corpus = brown.words()
frequencia = nltk.FreqDist(corpus)
frequencia = list(frequencia.items())
frequencia = sorted(frequencia, key= lambda x:x[1], reverse=True)
mais_frequentes  = frequencia[0:50]
unigramas = [i[0] for i in mais_frequentes]
valores = [i[1] for i in mais_frequentes]
tags = [i[1] for i in (nltk.pos_tag(unigramas))]
tags = nltk.FreqDist(tags)
print(tags.items())
plt.bar(unigramas, valores)
plt.show()