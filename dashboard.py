# Import library
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv("D:/Semester 6/Bangkit/Dicoding/Analisis_Data_Nadya/data/day.csv")
hour_df = pd.read_csv("D:/Semester 6/Bangkit/Dicoding/Analisis_Data_Nadya/data/hour.csv")


# Define title and styling
st.write('<h1 style="text-align: center;">Dashboard Analisis Data Bike Sharing</h1>', unsafe_allow_html=True)
st.write('<hr style="margin-bottom: 20px;">', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Bike Sharing Dashboard")
selected_option = st.sidebar.selectbox("Pilih Musim", ["", "Data Visual"])

# Load your CSV data
hour_data = pd.read_csv("hour.csv")
day_data = pd.read_csv("day.csv")

# Sidebar
st.sidebar.title("Download Data")


# Add button to download the main data CSV file in the sidebar
if st.sidebar.button("Download Main Data CSV"):
    csv = all_df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Some encoding
    href = f'<a href="data:file/csv;base64,{b64}" download="main_data.csv">Download Main Data CSV</a>'
    st.sidebar.markdown(href, unsafe_allow_html=True)

# Main content
if selected_option == "Tabel":
    st.subheader("Tabel Data")
    st.write("### Day Dataset")
    st.write(day_df.describe())
    st.write("### Hour Dataset")
    st.write(hour_df.describe())

elif selected_option == "Data Visual":
    # Data Visual jumlah peminjaman sepeda berdasarkan hari dalam seminggu
    st.subheader('Data Visual jumlah peminjaman sepeda berdasarkan hari dalam seminggu')
    fig1 = plt.figure(figsize=(12, 6))
    sns.lineplot(data=day_df, x='weekday', y='cnt', hue='season')
    plt.title('Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Peminjaman')
    plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    plt.legend(title='Musim')
    st.pyplot(fig1)

    # Data Visual jumlah peminjaman sepeda berdasarkan jam dalam sehari
    st.subheader('Data Visual jumlah peminjaman sepeda berdasarkan jam dalam sehari')
    fig2 = plt.figure(figsize=(12, 6))
    sns.lineplot(data=hour_df, x='hr', y='cnt', hue='season')
    plt.title('Jumlah Peminjaman Sepeda Berdasarkan Jam dalam Sehari')
    plt.xlabel('Jam dalam Sehari')
    plt.ylabel('Jumlah Peminjaman')
    plt.legend(title='Musim')
    st.pyplot(fig2)
