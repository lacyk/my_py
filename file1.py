import string 

a = string.ascii_lowercase
b = list(a)
text = 'hello world'
text_len = len(text)

for i in b:
	print(i)
	if i == text.index(i):
		print(i)