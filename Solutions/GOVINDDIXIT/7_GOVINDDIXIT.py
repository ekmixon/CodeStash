t=int(input())
for _ in range(t):
    word=""
    ans=""
    a=str(input())
    for j in a:
        if j=='.':
            ans = ans+word if ans=="" else f'{word}.{ans}'
            word=""
        else:
            word=word+j
    if word!="":
        ans = f'{word}.{ans}'
    print(ans)
