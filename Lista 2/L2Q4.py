import nltk

frase = "The last love letter I wrote was probably about 10 years ago"
frase = nltk.word_tokenize(frase)

grammar = nltk.CFG.fromstring("""
 S -> NP VP
 PP -> P NP
 NP -> Det N | NP PP
 VP -> V NP | VP PP
 Det -> 'a' | 'The'
 N -> 'love' | 'letter' | 'I' | 'years' | 'was'
 V -> 'wrote'
 P -> 'on' | 'in' | 'about' | 'last' | 'ago' | 'probably' | '10'
  """)


parser = nltk.ChartParser(grammar)
for tree in parser.parse(frase):
    print(tree)
