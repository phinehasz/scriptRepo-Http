# coding=UTF-8
f = abs

print(f(-100))


def magic(x, y, func):
    print(str(func(x)) + str(func(y)))


magic(-100, -200, f)


def normalize(name):
    return name[0].upper()+name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
