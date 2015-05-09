n = int(raw_input())

for i in range(n):
	st = str(raw_input())
	st = list(st)
	if len(st)%2 != 0:
		print -1
	else:
		div = len(st)/2
		st1 = st[0:div]
		st2 = st[div:]
		a,b = st1,st2
		# print st1
		# print st2
		for s1 in st1:
			for s2 in st2:
				if s1 == s2:
					a[a.index(s1)] = ""
					b[b.index(s2)] = ""
					break
		a = filter(None, a)
		b = filter(None, b)
		# print a
		# print b
		print len(a)