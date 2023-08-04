# Случайные буквы
# Демонстрирует индексацию строк.

import random 

print("")
word = "индекс"
print("В переменной word хранится слово:", word, "\n")
low = -len(word)
high = len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word [", position, "]\t", word[position])
    
input("\nHaжмитe Enter, чтобы выйти.")

