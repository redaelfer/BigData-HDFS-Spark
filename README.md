# Big Data Pipeline: Kafka to HDFS via Spark Streaming 

Ce projet met en place une architecture Big Data complète permettant de simuler la génération de données, leur ingestion en temps réel via **Kafka**, leur traitement avec **Spark Streaming**, et enfin leur stockage persistant dans **HDFS**.

## 🏗️ Architecture du Système

Le pipeline se compose des couches suivantes :

* **Générateur (Producer)** : Un script Python qui simule l'envoi de données vers Kafka.
* **Ingestion (Kafka)** : Gère les flux de données en temps réel via un broker et Zookeeper.
* **Traitement (Spark)** : Un processeur Spark Streaming qui consomme les messages Kafka et les traite.
* **Stockage (HDFS)** : Un cluster Hadoop (Namenode + Datanode) pour le stockage distribué des données finales.

## 🛠️ Technologies Utilisées

* **Apache Kafka & Zookeeper** : Ingestion et messagerie.
* **Apache Spark** : Traitement de flux (PySpark).
* **Hadoop HDFS** : Système de fichiers distribué.
* **Docker & Docker Compose** : Conteneurisation et orchestration.

## 🚀 Installation et Lancement

Grâce à Docker Compose, vous pouvez lancer l'intégralité de l'infrastructure (6 services) avec une seule commande :

```bash
# Lancement de tous les services (Kafka, Spark, Hadoop, Producer)
docker-compose up --build

```

### Services déployés :

* **Namenode** : Port `9870` (Interface Web Hadoop).
* **Datanode** : Stockage des blocs de données.
* **Kafka Broker** : Port `9092`.
* **Zookeeper** : Port `2181`.
* **Spark Master** : Gestion du cluster Spark.
* **Producer** : Service Python automatique.

## 📂 Structure du Repository

* `docker-compose.yml` : Orchestration de l'infrastructure complète.
* `/producer` : Contient le `Dockerfile` et `main.py` pour la génération des données.
* `/spark` : Contient `processor.py` pour la logique de traitement en streaming.

## 📊 Flux de Données

1. Le service **Producer** génère des messages et les publie dans un topic Kafka.
2. Le **Spark Processor** lit ces messages en continu depuis Kafka.
3. Après transformation, les données sont écrites de manière distribuée dans le cluster **HDFS**.
