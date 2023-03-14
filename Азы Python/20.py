# Первая часть
print('\nПервая часть')

# Списоки сэндвичей
sandwich_list1 = ('С магической пыльцой')
sandwich_list2 = ('С магической пыльцой', 'с экстрактом ягуара')
sandwich_list3 = ('С магической пыльцой', 'с макаронами', 'с бальзамическим уксусом')

def DataPrint (*data):
    print (data)

#Выведем списоки
DataPrint(sandwich_list1)
DataPrint(sandwich_list2)
DataPrint(sandwich_list3)

#Вторая часть
print('\nВторая часть')

def make_car(manufacturer, mark, *info):
    print('Производитель - ', manufacturer.title(), ',','Марка - ', mark.title(), '.','Другая информация: ', info)

#Выведем списоки
make_car('BMW', 'M3')
make_car('Audi', 'r8', 'Sport')
make_car('Toyta', 'Corolla')

