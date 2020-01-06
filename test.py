# use_time: 15 mins

def how_many_ways(digitarray):

	# 收敛条件
	if len(digitarray) == 3:
		if 9<int(digitarray[1:])<26 and 9<int(digitarray[:-1])<26:
			return 3
		elif int(digitarray[1:])>25 and int(digitarray[:-1])>25:
			return 1
		else:
			return 2
	elif len(digitarray) == 2:
		if int(digitarray)<26:
			return 2
		else:
			return 1
	elif len(digitarray) == 1:
		return 1

	# 递归
	if int(digitarray[:2])<26 and int(digitarray[0])!=0:
		return how_many_ways(digitarray[2:]) + how_many_ways(digitarray[1:])
	else:
		return how_many_ways(digitarray[1:])


if __name__ == '__main__':

	while True:
		digitarray = input('请输入一串编码：\n')
		print('解码方式种数有：',how_many_ways(digitarray))









