def reverse_vowels(str1):
	v= ""
	for char in str1:
		if char in "aeiouAEIOU":
			v+= char
	rs= ""
	for char in str1:
		if char in "aeiouAEIOU":
			rs += v[-1]
			v=v[:-1]
		else:
			rs += char
	return rs
str1=input()
print(reverse_vowels(str1))