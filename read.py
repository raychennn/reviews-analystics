data = []
count = 0
with open('reviews.txt' , 'r') as f:#計算資料筆數
	for line in f:
		data.append(line)
		count+=1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完畢，總共有',len(data),'筆資料')

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
print('一共有',len(good),'筆資料含good')
