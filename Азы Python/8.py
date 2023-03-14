# Исходный список
NewList = ['Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть']

#Выведем первые три элемента
print ('Первые три элемента из списка: ',NewList[0], ',',NewList[1], ',', NewList[2])

#Выведем середину
print ('Середина списка: ',NewList[1], ',',NewList[2], ',', NewList[3])

#Выведем последние три элемента
print ('Последние три элемента из списка: ',NewList[3], ',',NewList[4], ',', NewList[5])

#Моя пицца
PizzaList = ['с сыром', 'пеперони', 'мексикано', 'маргсрита']
PizzaList.append('с грибами')
for i in PizzaList:
    print('Моя любимая пицца: ', i)

#Друзеё
PizzaListOfFriends = ['с сыром', 'пеперони', 'мексикано', 'отшкурьита']
PizzaListOfFriends.append('с морепродуктами')
for i in PizzaListOfFriends:
    print('Любимая пицца друзей: ', i)