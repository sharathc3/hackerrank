inp1 = list(raw_input())
inp2 = list(raw_input())

a, b = inp1, inp2

for ip1 in inp1:
	# print "ip1 : "+str(ip1)
	for ip2 in inp2:
		# print "ip2 : "+str(ip2)
		if ip1 == ip2:
			# print "Inp1 : "+str(a)+" Ip1 : "+ip1
			# print "Inp2 : "+str(b)+" Ip2 : "+ip2
			a[a.index(ip1)] = ""
			b[b.index(ip2)] = ""
			# print "Inp1 : "+str(a)
			# print "Inp2 : "+str(b)
			break
a = filter(None, a)
b = filter(None, b)
# print a
# print b
print len(a)+len(b)