from kafka_producer import produce_transaction
from kafka_consumer import consume_transaction
from stream_processor import process_stream

def main():
    # Start Kafka consumer for receiving transactions
    consume_transaction()

    # Start Spark stream processing
    process_stream()

if __name__ == "__main__":
    main()
