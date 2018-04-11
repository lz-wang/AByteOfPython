# ab = AdressBook
ab = {
	'Swaroop': 'swaroop@swaroopch.com',
	'Larry': 'larry@wall.org',
	'Matsumoto': 'matz@ruby-lang.org',
	'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对 键值-值
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
	print('Contact {} at {}'.format(name, address))

# 新增一对 键值-值
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
	print("\nGuido's address is", ab['Guido'])