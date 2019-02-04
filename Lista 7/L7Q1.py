from gensim.models import Word2Vec
from gensim import models
from gensim.test.utils import common_texts
from sklearn.cluster import KMeans
import numpy

def get_similarities(word):
    result = ""
    if word in words:
        index = words.index(word)
        for i in range(len(words)):
            result = result + words[i] + "\n"
    return result


words = ['banana', 'potato', 'pear', 'pineapple', 'apple', 'turtle', 'peacock', 'dog', 'cat', 'duck', 'swan', 'elephant', 'pig', 'lion', 'penguin', 'cup', 'bowl', 'kettle', 'spoon', 'car', 'truck', 'ship', 'helicopter', 'boat', 'pen', 'pencil', 'knife', 'scissors', 'screwdriver']
model = Word2Vec([words],  min_count=1)

X = model[model.wv.vocab]
def kmeans(n):
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(X)
    print(kmeans.labels_)

kmeans(2)
kmeans(3)
kmeans(4)
kmeans(5)
#print(kmeans.cluster_centers_)

