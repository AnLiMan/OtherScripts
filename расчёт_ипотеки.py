import matplotlib.pyplot as plt

#------------------------------------------------
# ----------------Переменные---------------------
#------------------------------------------------

interest_rate = 7.5 # Процентная ставка (годовых)
mortgage_amount = 1500000  # Сумма ипотеки
loan_terms_mounth = 600  # Срок кредитования в месяцах
mane_of_currency = 'руб' # Название валюты
setting_1 = False  # Вывод помесячного расчёта для аннуитета
setting_2 = True  # Вывод помесячного расчёта для дифференциального вида платежа

#Обязательная страховка
property_insurance = 0.25 #Процент по страховке имущества. Тарифы предлагаются в диапазоне от 0,12% до 0,25%
#Необязательная страховка
life_insurance = 0.8 #Процент по страховке жизни. Застраховать здоровье предлагается от 0,3% до 1,5%.
title_insurance = 0.5 #Процент по страховке титула. Средняя цена полиса на год составляет от 0,3% до 0,5%

monthly_rate = interest_rate / 12 / 100  # Месячная ставка

#Функция отрисовки графиков
def draw_figure(title, xlabel, ylabel, x, y):
  fig = plt.figure(figsize=(10, 6))
  plt.grid()
  plt.title(title + str(mane_of_currency))
  plt.xlabel(xlabel)
  plt.ylabel(ylabel + str(mane_of_currency))
  plt.plot(x, y)
  plt.show()

#----------------------------------------------------------------------------------------------------------
# -------------------Аннуитетный платёж (одинаковая сумма на протяжении всего периода)---------------------
#----------------------------------------------------------------------------------------------------------

#Массивы переменных
massive_of_mounth1 = [] #Массив значений месяцев
massive_of_percentage = [] # Массив выплат процентной части по аннуитету
massive_of_main_part = [] # Массив выплат основной части по аннуитету 
massive_of_mortgage_amount_all = [] # Массив остатка долга по аннуитету
massive_of_mortgage_amount_all_for_insurance_payments = [] # Массив остатка долга по ипотеке на конец года

general_rate = (1 + monthly_rate) ** loan_terms_mounth  # Общаяя ставка
monthly_payment = mortgage_amount * monthly_rate * general_rate / (general_rate - 1)  # Ежемесячный платёж

# Расчёт переплат
overpayment = monthly_payment * loan_terms_mounth - mortgage_amount  # Размер переплаты
mortgage_amount_all = mortgage_amount + overpayment  # Общая сумма долга

for i in range(1, (loan_terms_mounth + 1)):
  percentage = mortgage_amount_all * monthly_rate  # Процентная часть
  massive_of_mounth1.append(i)
  massive_of_percentage.append(percentage)

  #Если процентная часть ушла в ноль и ниже, значит проценты по кредиту выплачены, дальше начинается погашение основного долга
  if (percentage <= 0):
    percentage = 0

  main_part = monthly_payment - percentage  # Основная часть (тело кредита)
  massive_of_main_part.append(main_part) 
  mortgage_amount_all = mortgage_amount_all - monthly_payment # Уменьшение долга на величину выплаты
  massive_of_mortgage_amount_all.append(mortgage_amount_all)

  if (setting_1):
    print('\nВ ', i, 'месяц')
    print('Процентная часть:', percentage)
    print('Основная часть:', main_part)
    print('Остаток платежа: ', mortgage_amount_all)

print('\n----------Аннуитетный платёж-----------')
print('\nКаждый месяц по аннуитетному виду платежа вы будете платить: ', round(monthly_payment, 2))
print('Переплата составит: ', round(overpayment, 2), mane_of_currency)
print('В процентном соотношении: ', round(overpayment / mortgage_amount * 100, 3), "%")

#Вывод графиков
fig = plt.figure(figsize=(10, 6))
plt.grid()
plt.title('Графики выплат (Аннуитет)')
plt.xlabel('Месяц')
plt.ylabel('Величина выплаты, ' + str(mane_of_currency))
plt.plot(massive_of_mounth1, massive_of_percentage, 'b-', label = 'Процентные выплаты')
plt.plot(massive_of_mounth1, massive_of_main_part, 'r-', label = 'Выплата долга')
plt.hlines(monthly_payment, 0, loan_terms_mounth, color = 'g', label = 'Размер выплат')
plt.legend(loc = 'upper right') 

draw_figure('Остаток по ипотеке (Аннуитет) ', 'Месяц', 'Остаток по ипотеке, ', massive_of_mounth1, massive_of_mortgage_amount_all)

#-----------------------------------------------------------------------------------------------------------------
# ---------------------Дифференцированный платёж (разная сумма на протяжении всего периода)----------------------
#-----------------------------------------------------------------------------------------------------------------

current_year = 1 #Начальное значение текущего года
mortgage_amount_diff = mortgage_amount #База расчёта для диффа
massive_mortgage_amount_diff = [] #Массив остатка по ипотеке
massive_mortgage_amount_diff_year_for_insurance_payments = [] #Массив остатка долга по ипотеке на конец года
massive_of_mortgage_amount_diff = [] #Массив значений выплат
massive_of_mounth = [] #Массив значений месяцев
overpayment_diff = 0

