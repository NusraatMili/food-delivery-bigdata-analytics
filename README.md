# 🍔 Food Delivery Big Data Analytics

## 📌 Overview
A Big Data analytics project that uses PySpark to process food delivery data and Power BI to uncover insights into order demand, delivery performance, restaurant activity, and customer ordering patterns.

## 💡Project Purpose

Food delivery platforms can generate a large amount of data every day — orders, restaurants, delivery times, locations, and ordering patterns.

When the amount of data becomes large, simply looking through individual records is not enough. Businesses need a way to process large datasets efficiently and turn them into information that people can actually understand.

**I built this project to explore how Big Data technologies can be used to process food delivery data and turn it into useful business insights.**

The project focuses on questions such as:

- Which areas generate the most orders?
- Which restaurants receive the most orders?
- When are customers ordering the most?
- How long does delivery typically take?
- What patterns can be found in a large food-delivery dataset?

The final results are presented through an interactive **Power BI dashboard**, making the processed data easier for business users to explore.

## Project Workflow

The project follows a simple Big Data pipeline:

**Raw Food Delivery Data → PySpark Processing → Aggregated Results → Power BI Dashboard → Business Insights**

### 1. 📂 Raw Data

The original food-delivery dataset contains order-related information that can be used to analyze ordering patterns, restaurants, locations, and delivery performance.

### 2. ⚡ Big Data Processing

I used Apache Spark with PySpark to process and analyze the dataset.

Instead of manually working through individual records, Spark performs the required calculations efficiently and produces summarized results.

### 3. 📊 Generate Analytical Outputs

The processed data is summarized into business-focused outputs such as:

- Orders by area
- Average delivery time
- Top-performing restaurants
- Orders by time period

### 4. 📈 Power BI Dashboard

The processed results are then brought into Power BI to create interactive visualizations and make the findings easier to understand.

## 👥 Who Could Benefit?

This type of analysis could be useful for:

- **Food Delivery Businesses** - to understand order demand and delivery performance.
- **Restaurant Partners** - to understand order activity and performance.
- **Operations Managers** - to monitor delivery patterns and identify operational areas for improvement.
- **Business Analysts** - to explore demand, location, restaurant, and delivery trends.
- **Decision Makers** - to use data when planning operational and business strategies.

Although this project focuses on food delivery, the same Big Data approach can be applied to other businesses that generate large volumes of transactional data.

## 📊 What I Analyzed

The project focuses on four main areas:

| Analysis Area | What It Helps Understand |
|-----|-----|
| Order Distribution by Area | Where customer demand is highest |
| Restaurant Performance | Which restaurants receive the most orders |
| Peak Order Hours | When customer demand is highest |
| Delivery Performance | How long orders typically take to be delivered |

## 🔍 Key Insights

The analysis produces business-focused insights around:
- Order demand by area - helping identify locations with higher customer activity.
- Top performing restaurants - showing which restaurants receive more orders.
- Peak order hours - helping identify the busiest times of the day.
- Average delivery time - providing an overview of delivery performance.

These insights can help a food-delivery business understand **where demand is coming from, when demand is highest, which restaurants are most active, and how delivery performance looks across the dataset.**

**Note**: The insights are based on the dataset used in this project and should not be interpreted as representing the performance of a real food-delivery company.

## 🛠 Tools Used

**Apache Spark (PySpark)**

Used for:
  
- Processing the food-delivery dataset
- Performing large-scale data analysis
- Grouping and aggregating order information
- Generating summarized analytical outputs

**Power BI**

Used for:

- Importing processed results
- Creating visualizations
- Building the analytical dashboard
- Presenting Big Data results in an easy-to-understand format

##  Skills Demonstrated

- Big Data Analytics
- Apache Spark
- PySpark
- Data Processing
- Data Aggregation
- Data Analysis
- Power BI
- Data Visualization
- Business Intelligence
- Business Insight Generation

## 🔄 Data Pipeline
Raw Data → Spark Processing → Aggregated Data → Power BI Dashboard → Business Insights




## 📁 Repository Structure

1. Review the Data

Explore the dataset inside the:
`data/` foder

2. Review the PySpark Analysis

Open:

`spark_jobs/`

to see how the raw data was processed and aggregated using PySpark.

3. Review the Outputs

The processed results are available inside:

`output/`

These files contain the summarized information used for dashboard analysis.

4. Explore the Dashboard

Open the Power BI file inside:

`dashboard/`

to explore the visual representation of the processed data.

## 🎯 The Main Idea

This project demonstrates an important concept:

**Big Data is not valuable simply because there is a lot of data. It becomes valuable when we can process that data efficiently and turn it into information that supports decisions.**

In this project, PySpark handles the large-scale data processing, while Power BI makes the results easy for people to explore and understand.

The complete journey is:

**Large Dataset → Efficient Processing → Meaningful Results → Business Insights**

## 👩‍💻 Author

**Nusrat Mili**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nusrat%20Mili-blue?logo=linkedin)](https://www.linkedin.com/in/nusrat-mili-3a21a9162/)
[![GitHub](https://img.shields.io/badge/GitHub-NusraatMili-black?logo=github)](https://github.com/NusraatMili)

## 📷 Dashboard Preview
![Dashboard](dashboard/Report.png)
