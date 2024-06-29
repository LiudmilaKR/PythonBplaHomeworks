from random import randint

my_list = [randint(1, 100) for _ in range(10)]
print(f'initial list => {my_list}')
my_list[1] = 8
print(f'изаменили 2-й элемент на 8 => {my_list}')
my_list.append(11)
print(f'добавили 11 в конец списка => {my_list}')