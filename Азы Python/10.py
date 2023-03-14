#Первая часть
print('\nВведите своё имя')
UserList = ['admin','alex','sandy','sam','gordon','eva']
UserName = str (input())

if (UserName == UserList[0]):
    print('Привет админ, я к вашим услугам')
elif ((UserName == UserList[1])):
    print('Здравствуйте, alex')
elif ((UserName == UserList[2])):
    print('Здравствуйте, sandy')
elif ((UserName == UserList[3])):
    print('Здравствуйте, sam')
elif ((UserName == UserList[4])):
    print('Здравствуйте, gordon')
elif ((UserName == UserList[5])):
    print('Здравствуйте, eva')
else:
    print('Вас нет в списке')

print('Конец первой части')

#Вторая часть
print('\nВторая часть')
NewUsersList = []
if (len(NewUsersList) == 0):
    print('Список пользователей пуст!')
print('Конец второй части')

#Третья часть
print('\nТретья часть')
CurrentUsersList = ['admin','alex','sandy','sam','gordon','eva']
NewUsers = ['rick','morty','mask','sam','wanta','prince']
switch = False
for i in NewUsers:
    if ((len(list(set(CurrentUsersList) & set(NewUsers))) != 0) and switch == False):
        print('Имя ', (list(set(CurrentUsersList) & set(NewUsers))), 'занято!')
        switch = True
    else:
        print('Имя ' + i + ' свободно')

print('Введите имя капсом или с большими буквами')
UserName2 = str (input())
print(UserName2.lower())

print('Конец третьей части')

#Четвёртая часть
print('\nЧетвёртая часть')
List = [1,2,3,4,5,6,7,8,9]
for i in List:
    if (i == 1):
        print("First")
    elif (i == 2):
        print("Second")
    elif (i == 3):
        print("Trird")
    else:
        print(i,"-th")
print('Конец четвёртой части')