count_list = int(input("Введите количество элементов: "))
print("Количество элементов списка", count_list)

my_list = []
i = 1

while len(my_list) < count_list:
    my_list.append(input("Введите {} элемент списка".format(i)))
    i += 1

my_list.sort()

print(my_list)

