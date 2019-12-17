s = [int(i) for i in input().split()]
n = int(input())
output = []
list = len(s)-1
if n in s:
    for i in range(0, list+1):
        if s[i] == n:
            output.append(i)
    g = len(output)-1
    for j in range(0, g+1):
        print(output[j], end=' ')
else:
    print('Отсутствует')












