a = 171
a3 = int(input('Число строк: '))
a4 = a3 - 1


a1 = ' '
a2 = '*'

b = a // 2
c = len(a2)

d = 0

for i in range(a3):
    print(a1 * b, a2 * c, a1 * b)
    b -= 1
    c += 2

while d <= a3:
    print(a1 * b, a2 * c, a1 * b)
    b += 1
    c -= 2
    #print(a1 * b, a2 * c, a1 * b)
    d += 1
