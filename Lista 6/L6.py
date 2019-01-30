from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
from L3Q5_Q6 import carregar
from sklearn import feature_extraction
from sklearn import metrics
from sklearn import feature_selection
def cluster(idf,alg,k,selecionar):
    ##ler data
    d1 = carregar("business")
    c1 = [2 for i in range(30)]
    c2 = [1 for i in range(30)]
    c3 = [0 for i in range(30)]
    labels = c1+c2+c3
    d2 = carregar("sports")
    d3 = carregar("tech")

    if idf:
        tipo = feature_extraction.text.TfidfVectorizer(stop_words="english")

    else :
        tipo = feature_extraction.text.CountVectorizer(binary=True)


    data = tipo.fit_transform(d1+d2+d3)
    if selecionar:
        selection = feature_selection.SelectKBest(feature_selection.chi2, k=k)
        data = selection.fit_transform(data, labels)

    if alg is "kmeans":
        kmeans = KMeans(n_clusters=3,random_state=7).fit(data)
        pred = kmeans.labels_


    else:
        spect = SpectralClustering(n_init=100, assign_labels="discretize", n_clusters=3,random_state=1).fit(data)
        pred = spect.labels_
    #kmeans.labels_array(c1+c2+c3)

    print(metrics.accuracy_score(labels,pred))
#    print(metrics.f1_score(labels, pred, average="weighted"))
print("xx")

cluster(True, 'kmeans', 100,True)
cluster(False, 'kmeans', 100,True)
cluster(True, 's', 100, True)
cluster(False, 's', 100, True)


cluster(True, 'kmeans', 100,False)
cluster(False, 'kmeans', 100,False)
cluster(True, 's', 100, False)
cluster(False, 's', 100, False   )

