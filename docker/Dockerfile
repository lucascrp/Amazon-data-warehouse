# Amazon Data Warehouse - Spark ETL Dockerfile
# ============================================
FROM openjdk:11-jre-slim

ENV SPARK_VERSION=3.5.0 \
    HADOOP_VERSION=3 \
    PYTHON_VERSION=3.11 \
    PYSPARK_PYTHON=python3

# Install Python, pip, wget, and other dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget curl && \
    rm -rf /var/lib/apt/lists/*

# Install Spark
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /opt && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
ENV PATH=$PATH:$SPARK_HOME/bin

# Copy requirements and install Python dependencies
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Copy ETL code and config
COPY etl/ ./etl/
COPY conf/ ./conf/
COPY Dimensions/ ./Dimensions/

# Default command: open a shell
CMD ["/bin/bash"]
