# Рантье (версия с ошибкой) 
# Демонстрирует логическую ошибку 

print(
""" 
\nРантье 
\nПрограмма подсчитывает ваши ежемесячные расходы.  
Введите суммы расходов по всем статьям, перечисляемым ниже. 
Пишите суммы в долларах, без центов. 
"""
)

саг = input("Техническое обслуживание автомобиля: ") 
гent = input("Аренда  квартиры: ") 
jet = input("Apeндa самолета: ") 
gifts = input ("Подарки: ") 
food = input("Oбeды и ужины: ") 
games = input("Компьютерные игры: ") 
staff = input("Жалованье персонала (повар, водитель, секретарь): ") 
guгu = input( "Жалованье психолога: ") 
total = саг + гent + jet + gifts + food + staff + guгu + games 
print("\nОбщая сумма:", total) 
input("\nHaжмитe Enteг, чтобы выйти.")