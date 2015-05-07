test_cases = int(raw_input())
for i in range(test_cases):
	height = 1
	test = int(raw_input())
	for j in range(test):
		if j%2 == 0:
			height = height * 2
		else:
			height = height+1
	print height