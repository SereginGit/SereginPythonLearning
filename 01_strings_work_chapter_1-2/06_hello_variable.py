# Привет 
# Демонстрирует использование переменных 

import time

name = "Мария"
patronymic = "Игоревна"

print("")

time.sleep(1)

print(name, patronymic) 

time.sleep(1)

print("\nПривет,", name, patronymic, end="!\n")

time.sleep(1)

input("\nHaжмитe Enter, чтобы выйти")

# end=".\n" убирает пробел между значением patronymic и восклицательным знаком
# Привет, Мария Игоревна!
# Если вместо end="!\n" прописать просто "!", то вывод будет:
# Привет, Мария Игоревна !

