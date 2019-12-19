'''
программа принимает на вход список однозначных/двузначных чисел в одной строке и выводит
на экран в одну строку значения, которые повторяются в нём более одного раза.
Выводимые числа не должны повторяться.
'''

#income = [int(i) for i in input().split()]
#output = []
#income.sort()
my_list = sorted([int(i) for i in input().split(' ')])
second_list = []
for i in range(len(my_list)-1):
    b = my_list[i]
    if b == my_list[i+1]:
        second_list.append(my_list[i])
print(second_list)
print('Саня бухой')
