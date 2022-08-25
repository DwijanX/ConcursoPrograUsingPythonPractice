import sys

def main():
    string="atcoder"
    L,R=map(int,sys.stdin.readline().split(" "))
    print(string[L-1:R])
main() 