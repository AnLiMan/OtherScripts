print("\nПервая часть")
glossary = {'Гвоздь -': 'прямой кусок проволоки, с одном острым и тупым концом (шляпкой)',
'Шуруп - ': '"кудрявый" гвоздь',
'Кот - ': 'шерстяное нечто, постоянно спит',
'собякин -':'шерстяной песель',
'инет -':'гугл,youtube все дела',
'фантация -':'у меня закончилась =)'}
for i in glossary:
    print(i)
    print(glossary[i])

#Реки
print("\nВторая часть")
glossary2 = {'Рашка': ['Дон', 'Енисей', 'Волга'],
'Египет ': ['Нил', 'Река2', 'Река3']}
for i in glossary2:
    print('В стране ' + i)
    print('Протекают реки:', glossary2[i])