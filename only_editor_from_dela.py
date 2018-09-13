import json
import config

with open('data.json', 'r', encoding = 'utf-8') as fh: 
			#загружаем из файла данные в словарь ques_ans
	config.ques_ans = json.load(fh)


		#Окно редактора
copi_ques_ans = config.ques_ans
for question in set(config.ques_ans):
	print('Вопрос: %s' %question)
	print('Ответ: %s' %config.ques_ans[question])
	xxx = input('''
				1 - дальше
				2 - Изменить вопрос
				3 - Изменить ответ
				4 - Удалить пару вопрос-ответ
				5 - Добавить пару вопрос-ответ
				6 - Сохранить и выйти в меню
				''')
	if xxx == "2" :
		zz1 = config.ques_ans[question]
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
		question = input("добавить вопрос:\n")
		answer = input("добавить ответ:\n")
		copi_ques_ans[question] = answer
	if xxx == "6" :
		#открываем файл на запись
		with open('data.json', 'w', encoding = 'utf-8') as fh: 
		#преобразовываем словарь data в unicode-строку и записываем в файл
			fh.write(json.dumps(copi_ques_ans, ensure_ascii = False))