import os
from bs4 import BeautifulSoup

# --- Настройки ---

# Список путей к вашим HTML-файлам закладок
# Убедитесь, что пути указаны правильно
bookmark_files = [
    r'd:\пользовательские папки\Загрузки\Telegram Desktop\Toolkit. Data Science. Open Internet. List of the links.html'
]

# Имя файла, в который будут сохранены все ссылки
output_filename = 'all_bookmarks.txt'

# --- Основная логика ---

def extract_links():
    """
    Извлекает ссылки из списка HTML-файлов и сохраняет их в один текстовый файл.
    """
    print("Начинаю извлечение ссылок...")
    total_links_found = 0

    try:
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            for file_path in bookmark_files:
                if not os.path.exists(file_path):
                    print(f"ПРЕДУПРЕЖДЕНИЕ: Файл не найден, пропускаю: {file_path}")
                    continue

                f_out.write(f"--- Ссылки из файла: {os.path.basename(file_path)} ---\n\n")
                print(f"Обрабатываю файл: {os.path.basename(file_path)}...")

                with open(file_path, 'r', encoding='utf-8') as f_in:
                    soup = BeautifulSoup(f_in, 'html.parser')
                    
                    # Находим все теги <a>, у которых есть атрибут href
                    links = soup.find_all('a', href=True)
                    
                    if not links:
                        f_out.write("В этом файле ссылок не найдено.\n")
                    else:
                        for link in links:
                            text = link.get_text(strip=True)
                            url = link.get('href')
                            if text and url:
                                f_out.write(f"{text}: {url}\n")
                                total_links_found += 1
                
                f_out.write("\n" + "="*80 + "\n\n") # Разделитель для наглядности

        print(f"\nГотово! Найдено и сохранено {total_links_found} ссылок в файл '{output_filename}'")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    extract_links()
