
def main():
    inp=int(input())
    distances=[]
    while(inp!=-1):
        tempTime=0
        distance=0
        for i in range(inp):
            speed,time=input().split(" ")
            timeInt=int(time)
            time=timeInt-tempTime
            tempTime=timeInt
            distance+=int(speed)*time
        distances.append(str(distance)+" miles")
        inp=int(input())
    for ans in distances:
        print(ans)
            
main()
