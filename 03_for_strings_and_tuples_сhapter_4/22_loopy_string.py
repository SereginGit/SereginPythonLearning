# Слово по буквам
# Демонстрирует применение цикла for к строке

import time

print("")

word = input("Введите слово:\n\n")
print("\nBoт все буквы вашего слова по порядку:\n")

for letter in word:
    print(letter)
    time.sleep(1)
    
input("\nHaжмитe Enter, чтобы выйти")