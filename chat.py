#讀取檔案
def read_file(filename):
	with open(filename, "r", encoding="utf-8-sig") as a:
		chats = []
		for chat in a:
			chats.append(chat.strip())
	return(chats)
#寫入檔案
def write_file(filename, chats):
	with open(filename, "w", encoding="utf-8-sig") as b:
		for c in chats:
			b.write(c + "\n")
#改寫格式
def convert(chats):
	chats2 = []
	person = None
	for d in chats:
		if d == "Allen":
			person = "Allen"
			continue
		elif d == "Tom":
			person = "Tom"
			continue
		if person:
			chats2.append(person + ":" + d)
	return chats2
#主程式
def main():
	chats = read_file("input.txt")
	chats = convert(chats)
	print(chats)		
	write_file("input2.txt",chats)

main()




