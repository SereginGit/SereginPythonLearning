# Только согласные
# Демонстрирует, как создавать новые строки из исходных с помощью цикла for.

print("")

message = input("Введите текст: ") 
new_message = "" 
VOWELS = "aeiouyаеёиоуыэюя" 
print() 
for letter in message: 
    if letter.lower() not in VOWELS: 
        new_message += letter 
        print("Создана новая строка ", new_message) 
print("\nBoт ваш текст с изъятыми гласными буквами:", new_message) 
input("\nHaжмитe Enter, чтобы выйти.")


#Переменные со сплошь прописными буквами в именах обладают особым значением. 
#Они называются константами и ссылаются на значения, которые не предполагается менять.
#То есть на постоянные величины.

# letter.lower() в строке 11 приводит символы в letter к нижнему регистру и сравнивает с тем, что прописано в VOWELS. 
# Таким образом получаем регистронезависимость.
# Аналогично можно было бы прописать в VOWELS верхний регистр и соответственно letter.upper() в строке 11.