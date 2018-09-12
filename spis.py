
spisok = []
for t in range (10):
	spis = []
	for i in range(10):
		spis.append(i)
	print(spis)

	slov = {}
	slov['spison'] = spis
	spisok.append(slov)

print (spisok)