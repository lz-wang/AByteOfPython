import pickle

shoplistfile = 'shoplist.data' # 存储的文件名

shoplist = ['apple', 'mango', 'carrot'] # 存储内容

f = open(shoplistfile, 'wb') # 二进制写入

pickle.dump(shoplist, f) # 封装
f.close()

del shoplist

f = open(shoplistfile, 'rb') # 二进制读出

storedlist = pickle.load(f) # 拆封
print(storedlist)