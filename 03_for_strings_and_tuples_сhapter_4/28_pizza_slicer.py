# Резчик пиццы 
# Демонстрирует срезы строк 

word = "пицца"
print("")

print(
"""
Памятка

0   1   2   3   4   5 
+---+---+---+---+---+ 
| п | и | ц | ц | а | 
+---+---+---+---+---+ 
-5  -4  -3  -2  -1 
"""
)

print("Введите начальный и конечный индексы для того среза 'пиццы', который хотите получить.") 
print("Для выхода нажмите Enter, не вводя начальную позицию") 
start = None 
while start != "":
    start = (input("\nНачальная позиция: ")) 
    if start: 
        start = int(start) 
        finish = int(input("Koнeчнaя позиция: ")) 
        print("Cpeз word [", start, ":", finish, "] выглядит как", end=" ") 
        print(word[start:finish]) 
        
input("\nHaжмитe Enter, чтобы выйти.")

# С помощью None в Python принято представлять пустое значение, заместитель еще не присвоенного. 
# В условной интерпретации None рассматривается как ложное False.
# В данном случае None нужно, чтобы инициализировать start для указания в условии цикла whilе. 

# Срезы можно сокращать.  
# Из возможных сокращений в записи срезов следует запомнить [:] - это способ получить точную копию последовательности.

