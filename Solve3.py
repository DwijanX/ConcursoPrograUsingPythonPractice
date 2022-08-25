from itertools import combinations

H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

for rr in combinations(range(H1), H2):
    print(rr)
    for cc in combinations(range(W1), W2):
        flag = True
        for ib, ia in enumerate(rr):
            #0 (0)
            print(ib,ia)
            for jb, ja in enumerate(cc):
                if A[ia][ja] != B[ib][jb]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            exit(print('Yes'))

print('No')