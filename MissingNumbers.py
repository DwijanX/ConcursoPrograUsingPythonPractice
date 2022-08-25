from collections import deque
import sys


def main():
    n1=int(input())
    arr=deque(map(int,sys.stdin.readline().split(" ")))
    n2=int(input())
    brr=deque(map(int,sys.stdin.readline().split(" ")))
    alreadyaddedNumbers=dict()
    for i in range(n2):
        aux1=brr.pop()
        
        if i<n1:
            aux2=arr.pop()
        if aux1!=aux2:
            if aux1 in alreadyaddedNumbers:
                alreadyaddedNumbers[aux1]+=1
            else:
                alreadyaddedNumbers[aux1]=1
            if aux2 in alreadyaddedNumbers:
                alreadyaddedNumbers[aux2]-=1
            else:
                alreadyaddedNumbers[aux2]=-1
    
    ansList=[i for i in alreadyaddedNumbers if alreadyaddedNumbers[i]>0]
    ansList.sort()
    for i in ansList:
        print(i,end=" ")
main()

