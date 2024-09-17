goods = [{"name":"电脑","price":1999},
{"name":"鼠标","price":10},
{"name":"游艇","price":20},
{"name":"美女","price":998},]

n = 1
L = []
x = 0
y = 1

total = len(goods)+1
for i in goods:
	for a in i:
		L.append(i.get(a))
	print(n, L[x], L[y])


	n += 1
	x += 2
	y += 2


while(1):
	user_input = input('请输入要打印的商品编号，退出请输入Q：')
	if user_input.lower() == 'q':
		break
	if int(user_input) not in range(0,total):
		user_input = input('输入错误，请按回车：')
	else:
		loop = 1
		x1 = 0
		y1 = 1
		for i in goods:
			for b in i:
				L.append(i.get(b))

				while int(loop) == int(user_input):
					print(user_input, L[x1], L[y1])
					break
				loop += 1
				x1 += 2
				y1 += 2
		


					