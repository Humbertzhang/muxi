# -*- coding: utf-8 -*-

def is_palindrome(n):

	number = str(n)
	if number[0:] == number[::-1] :
		return number
#[::-1] 意味将字符串中所有数反过来
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

