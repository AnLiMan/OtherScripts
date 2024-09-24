#----Настройки----
#Исходный файл для чтения. Структура:
# 1. Автор или название.
#2. Автор или название.      и так далее
input_file = "bibliography.txt"
output_file = "sorted_bibliography.txt"  # Выходной список
new_numbers = True  # Отображение новых номеров для источников (старые будут в любом случае)
only_nubers = not new_numbers #Вывести только скорректированную нумерацию

def read_bibliography(filename):
    bibliography = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(". ")
            if len(parts) >= 2:
                try:
                    number = int(parts[0])
                except ValueError:
                    print(f"Ошибка: невозможно преобразовать в число: {parts[0]}")
                    continue
                entry = {"number": number, "text": ". ".join(parts[1:])}  # Соединяем оставшуюся часть строки как текст
                bibliography.append(entry)
            else:
                print(f"Ошибка: некорректный формат строки: {line.strip()}")
    return bibliography

def save_bibliography(filename, bibliography):
    with open(filename, "w", encoding="utf-8") as file:
        # Отображение новой нумерации
        if new_numbers:
            i = 1  # Для нумерации нового списка
            for entry in bibliography:
                file.write(f" {i}. {entry['number']}. {entry['text']}\n")
                i += 1  # Прибавим 1 к номеру в списке
        elif only_nubers:
            i = 1  # Для нумерации нового списка
            for entry in bibliography:
                file.write(f" {i}. {entry['number']}.\n")
                i += 1  # Прибавим 1 к номеру в списке
        else:
            for entry in bibliography:
                file.write(f"{entry['number']}. {entry['text']}\n")

if __name__ == "__main__":
    bibliography = read_bibliography(input_file)
    original_numbers = [entry["number"] for entry in bibliography]

    # Разделяем список на две части: с русскими и английскими буквами
    russian_list = [entry for entry in bibliography if entry['text'][0].lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
    english_list = [entry for entry in bibliography if
                    entry['text'][0].lower() not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']

    # Сортируем каждую часть по тексту
    sorted_russian_list = sorted(russian_list, key=lambda x: x['text'])
    sorted_english_list = sorted(english_list, key=lambda x: x['text'])

    # Объединяем отсортированные списки
    sorted_bibliography = sorted_russian_list + sorted_english_list

    for i, entry in enumerate(sorted_bibliography):
        print(f"{original_numbers[i]}. {entry['text']}")

    save_bibliography(output_file, sorted_bibliography)
    print(f"\nСортированный список сохранен в файл: {output_file}")
