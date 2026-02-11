# Big Data Pipeline: Kafka to HDFS via Spark Streaming

This project implements a complete Big Data architecture allowing for data generation simulation, real-time ingestion via **Kafka**, processing with **Spark Streaming**, and finally, persistent storage in **HDFS**.

## 🏗️ System Architecture

The pipeline consists of the following layers:

* **Generator (Producer)**: A Python script that simulates sending data to Kafka.
* **Ingestion (Kafka)**: Manages real-time data streams via a broker and Zookeeper.
* **Processing (Spark)**: A Spark Streaming processor that consumes and processes Kafka messages.
* **Storage (HDFS)**: A Hadoop cluster (Namenode + Datanode) for distributed storage of the final data.

## 🛠️ Technologies Used

* **Apache Kafka & Zookeeper**: Ingestion and messaging.
* **Apache Spark**: Stream processing (PySpark).
* **Hadoop HDFS**: Distributed file system.
* **Docker & Docker Compose**: Containerization and orchestration.

## 🚀 Installation and Launch

Thanks to Docker Compose, you can launch the entire infrastructure (6 services) with a single command:

```bash
# Launching all services (Kafka, Spark, Hadoop, Producer)
docker-compose up --build

```

### Deployed Services:

* **Namenode**: Port `9870` (Hadoop Web Interface).
* **Datanode**: Storage of data blocks.
* **Kafka Broker**: Port `9092`.
* **Zookeeper**: Port `2181`.
* **Spark Master**: Spark cluster management.
* **Producer**: Automatic Python service.

## 📂 Repository Structure

* `docker-compose.yml`: Orchestration of the complete infrastructure.
* `/producer`: Contains the `Dockerfile` and `main.py` for data generation.
* `/spark`: Contains `processor.py` for the streaming processing logic.

## 📊 Data Flow

1. The **Producer** service generates messages and publishes them to a Kafka topic.
2. The **Spark Processor** reads these messages continuously from Kafka.
3. After transformation, the data is written in a distributed manner within the **HDFS** cluster.

---
