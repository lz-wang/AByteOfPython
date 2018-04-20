poem = '''\
Programing is fun
When the work is done 
if you wanna make your work also fun:
	use PYTHON!
'''

f = open('poem.txt', 'w') # 打开文件
f.write(poem) # 写入文件
f.close() # 关闭文件

f = open('poem.txt')
while True:
	line = f.readline()
	if len(line) == 0:
		break
		print(line, end='')
f.close()