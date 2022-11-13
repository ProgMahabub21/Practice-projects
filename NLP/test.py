import nltk
#nltk.download('all-nltk')
print("\n")

# Creating token of words
print("Creating token of words:")
from nltk.tokenize import word_tokenize
text="I am Mahabub !! I am a student of Computer Science and Engineering. I am doing my thesis on Natural Language Processing.My groupmates are Saharukh, Changu- Mangu"
tokenize_word=word_tokenize(text)
print(tokenize_word)
print("\n")

# Stemming
print("Stemming:")
from nltk.stem import PorterStemmer
words=["light","lighting","lights"]
ps=PorterStemmer()
for w in tokenize_word:
    rootword=ps.stem(w)
    print(rootword)
print("\n")


#POS Tag
print("POS Tag:")
from nltk import word_tokenize,pos_tag
result = pos_tag(word_tokenize(text))
print(result)    


#Lemmatiztion:Converts allverb forms into root word
print("Lemmatiztion:Converts allverb forms into root word:")
from nltk.stem import WordNetLemmatizer
lem=WordNetLemmatizer()
print(lem.lemmatize(result[0][0],pos="v"))
print("\n")


#Named Entity Recognition
print("Named Entity Recognition:")
from nltk import ne_chunk
print(ne_chunk(pos_tag(word_tokenize(text))))
print("\n")

#Chunking
print("Chunking:")
from nltk import RegexpParser
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = RegexpParser(grammar)
result = cp.parse(pos_tag(word_tokenize(text)))
print(result)
print("\n")


#find the frequency of words
print("find the frequency of words:")
from nltk.probability import FreqDist
fdist = FreqDist(tokenize_word)
print(fdist)
print(fdist.most_common(2))
print("\n")


#find particular word frequency
print("find particular word frequency:")
print(f"The word am is repeacted : {fdist['am']} tinmes")
print("\n")

#find the particular word with location sentences
print("find the particular word with location sentences:")
from nltk.tokenize import sent_tokenize
tokenize_sent=sent_tokenize(text)
for i in tokenize_sent:
    if 'am' in i:
        print(i)
print("\n")



#natural language generation
print("natural language generation:")
from nltk import CFG
grammar = CFG.fromstring("""   
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
from nltk.parse.generate import generate
for sentence in generate(grammar, n=10):
    print(' '.join(sentence))
print("\n")

