import psycopg2

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'fraud_detection_db'
DB_USER = 'user'
DB_PASSWORD = 'password'

def get_db_connection():
    return psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
