my_list = []

num_str = (input("Введите несколько цифр через запятую, слеш или точку с запятой: "))

num_str = num_str.replace(",", "").replace("/", "").replace(";", "").replace(" ", "")

for number in num_str:
    my_list.append(number)

print(my_list)

for del_number in my_list:
    if my_list.count(del_number) > 1:
        while my_list.count(del_number) != 0:
            my_list.remove(del_number)
print(my_list)