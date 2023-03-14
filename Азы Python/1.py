#Ввод данных
inputData = input()
#Печать
print("Вы ввели: " + inputData)
#Возможность продолжить
print ("Нажмите 1, если хотитите ввести что-то ещё, либо другое число, чтобы закончить")
inputData2 = int (input())
#Обработка исключений
if inputData2 == 1:
    print("Ок, вводите что-нибудь новое")
    inputData3 = input()
    print("Вы ввели: " + inputData3)
print("Пока!")

