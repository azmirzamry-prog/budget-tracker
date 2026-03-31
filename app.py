import streamlit as st
import pandas as pd

# Title
st.title("💰 Personal Budget Tracker")

# Initialize session state to store expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Form input
st.subheader("Add a New Expense")

date = st.date_input("Date")
item = st.text_input("Expense Item")
amount = st.text_input("Amount Spent (RM)")

# Submit button
if st.button("Add Expense"):
    try:
        amount_value = float(amount)

        # Check if negative
        if amount_value < 0:
            st.error("Amount cannot be negative!")
        else:
            # Save data
            st.session_state.expenses.append({
                "Date": date,
                "Expense Item": item,
                "Amount (RM)": amount_value
            })
            st.success(f"Expense '{item}' added successfully!")

    except ValueError:
        st.error("Amount must be a valid number!")

# Display table
st.subheader("Expense Summary")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df)

    # Calculate total
    total = df["Amount (RM)"].sum()
    st.write(f"### Total Expenses: RM {total:.2f}")
else:
    st.write("No expenses recorded yet.")