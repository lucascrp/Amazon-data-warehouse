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