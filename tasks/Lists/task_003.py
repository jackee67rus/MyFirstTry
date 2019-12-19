'''
Прогрмма выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
Подаётся на вход целое число (>0), n — столько элементов последовательности должна отобразить программа.
На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
'''


# на входе: 15
# на выходе: 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
my_list = []
my_listDic = []
string1 = ""
a = int(input())

yLambda = lambda x, lst: [lst.append(x) for i in range(x)]
xLambda = lambda lstSource, lstDic, b: [lstDic.append(lstSource[j]) for j in range(b)]

for i in range(a):
    yLambda(i+1, my_list)

xLambda(my_list, my_listDic, a)

#string1 = dev.join(str(my_listDic))
# Придумать как заменить этот for
for j in range(len(my_listDic)):
    string1 += str(my_listDic[j]) + " "

print(my_list)
print(my_listDic)
print(string1)
'''
что-то тут не так) выводит не совсем правильную последовательность :)



p = []
t = []
M = []
n = int(input())
l = len(t)
k = 0
m = 2
for h in range(1, n + 1):
    p.append(str(h))
for i in range(0, len(p)):
    if i == 0:
        t.insert(l, p[i])
        k = 0
    elif i == 1:
        while i >= k:
            l = len(t)
            t.insert(l, p[i])
            k += 1
        k -= 2
    elif i > 1:
        while i >= k:
            l = len(t)
            t.insert(l, p[i])
            k += 1
        k = i - m
        m += 1
    l = len(t)
x = len(t)
if len(t) == 1:
    print(1)
else:
    for j in range(0, x - 1):
        M.append(t[j])
    for g in range(0, n):
        print(M[g], end=' ')
'''