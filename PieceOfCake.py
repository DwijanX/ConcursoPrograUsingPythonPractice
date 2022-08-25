
import sys

def getMaxBorder(LengthSide,Var):
    if LengthSide/2>Var:
        return (LengthSide-Var)
    else:
        return Var

def main():
    MaxPiece=4
    LengthSide,h,v=sys.stdin.readline().split(" ")
    LengthSide=int(LengthSide)
    MaxPiece=MaxPiece*getMaxBorder(LengthSide,int(h))*getMaxBorder(LengthSide,int(v))
    print(MaxPiece)

main()