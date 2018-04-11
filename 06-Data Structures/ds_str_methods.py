name = 'Swaroop'

if name.startswith('Swa'): #判断开头的字符串
	print('Yes, the string starts with "Swa"')

if 'a' in name: #判断是否包含某些字符
	print('Yes, it contains the string "a"')

if name.find('war') != -1: #判断是否包含指定的字符串，如果找不到返回-1
	print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))