# Amazon Data Warehouse ETL & Analytics

[![Spark ETL](https://img.shields.io/badge/Spark-ETL-orange)](https://spark.apache.org/) [![PySpark](https://img.shields.io/badge/PySpark-3.5.0-blue)](https://pypi.org/project/pyspark/) [![Docker Ready](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/) [![Portfolio Project](https://img.shields.io/badge/portfolio-lucascrp.github.io-green)](https://lucascrp.github.io/)


> **Exam Project: Modern Data Warehouse with Spark ETL**

---


## Project Overview

This repository showcases the complete design, implementation, and presentation of a Data Warehouse, as required for a university exam. The project combines:

- **Dimensional modeling**: fact and dimension tables, documented schema, and sample data
- **Modern ETL**: automated pipeline with Apache Spark (PySpark), fully configurable and reproducible
- **Visualization**: interactive Python dashboard (Streamlit) and Power BI file as an example
- **Reproducibility**: Docker environment, requirements, and detailed instructions

### What this repo demonstrates
- Ability to design a real-world data warehouse
- Practical skills with Spark, Python, YAML, Docker
- ETL automation and data validation
- Effective presentation of results (dashboard, visuals)
- Documentation and clarity

---


## How to evaluate this project

1. **Analyze the data structure**: see the `Dimensions/` folder and schema files in `conf/`
2. **Review the ETL code**: Spark pipeline in `etl/` (ingestion, transformation, writing)
3. **Try the dashboard**: run `streamlit run etl/dashboard.py` to see the results
4. **Check the documentation**: this README, file comments, YAML mapping
5. **(Optional) Explore the Power BI visual**: .pbit file included as an example

---

---

## Descrizione
Questa repository implementa un moderno processo ETL per un data warehouse Amazon-like, usando Apache Spark e PySpark. Include pipeline di ingestione, pulizia, trasformazione e scrittura dati in formato columnar (Parquet/Delta), orchestrazione e test.

- **Fonte dati**: CSV di dimensioni e fatti (simulazione Amazon/Contoso)
- **Tecnologie**: PySpark, Docker, YAML config, test PySpark
- **Obiettivo**: Pipeline riproducibile, scalabile, pronta per analisi avanzate e BI

---

## Repository Structure

```
├── etl/                # PySpark ETL scripts (ingest, transform, write)
├── conf/               # YAML configurations (schema, mapping, parameters)
├── docker/             # Dockerfile for Spark-ready environment
├── tests/              # PySpark unit tests
├── Dimensions/         # Sample CSVs (dimensions, facts)
├── requirements.txt    # Python dependencies
├── README.md           # This documentation
```

---

## How to Run (Locally)

1. **Install dependencies**
  ```bash
  pip install -r requirements.txt
  ```
2. **Run ETL pipeline**
  ```bash
  spark-submit etl/ingest.py
  spark-submit etl/transform.py
  spark-submit etl/write.py
  ```

---

## Run in Docker

1. **Build the image**
  ```bash
  docker build -t amazon-dw-etl -f docker/Dockerfile .
  ```
2. **Start the container**
  ```bash
  docker run -it --rm -v "$PWD":/app amazon-dw-etl
  # Then run the scripts as above
  ```

---

## Example Data & Schema
- Dimensions: Product, Location, Supplier, Time
- Facts: Inventory-Fact
- Configurations and mapping in `conf/`

---

## Tests

- Unit tests in `tests/` (pytest + chispa)
- Run:
  ```bash
  pytest tests/
  ```

---

## Portfolio & Credits

- Project featured in my portfolio: [lucascrp.github.io](https://lucascrp.github.io/)
- Repo: [github.com/lucascrp/Amazon-data-warehouse](https://github.com/lucascrp/Amazon-data-warehouse)
- Author: [Luca Scarpelli](https://github.com/lucascrp)

---

## License
MIT
# 📦 Data Warehouse Project – Amazon Inventory Management Use Case

## 🧭 Project Overview

This project presents a practical and realistic data warehouse use case centered on Amazon’s inventory management operations. It is designed to help users understand and apply fundamental concepts of data warehouse design, dimensional modeling, ETL development, and business intelligence.

By building a complete data warehouse solution—from conceptual modeling to fact and dimension table design, ETL implementation, and analytical queries—users gain hands-on experience with real-world challenges typical of large-scale data environments.

Whether you're a student, an aspiring data engineer, or a business analyst, this project offers a guided, end-to-end experience in designing analytics-ready architectures and defining key KPIs for stock tracking, supplier performance, and inventory optimization.

## 🏢 Domain: Amazon

**Company Overview**  
Founded by Jeff Bezos in 1994, Amazon began as an online bookstore and evolved into a global e-commerce, cloud computing, and digital services giant. Today, Amazon includes vast operations in online retail, logistics, AWS cloud services, AI technologies (e.g., Alexa), and fulfillment center robotics.

This project focuses on **inventory management**, a vital component of Amazon’s marketplace and technological infrastructure.

---

## 🎯 Motivation for Data Warehouse Development

Amazon’s massive scale demands precise and real-time inventory insights. A dedicated **Data Warehouse (DW)** provides a centralized platform to:
- Consolidate data from suppliers, sales, and logistics
- Enable data-driven decisions for stock optimization
- Reduce stockouts and overstocking
- Track inventory turnover and product aging
- Analyze supplier performance and demand fluctuations

The warehouse enables **scalable**, **historically aware**, and **granular** inventory insights that support operational efficiency across Amazon’s vast supply chain.

---

## 🔄 Business Processes Modeled

The following business processes are modeled in the warehouse:

### 1. Inventory Management
- Tracking stock levels per product, supplier, location, and time
- Optimizing stock based on demand and warehouse capacity
- Analyzing inventory turnover and movement rates

### 2. Supplier Management
- Evaluating supplier delivery performance
- Monitoring variability in lead time and delivery quality
- Identifying suppliers affecting stock availability

### 3. Sales & Demand Forecasting
- Understanding seasonal variations in product demand
- Identifying patterns affecting replenishment strategies
- Predicting peak demand periods using historical sales

---

## ❓ Key Business Questions

### Inventory Management
- How can Amazon optimize stock levels to prevent overstocking or stockouts?
- What are the inventory turnover rates by product and region?
- Which products have the highest or lowest stock movement?
- How often does stock move between warehouses?
- Are there seasonal or regional patterns in inventory levels?

### Supplier Management
- How do supplier delays impact inventory?
- Which suppliers consistently meet or miss deadlines?
- Are quality issues affecting stock availability?

### Sales & Demand Forecasting
- How does peak-season demand affect inventory levels?
- What reorder points ensure balance between cost and service level?
- Are certain products aging in stock, impacting sales?

---

## 🧱 Conceptual Design

### 📊 Business Matrix

| Business Area        | Time | Product | Location | Supplier |
|----------------------|------|---------|----------|----------|
| Inventory Management |  X   |    X    |    X     |    X     |

- **Granularity:** Inventory levels by product, per supplier, at each warehouse, at specific times.
- **Facts:** Stock Level, Stock Movement

---

## 🧩 Dimensions

### Time Dimension
- Date, Time of Day, Day of Week, Month, Quarter, Season, Year
- Peak shopping times, Holidays, Promotional periods, Order/Return cycles

### Product Dimension
- Product ID, Category, Description, Unit Price, Manufacturer
- Weight, Size, Supplier SKU, Customer Ratings, Sales Rank, Fulfillment Type

### Location Dimension
- Warehouse ID, Region, Address, Capacity, Last Mile Info
- Inventory movement history, Local regulations, Peak season impact

### Supplier Dimension
- Supplier ID, Name, Lead Time, Cost Metrics
- Dropshipping Capability, Quality Control, Performance Variability

---

## 📈 Fact Tables

### Inventory Fact Table
- **Dimensions:** Time, Product, Location, Supplier
- **Measures:**
  - `Stock Level` – *Semi-additive*
  - `Stock Movement` (Items In - Items Out) – *Non-additive*

---

## ✅ Outcome

By the end of this project, users will:
- Design a normalized and dimensional model for inventory management
- Implement KPIs like stock movement and inventory turnover
- Explore how a DW supports Amazon’s scale and agility in logistics