import sqlite3

__connection = None


def ensure_connection(func):  # создание функции-декоратора для безопасного подключения БД
    def inner(*args, **kwargs):
        with sqlite3.connect('anime.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res
    return inner


# --------------------------------------------- СОЗДАНИЕ ГЛАВНОЙ ТАБЛИЦЫ -----------------------------------------------
@ensure_connection
def creating_general_table(conn, force: bool = False):
    c = conn.cursor()  # установка курсора (т.е. некой пачки запросов к БД)
    if force:  # если был передан флаг force = True, то...
        c.execute('DROP TABLE IF EXISTS general_table')  # удалить таблицу category (для дальнейшего пересоздания)
    c.execute('''CREATE TABLE IF NOT EXISTS general_table(
                    Category    VARCHAR NOT NULL,
                    Name        VARCHAR NOT NULL UNIQUE,
                    Url         VARCHAR NOT NULL UNIQUE)''')  # создать таблицу category
    conn.commit()  # сохранить изменения в бд


# ---------------------------------------- ПОЛУЧИТЬ СПИСОК ИМЕЮЩИХСЯ КАТЕГОРИЙ -----------------------------------------
@ensure_connection
def get_category_list(conn):
    c = conn.cursor()
    c.execute('SELECT DISTINCT Category FROM general_table')
    res = []
    for i in c.fetchall():
        res.append(i[0])
    return res


# ------------------------------------------ ПОЛУЧИТЬ СПИСОК ИМЕЮЩИХСЯ АНИМЕ -------------------------------------------
@ensure_connection
def get_anime_list(conn, ctg: str):
    c = conn.cursor()
    c.execute('SELECT "Name" FROM "general_table" WHERE Category=? ORDER BY Name', (ctg,))
    res = []
    for i in c.fetchall():
        res.append(i[0])
    return res


# ------------------------------------------ ПОЛУЧИТЬ СПИСОК ИМЕЮЩИХСЯ ССЫЛОК ------------------------------------------
@ensure_connection
def get_refs_list(conn):
    c = conn.cursor()
    c.execute('SELECT Url FROM general_table')
    res = []
    for i in c.fetchall():
        res.append(i[0])
    return res


# ------------------------------------- ПОЛУЧИТЬ СПИСОК ИМЕЮЩИХСЯ АНИМЕ С ССЫЛКАМИ -------------------------------------
@ensure_connection
def get_anime_list_and_refs(conn, ctg: str):
    c = conn.cursor()
    c.execute('SELECT Name, Url FROM general_table WHERE Category=? ORDER BY Name', (ctg,))
    res = c.fetchall()
    return res

# -------------------------------------------------- ДОБАВИТЬ АНИМЕ ----------------------------------------------------
@ensure_connection
def add_anime(conn, ctg: str, name: str, url: str):
    c = conn.cursor()
    c.execute('INSERT INTO general_table (Category, Name, Url) VALUES (?, ?, ?)', (ctg, name, url))
    conn.commit()


# --------------------------------------------------- УДАЛИТЬ АНИМЕ ----------------------------------------------------
@ensure_connection
def delete_anime(conn, name: str):
    c = conn.cursor()
    c.execute("DELETE FROM 'general_table' WHERE Name=?", (name,))
    conn.commit()
