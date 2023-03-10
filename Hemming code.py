# -*- coding: utf-8 -*-

print('Введите число: ') #Ввод исходного числа в десятичном формате (5-значное)
origin  = int(input())

originDec = (bin(origin)[2:]) #Переведём в двоичный код

#Создадим список
originBinCode = []
for i in originDec:
    originBinCode.append(int(i))

# Вспомогательная копия
HemmingBin = originBinCode.copy()

# Создадим список Хемминга, в котором все контрольные биты = 0
for i in range(5):
    HemmingBin.insert((2**i)-1,0)

# Список контрольных битов полученный приемником
ListOfBitsReceiver = [0,0,0,0,0]

# Список контрольных вычесленных битов
ListOfBitsCalc = [0,0,0,0,0]

# Списки контролируемых битов
ListOfControl_1 = [0,2,4,6,8,10,14,16,18,20]
ListOfControl_2 = [1,2,5,6,9,10,13,14,17,18]
ListOfControl_4 = [3,4,5,6,11,12,13,14,19,20]
ListOfControl_8 = [7,8,9,10,11,12,13,14]
ListOfControl_16 = [15,16,17,18,19,20]

# Список списков контролируемых битов
ListOfControl = [ListOfControl_1, ListOfControl_2, ListOfControl_4, ListOfControl_8, ListOfControl_16]

# Генерация кода Хемминга для отправляемого сообщения
j = 0
for List in ListOfControl:
    sum = 0
    for i in List:
        sum += HemmingBin[i]
    HemmingBin[2**j - 1] = (sum % 2)
    j += 1

# ---------------------------Декодирование и поиск ошибок--------------------------------------------------

# Создадим копию кода Хемминга и внесём ошибку в k-й элемент, со значением p

k = 6 # Позиция
p = 0 # Бит-

HemmingBinWithBugs = HemmingBin.copy()
HemmingBinWithBugs[k] = p

for i in range(5):
    ListOfBitsReceiver[i] = HemmingBinWithBugs[2 ** i - 1]

# Генерация кода Хемминга для принятого сообщения

j = 0

for List in ListOfControl:
    sum = 0
    for i in List[1:]:
        sum += HemmingBinWithBugs[i]
    ListOfBitsCalc[j] = sum % 2
    j += 1

# Сравниваем контрольные биты приемника и передатчика и вычисляем номер бита, переданного с ошибкой

BugPosition = -1
for i in range(len(ListOfBitsReceiver)):
    if ListOfBitsCalc[i] != ListOfBitsReceiver[i]:
        BugPosition += 2**i

#--------------------------Вывод результатов--------------------------------
print('Исходное число:', origin)
print('Двоичный код:', originBinCode)
print("Список контрольных битов: ",ListOfBitsReceiver)
print("Список вычисленных битов: ",ListOfBitsCalc)
print('Код Хемминга: ', HemmingBin)
print('Код с ошибкой:', HemmingBinWithBugs)
print('Номер бита с ошибкой:', BugPosition)
