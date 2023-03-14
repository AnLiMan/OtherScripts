#Исходный список
print ("Первая часть")
print ("")
listOfCountries = ['Исландия', 'Аргентина', 'Италия' , 'Швеция', 'Франция', 'Мексика']
#Выведем его
print (listOfCountries)

#Сортированный список
print ("Вторая часть")
print ("")
listOfCountries.sort()
print (listOfCountries)

#Сортированный список
print ("Третья часть")
print ("")
listOfCountries.reverse()
print (listOfCountries)

#Количество элементов в списке
print ("Четвертая часть")
print ("")
print ("Количество стран в списке: ", listOfCountries.__len__())

#Теперь все функции из лекции
list1 = ["Один", "Два", "Восемь", "Окно", "Гравитация", "Огонь", "Коддинг","Питон"]
print ("Пятая часть")
print ("")
print ("Список по алфавиту в прямом порядке: ")
list1.sort()
print(list1)
print ("Список по алфавиту в обратном порядке: ")
list1.reverse()
print(list1)
print ("Количество элементов: ", list1.__len__())
