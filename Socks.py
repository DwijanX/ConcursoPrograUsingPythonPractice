import sys
from collections import Counter,deque

def main():
    S,C,K=map(int,sys.stdin.readline().split(" "))
    Values=Counter(map(int,sys.stdin.readline().split(" ")))
    minVal=min(Values)
    maxVal=max(Values)
    ValidSets=[]
    Charges=0
    WaitingSocks=0
    for i in range(minVal,maxVal+1):
        aux1=Values[i]//C
        Charges+=aux1
        WaitingSocks=Values[i]-aux1*C
        Values[i]=0
        j=i+1
        while WaitingSocks>0 and j-i<=K:
            if Values[j]>C-WaitingSocks:
                Values[j]-=C-WaitingSocks
                WaitingSocks=0
                Charges+=1
            else:
                WaitingSocks+=Values[j]
                Values[j]=0
                j+=1;
        if WaitingSocks>0:
            Charges+=1
    print(Charges)

main()
