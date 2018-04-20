def reverse(text):
	return text[::-1] #通过切片功能翻转文本

def is_palindrome(text): # 判断是否为回文单词
	return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
	print("Yes, it is a palindrome")
else:
	print("No, it is not a palindrome")