def check_funny():
	inp = str(raw_input())
	inp_rev = inp[::-1]
	for i in range(len(inp)-1):
		if abs(ord(inp[i])-ord(inp[i+1])) != abs(ord(inp_rev[i])-ord(inp_rev[i+1])):
			return "Not Funny"
	return "Funny"

n = int(raw_input())
for i in range(n):
	res = check_funny()
	print res