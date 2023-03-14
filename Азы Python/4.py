#Исходный список
print ("Первая часть")
print ("")
listOfGuests = ['Георгий', 'Валерия', 'Мартьян', 'Джигурдяю', 'Тортик', 'Имя']
#Выведем его
print (listOfGuests)

print ("")
print ("Вторая часть")
print ("")
print ("Джигурдяю прийти не сможет, всместо него будет Мяурзик")
listOfGuests.remove('Джигурдяю')
listOfGuests.append("Мяурзик")
print (listOfGuests)

print ("Третья часть")
print ("")
#У нас будет новый стол! Добавим гостей...
AdditionalListOfGuests = ["Наполеон", "Арнольд", "Ваааааааааааааааааася", "Александр" , "Бориииииииииис"]
NewListOfGuests = listOfGuests + AdditionalListOfGuests
print (NewListOfGuests)

print ("Четвёртая часть")
print ("")
#Как же долго идут посылки из Китая... Осталось только 2 табуретки...
listOfBestFriend = ["Тортик", "Имя"]
print (listOfBestFriend)

