################################
#     Minimum Edit Distance    #
################################

def criar_matriz(word1, word2):

    matriz = []

    for i in word1+'*':
        matriz.append([])
        for j in word2+'*':
            matriz[-1].append(0)


    for i in range(len(matriz)):
        matriz[i][0] = i

    for i in range(len(matriz[0])-1):
        matriz[0][i+1] = i+1

    return matriz

def minimum_edit_distance(string, string1, npassos):
    matriz = criar_matriz(string, string1)
    insertion = 1
    deletion = 1
    substitution = 2
    match = 0
    count = 0

    for i in range(1,len(matriz)):
        for j in range(1,len(matriz[i])):

         if count % npassos is 0:
             mprint(matriz)

         inserir = matriz[i][j-1] + deletion
         remover = matriz[i-1][j] + insertion
         c1 =string[i-1]
         c2 = string1[j-1]
         if c1 is c2:
            m = matriz[i-1][j-1] + match
         else:
            m = matriz[i-1][j-1] + substitution

         matriz[i][j] = min([inserir,remover, m])
         count = count + 1
    mprint(matriz)

def mprint(matriz):
    for i in matriz:
        print(i)
    print("\n")
minimum_edit_distance("bruta", "bruta",100)