print('\n---------Дифференцированный платёж----------')
if (setting_2):
  print("\nГод: ", current_year)

for i in range((loan_terms_mounth - 1), 0, -1):
    monthly_payment_diff = mortgage_amount / loan_terms_mounth + mortgage_amount_diff * monthly_rate  # Ежемесячный платёж

    if (setting_2):
      print('В', loan_terms_mounth - i, 'месяц по дифференцированному виду платежа вы будете платить: ', round(monthly_payment_diff, 2), mane_of_currency)
      
      if ((loan_terms_mounth - i) % 12 == 0 or i == 0): #Расчёт текущего года
        current_year+=1
        print("\nГод: ", current_year)
      
    
    massive_of_mortgage_amount_diff.append(monthly_payment_diff) #Добавляем значения в массив графика выплат
    massive_of_mounth.append(loan_terms_mounth - i) #Добавление значений в массив месяцев
    overpayment_diff = overpayment_diff + monthly_payment_diff # Сумма ипотеки с учётом переплаты
    mortgage_amount_diff = mortgage_amount_diff - monthly_payment_diff
    massive_mortgage_amount_diff.append((overpayment_diff + mortgage_amount) - mortgage_amount - monthly_payment_diff) 
   
massive_mortgage_amount_diff.reverse() #Инвертируем массив выплаченного долга и получим массив остатка по ипотеке 

#Вывод графиков
draw_figure('График выплат (Дифференцированный), ', 'Месяц', 'Величина выплаты, ', massive_of_mounth, massive_of_mortgage_amount_diff)
draw_figure('Остаток по ипотеке (Дифференцированный), ', 'Месяц', 'Остаток по ипотеке, ', massive_of_mounth, massive_mortgage_amount_diff)

print('\nПереплата по дифференцированному виду составит: ', round(overpayment_diff - mortgage_amount, 2), mane_of_currency)
print('В процентном соотношении: ', round((overpayment_diff - mortgage_amount) / mortgage_amount * 100, 3), "%")

#-------------------------------------------------------------------------------
#--------------------------------Расчёт страховок-------------------------------
#-------------------------------------------------------------------------------

total_amount_of_insurance_payments =  mortgage_amount + (interest_rate / 100) * mortgage_amount #Общая сумма страховых выплат

#-----------------------------Аннуитет-----------------------------------

print('\n---------Расчёт страховых выплат по аннуитетному виду платежа------------')
total_amount_of_insurance_payments_premium_property_ann = 0 #Всего выплат по страховке имущества
total_amount_of_insurance_payments_premium_life_ann = 0 #Всего выплат по страховке жизни
total_amount_of_insurance_payments_premium_title_ann = 0 #Всего выплат по страховке титула

# Запишем значения остатка долга на конец года
for i in range(0, loan_terms_mounth, 12):
  massive_of_mortgage_amount_all_for_insurance_payments.append(massive_of_mortgage_amount_all[i])

for i in range(0, int(loan_terms_mounth/12)):
  if (massive_of_mortgage_amount_all_for_insurance_payments[i] < mortgage_amount): #Если остаток долга по ипотеке на конец года стал меньше заёмной суммы
    
    print('\nГод', i + 1)
    annual_deduction_of_insurance_premium_property_ann = massive_of_mortgage_amount_all_for_insurance_payments[i] * property_insurance / 100 #Расчёт страховки имущества
    total_amount_of_insurance_payments_premium_property_ann += annual_deduction_of_insurance_premium_property_ann #Всего выплат по страховке имущества
    print('Страховка имущества: ', round(annual_deduction_of_insurance_premium_property_ann, 2), mane_of_currency) 

    annual_deduction_of_insurance_premium_life_ann = massive_of_mortgage_amount_all_for_insurance_payments[i] * life_insurance / 100 #Расчёт страховки жизни
    total_amount_of_insurance_payments_premium_life_ann += annual_deduction_of_insurance_premium_life_ann #Всего выплат по страховке жизни
    print('Страховка жизни: ', round(annual_deduction_of_insurance_premium_life_ann, 2), mane_of_currency)

    annual_deduction_of_insurance_premium_title_ann = massive_of_mortgage_amount_all_for_insurance_payments[i] * title_insurance / 100 #Расчёт страховки титула
    total_amount_of_insurance_payments_premium_title_ann += annual_deduction_of_insurance_premium_title_ann #Всего выплат по страховке титула
    print('Страховка титула: ', round(annual_deduction_of_insurance_premium_title_ann, 2), mane_of_currency)
 
  else:
    print('\nГод', i +1 )
    annual_deduction_of_insurance_premium_property_ann = total_amount_of_insurance_payments * property_insurance / 100 #Расчёт страховки имущества
    total_amount_of_insurance_payments_premium_property_ann += annual_deduction_of_insurance_premium_property_ann #Всего выплат по страховке имущества
    print('Страховка имущества: ', round(annual_deduction_of_insurance_premium_property_ann, 2), mane_of_currency) 

    annual_deduction_of_insurance_premium_life_ann = total_amount_of_insurance_payments * life_insurance / 100 #Расчёт страховки жизни
    total_amount_of_insurance_payments_premium_life_ann += annual_deduction_of_insurance_premium_life_ann #Всего выплат по страховке жизни
    print('Страховка жизни: ', round(annual_deduction_of_insurance_premium_life_ann, 2), mane_of_currency)

    annual_deduction_of_insurance_premium_title_ann = total_amount_of_insurance_payments * title_insurance / 100 #Расчёт страховки титула
    total_amount_of_insurance_payments_premium_title_ann += annual_deduction_of_insurance_premium_title_ann #Всего выплат по страховке титула
    print('Страховка титула: ', round(annual_deduction_of_insurance_premium_title_ann, 2), mane_of_currency)

