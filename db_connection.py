import psycopg2


def connect():
    try:
        connections = None

        db_params = {
            "host": "localhost",
            "port": "5432",
            "database": "work_db",
            "user": "postgres",
            "password": "postgres"
        }

        print("Connecting to postgres sql...")
        connections = psycopg2.connect(**db_params)

        cr = connections.cursor()
        cr.execute("select * from data where name like 'A%' and salary > 40000")
        db_version = cr.fetchall()
        print(db_version)


    except(Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if connections is not None:
            connections.close()
            print("Connection closed")


if __name__ == "__main__":
    connect()