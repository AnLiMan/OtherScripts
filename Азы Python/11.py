#Исходный словарь
print("\nПервая часть")
NewDict = {'first_name':'Андрей',
'last_name': 'Лисов',
'city': 'Zlatoust'}
print(NewDict.items())
print(NewDict.keys())
print(NewDict.values())

print("\nВторая часть")
NewDict2 = {'Андрей':'1',
'Маша': '2',
'Миша': '3',
'Вася': '4',
'Паша': '5'}
print(NewDict2.items())
print(NewDict2.keys())
print(NewDict2.values())

print("\nТретья часть")
glossary = {'Гвоздь -': 'прямой кусок проволоки, с одном острым и тупым концом (шляпкой)',
'Шуруп - ': '"кудрявый" гвоздь',
'Кот - ': 'шерстяное нечто, постоянно спит'}
for i in glossary:
    print(i)
    print(glossary[i])


