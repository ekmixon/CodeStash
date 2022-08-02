t = int(input())

for _ in range(t):
    count = 0
    n = int(input())
    ls = list(map(int,input().split()))
    mem = int(input())
    cache = []
    for i in range(n):
        ele = ls[i]
        if ele in cache:
            del cache[cache.index(ele)]
        else:
            if len(cache)>=mem:
                del cache[0]
            count += 1
        cache.append(ele)
    print(count)
            