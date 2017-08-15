from nltk.corpus import wordnet as wn
synonyms=[]
def findsynonyms(givenword):   
    for syn in wn.synsets(givenword):
        for l in syn.lemmas():
            synonyms.append(l.name()) 
    return synonyms            
            
synonym=findsynonyms("love")
print (synonym)  
