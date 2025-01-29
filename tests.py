from faker import Faker
import pandas as pd
import random
from datetime import datetime, date

faker = Faker()

def generate_monthly_data(month, year):
    data = []
    categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Groceries', 'Subscriptions']
    payment_modes = ['Cash', 'Online', 'Credit Card', 'Debit Card']

    # Create valid start and end dates using datetime.date()
    start_date = date(year, month, 1)
    end_date = date(year, month, 28)  # Keeping it 28 to avoid issues in Feb

    for _ in range(100):  # Generate 100 transactions per month
        data.append({
            'Date': faker.date_between(start_date=start_date, end_date=end_date),
            'Category': random.choice(categories),
            'Payment_Mode': random.choice(payment_modes),
            'Description': faker.sentence(nb_words=4),
            'Amount_Paid': round(random.uniform(50, 1000), 2),
            'Cashback': round(random.uniform(0, 50), 2)
        })
    return pd.DataFrame(data)

# Generate data for 12 months
all_data = pd.concat([generate_monthly_data(month, 2024) for month in range(1, 13)])

# Save to CSV
all_data.to_csv("expenses.csv", index=False)

import sqlite3
import pandas as pd

conn = sqlite3.connect("expenses.db")
all_data = pd.read_csv("expenses.csv")
all_data.to_sql("Expenses", conn, if_exists="replace", index=False)
conn.close()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("expenses.csv")

import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("expenses.db")
query = "SELECT * FROM Expenses"
data = pd.read_sql_query(query, conn)

st.title("Personal Expense Tracker")
st.sidebar.header("Filters")
category = st.sidebar.selectbox("Select Category", data["Category"].unique())

filtered_data = data[data["Category"] == category]
st.write(filtered_data)

st.bar_chart(filtered_data.groupby("Payment_Mode")["Amount_Paid"].sum())

query = "SELECT Category, SUM(Amount_Paid) AS Total_Spending FROM Expenses GROUP BY Category ORDER BY Total_Spending DESC;"
data = pd.read_sql_query(query, conn)
st.bar_chart(data.set_index('Category')['Total_Spending'])

query = "SELECT Payment_Mode, SUM(Amount_Paid) AS Total_Spending FROM Expenses GROUP BY Payment_Mode ORDER BY Total_Spending DESC;"
data = pd.read_sql_query(query, conn)
st.pie_chart(data.set_index('Payment_Mode')['Total_Spending'])

query = "SELECT SUM(Cashback) AS Total_Cashback FROM Expenses;"
data = pd.read_sql_query(query, conn)
st.metric(label="Total Cashback Received", value=f"₹{data['Total_Cashback'][0]:,.2f}")

query = """SELECT Category, SUM(Amount_Paid) AS Total_Spending 
           FROM Expenses 
           GROUP BY Category 
           ORDER BY Total_Spending DESC 
           LIMIT 5;"""
data = pd.read_sql_query(query, conn)
st.bar_chart(data.set_index('Category')['Total_Spending'])

query = """SELECT Payment_Mode, SUM(Amount_Paid) AS Total_Spending 
           FROM Expenses 
           WHERE Category = 'Transportation' 
           GROUP BY Payment_Mode;"""
data = pd.read_sql_query(query, conn)
st.bar_chart(data.set_index('Payment_Mode')['Total_Spending'])

query = "SELECT * FROM Expenses WHERE Cashback > 0;"
data = pd.read_sql_query(query, conn)
st.dataframe(data)

query = """SELECT strftime('%m', Date) AS Month, SUM(Amount_Paid) AS Total_Spending 
           FROM Expenses 
           GROUP BY Month 
           ORDER BY Month;"""
data = pd.read_sql_query(query, conn)
st.line_chart(data.set_index('Month')['Total_Spending'])

query = """SELECT strftime('%m', Date) AS Month, Category, SUM(Amount_Paid) AS Total_Spending 
           FROM Expenses 
           WHERE Category IN ('Travel', 'Entertainment', 'Gifts') 
           GROUP BY Month, Category 
           ORDER BY Total_Spending DESC;"""
data = pd.read_sql_query(query, conn)
st.bar_chart(data.set_index(['Month', 'Category'])['Total_Spending'])

query = """SELECT strftime('%m', Date) AS Month, Description, SUM(Amount_Paid) AS Total_Spending 
           FROM Expenses 
           GROUP BY Month, Description 
           HAVING COUNT(*) > 1;"""
data = pd.read_sql_query(query, conn)
st.dataframe(data)

query = """SELECT strftime('%m', Date) AS Month, SUM(Cashback) AS Total_Cashback 
           FROM Expenses 
           GROUP BY Month;"""
data = pd.read_sql_query(query, conn)
st.line_chart(data.set_index('Month')['Total_Cashback'])

query = """SELECT Description, AVG(Amount_Paid) AS Avg_Cost 
           FROM Expenses 
           WHERE Category = 'Travel' 
           GROUP BY Description;"""
data = pd.read_sql_query(query, conn)
st.dataframe(data)

query = """SELECT strftime('%w', Date) AS DayOfWeek, SUM(Amount_Paid) AS Total_Spending 
           FROM Expenses 
           WHERE Category = 'Groceries' 
           GROUP BY DayOfWeek;"""
data = pd.read_sql_query(query, conn)
st.bar_chart(data.set_index('DayOfWeek')['Total_Spending'])

query = """SELECT Category, SUM(Amount_Paid) AS Total_Spending,
                  CASE 
                      WHEN SUM(Amount_Paid) > 1000 THEN 'High Priority'
                      ELSE 'Low Priority'
                  END AS Priority 
           FROM Expenses 
           GROUP BY Category;"""
data = pd.read_sql_query(query, conn)
st.dataframe(data)

query = """SELECT Category, SUM(Amount_Paid) * 100.0 / (SELECT SUM(Amount_Paid) FROM Expenses) AS Percentage 
           FROM Expenses 
           GROUP BY Category 
           ORDER BY Percentage DESC;"""
data = pd.read_sql_query(query, conn)
st.bar_chart(data.set_index('Category')['Percentage'])

