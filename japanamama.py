import random
#создаем список класссов
#список словарей
	#словарь{ключ:значение,ключ:список}
		#[список]
#сначала начальные классы


#Создаем журнал учителя)
school=[]
liste=[]

abv = ['А','Б','В','Г']
for letter in abv:
	for number in range(5):
		school_class_scores= {}
		classname = letter + str(number+1)
		school_class_scores['school_class'] = classname
		liste.append(classname)

		#список оценок 
		scores = []
		for school_boy in range(10):
			scores.append(random.randint(1,5))
		
		school_class_scores['scores_list'] = scores
		school.append(school_class_scores)
#Журнал учителя создан
print(school)
#20 классов 4 буквы 5 букв на класс в 1 строку не забыть про +1к пределу классов
#a = list(range(0,21,5))
#b = list(range(5,21,5))
#print(a)
#print(b)

#for step in range(4):
	#print(liste[a[step]:b[step]])


mid_ball_class = {}
summ=0
for i in school: #для каждого клсса
	print(school_class_scores['school_class'])
	for ii in school_class_scores['scores_list']: #для каждой оценки
		summ += ii
		mid_class_ball = summ / len(school_class_scores['scores_list'])
	#записываем средний балл по классу в отчетный словарь
	mid_ball_class[school_class_scores['school_class']] = mid_class_ball

print(mid_ball_class)