#---Библиотеки---
import os
from datetime import datetime

#---Настройки----
ROOT_FOLDER = r"Z:\Группа электрооборудования и ЭСУ"  # Путь к сканируемой папке
OUTPUT_FILE = "folder_report.txt"  # Имя выходного файла
add_comment = False # Добавление надписей для комментирования

# Генерирует текстовый файл со списком файлов и папок
def generate_text_report(folder_path, output_file):
    # Начинаем формировать содержимое
    content = []
    content.append("=== Структура папки ===")
    content.append(f"Сгенерировано: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    content.append(f"Исходная папка: {folder_path}")
    content.append("\nСписок папок и файлов:\n")

    total_folders = 0
    total_files = 0

    for root, dirs, files in os.walk(folder_path):
        total_folders += 1
        rel_path = os.path.relpath(root, folder_path)
        indent = "    " * (rel_path.count(os.sep) + 1)

        # Добавляем папку
        folder_name = os.path.basename(root)
        content.append(f"{indent}{folder_name} [FOLDER]")
        if (add_comment):
            content.append(f"{indent}Добавьте комментарий...\n")

        # Добавляем файлы
        for file in files:
            total_files += 1
            content.append(f"{indent}    {file}")
            if (add_comment):
                content.append(f"{indent}    Добавьте комментарий...\n")

    # Добавляем итоги
    content.append("\n=== Итоги ===")
    content.append(f"Всего папок: {total_folders}")
    content.append(f"Всего файлов: {total_files}")

    # Записываем файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

    print(f"Отчёт успешно создан: {output_file}")
    print(f"Всего папок: {total_folders}, файлов: {total_files}")

if __name__ == "__main__":
    # Проверяем путь
    if not os.path.isdir(ROOT_FOLDER):
        print(f"Ошибка: Папка не найдена - {ROOT_FOLDER}")
        exit(1)

    generate_text_report(ROOT_FOLDER, OUTPUT_FILE)