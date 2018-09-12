import json

def fill_ans_que():
	ques_ans = {}
	while True:
		question=input("вопрос:\n")
		if question == "done":
			break
		answer=input("ответ:\n")
		ques_ans[question] = answer

	#открываем файл на запись
	with open('data.json', 'w', encoding='utf-8') as fh: 
		 #преобразовываем словарь data в unicode-строку и записываем в файл
		fh.write(json.dumps(ques_ans, ensure_ascii=False))
	ask_user()



def ask_user():
	x = input("Мне есть, что ответить?\n да/нет\n")

	if x == 'да':
		print('отлично)')
		#открываем файл на чтение
		with open('data.json', 'r', encoding='utf-8') as fh: 
			#загружаем из файла данные в словарь ques_ans
			ques_ans = json.load(fh)

	if x == 'нет':
		fill_ans_que()




	x = input("Поговорим?")
	while True:
		if x == 'пока':
				break
		elif x in ques_ans:
			x = input(ques_ans[x]+'\n')
		else:
			x = input('o_O \n Даже не знаю как ответить на это.\n спроси что-нибудь еще\n')
		


ques_ans = {}
ask_user()