# Манипуляции с цитатой 
# Демонстрирует строковые методы 
# Цитата из Томаса Уотсона, который в 1943 г. был директором IBM 

import time
quote = "Думаю, на мировом рынке можно будет продать штук пять компьютеров."

print("")
time.sleep(3)
print("Исходная цитата") 
print(quote) 
time.sleep(3)
print("\nOнa же в верхнем регистре:") 
print(quote.upper()) 
time.sleep(3)
print("\nB нижнем регистре:") 
print(quote.lower()) 
time.sleep(3)
print("\nKaк заголовок:") 
print(quote.title()) 
time.sleep(3)
print("\nC ма-а-аленькой заменой:") 
print(quote.replace("штук пять", "несколько миллионов"))
time.sleep(3)
print("\nA вот опять исходная цитата:") 
print(quote) 
time.sleep(3)
input("\nHaжмитe Enter. чтобы выйти.") 