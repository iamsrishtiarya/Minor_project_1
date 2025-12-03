💰 Personal Expense Tracker — Project Overview

This project focuses on building a complete data analytics pipeline to simulate, store, analyze, and visualize a person’s monthly financial behavior. Using Python, SQL, and Streamlit, the system generates a realistic expense dataset, performs exploratory analysis, and presents actionable spending insights through an interactive dashboard.

🎯 Project Objective

To design an end-to-end Personal Expense Tracker capable of:

Generating a synthetic yet realistic monthly expense dataset

Storing data in a structured SQL database for optimized querying

Performing EDA to identify spending trends, behaviors, and anomalies

Building a Streamlit application to visualize expenses and run SQL queries

Delivering insights and recommendations to improve budgeting habits

💼 Business Use Cases
Use Case	Description
Budget Planning	Helps users understand monthly spending patterns and allocate money more effectively
Expense Categorization	Breaks down spending into categories (Food, Travel, Shopping, Bills, etc.)
Financial Awareness	Highlights high-spend areas, overspending alerts, and monthly trends
Personal Finance Insights	Supports informed decision-making to improve savings and reduce unnecessary expenditure
Data-Driven Reports	Enables monthly and annual financial summaries through SQL queries & dashboards
🧭 Project Approach
1. 🧪 Data Simulation

Utilized the Faker library to create a high-quality synthetic dataset representing a person's monthly expenses

Generated 12 separate tables, one for each month, simulating:

Dates

Categories

Payment modes

Short descriptions

Amount and cashback

Ensured realistic expense distribution across categories and months

2. 🗄️ Database Creation

Designed a SQL schema to store monthly expense data

Loaded all 12 monthly tables into a MySQL database

Performed indexing and formatting for optimized SQL querying

Enabled efficient analysis of monthly and cross-monthly financial trends

3. 📊 Exploratory Data Analysis (EDA)

Analyzed spending patterns using Python libraries (Pandas, Matplotlib, Seaborn)

Explored:

Category-wise spending

Daily and weekly spend trends

Cashback vs amount patterns

Payment mode preferences

Identified peak spending periods, outliers, and recurring expense behavior

4. 🌐 Streamlit Application

Built a user-friendly web dashboard showcasing:

Monthly and yearly expense visualizations

SQL query outputs directly within the UI

Interactive filters for category, date, and payment mode

Dynamic charts (line plots, bar charts, pie charts)

Enabled users to explore insights in real time with minimal effort

5. 💡 Insights & Recommendations

Based on the simulated data analysis, the system provides actionable insights such as:

Top spending categories and opportunities to cut costs

Best months for savings and months with excessive spending

High-value purchases & recurring payments

Cashback optimization strategies

Personalized recommendations for budgeting and financial discipline
