# Персональный привет 
# Демонстрирует получение пользовательского ввода 

import time

print("")
time.sleep(1)

name = input("Привет, как тебя зовут?\n\n") 

print("")
time.sleep(1)

print(name, end="???\n")
time.sleep(1) 

print("\nНу привет,", name, end="!\n") 
input("\nHaжмитe Enter, чтобы выйти.")
