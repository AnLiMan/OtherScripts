print("\nПервая часть")
NewList = ['с яйцом','с маслом','с кусоком жаренного гвоздя','с песчинкой ауриканского окорока','с вселеноской пустотой']
NewListUpdate = []

for i in NewList:
    print('Запилим бутер ', i)
    NewListUpdate.append(i)
print(NewListUpdate)

print("\nВторая часть")
WeHave = ['Индейка','Батарейка','Канарейка','Кусок куска','Шматок мяска']
WeWant = ['Индейка','Отшкурьяйка','Отшкурьяйка','Отшкурьяйка', 'Шматок мяска', 'Канарейка']

for i in range (WeWant.count('Отшкурьяйка')):
        WeWant.remove('Отшкурьяйка')
print(WeWant)

print("\nТретья часть")
inputData = True
CountryList = []
print('\nВведите названия стран, которое хотите посетить, когда закончите введите "quit"')
while inputData == True:
    Data = str (input())
    CountryList.append(Data)
    if (Data == 'quit'):
        inputData = False
        CountryList.remove(Data)
print(CountryList)