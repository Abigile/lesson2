def get_summ(int1,int2):


	print('сложим два числа')

	try:
		summ = int(int1) + int(int2)
	except ValueError:
		print('Данные ваши, миру чисел чужды! <-_->')
		return
	print(summ) 

while True:
	int1 = input('первое число:\n')
	if int1 == "пока":
		break
	int2 = input('второе число:\n')
	get_summ(int1,int2)



