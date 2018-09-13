import json
import config

def save():


	#открываем файл на запись
	with open('data.json', 'w', encoding = 'utf-8') as fh: 
		 #преобразовываем словарь data в unicode-строку и записываем в файл
		fh.write(json.dumps(config.ques_ans, ensure_ascii = False))


def load():


	#Открываем файл на чтение.
	with open('data.json', 'r', encoding='utf-8') as fh: 
		#загружаем из файла данные в словарь ques_ans
		config.ques_ans = json.load(fh)


def fill():


	print = ('Пишем словарь. done - закончить заполнение.\n\n')

	while True:
		question = input("вопрос:\n")
		if question == "done":
			break
		answer = input("ответ:\n")
		config.ques_ans[question] = answer
	save()
	menu()


def menu():


	x = input("Мне есть, что ответить?\n да/нет/опции/поясни\n")

	if x == 'да':
		print('отлично)')
		if config.ques_ans :
			load()
			talk()
		else:
			print("(0_0) \n К сожалению словаря нет или он пуст. ")
			menu()

	elif x == 'нет':
		fill()

	elif x == 'опции':
		options()

	elif x == 'поясни':
		readme()
		

def talk():

		
	x = input("Поговорим?\n")
	while True:
		if x == 'пока':
				break
		elif x in config.ques_ans:
			x = input(config.ques_ans[x] + '\n')
		else:
			x = input("""o_O \n Даже не знаю как ответить на это.
				спроси что-нибудь еще\n""")


def readme():


	print("""\nИзначально у бота нет словаря.
\nКогда он приступает к созданию словаря,
он запрашивает у пользователя вопросы и ответы, 
попутно занося их в словарь. 
После словарь сохраняется в файле "data.json".
Если словарь уже есть, то загружается файл со словарем
и идет дальнейшее выполнение программы
			""")
	menu()


def options():


	xx = input('''
		Что ты хочешь сделать?\n\n
		1 - вернуться в меню \n\n
		2 - записать словарь вопросов и ответов\n\n 
		3 - редактировать словарь\n\n
		''')

	if xx == "1" :
		menu()

	if xx == "2" :
		fill()

	if xx == "3" :
		editor()

def editor():
	if config.ques_ans:
		print = ('Редактируем словарь. done - закончить редактирование.\n\n')

		copi_ques_ans = config.ques_ans
		for question in set(config.ques_ans):
			question = str(question)
			print('Вопрос: %s' %(question))
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
			menu()

		load()
		menu()
	else:
		print("(0_0) \n К сожалению словаря нет или он пуст. ")
		editor()

	
#Program start.
#Открываем файл на чтение.
load()
editor()##################
menu()