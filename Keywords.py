import sys
from collections import deque 

 
def processWord(word:str):
    newWord=""
    for i in word:
        if i=="-":
            newWord+=" "
        else:
            newWord+=i.lower()
    return newWord
def main():
    Nkeywords=int(sys.stdin.readline())
    RepetitionWords={}
    wordsQ=deque([])
    for Nkey in range(Nkeywords):
        word=str(sys.stdin.readline())
        word=processWord(word)
        if word not in RepetitionWords:
            RepetitionWords[word]=1
            wordsQ.append(word)
    print(len(wordsQ))

main()