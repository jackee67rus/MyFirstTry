'''
Программа считывает список чисел lst из первой строки и число x из второй строки, которая выводит
все позиции, на которых встречается число x в переданном списке lst.
Позиции нумеруются с нуля, если число x не встречается в списке,
вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''
# s = [int(i) for i in input().split()]
# n = int(input())
output = ""
s = [int(i) for i in input().split()]
n = int(input())

if n in s:
    for i in range(len(s)):
        if s[i] == n:
            output += str(i) + " "
    print(output)
else:
    print('Отсутствует')
