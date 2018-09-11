def compare(str1,str2):
	if type(str1) and type(str2) is str:	
		if str1 == str2:
			print(1) 
		elif str2 == "learn":	
			print(3) 
		elif len(str1) > len(str2):
			print(2) 
	else:
		print(0)

print('не строковые данные: ')
compare(5353,646456)

print('другие не строковые данные: ')
compare(True,5.646456)

print('строки одинаковые: ')
compare('gffgnn','gffgnn')

print('строки разные и первая длиннее: ')
compare('tegdfgdgdg','sfgd')

print('стоки разные и вторая "learn": ')
compare('grgrgg','learn')
