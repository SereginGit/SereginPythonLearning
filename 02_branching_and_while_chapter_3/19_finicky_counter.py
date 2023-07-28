# Привередливая считалка 
# Демонстрирует работу команд break и continue 

import time

print("")
count = 0
while True: 
    count += 1 
    # Завершить цикл, если count принимает значение больше 10
    if count > 10: 
        break 
    # Пропустить 5 
    if count == 5: 
        continue 
    time.sleep(1)
    print(count) 
    
input("\nHaжмитe Enter, чтобы выйти.") 
