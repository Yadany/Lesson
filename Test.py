print('РЕГИСТРАЦИЯ') # Выводит слово "РЕГИСТРАЦИЯ"
name = input('Введите имя пользователя: ') # Регистрируется имя пользователя
password = input('Введите пароль: ') # Регистрируется пароль
password2 = input('Повторите пароль: ') # Подтверждается пароль

if password == password2: # Если зарегистрированный пароль совпадает с подтверждающим,
	print('Вы успешно зарегистрировались!\nВОЙДИТЕ В СИСТЕМУ') # выводится фраза "Вы успешно зарегистрировались!" и "ВОЙДИТЕ В СИСТЕМУ"
else: # Если эти условия не выполняются, 
    print('Пароли не совпадают') # выводится фраза "Пароли не совпадают"
    exit() # и программа завершается

name2 = input('Введите имя пользователя: ') # Вводится имя пользователя
password3 = input('Введите пароль ') # Вводится пароль

if name == name2 and password2 == password3: # Если зарегистрированные имя и пароль совпадают с вводимыми,
	print('Вы успешно вошли в систему!') # выводится фраза "Вы успешно вошли в систему!"
else: # Если эти условия не выполняются, 
    print('Неправильное имя пользователя или пароль!') # выводится фраза "Неправильное имя пользователя или пароль!"

