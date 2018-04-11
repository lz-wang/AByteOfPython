print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
#mylist仅仅是shoplist的另一个名字，它们指向的是同一个内容
mylist = shoplist

del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
#删除了shoplist指向的第一项内容后，发现mylist的指向内容也是更改了的

print('Copy by making a full slice')
#通过制作一份完整的切片来进行“深拷贝”
mylist = shoplist[:]
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
#此时的shoplist与mylist内容是不一样的