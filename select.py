import sqlite3


def execute_query():
    with open(query, 'r') as f:
        sql = f.read()

    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        cur.executescript(sql)
        return cur.fetchall()


if __name__ == "__main__":
    query = ''
    print(execute_query(sql))