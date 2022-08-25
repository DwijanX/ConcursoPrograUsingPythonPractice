
from collections import deque

def getSpecialSum(array,i):
    queueaux=deque(array[i:])
    order=1
    Sum=0
    while(order<=len(queueaux)):
        for j in range(order):
            Sum+=int(queueaux.popleft())
        order+=1
    return Sum


n=int(input())
A=input().split(" ")
AEnumeratedIndexes=enumerate(A)
maxIndex=-1
maxValue=0
for ind,val in AEnumeratedIndexes:
    ans=getSpecialSum(A,ind)
    if(ans>maxValue):
        maxValue=ans
        maxIndex=ind
print(maxValue)
