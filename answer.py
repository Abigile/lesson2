def get_answer():
	print('привет!')
	while True:
		x = input()
		
		if x == "пока":
			break

		print('хм, что значит "{}"?'.format(x))

get_answer()