
import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import plotly.express as px 


#Connected to MYSQL
def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Anjana@2025",
            database="Expense_Tracker"
        )
        return connection
    except mysql.connector.Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Function to execute a query and return the result as a DataFrame
def execute_query(query):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            connection.close()
            return pd.DataFrame(result)
        except mysql.connector.Error as e:
            st.error(f"Error executing query: {e}")
            return pd.DataFrame()
    else:
        return pd.DataFrame()

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",  
    layout="centered"  
)
st.title("💰 Expense Tracker")

data ={
    "Total_Exp for the year 2024": "SELECT SUM(Amount) AS TotalExpense FROM per_exp_track",
    "cashback_query": "SELECT SUM(Cashback) AS TotalCashback FROM per_exp_track",
    "MAX_Exp_Amount": "SELECT MAX(Amount) AS Maxexpamount FROM per_exp_track",
    "AVG_Amount": "SELECT AVG(Amount) AS Avgamount FROM per_exp_track",
    "Total_Exp for Month": "SELECT DATE_FORMAT(Date, '%Y-%m') AS Month, SUM(Amount) AS Total_Expense FROM per_exp_track WHERE Date >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH) GROUP BY DATE_FORMAT(Date, '%Y-%m') ORDER BY Month ASC",
    "Great_Amount_query": "SELECT * FROM per_exp_track WHERE Amount > 1000 LIMIT 10",
    "UPI_query": "SELECT * FROM per_exp_track WHERE Paymentmode = 'UPI' ",
    "Cate_Fee_query": "SELECT * FROM per_exp_track WHERE Categories = 'Fees' ",
    "DESC_Amt_query": "SELECT * FROM per_exp_track ORDER BY Amount DESC LIMIT 10",
    "Category_query": "SELECT Categories, COUNT(*) AS Trancount FROM per_exp_track GROUP BY Categories UNION ALL SELECT 'Total' AS Categories, COUNT(*) AS Trancount FROM per_exp_track",
    "Category_Amt_query": "SELECT Categories, SUM(Amount) AS Total FROM per_exp_track GROUP BY Categories ORDER BY Categories ASC",
    "Paymode_query": "SELECT Paymentmode, COUNT(*) AS Transcount FROM per_exp_track GROUP BY Paymentmode",
    "Group_by_Month": "SELECT Categories, MONTH(Date) AS Month, COUNT(*) AS Count, SUM(Amount) AS Totalexp FROM per_exp_track GROUP BY Categories, MONTH(Date) ORDER BY Categories, Month LIMIT 20",
    "May_Month_query": "SELECT * FROM per_exp_track WHERE Date BETWEEN '2024-05-01' AND '2024-05-31' LIMIT 10",
    "Dec_Month_query": "SELECT * FROM per_exp_track WHERE MONTH(Date) = 12 AND YEAR(Date) = 2024",
    "REC_Date_Exp": "SELECT * FROM per_exp_track ORDER BY Date DESC LIMIT 10",
    "REC_Exp_Amt_DESC": "SELECT * FROM per_exp_track ORDER BY Amount DESC LIMIT 10",
    "Exp_Shop": "SELECT COUNT(*) AS total_expenses, SUM(Amount) FROM per_exp_track WHERE Categories='shopping'",
    "Concat_query": "SELECT CONCAT(Paymentmode, ' - ', Categories) AS Combined_Column, Amount FROM per_exp_track LIMIT 6"
}

#Execute the Queries
select_option = st.selectbox("Select a Query to Execute:", list(data.keys()))
if select_option:
    query = data[select_option]
    st.write("Executing query")
    if st.button("submit"):
        result_df = execute_query(query) 
    
        if not result_df.empty:
            st.write("Query Result:")
            st.dataframe(result_df)
            st.success("Query results submitted successfully!")

        #Visualize the Queries
            if select_option == "Category_Amt_query":
                st.write("Pie - Chart")
                fig = px.pie(result_df, names="Categories", values="Total", title="Category Wise Amount Visualization:",color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig)
                st.write("Bar Chart")
                st.bar_chart(result_df.set_index("Categories")["Total"])
                st.write("Scatter Chart")
                st.scatter_chart(result_df.set_index("Categories")["Total"])
                st.write("Line Chart")
                st.line_chart(result_df.set_index("Categories")["Total"])
                
            
            elif select_option == "May_Month_query":
                st.write("Bar Chart")
                st.bar_chart(result_df.set_index("Date")["Amount"])
                st.write("Line Chart")
                st.line_chart(result_df.set_index("Date")["Amount"])
           
            elif select_option == "Concat_query":
                st.subheader("Concat Column:")
                st.write("Bar Chart")
                st.bar_chart(result_df.set_index("Amount")["Combined_Column"])
                st.write("Line Chart")
                st.line_chart(result_df.set_index("Amount")["Combined_Column"])
                st.write("Pie - Chart")
                fig = px.pie(result_df,names="Combined_Column", values="Amount", title="Concat the Categories and Paymentmode", color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig)
            
            elif select_option == "Total_Exp for Month":
                st.write("Pie - Chart")
                fig = px.pie(result_df,names="Month", values="Total_Expense", title="Expense Distribution by Categories", color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig)
            
            elif select_option == "Paymode_query":
                st.write("Pie - Chart")
                fig = px.pie(result_df, names="Paymentmode", values="Transcount", title="Payment Mode Visualiztion",color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig)
            
        else:
            st.warning("No data to display.")