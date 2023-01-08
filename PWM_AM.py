#--Библиотеки---
import matplotlib.pyplot as plt
import math
from scipy import signal

#Настройки
time_step = 0.01 # Шаг расчёта
steps = 20000 #количество шагов расчёта
k1 = 1/70 # Коэффициент для аргумента косинуса
k2 =1/50 # Коэффициент для аргумента синуса
b = 0.35 # Величина смещения
T_carrier_frequency = 0.5 # Период несущей частоты
k_PWM_AM = 7.8 #Величина фильтра для демодуляции ШИМ и АИМ

#Списки значений
time_list = [] # Список значений времени
original_signal_list = [] # Список значений исходного сигнала
normalized_original_sigmal_list = [] #Нормализованный сигнал от 0 до 1
pwm_list = [] # Значения ШИМ
u_saw_gen_list = [] # Еапряжение генератора (пила)
carrier_frequency_list = [] # Несущая частота (синус)
U_modulate_list = [] # Модулированный сигнал
U_PWM_reconstruction_list = [] # Восстановленный из ШИМ сигнал
U_AM_reconstruction_list = [] # Восстановленный из АИМ сигнал
absolute_error_PWM = []
relative_error_PWM = []
absolute_error_AM = []
relative_error_AM = []

#----Функции----
#1. Генерация списка времени
def time_list_generate():
    for i in range(steps):
        time_list.append(i * time_step)

#2. Генерация заданного сигнала
def signal_generate():
    for i in range(steps):
        original_signal_list.append(math.cos(k1*time_list[i]) * math.sin(k2 * time_list[i]) + b)

#3. Нормализация исходного сигнала в диапазон от 0 до 1
def signal_normalize ():
    signal_amplitude = round(max(original_signal_list), 3)
    print("Амплитуда исходного сигнала = ", signal_amplitude)
    for i in range(steps):
        normalized_original_sigmal_list.append(round(original_signal_list[i] / signal_amplitude, 3))

#4. Генерация несущей частоты
def carrier_frequency_generate ():
    for i in range(steps):
        carrier_frequency_list.append(math.sin(2 * math.pi * time_list[i] / T_carrier_frequency))

#5. Генерирование напряжения генератора (пила)
def saw_generate():
    for i in range(steps):
        u_saw_gen_list.append((signal.sawtooth(1 / T_carrier_frequency * 2 * math.pi * time_list[i], 1) + 1) / 2)

#6. Модулированный сигнал
def U_modulate_generate ():
    for i in range(steps):
        U_modulate_list.append(normalized_original_sigmal_list[i] * carrier_frequency_list[i])

#7. Генерирование ШИМ
def PWM_generate ():
    for i in range(steps):
        if (normalized_original_sigmal_list[i] > u_saw_gen_list [i]):
            pwm_list.append(1)
        else:
            pwm_list.append(0)

#8. Восстановление из ШИМ-сигнала
def PWM_reconstruction ():
    U_PWM_reconstruction_list.append(normalized_original_sigmal_list[0])
    for i in range(steps - 1):
        U_PWM_reconstruction_list.append((time_step / k_PWM_AM * (pwm_list[i + 1] - U_PWM_reconstruction_list[i])) + U_PWM_reconstruction_list [i])

#9. Восстановление из АИМ-сигнала
def AM_reconstruction ():
    U_AM_reconstruction_list.append(normalized_original_sigmal_list[0])
    for i in range(steps - 1):
        if (U_modulate_list[i + 1] <= 0):
            U_AM_reconstruction_list.append(math.fabs(U_modulate_list[i + 1]))
        else:
            U_AM_reconstruction_list.append(time_step / k_PWM_AM * ((U_modulate_list[i + 1] - U_AM_reconstruction_list[i]) + U_AM_reconstruction_list[i]))

# 10. Расчёт ошибки
def error_calculate():
    for i in range(steps):
        absolute_error_PWM.append(U_PWM_reconstruction_list[i] - normalized_original_sigmal_list [i])
        relative_error_PWM.append(absolute_error_PWM[i]/ normalized_original_sigmal_list[i] * 100)
        absolute_error_AM.append(U_AM_reconstruction_list[i] - normalized_original_sigmal_list[i])
        relative_error_AM.append(absolute_error_AM[i] / normalized_original_sigmal_list[i] * 100)

#11. Отрисовка графиков
def draw_figure(title, xlabel, ylabel, x, y):
    plt.figure(figsize=(8, 4))
    plt.xlim(0, steps * time_step)
    plt.grid()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x, y, color = 'r')
    plt.hlines(0, 0, steps*time_step)
    plt.show()

#---Основной код---
time_list_generate()
signal_generate()
signal_normalize()
carrier_frequency_generate()
U_modulate_generate()
saw_generate ()
PWM_generate ()
PWM_reconstruction ()
AM_reconstruction ()
error_calculate ()

#Выводим результаты
draw_figure("Исходный сигнал", "Время", "Y", time_list, original_signal_list)
draw_figure("Нормализованный сигнал", "Время", "Y", time_list, normalized_original_sigmal_list)
draw_figure("Несущая частота с периодом T = " + str(T_carrier_frequency), "Время", "Y", time_list, carrier_frequency_list)
draw_figure("Напряжение генератора", "Время", "Y", time_list, u_saw_gen_list)
draw_figure("Модулированный сигнал", "Время", "Y", time_list, U_modulate_list)
draw_figure("ШИМ сигнал", "Время", "Y", time_list, pwm_list)
draw_figure("Восстановленный из ШИМ сигнал", "Время", "Y", time_list, U_PWM_reconstruction_list)
draw_figure("Восстановленный из АИМ сигнал", "Время", "Y", time_list, U_AM_reconstruction_list)
draw_figure("График абсолютной погрешности ШИМ", "Время", "Y", time_list, absolute_error_PWM)
draw_figure("График относительной погрешности ШИМ", "Время", "%", time_list, relative_error_PWM)
draw_figure("График абсолютной погрешности АИМ", "Время", "Y", time_list, absolute_error_AM)
draw_figure("График относительной погрешности АИМ", "Время", "%", time_list, relative_error_AM)
