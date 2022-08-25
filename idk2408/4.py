import sys

values={"a":0,"t":1,"c":2,"o":3,"d":4,"e":5,"r":6}
def main():
    word=list("atcoder")
    word2=list(input())
    count=0
    maxlen=7
    while(str(word)!=str(word2)):
        for i,char in enumerate(word):
            if  i<maxlen-1 and values[word2[i]]>values[word2[i+1]] :
                aux1=word2[i]
                word2[i]=word2[i+1]
                word2[i+1]=aux1
                count+=1
    print(count)
    

main()