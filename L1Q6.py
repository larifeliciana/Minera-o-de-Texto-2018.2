

def getNextToken(stream, currentPosition, internalQuoteFlag, delimiter, whiteSpace):
 onde = ""

 while True:


    if onde is not "l2":
        cursor = currentPosition
        ch = stream[cursor]

    if ch is "*" and onde is not "l2":
        return None,None
    else:
      #   while l2:
            onde = ""
            while ch is not "*" and ch not in delimiter:
                cursor = cursor+1
                ch = stream[cursor]

            if ch is "*":
                return None,None
            if ch in whiteSpace:
                if currentPosition is cursor:
                    currentPosition = currentPosition + 1
                    #go to l1
                    onde  = "l1"


                else:
                    token = stream[currentPosition:cursor]
                    currentPosition = cursor+1
                    return token, currentPosition
            elif ch is '\'' :
               if stream[cursor-1] in delimiter:
                   internalQuoteFlag = True
                   currentPosition = currentPosition+1

                   #go to l1
                   onde = "l1"

               if stream[cursor+1] in delimiter:
                   cursor = cursor+1
                   ch = stream[cursor]
                   #goto l2
                   onde = "l2"

               elif internalQuoteFlag is True:
                   token = stream[currentPosition:cursor-1]
                   internalQuoteFlag = False

               else:
                    token = stream[currentPosition:cursor]


                    currentPosition = cursor+1
                    return token, currentPosition

            if onde is "":
                if cursor is currentPosition:
                    token = ch
                    currentPosition = cursor+1
                else:
                    token = stream[currentPosition:cursor]
                    currentPosition = cursor
                return token, currentPosition




stream = open('texto_pt.txt', 'r').read()+"*"


def tokenize(stream):
    currentPosition = 0
    internalQuoteFlag = False
    delimiter = ['\'', ',', '.', ';', ':', '!', '?', '(', ')', '<', '>', '+', '\"', '\n', '\t', ' ']
    whiteSpace = ['\t', '\n', ' ']
    tokens = []
    fim = False
    while not fim:
        x, currentPosition = getNextToken(stream, currentPosition, internalQuoteFlag, delimiter, whiteSpace)
        if x is not None:
            tokens.append(x)
        else: fim = True
    return tokens

print(tokenize(stream))
