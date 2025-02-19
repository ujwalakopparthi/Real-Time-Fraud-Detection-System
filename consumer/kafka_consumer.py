import json
from kafka import KafkaConsumer

consumer = KafkaConsumer('transaction_topic', bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

def consume_transaction():
    for message in consumer:
        transaction = message.value
        print(f"Received transaction: {transaction}")

consume_transaction()
