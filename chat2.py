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
	allen_comments_count = 0
	allen_sticker_count = 0
	allen_img_count = 0
	viki_comments_count = 0
	viki_sticker_count = 0
	viki_img_count = 0
	for line in chats:
		s = line.split(" ")
		name = s[1]
		time = s[0]
		if name == "Allen":
			if s[2] == "貼圖":
				allen_sticker_count+=1
			elif s[2] == "圖片":
				allen_img_count+=1
			else:
				for line in s[2:]:
					allen_comments_count+=len(line)
		elif name == "Viki":
			if s[2] == "貼圖":
				viki_sticker_count+=1
			elif s[2] == "圖片":
				viki_img_count+=1
			else:
				for line in s[2:]:
					viki_comments_count+=len(line)
	print(viki_comments_count, "傳了:", viki_sticker_count, "個貼圖", allen_comments_count, "傳了:", allen_sticker_count, "個貼圖", "vikiimg: ", viki_img_count, "allenimg: ", allen_img_count)
#主程式
def main():
	chats = read_file("LINE-Viki.txt")
	chats = convert(chats)		
	#write_file("input2.txt",chats)

main()
