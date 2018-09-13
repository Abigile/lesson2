def get_answer():
	print('привет!')
	while True:
		try:

			x = input()
		
		except KeyboardInterrupt:
			print('пока')
			break

		if x == "пока":
			break

		print('хм, что значит "{}"?'.format(x))


if __name__ = "__main__":
	get_answer()