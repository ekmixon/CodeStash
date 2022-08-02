for _ in range(int(input())):
	s=input().split(".")
	a = [s[j] for j in range(len(s)-1,-1,-1)]
	print(".".join(a))