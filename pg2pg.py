import psycopg2
import psycopg2.extras


class DBTable:
    def __init__(self, database, table, user, password, host, port, title):
        self.database = database
        self.table = table
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.title = title


def pg2pg(from_tab, to_tab):
    conn_from = psycopg2.connect(
        database=from_tab.database,
        user=from_tab.user,
        password=from_tab.password,
        host=from_tab.host,
        port=from_tab.port,
    )

    cur_from = conn_from.cursor()
    cur_from.execute("SELECT %s FROM %s" % (",".join(from_tab.title), from_tab.table))

    rows = cur_from.fetchall()

    for row in rows:
        print(",".join(row))

    conn_to = psycopg2.connect(
        database=to_tab.database,
        user=to_tab.user,
        password=to_tab.password,
        host=to_tab.host,
        port=to_tab.port,
    )





tab1 = DBTable(
    database="",
    table="",
    user="",
    password="!",
    host="",
    port="",
    title=["", ""],
)

tab2 = DBTable(
    database="",
    table="",
    user="",
    password="!",
    host="",
    port="",
    title=["", ""],
)

pg2pg(tab1, tab2)
