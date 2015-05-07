#!/bin/python

# Complete the function below.
from operator import xor

def maxXor(l,r):
	flag = 1
	a,b = l,l 
	x = []
	# y = []
	while(flag):
		# y.append((a,b))
		x.append(xor(a,b))
		# print a
		# print b
		if b == r:
			a = a+1
			b = a-1
		if b < r:
			b = b+1
		if a == r and b == r:
			flag = 0
	# y.append((a,b))
	x.append(xor(a,b))
	return max(x)
	# xor_max_index = []
	# for m in x:
	# 	print m
	# 	if m == max_xor:
	# 		print "index "+str(x.index(m))
	# 		xor_max_index.append(x.index(m))
	# return xor_max_index
	# print a
	# print b

l = int(raw_input())
r = int(raw_input())

res = maxXor(l, r)
print(res)