
Data_input = input('Введите дату в формате dd.mm.gggg')
Data_split = Data_input.split('.')
# print(Data_split)

# Dates = {
#     '01': 'Первое',
#     '02': 'Второе',
#     '03': 'Третье',
#     '04': 'Первое',
#     '05': 'Пятое',
#     '06': 'Шестое',
#     '07': 'Седьмое',
#     '08': 'Восьмое',
#     '09': 'Девятое',
#     '10': 'Десятое',
#     '11': 'Одинадцатое'
# }
# Months = {
#     '01': 'Января',
#     '02': 'Февраля',
#     '03': 'Марта',
#     '04': 'Апреля',
#     '05': 'Мая',
#     '06': 'Июня',
#     '07': 'Июля',
#     '08': 'Августа',
#     '09': 'Сентября',
#     '10': 'Октября',
#     '11': 'Ноября',
#     '12': 'Декабря'
# }

# data_day = Data_input[:2]
# data_month = Data_input[3:5]
# data_year = Data_input[6:]
#
# if data_day in Dates:
#     data_day = Dates[data_day]
#
# if data_month in Months:
#     data_month = Months[data_month]
#
# print(f" {data_day} {data_month} {data_year} года" )

# print(f"{Dates[Data_split[0]]} {Months[Data_split[1]]} {Data_split[2]} года")
Dates = {
    1: 'Первое',
    2: 'Второе',
    3: 'Третье',
    4: 'Первое',
    5: 'Пятое',
    6: 'Шестое',
    7: 'Седьмое',
    8: 'Восьмое',
    9: 'Девятое',
    10: 'Десятое',
    11: 'Одинадцатое'
}
Months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}
first_day = Data_split[0]
first_el_day = first_day[:1]

first_month = Data_split[1]
first_el_month = first_month[:1]

if int(first_el_day) == 0:
    first_day = int(first_day[1:])

if int(first_el_month) == 0:
    first_month = int(first_month[1:])

print(f"{Dates[first_day]} {Months[first_month]} {Data_split[2]} года")


