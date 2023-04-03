# Задание:
# Создать список из трех любых элементов.
l = [1, 'hello', True]

# Создать словарь из трех пар ключ-значение.
df = {'ore': 25, 'wood': 117, 'ppl': 0}

# Создать множество из трех элементов.
s = set('dfdfdifdifdifdifidfi')

# Из списка получить элемент с индексом 1
L1 = l[1]

# Написать условие if с двумя блоками elif и блоком else.
party = 'alone'
difficult = 'hard'
if party == 'full' and difficult == 'easy':
    print('Get ready!')
elif party != 'full':
    print('Need more players!')
elif difficult == 'insane':
    print('You cannot win!')
else:
    print('You are not ready for this!')

# Написать цикл while.
i = 234
while i > 0:
    if i != 1:
        if (i % 2) == 0:
            i /= 2
            print(i, end=', ')
        else:
            i = i * 3 + 1
            print(i, end=', ')
    else:
        print('Welcome to Collatz conjecture!')
        break

# Создать список их трех элементов и распечатать его элементы с помощью цикла for
h = [j for j in range(3)]
for i in range(3):
    print(h[i])

# распечатать числа от 0 до 5
Ih = [1, 2, 3, 4, 5]
for lp in Ih:
    print(lp)

# создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'
st = list('TEST')
if ('E' in st) is True:
    print('pass')

# Запросить данные у пользователя и распечатать их используя форматированную строку
count_beer = input('beer: ')
count_coin = input('coin: ')
"Dwarfs like drink {} beers per day and spend {} coins in every tavern.".format(int(count_beer), int(count_coin))

# Распечатать содержимое файла.
f = open('example.txt')
f.read()
f.close()

# Создать функцию, которая принимает два аргумента, вернуть сумму двух аргументов.
def fun1(arg1, arg2):
    sum = arg1 + arg2
    print(sum)

# Создать функцию, которая принимает любое колдичество параметров, распечатать эти параметры.
def fun2(*args):
    print(args)