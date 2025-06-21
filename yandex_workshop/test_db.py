import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()

# Запрашиваем все столбцы всех записей из таблицы video_products;
# символ * после SELECT означает "верни все поля найденных записей".

cur.execute('''
SELECT 
    tbl_name
FROM 
    sqlite_master
WHERE 
    type ='table';
''')
print(cur.fetchall()[0][0])

# При получении данных из таблицы не нужно вызывать метод con.commit()!
con.close()