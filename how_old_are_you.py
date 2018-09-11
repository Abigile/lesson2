def social_distributor(age):
	"""запрашивает возраст и возвращает комментарий"""
	age = int(age)
	if age < 6:
		text = "Малыш, отойди от компьютера." 
	elif age > 6 and age < 16:
		text = "А в каком ты уже классе?"
	elif age > 16 and age < 23:
		text = "По какой специальности учитесь?"
	elif age > 23 and age < 65:
		text = "Вы уже работник месяца?"
	elif age > 65 and age < 130:
		text = "Поздравляем! Вы пенсионер!"
	elif age > 130:
		text = "Вообразите, государство выплачивает вам пенсию дольше, \n чем вы платили налоги \n O_o"
	
	return text

print('"Choose your destiny" приветствует вас"  \n\tТолько для 2+')
age = input('Пожалуйста,  укажите сколько вам полных лет.\n')
a = social_distributor(age)
print (a)