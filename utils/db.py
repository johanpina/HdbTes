from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

load_dotenv()  # take environment variables from .env.
global parse_connection_string
connection_string = os.getenv("AZURE_POSTGRESQL_CONNECTIONSTRING")


import urllib.parse as urlparse

def parse_connection_string(conn_str):
    pair = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
    conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
    # Retorna un diccionario con los componentes de la cadena de conexión
    return {
        'dbname': conn_str_params['dbname'],
        'user': conn_str_params['user'],
        'password': conn_str_params['password'],
        'host': conn_str_params['host'],
        'port': conn_str_params['port']
    }



def DataBaseConnection():
    conn = None
    
    try:
        # Parsear la cadena de conexión
        params = parse_connection_string(connection_string)
        conn = psycopg2.connect(
                            host=params['host'],
                            database=params['dbname'],
                            user=params['user'],
                            password=params['password'],
                            port=params['port']
                            )

        return conn
    except psycopg2.OperationalError as err:
        print(err)
        conn.close()

def run_query(query='', data=any): 
    
    conn = DataBaseConnection() 
    cursor = conn.cursor()  
    print(query, data)       
    cursor.execute(query, data)          

    columns = list(cursor.description)

    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   
    else: 
        conn.commit()             
        data = None 

    results = []
    for row in data:
        row_dict = {}
        for i, col in enumerate(columns):
            row_dict[col.name] = row[i]
        results.append(row_dict)
    
    cursor.close()                
    conn.close()                   

    return results