' Улучшенный скрипт для сворачивания окон и перемещения курсора
' Работает без прав администратора

Option Explicit

' Настройки (можно менять)
Const minDelay = 45000     ' Минимальная задержка (45 секунд)
Const maxDelay = 300000    ' Максимальная задержка (5 минут)
Const moveChance = 0.4     ' Вероятность перемещения курсора (40%)
Const screenWidth = 1920   ' Ширина экрана (подстройте под ваше разрешение)
Const screenHeight = 1080  ' Высота экрана (подстройте под ваше разрешение)

' Инициализация объектов
Dim WshShell
Set WshShell = CreateObject("WScript.Shell")

' Функция для перемещения курсора (альтернативный метод)
Sub MoveCursor()
    Dim x, y
    Randomize
    x = Int((screenWidth * Rnd) + 1)
    y = Int((screenHeight * Rnd) + 1)
    
    ' Используем более простое API для перемещения курсора
    On Error Resume Next ' Подавляем возможные ошибки из-за ограниченных прав
    WshShell.Run "rundll32 user32.dll,SetCursorPos " & x & "," & y, 0, True
    On Error GoTo 0
End Sub

' Улучшенная функция для сворачивания окон
Sub MinimizeWindows()
    On Error Resume Next ' Игнорируем ошибки если не получится
    
    ' Альтернативные методы сворачивания окон:
    ' 1. Попробуем стандартный Win+D
    WshShell.SendKeys "^{ESC}d"
    
    ' 2. Если не сработало, попробуем другой метод
    WScript.Sleep 300
    WshShell.Run "explorer shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}", 9, True
    
    ' 3. Еще один запасной вариант
    WScript.Sleep 300
    WshShell.SendKeys "%{F4}"
    
    On Error GoTo 0
End Sub

' Основной цикл работы
Randomize
Do While True
    Dim waitTime
    
    ' Случайное время ожидания
    waitTime = Int((maxDelay - minDelay + 1) * Rnd + minDelay)
    
    ' Ожидаем случайное время
    WScript.Sleep waitTime
    
    ' Выбираем случайное действие
    If Rnd < moveChance Then
        MoveCursor
    Else
        MinimizeWindows
    End If
    
    ' Небольшая пауза между действиями
    WScript.Sleep 1000
Loop