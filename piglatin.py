from collections import deque

vowels=['a','e','i','o','u']

def Case1(deq:deque):
    while deq[0] not in vowels:
        aux=deq.popleft()
        deq.append(aux)
    deq.append("ay")
    return "".join(deq)

def Case2(deq:deque):
    deq.append("yay")
    return "".join(deq)





def main():
    inputs=[]
    while(1):
        try:
            inp=input()
            inputs.append(inp)
        except EOFError:
            break
    ans=[]
    for i in inputs:
        
        deq=deque(i.split(' '))
        ansxi=""
        while len(deq)!=0:
            aux=deque(deq.popleft())
            if aux[0] in vowels:
                ansxi+=Case2(aux)+" "
            else:
                ansxi+=Case1(aux)+" "
            del aux
        ans.append(ansxi)
    for i in ans:
        print(i)

main()

"""
the quick brown fox
jumps over the lazy dog
and ordinary foxes
dont jump over lazy dogs
"""