from bs4 import BeautifulSoup
import requests
import sqlite3

"""
1. Работа с HTML
Скачать содержимое страницы https://epam.com с помощью requests
Посчитать количество тегов div на этой странице (лучше использовать для этого библиотеку beautifulsoup4)
"""
req = requests.get('https://epam.com')
soup = BeautifulSoup(req.text, 'html.parser')
count = len(soup.find_all('div'))
print(count)


"""
2. Базы данных
Работа с sqlite.
С помощью SQL запросов создать таблицу содержаюую 2 стобца: номер и имя
Добавить три строки с данными.
Получить данные из таблицы и распечатать их на экране.
"""
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE lesson6
            (id, name)''')
c.execute("INSERT INTO lesson6 VALUES (1,'Иван')")
c.execute("INSERT INTO lesson6 VALUES (2,'Анастасия')")
c.execute("INSERT INTO lesson6 VALUES (3,'Джонатан')")

conn.commit()

for row in c.execute('SELECT * FROM lesson6'):
    print(row)
