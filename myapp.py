import pandas as pd
import streamlit as st

st.title("Know your hospital near by")
st.subheader("Primary Health Care Facilities in WashingTom DC")


# st.cache saves the data so we save on network calls
@st.cache
def fetch_data():
    df = pd.read_csv('Primary_Care_Centers.csv')
    # rename for ST map function requirement & simplicity
    df = df.rename(columns={
        'X': 'longitude',
        'Y': 'latitude',
        'PrimaryCarePtWARD': 'ward'
    })
    return df


data = fetch_data()

# Chart 1: Interactive Map
st.write('## Map of Hospitals')
st.map(data)

# Chart 2: Bar chart of hospitals by ward
# @st.cache
def hospitals_by_ward(data):
    if st.checkbox("Show the Bar Chart"):
        return data['ward'].value_counts()


st.write('## Hospital count by ward')
st.bar_chart(hospitals_by_ward(data))

# Table 1: Raw data
st.write('## Raw hospital data')
if st.checkbox("Show the data"):
    st.dataframe(data)