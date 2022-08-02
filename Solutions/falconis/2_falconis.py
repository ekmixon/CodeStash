arr = list(map(int,input().split()))
n = len(arr)
ranks = [0 for _ in range(n)]
for x in range(n):
    rep = 1
    rank = 1
    for y in range(n):
        if arr[y] < arr[x] and y != x:
            rank += 1
        if arr[y] == arr[x] and y!= x:
            rep += 1

    rrank = (rank*rep + rep*(rep-1)/2)/rep
    ranks[x] = rrank

for x in range(n):
    print(ranks[x],end= " ")