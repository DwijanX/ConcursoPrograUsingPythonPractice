import sys

def aux(r,c):
    #r=2,c=3
    max=15  
    maxSubq=7
    if r>8:
        r=max-r+1
    if c>8:
        c=max-c+1
    #r7c8
    if r==8:
        if c%2==0:
            print("white",end=" ")
        else:
            print("black",end=" ")
    elif c==8:
        if r%2==0:
            print("white",end=" ")
        else:
            print("black",end=" ")
    elif c<=maxSubq-(maxSubq-(r-1)):
        
        if c%2==0:
            print("white",end=" ")
        else:
            print("black",end=" ")
        
    else:
        if r%2==0:
            print("white",end=" ")
        else:
            print("black",end=" ")

def main():
    centro=8
    max=15  
    r,c=map(int,sys.stdin.readline().split(" "))
    aux(r,c)


main() 


for i in range(1,16):
    print(i,end=" ")
    for j in range(1,16):
        aux(i,j)
    print("",end="\n")