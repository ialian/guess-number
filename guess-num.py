# 猜數字遊戲
# 讓使用者重複輸入數字去猜
# 如果正確回答你答對了，如錯誤則告知猜的數值比答案大或小

import random

r = random.randint(1,100)
count = 0
while True:
	count = count + 1
	num = input('請猜數字: ')
	num = int(num) # 型別轉換
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
