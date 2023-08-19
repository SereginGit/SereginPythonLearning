# Анаrраммы (Word JumЬle)
# Компьютер выбирает какое-пибо слово и хаотически переставляет его буквы
# Задача иrрока - восстановить исходное слово

import random

# начало игры 
print(
"""
\t\t\tДобро пожаловать в игру 'Анаграммы'! 
\t\tНадо переставить буквы так, чтобы получилось осмысленное слово. 
\t(Для выхода нажмите Enter, не вводя своей версии.)
"""
)

# Создадим последовательность слов, из которых компьютер будет выбирать
WORDS = ("питон",
         "анаграмма",
         "простая",
         "сложная",
         "ответ",
         "подстаканник")

# Случайным образом выберем из последовательности одно слово 
word = random.choice(WORDS)

# Создадим переменную, с которой будет затем сопоставлена версия игрока 
correct = word

# Создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично 
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position] 
    word = word[:position] + word[(position + 1):]

print("Boт анаграмма:", jumble) 

guess = input("\nПопробуйте отгадать исходное слово: ") 
while guess != correct and guess != "": 
       print("K сожалению это неправильный ответ.") 
       guess = input("\nПопробуйте отгадать исходное слово: ") 
if guess == correct: 
       print("Дa, именно так! Вы отгадали!\n") 
      
print("Cnacибo за игру.") 
input("\nHaжмитe Enter, чтобы выйти.") 
