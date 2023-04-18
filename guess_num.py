#  產生一個隨機整數1~100(不要印出來)
#  讓使用者重複輸入數字去猜猜看
#  猜對的話，印出"恭喜猜對了!"
#  猜錯的話，要告訴使用者，比答案大/小
#  延伸: 印出猜了幾次 count變數
#  延伸2: 讓使用者自行決定範圍

import random
start = input('開始值: ')
end = input('結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0

while True:
	count += 1    # count = count + 1 (快寫法)
	x = input('猜一個數字: ')
	x = int(x)

	if x == r:
		print('恭喜猜對了!')
		break
	else:
		if x > r:
			print('比答案大喔')
		else:
			print('比答案小喔')
	print('這是你猜的第', count, '次')

