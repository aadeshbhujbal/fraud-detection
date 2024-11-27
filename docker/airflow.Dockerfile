FROM apache/airflow:2.7.1

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        openjdk-17-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Copy requirements file
COPY requirements.txt /requirements.txt

# Switch to airflow user for pip installations
USER airflow

# Install dependencies with specific pip version
RUN pip install --upgrade pip && \
    pip install --user --no-cache-dir -r /requirements.txt

# Copy DAGs
COPY --chown=airflow:root dags/ /opt/airflow/dags/