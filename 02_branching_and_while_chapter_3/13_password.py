# Пароль
# Демонстрирует использование конструкции if else с циклом while
# Если идти строго по книге, то здесь должна быть только if

import time

print("")
print("Дoбpo пожаловать к нам в ООО \"Системы безопасности\". ")
print("-- Безопасность - наше второе имя\n")

while True:

	password = input("Введите пароль: ")

	if password == "secret":
		time.sleep(1)
		print("\n\tДocтyп открыт")
		break # выход из цикла, если пароль верный
	else: 
		time.sleep(1)
		print("\n\tНеверный пароль\n")
	
input("\nHaжмитe Enter, чтобы выйти")

# Оператор «равно» состоит из двух знаков равенства. 
# Если оставить только один, то система выдаст ошибку, потому что одиночный знак равенства используется в контексте присвоения значений переменным.
# Выражение password = «secret» - это конструкция, в которой переменной password присваивается значение «secret». 
# А вот password == «secret» - это условие, результат проверки которого имеет вид True или False. 

# Операторы сравнения

#Оператор    Значение            Пример     Истинность 
# --         Равно               5 == 5     True 
# !=         Не равно            8 != 5     True
# >          Больше              3 > 10     False 
# <          Меньше              5 < 8      True 
# >=         Больше или равно    5 >= 10    False 
# <=         Меньше или равно    5 <= 5     True