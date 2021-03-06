import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    #create database and connect to default database
    conn= psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=postgres port=5432")
    conn.set_session(autocommit=True)
    cur=conn.cursor()

    #create a new database
    cur.execute("DROP DATABASE IF EXISTS Sparkifydb")
    cur.execute("CREATE DATABASE Sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    #close connection to default database
    cur.close()

    #connect to the new database
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=postgres port=5432")
    cur=conn.cursor()

    return cur , conn

def drop_tables(cur,conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur,conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    drop_tables(cur,conn)
    create_tables(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()