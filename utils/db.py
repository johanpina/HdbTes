import psycopg2

def DataBaseConnection():
    conn = None
    try:
        conn = psycopg2.connect(
                                            host="localhost",
                                            database="HospitalizacionenCasa",
                                            user="postgres",
                                            password="123")
        return conn
    except psycopg2.OperationalError as err:
        print(err)
        conn.close()