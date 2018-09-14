import json

pques_ans = {}
print('''Внимание: по достижении последнего вопроса 
	словарь сохраняется и вы выходите из программы.''')

try:
	with open('data.json', 'r', encoding = 'utf-8') as fh: 
		#загружаем из файла данные в словарь ques_ans
		pques_ans = json.load(fh)
except FileNotFoundError:
	print ('Сейчас словарь пуст, но мы добавили в него две пары значений')
	pques_ans["key1"] = "none"
	pques_ans["key2"] = "none"

		#Окно редактора
copi_ques_ans = pques_ans
for question in set(pques_ans):
	print('Вопрос: %s' %question)
	print('Ответ: %s' %pques_ans[question])
	xxx = input('''
				1 - дальше
				2 - Изменить вопрос
				3 - Изменить ответ
				4 - Удалить пару вопрос-ответ
				5 - Добавить пару вопрос-ответ
				6 - Поменять местами вопрос и ответ
				7 - Сохранить и выйти
				8 - Отобразить словарь
				''')
	if xxx == "2" :
		zz1 = pques_ans[question]
		zz = input('Введите вопрос ')
		del copi_ques_ans[question]
		copi_ques_ans[zz] = zz1

	if xxx == "3" :
		zzz1 = question
		zzz = input('Введите ответ ')
		del copi_ques_ans[question]
		copi_ques_ans[zzz1] = zzz
	if xxx == "4" :
		del copi_ques_ans[question]
	if xxx == "5" :
		while True:
			print ("q - выход")
			question = input("добавить вопрос:\n")
			if question == 'q':
				break
			answer = input("добавить ответ:\n")
			copi_ques_ans[question] = answer

	if xxx == "6":
		zz = question
		zz1 = pques_ans[question]
		print('меняем местами {} и {}'.format(zz,zz1))
		del copi_ques_ans[question]
		copi_ques_ans[zz1] = zz

	if xxx == "7" :
		#открываем файл на запись
		with open('data.json', 'w', encoding = 'utf-8') as fh: 
		#преобразовываем словарь data в unicode-строку и записываем в файл
			fh.write(json.dumps(copi_ques_ans, ensure_ascii = False))
		break

	if xxx == "8" :
		yyy = 0
		for question in set(copi_ques_ans):
			print('Вопрос: %s' %question)
			print('Ответ: %s' %copi_ques_ans[question])
			yyy = yyy + 1
		print('В словаре сейчас {} вопросов(а)'.format(yyy))

with open('data.json', 'w', encoding = 'utf-8') as fh: 
	#преобразовываем словарь data в unicode-строку и записываем в файл
	fh.write(json.dumps(copi_ques_ans, ensure_ascii = False))