#---Библиотеки---
import os
from datetime import datetime
import colorama as cl  # Для красивого текста консоли

#---Настройки----
ROOT_FOLDER = r"C:\Users\LisovAA\Desktop\Файлы\Инфа"  # Путь к сканируемой папке
OUTPUT_FILE = "folder_report.html"  # Имя выходного файла

#---Генерирует HTML-файл с интерактивным деревом папок и файлов---
def generate_html_report(folder_path, output_file):
    print(cl.Fore.MAGENTA + "Начало генерации структуры дерева каталога...")

    # HTML шапка с CSS и JavaScript для сворачивания/разворачивания
    html_header = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Структура файлов в папке</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
        }}
        .folder {{
            cursor: pointer;
            font-weight: bold;
            color: #2980b9;
            margin-left: 15px;
        }}
        .folder:before {{
            content: "📁 ";
        }}
        .folder.collapsed:before {{
            content: "📂 ";
        }}
        .file {{
            margin-left: 30px;
            color: #27ae60;
        }}
        .file:before {{
            content: "📄 ";
        }}
        .comment {{
            font-style: italic;
            color: #7f8c8d;
            margin-left: 45px;
        }}
        .summary {{
            margin-top: 20px;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 5px;
        }}
        .toggle-all {{
            margin: 10px 0;
            padding: 5px 10px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }}
        /* Добавленные стили для отступов */
        .folder-level-1 {{ margin-left: 15px; }}
        .folder-level-2 {{ margin-left: 30px; }}
        .folder-level-3 {{ margin-left: 45px; }}
        .folder-level-4 {{ margin-left: 60px; }}
        .folder-level-5 {{ margin-left: 75px; }}
        .folder-level-6 {{ margin-left: 90px; }}
        .folder-level-7 {{ margin-left: 105px; }}
        .folder-level-8 {{ margin-left: 115px; }}
        .file-level-1 {{ margin-left: 30px; }}
        .file-level-2 {{ margin-left: 45px; }}
        .file-level-3 {{ margin-left: 60px; }}
        .file-level-4 {{ margin-left: 75px; }}
        .file-level-5 {{ margin-left: 90px; }}
        .file-level-6 {{ margin-left: 115px; }}
        .file-level-7 {{ margin-left: 130px; }}
        .file-level-8 {{ margin-left: 145px; }}
    </style>
</head>
<body>
    <h1>Структура файлов в папке</h1>
    <p>Файл сгенерирован: {date}</p>
    <p>Путь к папке: {root_path}</p>
    <button class="toggle-all" onclick="toggleAll()">Свернуть/развернуть всё</button>
    <div id="tree">
"""
    html_footer = """
    </div>
    <div class="summary">
        <p><strong>Итоги:</strong></p>
        <p>Всего папок: <span id="folder-count">0</span></p>
        <p>Всего файлов: <span id="file-count">0</span></p>
    </div>
    <script>
        function toggleFolder(element) {{
            element.classList.toggle('collapsed');
            const content = element.nextElementSibling;
            content.style.display = content.style.display === 'none' ? 'block' : 'none';
        }}

        function toggleAll() {{
            const folders = document.querySelectorAll('.folder');
            const isCollapsed = folders[0].classList.contains('collapsed');

            folders.forEach(folder => {{
                if (isCollapsed) {{
                    folder.classList.remove('collapsed');
                    folder.nextElementSibling.style.display = 'block';
                }} else {{
                    folder.classList.add('collapsed');
                    folder.nextElementSibling.style.display = 'none';
                }}
            }});
        }}

        // Развернуть все папки по умолчанию
        document.addEventListener('DOMContentLoaded', function() {{
            document.getElementById('folder-count').textContent = document.querySelectorAll('.folder').length;
            document.getElementById('file-count').textContent = document.querySelectorAll('.file').length;
        }});
    </script>
</body>
</html>
"""

    # Генерация HTML-структуры
    html_content = []
    total_folders = 0
    total_files = 0

    print(cl.Fore.GREEN + "HTML-структура создана. Построение дерева контента...")

    def build_tree(current_path, depth=0):
        nonlocal total_folders, total_files
        indent = '    ' * depth

        # Определяем классы для отступов
        folder_class = f'folder folder-level-{depth}' if depth > 0 else 'folder'
        file_class = f'file file-level-{depth}' if depth > 0 else 'file'

        # Добавляем папку
        folder_name = os.path.basename(current_path)
        html_content.append(f'{indent}<div class="{folder_class}" onclick="toggleFolder(this)">{folder_name}</div>')
        html_content.append(f'{indent}<div>')
        total_folders += 1

        print(cl.Fore.LIGHTBLACK_EX + "Добавление файлов...")

        # Добавляем файлы в папке
        try:
            for item in os.listdir(current_path):
                item_path = os.path.join(current_path, item)
                if os.path.isdir(item_path):
                    build_tree(item_path, depth + 1)
                else:
                    html_content.append(f'{indent}    <div class="{file_class}">{item}</div>')
                    total_files += 1
        except PermissionError:
            html_content.append(f'{indent}    <div style="color:red">[Access denied]</div>')

        html_content.append(f'{indent}</div>')

    # Строим дерево
    print(cl.Fore.CYAN + "Построение дерева...")
    build_tree(folder_path)
    print(cl.Fore.GREEN + "Дерево построено")

    # Собираем полный HTML
    full_html = html_header.format(
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        root_path=folder_path
    ) + '\n'.join(html_content) + html_footer

    # Записываем файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(cl.Fore.GREEN + f"HTML-отчёт успешно создан: {output_file}")
    print(cl.Fore.BLACK + f"Всего папок: {total_folders}, файлов: {total_files}")
    print(cl.Fore.BLACK + f"Откройте файл {output_file} в браузере")


if __name__ == "__main__":
    # Проверяем путь
    if not os.path.isdir(ROOT_FOLDER):
        print(cl.Fore.RED + f"Ошибка: Папка не найдена - {ROOT_FOLDER}")
        exit(1)

    generate_html_report(ROOT_FOLDER, OUTPUT_FILE)