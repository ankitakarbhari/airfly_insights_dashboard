 📊 AirFly Insights: Data Visualization and Analysis of Airline Operations

## 📌 Project Overview

This project focuses on analyzing airline flight data to uncover patterns in **flight operations, delays, cancellations, and seasonal trends** using data visualization techniques.

The main objective is to generate **actionable insights** that help understand airline performance, airport congestion, and delay patterns.

---

# 🎯 Objectives

* Analyze airline dataset to identify trends and patterns
* Understand delay causes and cancellation behavior
* Perform airport and route-level analysis
* Visualize seasonal and operational insights
* Build a structured analytical workflow

---

# 📂 Dataset Information

* Dataset: Airline Dataset (Kaggle-based)
* Format: Excel (`.xlsx`)
* Key Columns Used:

  * Passenger ID, Gender, Age
  * Airport Name, Country
  * Departure Date
  * Arrival Airport
  * Flight Status

---

# ⚙️ Tools & Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Jupyter Notebook (VS Code)
* Git & GitHub

---

# 🧩 Project Workflow

---

## 🔹 Milestone 1: Data Foundation and Cleaning

### ✔ Week 1: Data Understanding

* Loaded dataset using Pandas
* Explored dataset structure, columns, and data types
* Identified missing values
* Performed initial data inspection

### ✔ Week 2: Data Preprocessing & Feature Engineering

* Handled missing values
* Converted `Departure Date` to datetime format
* Created new features:

  * **Month**
  * **Day of Week**
* Cleaned and structured dataset for analysis

---

## 📊 Milestone 2: Visual Exploration and Delay Trends

### ✔ Week 3: Univariate & Bivariate Analysis

* Created visualizations:

  * Flight distribution by month
  * Flights by day of week
  * Departure time distribution
* Identified busiest periods

### ✔ Week 4: Delay Analysis

* Analyzed delay patterns (based on available dataset fields)
* Compared flight status (Delayed vs On-time)
* Visualized:

  * Delay distribution
  * Peak delay periods

---

## 🌍 Milestone 3: Route, Cancellation, and Seasonal Insights

### ✔ Week 5: Route & Airport Analysis

* Identified **Top 10 busiest airports**
* Analyzed **origin-destination patterns** using:

  * Airport Name → Arrival Airport
* Created:

  * Bar charts for busiest airports
  * Heatmaps for route frequency

---

### ✔ Week 6: Seasonal & Cancellation Analysis

#### 📅 Monthly Trends

* Extracted Month from departure date
* Visualized:

  * Monthly flight distribution
  * Seasonal traffic trends

#### ❌ Cancellation Analysis

* Used **Flight Status** to identify cancellations
* Created:

  * Cancellation count plots
  * Comparison of cancelled vs completed flights

#### 🌦 Seasonal Insights

* Observed higher disruptions during:

  * Peak travel months
  * Possible winter/holiday periods

---

# 📈 Key Visualizations Created

* Bar charts (Top airports, monthly flights)
* Line plots (seasonal trends)
* Heatmaps (route analysis)
* Histograms (departure time distribution)
* Count plots (flight status)

---

# 🔍 Key Insights

### ✈️ Airport Insights

* Certain airports handle significantly higher traffic
* Indicates possible congestion points

### 🛫 Route Insights

* Some routes are highly frequent → high demand
* Potential areas of delay concentration

### 📅 Seasonal Trends

* Flight volume varies by month
* Peak months show higher traffic

### ❌ Cancellation Insights

* Cancellation patterns vary across time
* Indicates operational or seasonal impact

---

# 📁 Project Structure

```
airfly_insights_dashboard/
│
├── notebooks/
│   ├── milestone1.ipynb
│   ├── milestone2.ipynb
│   ├── milestone3_analysis.ipynb
│
├── data/
│   └── raw/
│       └── Airline_Dataset_Updated_Final.xlsx
│
├── README.md
```

---

# 🚀 How to Run the Project

```bash
# Clone repository
git clone https://github.com/your-username/airfly_insights_dashboard.git

# Open in VS Code
cd airfly_insights_dashboard

# Run Jupyter Notebook


# ✅ Current Status

✔ Milestone 1 Completed
✔ Milestone 2 Completed
✔ Milestone 3 Completed
⬜ Milestone 4 Pending
