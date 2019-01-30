text = open("texto_pt.txt", "r")

a = text.read()
# print(a)
print(len(a))
indexesOfEOS = []


def countWordBehindSize(fullText, actualIndex):
    cont = 0
    aux = actualIndex
    while fullText[aux] != " ":
        aux = aux - 1
        cont = cont + 1

    return cont

def segmentation(a):

    for x in range(len(a)):

        if (a[x] == "\n"):
            continue

        if x+2 < len(a):
            if ((a[x] == "?") or (a[x] == "!")) & ((a[x+1] != "\"") & (a[x+1] != "\'")):
                indexesOfEOS.append(x)
                print("a")
                continue
            if (a[x-1] == "\"" or a[x-1] == "\'") & (a[x] == "."):
                indexesOfEOS.append(x)
                print("b")
                continue
            if (a[x] == ".") & ((a[x+1] != " ") & (a[x+1] != "\n")):
                continue
            if (a[x-1] == "]" or a[x-1] == "}"or a[x-1] == ")") & (a[x] == "."):
                indexesOfEOS.append(x)
                print("c")
                continue
            if (a[x] == ".") & a[x-1].isupper() & countWordBehindSize(a, x-1) < 5 & (a[x+1] != " ") & a[x+1].isupper():
                continue
            if (a[x] == ".") & (a[x-1] == "." or a[x+1] == "."):
                continue
            if (a[x] == ".") & (a[x+1] == " " or a[x+1] == "\n") & (a[x+2].isupper() or a[x+2] == "\n"):
                # if not (a[x - countWordBehindSize(a, x-1)].isupper()):
                    indexesOfEOS.append(x)
                    # print("d")
                    continue
            if (a[x] == ".") & countWordBehindSize(a, x-1) < 2:
                continue
            if (a[x] == ".") & (a[x+1] == " ") & (a[x+2] == "&" or a[x+2] == "(" or a[x+2] == "[" or a[x+2] == "{" or a[x+2].isupper()):
                indexesOfEOS.append(x)
                print("e")
                continue
        elif (a[x] == "?") or (a[x] == ".") or (a[x] == "!") or (a[x] == "]") or (a[x] == "}") or (a[x] == ")"):
            indexesOfEOS.append(x)

    aux = 0
    returnString = a
    for x in indexesOfEOS:
        returnString = (returnString[0:(x+1+aux)] + "[EOS]" + "\n" + returnString[(x+1+aux):])
        aux = aux + 6

    listOfSentences = []

    aux = 0
    for x in indexesOfEOS:
        listOfSentences.append(a[aux:x+1])
        aux = x+1
    listOfSentences.append(a[aux:])

    # for x in range(len(listOfSentences)):
    #     print("-" + listOfSentences[x][0] + "-")
    #     if listOfSentences[x][0] == " " or listOfSentences[x][0] == "\n":
    #         print("yes")
    #         print("a-" + listOfSentences[x])
    #         listOfSentences.insert(x, listOfSentences[x][1:])
    #         print("b-" + listOfSentences[x])
    #         print("c-" + listOfSentences[x+1])
    #         listOfSentences.remove(listOfSentences[x+1])

    print(indexesOfEOS)
    # print(returnString)
    return listOfSentences


for x in segmentation(a):
    print("*" + x)
    print()

st = "aaa bbbbbb cccccc"
print("123".isupper())
text.close()