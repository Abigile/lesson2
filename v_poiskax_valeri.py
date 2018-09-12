def iseekyou (spis1,spis2,seek):
	piple = 'ищем'
	x=0
	while piple != seek:
		piple = spis1.pop(1)
		x+=1
	print('Мы нашли {}!'.format(spis2[x]))

a = ['Вася','Маша','Петя','Валера','Саша','Даша']
b = ['Васю','Машу','Петю','Валеру','Сашу','Дашу']

seek = input('Сегодня в школу не пришли: \n {}, \n кого из них будем вызванивать?\n'.format(a))

iseekyou(a,b,seek)


