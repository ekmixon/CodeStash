a=[int(x) for x in input().split()]
b = sorted(a)
for item in a:
    c = b.index(item) + 1
    d = b.count(item)
    s=(c*d+d*(d-1)/2)/d
    print(format(s,'.1f'),end=" ")
    
    
