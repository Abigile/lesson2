school_jornal = [
{'school_class':'А1','scores':[5,5,5,5,5,5,5,5,5,5,5]},
{'school_class':'Б1','scores':[5,4,5,4,4,4,5,5,5,5,5]},
{'school_class':'В1','scores':[5,4,3,5,5,5,4,4,5,4,3]},
{'school_class':'Г1','scores':[5,5,4,4,5,4,5,4,5,4,5]},
{'school_class':'Д1','scores':[3,3,4,4,4,4,4,4,5,5,5]}]



teacher_jornal = {}
mid_bal2 = 0
summ1 = 0
a = 0

for sclass in school_jornal:
	#заходим в словарь - класс
	for school_class, scores in sclass.items():
		mid_bal = 0
		#открываем лист оценок
		for i in sclass['scores']:
			mid_bal = mid_bal + i
		#у нас есть сумма баллов и сумма учеников
		summ = len(sclass['scores'])
		mid_bal1 = mid_bal
		mid_bal = mid_bal / len(sclass['scores'])
		#отмечаем класс в журнале учителя
		teacher_jornal[sclass['school_class']] = mid_bal
		
	mid_bal2 = mid_bal2 + mid_bal1
	summ1 = summ1 + summ

mid_school_ball = mid_bal2 / summ1
print('\nСредний бал по школе : {} \n'.format(round(mid_school_ball,2)))
		
for class_name,midbal in teacher_jornal.items():
	print('Класс: {} средний бал: {} '.format(class_name,round(midbal,2)))
