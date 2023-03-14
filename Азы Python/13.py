print("\nПервая часть")
NewDict = {'first_name':'Андрей',
'last_name': 'Лисов',
'city': 'Златоуст'}

NewDict2 = {'first_name':'Маргомед',
'last_name': 'Махмандыров',
'city': 'Мельбурн'}

NewList = [NewDict,NewDict2]

for i in NewList:
    print('Значения', i.values())
    print('Ключи' , i.keys())
    print('items', i.items())

print("\nВторая часть")
NewDict3 = {'Кот':'Мярзик',
'Собакен': 'Рекс',
'Черепаха': 'Тортила'}

NewDict4 = {'Попугай':'Кеша',
'Хомяк': 'Петя',
'Кролик': 'Светлана'}

NewList2 = [NewDict3,NewDict4]

for i in NewList2:
    print('Значения', i.values())
    print('Ключи' , i.keys())
    print('items', i.items())

print("\nТретья часть")
NewDict5 = {'Италия':'Колизей',
'Турция': 'море',
'Челябинск': 'отдых'}

NewDict6 = {'Рио':'карнавал',
'Вена': 'венский собор',
'Алтай': 'природа'}

NewList3 = [NewDict5,NewDict6]

for i in NewList3:
    print('Места', i.keys(), 'в', i.values())

print("\nЧетвёртая часть")
NewDict7 = {'Андрей': (1, 2, 3)}
NewDict8 = {'Вася':(4,5,6)}
NewList4 = [NewDict7,NewDict8]

for i in NewList4:
    print('Человек- ', i.keys(), 'любит числа:', i.values())

print("\nПятая часть")
NewDict9 = {'Страна':'Рашка',
'Население': '146 млн человек',
'Интересный факт': 'холодно и грустно'}
NewList4 = [NewDict9]

for i in NewList4:
    print('Ключ: ', i.keys(), 'значение:', i.values())