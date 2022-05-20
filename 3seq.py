count_list_n1 = int(input("Введите количество элементов 1го списка: "))
print("Количество элементов 1го списка", count_list_n1)

my_list_n1 = []
i = 1

while len(my_list_n1) < count_list_n1:
    my_list_n1.append(input("Введите {} элемент списка: ".format(i)))
    i += 1

print("Список 1:", my_list_n1)

count_list_n2 = int(input("Введите количество элементов 2го списка: "))
print("Количество элементов 2го списка", count_list_n2)

my_list_n2 = []
n = 1

while len(my_list_n2) < count_list_n2:
    my_list_n2.append(input("Введите {} элемент списка: ".format(n)))
    n += 1

print("Список 2:", my_list_n2)

intersection_set = set(my_list_n1).intersection(my_list_n2)

for number in intersection_set:
    my_list_n1.remove(number)
print("Измененный список 1:", my_list_n1)

