b = []
with open ("3.txt", "r", encoding="utf-8-sig") as a:
	for line in a:
		b.append(line.strip("\n"))
for line in b:
	s = line.split(" ")
	time = s[0][:5] 
	name = s[0][5:]
	print(name)
	print(time)
