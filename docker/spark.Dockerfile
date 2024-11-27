FROM apache/spark:3.5.0

USER root

# Install necessary utilities
RUN apt-get update && \
    apt-get install -y netcat-openbsd curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create directory for logs
RUN mkdir -p /opt/spark/logs && \
    chmod -R 777 /opt/spark/logs

COPY docker/spark-entrypoint.sh /
RUN chmod +x /spark-entrypoint.sh

ENTRYPOINT ["/spark-entrypoint.sh"] 