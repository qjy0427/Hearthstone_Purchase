
def HS_buy():
	import sys
	print("请输入需要购买的符文石数量（输入非正整数结束程序）：")
	try:
		need = int(sys.stdin.readline())
	except:
		print("请输入数字！\n")
		HS_buy()
		return
	if need <= 0:
		print("再见！")
		return
	ans = {}
	options = [488, 388, 328, 128, 60, 30]

	def helper(first, temp):
		for i in range(need//options[first] + 2):
			temp[first] = i
			if first < len(options)-1:
				helper(first+1, temp[:])
			total = 0
			for j in range(len(options)):
				total += temp[j]*options[j]
			if total >= need:
				ans[total] = ans.get(total, []) + [[sum(temp)] + [temp[k] for k in range(len(options))]]
				break

	helper(0, [0, 0, 0, 0, 0, 0])
	res = sorted(ans[min(ans.keys())])[0]
	print("你可以买", end='')
	for i in range(1,7):
		if res[i] != 0:
			print(str(res[i]) + '份' + str(options[i-1]), end='的，')
	print("共需" + str(min(ans.keys())) + "元。\n")
	HS_buy()

HS_buy()



# def HS_buy():
# 	import sys
# 	print("请输入需要购买的符文石数量：")
# 	need = int(sys.stdin.readline())
# 	ans = {}
# 	for a in range(need//488 + 2):
# 		for b in range(need//388 + 2):
# 			for c in range(need // 328 + 2):
# 				for d in range(need // 128 + 2):
# 					for e in range(need // 60 + 2):
# 						for f in range(need // 30 + 2):
# 							total = a*488 + b*388 + c*328 + d*128 + e*60 + f*30
# 							if total >= need:
# 								ans[total] = ans.get(total, []) + [[a+b+c+d+e+f, a, b, c, d, e, f]]
# 								break
# 	res = sorted(ans[min(ans.keys())])[0]
# 	options = [488, 388, 328, 128, 60, 30]
# 	print("你可以买", end='')
# 	for i in range(1,7):
# 		if res[i] != 0:
# 			print(str(res[i]) + '份' + str(options[i-1]), end='的，')
# 	print("共需" + str(min(ans.keys())) + "元。")
#
#
# HS_buy()

