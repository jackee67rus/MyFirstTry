my_list = []
a = int(input())
for i in range(a):
    count = 0
    if a == 1:
        print(a)
        break
while count <i + 1:
    my_list.append(i + 1)
    count += 1
    if len(my_list) == a:
        print(my_list)
        break
'''
что-то тут не так) выводит не совсем правильную последовательность :)
'''