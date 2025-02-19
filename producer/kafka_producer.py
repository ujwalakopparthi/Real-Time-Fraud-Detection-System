import json
from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

def produce_transaction(transaction_data):
    producer.send('transaction_topic', value=transaction_data)

# Sample data sending loop
while True:
    transaction = {"transaction_id": 1, "amount": 1000, "user_id": 123}
    produce_transaction(transaction)
    sleep(1)
