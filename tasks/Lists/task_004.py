'''
Программа считывает список чисел lst из первой строки и число x из второй строки, которая выводит
все позиции, на которых встречается число x в переданном списке lst.
Позиции нумеруются с нуля, если число x не встречается в списке,
вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
'''
# s = [int(i) for i in input().split()]
# n = int(input())
output = []
s = [int(i) for i in input().split()]
n = int(input())

myLambda = lambda lst, n, output: [output.append(i) if lst[i] == n else not n for i in range(len(lst))]
'''
<действие> if (Условие) else <другое действие>
'''

if n in s:
    myLambda(s, n, output)
    print(str(output).replace('[', '').replace(']', '').replace(',', ''))
else:
    print('Отсутствует')
