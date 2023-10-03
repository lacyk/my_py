import string 
import os
import time

abc = string.ascii_lowercase
lst_abc = list(abc)
lst_abc.append(" ")

word = "hello world"
word_len = len(word)
tmp = ""
finish = ""
i = 0

# the way to add letter to final 
# finish += lst_abc[6]

# print(lst_abc)


while i < word_len:
	for e in lst_abc:
		time.sleep(0.1)
		tmp = finish + e
		os.system('clear')
		print(tmp)
		if e == word[i]:
			finish += e
			break
	i+=1


os.system('clear')
print(finish)
