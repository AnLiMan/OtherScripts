# Первая часть
print('\nПервая часть')

def city_country(city='No City', country='No Country'):
    return city, country

print(city_country('Челябинск', 'Рашка'))
print(city_country('Нью-Йорк', 'США'))
print(city_country('Барселона', 'Испания'))
print('\nБез двух аргументов')
print(city_country())

# Вторая часть
print('\nВторая часть')

def make_album(singer, name, track_number = 1):
    return 'Певец - ', singer, 'Название - ', name, 'Номер трека - ', track_number

print(make_album('Skillet', 'Monster'))
print(make_album('Sabaton', 'Carolus Rex'))
print(make_album('Alan Walker', 'Faded', 5))

# Третья часть
print('\nТретья часть')
inputData = True
#Список, в котором будут хванится введенные данные
data_list = []

def DataPrint (data):
    print (data)

print('\nВведите что-нибудь, когда закончите введите "quit"')
while inputData == True:
    Data = input()
    data_list.append(Data)
    if (Data == 'quit'):
        inputData = False
        data_list.remove(Data)
#Выведем список
DataPrint(data_list)