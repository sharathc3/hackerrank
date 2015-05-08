n = int(raw_input())
ip_list = []
for i in range(n):
	ip = str(raw_input())
	ip_list.append(ip.lower())
if n == 1:
 	print len(ip)
elif n > 1:
	op = []
	to_remove = []
	for i in range(len(ip_list)):
		if i == 0:
			for ch in ip_list[i]:
				for c in ip_list[i+1]:
					if (c == ch) and (c not in op):
						op.append(c)
		elif i>1:
			for o in op:
				flag = False
				for inp in ip_list[i]:
					# print "o : "+o+" inp : "+inp
					if o == inp:
						flag = True
						break
				if not flag:
					to_remove.append(o)
	# print op
	# print to_remove
	if op:
		print len(op)-len(to_remove)
	else:
		print 0

