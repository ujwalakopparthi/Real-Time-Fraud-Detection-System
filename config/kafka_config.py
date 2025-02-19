from kafka import KafkaProducer, KafkaConsumer

KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'transaction_topic'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)
