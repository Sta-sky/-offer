import re


def testifo():
	while True:
		key_word = input('请输入字母、空格、数字')
		patten = '^[0-9a-zA-Z ]{1,}$'
		data = re.match(patten, key_word)
		if not data:
			print('输入参数只接受数字、字母、空格')
			continue
		break
	word = input('请输入一个字母')
	count = 0
	for i in data.group():
		if i.islower():
			if i == word:
				count += 1
			elif i.upper() == word:
				count += 1
		elif i.isupper():
			if i == word:
				count += 1
			elif i.lower() == word:
				count += 1
			
	return count

if __name__ == '__main__':
	print(testifo())
