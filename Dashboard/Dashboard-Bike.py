pip install streamlit babel

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

cleaned_days_df = pd.read_csv("cleaned_days.csv")
cleaned_days_df.head()

cleaned_days_df.groupby(by=["yr", "season", "mnth"]).agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum",
    "dteday": "first"
}).reset_index().sort_values(by=["dteday"], ascending=[True])

cleaned_days_df['dteday'] = pd.to_datetime(cleaned_days_df['dteday'])

monthly_users_df = cleaned_days_df.resample(rule='M', on='dteday').agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
})

monthly_users_df = cleaned_days_df.resample(rule='M', on='dteday').agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
})

monthly_users_df.index = pd.to_datetime(monthly_users_df.index)
monthly_users_df.index = monthly_users_df.index.strftime('%b-%y')
monthly_users_df = monthly_users_df.reset_index()
monthly_users_df = monthly_users_df.rename(columns={'dteday': 'month-year'})

type_users_df = cleaned_days_df.resample(rule='M', on='dteday').agg({
    "casual": "mean",
    "registered": "mean",
    'cnt': "mean"
})

type_users_df.index = pd.to_datetime(type_users_df.index)
type_users_df.index = type_users_df.index.strftime('%b-%y')
type_users_df = type_users_df.reset_index()
type_users_df = type_users_df.rename(columns={'dteday': 'month-year'})

type_users_df["%casual"] = (type_users_df["casual"]/type_users_df["cnt"])*100
type_users_df["%registered"] = (type_users_df["registered"]/type_users_df["cnt"])*100

seasonal_users_df = cleaned_days_df.groupby(by="season").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum",
}).reset_index().sort_values(by=["season"], ascending=[True])

# QUESTION 1
st.subheader('Bike Share Trend')

col1, col2 = st.columns(2)

# Chart 1 - Monthly count of casual and registered bikeshare rides
with col1:
    fig, ax = plt.subplots(figsize=(16, 6))
    
    # Create line plots using sns.lineplot
    sns.lineplot(x="month-year", y="casual", data=monthly_users_df, label='Casual')
    sns.lineplot(x="month-year", y="registered", data=monthly_users_df, label='Registered')

    # Customize the plot
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Rides")
    ax.set_title("Monthly count of casual and registered bikeshare rides (2011-2012)", loc="center", fontsize=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    plt.legend(loc='upper right', fontsize=10)

    # Show the plot using st.pyplot
    st.pyplot(fig)

# Chart 2 - Ratio of casual to sum of all bikeshare rides
with col2:
    fig, ax = plt.subplots(figsize=(16, 6))

    # Create line plot for the ratio
    sns.lineplot(x="month-year", y="%casual", data=type_users_df, label='Casual')

    # Customize the plot
    ax.set_xlabel("Date")
    ax.set_ylabel("Ratio (%)")
    ax.set_title("Ratio of casual to sum of all bikeshare rides (2011-2012)", loc="center", fontsize=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    plt.legend(loc='upper right', fontsize=10)

    # Show the plot using st.pyplot
    st.pyplot(fig)

# QUESTION 2
st.subheader('Bike Share Seasonal Trend Usage')

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 5))

sns.barplot(x='season',
            y='cnt',
            data=seasonal_users_df,
            palette="viridis")

# Customize the plot
ax.set_title('Histogram of Users Count by Season')
ax.set_xlabel('Season')
ax.set_ylabel('Count of Users')
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

# Show the plot
st.pyplot(fig)

# QUESTION 3
st.subheader('Correlation Environmental Condition to Bike Share Usage')

fig, ax = plt.subplots(figsize=(14,6))

sns.scatterplot(x='hum', y='cnt', data=cleaned_days_df, hue='season')

ax.set_xlabel("Humidity (%)")
ax.set_ylabel("Number of Users")
ax.set_title("Correlation of active Users related to Humidity of the Season")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

# Show the plot
st.pyplot(fig)
