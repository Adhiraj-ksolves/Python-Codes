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

        crsr = connections.cursor()
        print("Postgresql is configured")
        crsr.execute("select * from data where name like 'A%'")
        db_version = crsr.fetchall()
        print(db_version)


    except(Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if connections is not None:
            connections.close()
            print("Database connection closed successfully")


if __name__ == "__main__":
    connect()