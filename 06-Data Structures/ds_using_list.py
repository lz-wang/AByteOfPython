# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana'] #列表的初始化
print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')

for item in shoplist:
	print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice') #添加列表元素
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort() #排序列表元素
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0] #删除列表元素
print('I bought the', olditem)
print('My shopping list is now', shoplist)