print('\nВсего выплат по страховке имущества для аннуитетного вида платежа: ', round(total_amount_of_insurance_payments_premium_property_ann, 2), mane_of_currency)
print('Всего выплат по страховке жизни для аннуитетного вида платежа: ', round(total_amount_of_insurance_payments_premium_life_ann, 2), mane_of_currency)
print('Всего выплат по страховке титула для аннуитетного вида платежа: ', round(total_amount_of_insurance_payments_premium_title_ann, 2), mane_of_currency)

#-----------------------------Дифференцированный-----------------------------------

print('\n---------Расчёт страховых выплат по дифференцированному виду платежа------------')
total_amount_of_insurance_payments_premium_property_diff = 0 #Всего выплат по страховке имущества
total_amount_of_insurance_payments_premium_life_diff = 0 #Всего выплат по страховке жизни
total_amount_of_insurance_payments_premium_title_diff = 0 #Всего выплат по страховке титула

# Запишем значения остатка долга на конец года
for i in range(0, loan_terms_mounth, 12):
  massive_mortgage_amount_diff_year_for_insurance_payments.append(massive_mortgage_amount_diff[i])

for i in range(0, int(loan_terms_mounth/12)):
  if (massive_mortgage_amount_diff_year_for_insurance_payments[i] < mortgage_amount): #Если остаток долга по ипотеке на конец года стал меньше заёмной суммы
    
    print('\nГод', i + 1)
    annual_deduction_of_insurance_premium_property = massive_mortgage_amount_diff_year_for_insurance_payments[i] * property_insurance / 100 #Расчёт страховки имущества
    total_amount_of_insurance_payments_premium_property_diff += annual_deduction_of_insurance_premium_property #Всего выплат по страховке имущества
    print('Страховка имущества: ', round(annual_deduction_of_insurance_premium_property, 2), mane_of_currency) 

    annual_deduction_of_insurance_premium_life = massive_mortgage_amount_diff_year_for_insurance_payments[i] * life_insurance / 100 #Расчёт страховки жизни
    total_amount_of_insurance_payments_premium_life_diff += annual_deduction_of_insurance_premium_life #Всего выплат по страховке жизни
    print('Страховка жизни: ', round(annual_deduction_of_insurance_premium_life, 2), mane_of_currency)

    annual_deduction_of_insurance_premium_title = massive_mortgage_amount_diff_year_for_insurance_payments[i] * title_insurance / 100 #Расчёт страховки титула
    total_amount_of_insurance_payments_premium_title_diff += annual_deduction_of_insurance_premium_title #Всего выплат по страховке титула
    print('Страховка титула: ', round(annual_deduction_of_insurance_premium_title, 2), mane_of_currency)
 
  else:
    print('\nГод', i +1 )
    annual_deduction_of_insurance_premium_property = total_amount_of_insurance_payments * property_insurance / 100 #Расчёт страховки имущества
    total_amount_of_insurance_payments_premium_property_diff += annual_deduction_of_insurance_premium_property #Всего выплат по страховке имущества
    print('Страховка имущества: ', round(annual_deduction_of_insurance_premium_property, 2), mane_of_currency) 

    annual_deduction_of_insurance_premium_life = total_amount_of_insurance_payments * life_insurance / 100 #Расчёт страховки жизни
    total_amount_of_insurance_payments_premium_life_diff += annual_deduction_of_insurance_premium_life #Всего выплат по страховке жизни
    print('Страховка жизни: ', round(annual_deduction_of_insurance_premium_life, 2), mane_of_currency)

    annual_deduction_of_insurance_premium_title = total_amount_of_insurance_payments * title_insurance / 100 #Расчёт страховки титула
    total_amount_of_insurance_payments_premium_title_diff += annual_deduction_of_insurance_premium_title #Всего выплат по страховке титула
    print('Страховка титула: ', round(annual_deduction_of_insurance_premium_title, 2), mane_of_currency)

print('\nВсего выплат по страховке имущества для дифференциального вида платежа: ', round(total_amount_of_insurance_payments_premium_property_diff, 2), mane_of_currency)
print('Всего выплат по страховке жизни для дифференциального вида платежа: ', round(total_amount_of_insurance_payments_premium_life_diff, 2), mane_of_currency)
print('Всего выплат по страховке титула для дифференциального вида платежа: ', round(total_amount_of_insurance_payments_premium_title_diff, 2), mane_of_currency)
