# Задача №2:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
a = 0

for i in range(0, 1001):
    if a: break
    for j in range(0, 1001):
        if i + j == s and i * j == p:
            a = 1
            print(i, j)
            break
else:
    print('Нет значений, соответствующих введеным числам')
