age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

#请注意，Python 从 0 开始计数，这意味着索引中的第一位是 0，第二位是1，以此类推。

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 通过 end 指定其应以空白结尾：
print('a', end='') #引号内一个空格
print('b', end='')
# 通过 end 指定以空格结尾：
print('a', end=' ') #引号内两个空格
print('b', end=' ')
print('c')

# 转义序列，类似C++
print('what\'s your name?') #显示'等特殊字符
# 在一个字符串中，一个放置在末尾的反斜杠表示字符串将在下一行继续，但不会添加新的一行。
print('This is the first line,\
	this is still the first line.')
print('This is the first line, this is still the first line.')

