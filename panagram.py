import string

def test_panagram(s):
	t = list(string.ascii_lowercase)
	for var in s:
		if var.lower() in t:
			t.remove(var.lower())
	if t:
		return "not pangram"
	else:
		return "pangram"

ip = str(raw_input())
res = test_panagram(ip)
print res