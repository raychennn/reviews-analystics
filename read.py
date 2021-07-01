data = []
count = 0
with open('reviews.txt' , 'r') as f:#計算資料筆數
	for line in f:
		data.append(line)
		count+=1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完畢，總共有',len(data),'筆資料')

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] >100:
		print(word,wc[word])

while True:
	word = input('請輸入想查找的字：')
	if word == 'q':
		break
	if word in wc:
		print(word , '出現的次數為：' , wc[word])
	else:
		print('這個字不存在留言')
print('感謝查詢')





sum_len = 0#計算資料平均長度
for d in data:
	sum_len+= len(d)

print('留言平均長度為',(sum_len/len(data)))

new = []#篩選字數小魚100字的資料
for d in data:
	if len(d)<100:
		new.append(d)
print('一共有' , len(new) , '筆資料長度小於100')

good = []#篩選特定字
for d in data:
	if 'good' in d:
		good.append(d)
#也可以寫成
good = [d for d in data if 'good' in d]
print('一共有',len(good),'筆資料含good')
#尋找差評
bad = ['bad' in d for d in data]
print(bad)

