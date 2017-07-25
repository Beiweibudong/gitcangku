
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
总结：
	１.　reduce使用的functools模块需要导入
	２.　环境需要指定为python3
	３.　str类型数据可以直接用list()转化为单个字符的list
	４.  zip()可以将两个list类型数据组合为[(),()]类型
	5.	格式化字符　%　有多个变量时需要加括号
'''

from functools import reduce
def getIdNum():
	print('请输入身份证号（按回车结束输入）：')
	idnum = input()
	return idnum 

def dataHandle(id_num):
	id = list(id_num)
	idtoint = list(map(int,id))
	idtocheck = idtoint[0:17]
	checkNUM = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
	sumidandcheck = (x*y for x,y in zip(idtocheck,checkNUM))
	sum = reduce(lambda x,y:x+y,sumidandcheck)
	mod = sum % 11
	return mod

def checkBit(mod):
	dict1= {
		0:1,
		1:0,
		2:'X',
		3:9,
		4:8,
		5:7,
		6:6,
		7:5,
		8:4,
		9:3,
		10:2
	}
	check_bit = dict1[mod]
	return check_bit

if __name__ == '__main__':
	id_num = getIdNum()
	mod = dataHandle(id_num)
	check_bit = checkBit(mod)
	print('身份证号为: %s 的校验码为 :%s' % (id_num,check_bit))