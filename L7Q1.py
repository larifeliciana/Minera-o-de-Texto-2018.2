from gensim.models import Word2Vec
import numpy

words = ['banana', 'potato', 'pear', 'pineapple', 'apple', 'turtle', 'peacock', 'dog', 'cat', 'duck', 'swan', 'elephant', 'pig', 'lion', 'penguin', 'cup', 'bowl', 'kettle', 'spoon', 'car', 'truck', 'ship', 'helicopter', 'boat', 'pen', 'pencil', 'knife', 'scissors', 'screwdriver']

model = Word2Vec([words], size=32, min_count=1)

print(model.similarity("banana", "potato"))

similarities = [[] for i in words]
print(len(similarities))
for i in range(len(words)):
    for j in range(len(words)):
        similarities[i].append(model.similarity(words[i], words[j]))

for sim in similarities:
    print(sim)


def get_similarities(word):
    result = ""
    if word in words:
        index = words.index(word)
        for i in range(len(words)):
            result = result + words[i] + "\n"
    return result


print(get_similarities(words[10]))

for x in similarities:
    line = ""
    for y in x:
        line = line + str(y) + "\t"
    print(line)

# print(model.)

# cosine_similarity = numpy.dot(model['spain'], model['france'])/(numpy.linalg.norm(model['spain'])* numpy.linalg.norm(model['france']))