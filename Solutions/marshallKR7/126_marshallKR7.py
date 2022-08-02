t=int(input())
for _ in range(t):
    r,c=[int(x) for x in input().split()]
    total=r*c
    arr=[0]*total
    count=0
    for _ in range(r):
        lst=[int(x) for x in input().split()]
        for item in lst:
            arr[count] = item
            count=count+1
    l=len(arr)
    arr.sort()
    print(arr[l // 2])
    