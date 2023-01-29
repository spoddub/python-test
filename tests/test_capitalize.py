from capitalize import capitaize

if capitaize('hello') != 'Hello':
	raise Exception('Функция работает неверно!')
if capitaize('') != '':
	raise Exception('Функция работает неверно!')
