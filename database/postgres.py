from postgres_config import get_db_connection

def save_flagged_transaction(transaction):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flagged_transactions (transaction_id, user_id, amount, status) VALUES (%s, %s, %s, %s)",
                   (transaction['transaction_id'], transaction['user_id'], transaction['amount'], 'fraud'))
    conn.commit()
    cursor.close()
    conn.close()
