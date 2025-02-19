from pyspark.streaming import StreamingContext
from pyspark.sql.functions import col
from fraud_detection_model import predict_fraud

def process_stream():
    ssc = StreamingContext.getOrCreate('spark://localhost:7077')
    stream = ssc.socketTextStream('localhost', 9999)  # Using socket or Kafka for streaming
    stream.foreachRDD(lambda rdd: rdd.map(lambda x: predict_fraud(x)))  # Call fraud detection logic
    ssc.start()
    ssc.awaitTermination()
