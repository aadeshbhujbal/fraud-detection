#!/bin/bash

if [ "$SPARK_MODE" = "master" ]; then
    echo "Starting Spark master node..."
    /opt/spark/bin/spark-class org.apache.spark.deploy.master.Master \
        --host $SPARK_MASTER_HOST \
        --port $SPARK_MASTER_PORT \
        --webui-port $SPARK_MASTER_WEBUI_PORT >> /opt/spark/logs/spark-master.log 2>&1
else
    echo "Starting Spark worker node..."
    /opt/spark/bin/spark-class org.apache.spark.deploy.worker.Worker \
        spark://spark-master:7077 >> /opt/spark/logs/spark-worker.log 2>&1
fi

tail -f /opt/spark/logs/*.log 