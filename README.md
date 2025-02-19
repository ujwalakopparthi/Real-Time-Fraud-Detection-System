# Real-Time Fraud Detection System 🚨💳

This project implements a **Real-Time Fraud Detection System** using **Apache Kafka**, **Spark Streaming**, **scikit-learn**, **PostgreSQL**, and **Grafana**. The system processes up to **1 million transactions** every day and detects fraudulent transactions using **Machine Learning** techniques. The pipeline includes low-latency processing with Apache Kafka and Spark Streaming for real-time transaction monitoring. Fraudulent transactions are flagged using an **Isolation Forest** model, achieving high precision and recall.

## Key Features 🌟
- **Real-time processing** of up to 1 million transactions/day 🏃‍♂️
- **Fraud detection** using the **Isolation Forest** algorithm 🤖
- **Low-latency streaming pipeline** integrated with **Apache Kafka** and **Spark Streaming** ⏱️
- **Anomaly detection** and alerting on fraudulent transactions 🚨
- **Grafana Dashboard** for real-time monitoring 📊

## Technologies Used 🛠️
- **Python** 🐍
- **Apache Kafka** 🛠️
- **Spark Streaming** ⚡
- **scikit-learn** 📚
- **PostgreSQL** 🗄️
- **Grafana** 📊

## Prerequisites 📋
Before running the project, make sure you have the following installed:
- **Python 3.x** 🐍
- **Apache Kafka** 🛠️
- **Apache Spark** ⚡
- **PostgreSQL** 🗄️
- **Grafana** 📊

## Installation 🚀

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fraud-detection-system.git
   cd fraud-detection-system
2. Install the dependencies:
    pip install -r requirements.txt
3. Set up PostgreSQL:
    * Create a database and user for the system.
    * Run the SQL scripts in database/ to create the necessary tables for transaction data.
4. Set up Apache Kafka:
    * Follow the instructions here to install and run Kafka locally.
    * Create a Kafka topic for transaction data:
        kafka-topics.sh --create --topic transaction_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
5.  Set up Spark Streaming:
    * Install Apache Spark and start the Spark streaming context.
6.  Run the project:
    * Start the Kafka Producer to send sample transaction data:
        python producer/kafka_producer.py
    * Start the Kafka Consumer to process transactions:
        python consumer/kafka_consumer.py
    * Start the Spark Streaming Processor:
        python processor/stream_processor.py
    * Run the main application:
        python main.py

