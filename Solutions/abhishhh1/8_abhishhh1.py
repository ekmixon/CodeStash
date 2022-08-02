for _ in range(int(input())):
	r,c=input().split()
	r,c=int(r),int(c)
	b=[]
	for _ in range(r):
		a=[int(x) for x in input().split()]
		b.append(a)
	f=[]
	for j in range(r):
		f.extend(b[j][k] for k in range(c))
	f.sort()
	n=len(f)
	if n%2==1:
		print(f[n // 2])
	else:
		print("according to question r and c both should be odd")
