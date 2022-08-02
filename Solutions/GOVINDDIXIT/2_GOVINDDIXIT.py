m=[int(i) for i in input().split()]
n = sorted(m)
for item in m:
    a = n.index(item) + 1
    b = n.count(item)
    ans=(a*b+b*(b-1)/2)/b
    print(ans,end=" ")
