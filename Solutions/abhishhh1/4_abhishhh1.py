def longest_size(a):
    size=0
    seq=[]
    flag=0
    for i in range(len(a)):
        seq = [a[i]]
        for j in range(len(a)):
            if i==j:
                continue
            flag=1
            for item in seq:
                if item % a[j] != 0 and a[j] % item != 0:
                    flag=0
            if flag:    
                seq.append(a[j])
            if len(seq)>size:
                size=len(seq)
    return -1 if size<=1 else size
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    print(longest_size(a))
