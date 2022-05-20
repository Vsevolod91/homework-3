birthdays_list = ["Юлия: 04.07.1985",
"Владислав: 20.07.1995",
"Николай: 02.05.1963",
"Татьяна: 26.02.1962",
"Роман: 18.04.1992",
"Владимир: 19.07.1972",
"Екатерина: 20.08.1991",
"Дмитрий: 27.09.1989",
"Ярослав: 30.01.1982",
"Алексей: 06.02.1987"]

import random

result = random.sample(birthdays_list, 5)
print("Победители:", result)

days = {
    "01": "первое",
    "02": "второе",
    "03": "третье",
    "04": "четвертое",
    "05": "пятое",
    "06": "шестое",
    "07": "седьмое",
    "08": "восьмое",
    "09": "девятое",
    "10": "десятое",
    "11": "одиннадцатое",
    "12": "двенадцатое",
    "13": "тринадцатое",
    "14": "четырнадцатое",
    "15": "пятнадцатое",
    "16": "шестнадцатое",
    "17": "семнадцатое",
    "18": "восемнадцатое",
    "19": "девятнадцатое",
    "20": "двадцатое",
    "21": "двадцать первое",
    "22": "двадцать второе",
    "23": "двадцать третье",
    "24": "двадцать четвертое",
    "25": "двадцать пятое",
    "26": "двадцать шестое",
    "27": "двадцать седьмое",
    "28": "двадцать восьмое",
    "29": "двадцать девятое",
    "30": "тридцатое",
    "31": "тридцать первое"
}

months = {
    "01": "январь",
    "02": "февраль",
    "03": "март",
    "04": "апрель",
    "05": "май",
    "06": "июнь",
    "07": "июль",
    "08": "август",
    "09": "сентябрь",
    "10": "октябрь",
    "11": "ноябрь",
    "12": "декабрь"
}

date = "04.07.1985"
date = "20.07.1995"
date = "02.05.1963"
date = "26.02.1962"
date = "18.04.1992"
date = "19.07.1972"
date = "20.08.1991"
date = "27.09.1989"
date = "30.01.1982"
date = "06.02.1987"

day, month, year = date.split(".")

i = 1
mistake = 0

for birthday in result:
    birthday_user = input("Введите день рождения {} победителя: ".format(i))
    i += 1
    if birthday_user in birthday:
        print("Вы ввели верную дату рождения")
    else:
        mistake += 1
        print("Верная дата:", days[day], months[month], year, "года")
print("Вы ошиблись", mistake, "раз. Попробуйте снова")


