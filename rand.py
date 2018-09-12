import random
slime = []
for i in range(10):
	slime.append(random.randint(1,99))
print('вот список - {}'.format(slime))
for l in slime:
	print(l + 1)

slime = input("введите строку\n")
for i in slime:
	print (i)

