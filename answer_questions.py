import json

def fill_ans_que():
	ques_ans = {}
	while True:
		question=input("вопрос")
		if question == "done":
			break
		answer=input("ответ")
		ques_ans[question] = answer


	#return ques_ans
	#сохранить в json
	with open('data.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
		fh.write(json.dumps(ques_ans, ensure_ascii=False)) #преобразовываем словарь data в unicode-строку и записываем в файл

#filename = ques_ans_file.txt

#if len(answer_questions) != 0 :
	#q_a = answer_questions.ques_ans
#else:
fill_ans_que()

