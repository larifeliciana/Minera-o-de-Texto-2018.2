import nltk
import L4Q1
import L3Q5_Q6

def corretor(errada, n):
    corpus = open("Corpus_PT.txt",'r', encoding='utf-8').read().lower()
    corretas = set(nltk.word_tokenize(corpus))
    errada = errada.lower()
    dic = {}
    for i in corretas:
        dic.update({i:L4Q1.minimum_edit_distance(i, errada, 0)[-1][-1]})


    candidatas = [i for i in dic if dic[i] <= n]

    return candidatas

print("Edit Distance 2")
print(corretor("caza",2))
print(corretor("meza",2))
print(corretor("enscrever",2))
print(corretor("nesza",2))
print(corretor("durx",2))
print(corretor("caxa",2))

print("Edit Distance 1")
print(corretor("caza",1))
print(corretor("meza",1))
print(corretor("enscrever",1))
print(corretor("nesza",1))
print(corretor("durx",1))

print(corretor("caxa",1))


#print(corretor("",2))
#L4Q1.mprint(L4Q1.minimum_edit_distance("virado", "bibrioteca",0))
#corpus = open("Corpus_PT.txt", 'r', encoding='utf-8').read().lower()
#corretas = set(nltk.word_tokenize(corpus))
#print(corretas)