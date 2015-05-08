from itertools import permutations

st = raw_input()
 
found = False
# try:
# 	# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
# 	perm_string = [''.join(p) for p in permutations(st)]
# 	perm_set = list(set(perm_string))
# 	print len(perm_set)
# 	for p in perm_set:
# 		if p == p[::-1]:
# 			found = True
# 			break
# except Exception,e:
# 	print "Error : "+str(e)

# for perm in set(''.join(p) for p in permutations(st)):
# 	if perm == perm[::-1]:
# 		found = True
# 		break

# def permutationGenerator():
# 	for perm in (''.join(p) for p in permutations(st)):
# 		yield perm

# permGenerator = permutationGenerator()

# for p in permGenerator:
# 	if p == p[::-1]:
# 		found = True
# 		break

ip = list(set(st))
length = []
for i in ip:
	leng = st.count(i)
	length.append(leng)

count = 0
for l in length:
	if l%2 != 0:
		count = count+1

if count <= 1:
	found = True

if not found:
    print("NO")
else:
    print("YES")

# c code
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
# using namespace std;


# int main()
# {
#     string str;
#     cin>>str;
#     int A[26];
#     for(int i =0 ; i<26 ; i++)
#         A[i] = 0;
#     for(int i=0 ; i<str.length() ; i++ )
#     {
#        A[str[i] - 'a']++;
#     }

#     int sum = 0;
#     for(int i=0 ; i<26 ; i++)
#     {
#         sum = sum + (A[i]%2);
#     }

#     if(sum>=2)
#         cout<<"NO"<<endl;
#     else
#         cout<<"YES"<<endl;
#     return 0;
# }