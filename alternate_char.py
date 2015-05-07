import string

def calculate_deletion():
	ip = str(raw_input())
	count = 0
	b = ''
	for i in ip:
		a = i
		if a == b:
			count = count+1
		b = a
	return count

n = int(raw_input())
for i in range(n):
	res = calculate_deletion()
	print res
