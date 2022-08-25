from operator import index
from re import search
import sys

def searchForNumbersInList(numbers,list):

    Columns=[]
    indexList=0
    ListLen=len(list)
    for ind,val in enumerate(numbers):
        while(indexList<ListLen):
            if list[indexList]==val:
                Columns.append(indexList)
                break
            indexList+=1
        if ind+1!=len(Columns):
            return []
    return Columns

def CompareTwoLists(l1,l2):
    lenL1=len(l1)
    lenL2=len(l2)
    if lenL1!=lenL2:
        return False
    for i in range(lenL1):
        if l1[i]!=l2[i]:
            return False
    return True
        

def main():
    r1,c1=map(int,sys.stdin.readline().split(" "))
    A=[]
    for i in range(r1):
        A.append([ int(x) for x in sys.stdin.readline().split(" ") ])
    r2,c2=map(int,sys.stdin.readline().split(" "))
    B=[]
    for i in range(r2):
        B.append([ int(x) for x in sys.stdin.readline().split(" ") ])
    PossibleColumnsDetected=[]
    firstAdetected=-1
    RowA=0
    RowB=0
    while(RowB<r2):
        while(RowA<r1):
            aux=searchForNumbersInList(B[RowB],A[RowA])
            if aux!=[]:
                if PossibleColumnsDetected==[]:
                    PossibleColumnsDetected=aux
                    firstAdetected=RowA
                elif CompareTwoLists(PossibleColumnsDetected,aux)==False:
                    RowB=0
                    RowA=firstAdetected+1
            RowA+=1
        PossibleColumnsDetected=[]
        RowB+=1
    if PossibleColumnsDetected==[]:
        print("No")
    else:
        print("Yes")

                
    
    




#print(searchForNumbersInList([3,1,2],[1,4,3,5,6,2]))
main()