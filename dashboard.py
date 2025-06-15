import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analisis E-Commerce",
    page_icon="📈",
    layout="wide"
)

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)

    df['sold_at'] = pd.to_datetime(df['sold_at'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['sale_month'] = df['sold_at'].dt.to_period('M').astype(str) # Ubah ke string agar bisa di-filter
    return df

df = load_data('dataset/inventory_item_cleaned_final.csv')


st.title('📈 Dashboard Analisis Inventory Item E-Commerce')
st.markdown('---')


st.sidebar.header('Filter Data:')

selected_category = st.sidebar.multiselect(
    'Pilih Kategori Produk:',
    options=df['product_category'].unique(),
    default=df['product_category'].unique()[:5]
)

df_filtered = df[df['product_category'].isin(selected_category)]


st.header('Ringkasan Bisnis Keseluruhan')
total_profit = df_filtered['profit'].sum()
total_sales_count = df_filtered['is_sold'].sum()
avg_days_to_sell = df_filtered['days_to_sell'].mean()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Profit", f"US$ {total_profit:,.2f}")
with col2:
    st.metric("Total Produk Terjual", f"{int(total_sales_count):,}")
with col3:
    st.metric("Rata-rata Hari Penjualan", f"{avg_days_to_sell:.1f} Hari")

st.markdown('---')


st.header('Visualisasi Analisis')

col_viz1, col_viz2 = st.columns(2)

with col_viz1:

    st.subheader('Top Kategori Paling Menguntungkan')
    profit_by_category = df_filtered.groupby('product_category')['profit'].sum().nlargest(10).sort_values()
    fig_profit = px.bar(
        profit_by_category,
        x='profit',
        y=profit_by_category.index,
        orientation='h',
        title='Total Profit per Kategori Produk',
        labels={'profit': 'Total Profit (US$)', 'index': 'Kategori Produk'},
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    st.plotly_chart(fig_profit, use_container_width=True)

    st.subheader('Top Merek Paling Laris')
    brand_sales = df_filtered[df_filtered['is_sold']].groupby('product_brand').size().nlargest(10).sort_values()
    fig_brand = px.bar(
        brand_sales,
        x=brand_sales.values,
        y=brand_sales.index,
        orientation='h',
        title='Jumlah Penjualan per Merek',
        labels={'x': 'Jumlah Terjual', 'index': 'Merek'},
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    st.plotly_chart(fig_brand, use_container_width=True)


with col_viz2:
    st.subheader('Kategori dengan Perputaran Tercepat')
    turnover_by_category = df_filtered.groupby('product_category')['days_to_sell'].mean().nsmallest(10).sort_values(ascending=False)
    fig_turnover = px.bar(
        turnover_by_category,
        x='days_to_sell',
        y=turnover_by_category.index,
        orientation='h',
        title='Rata-rata Hari untuk Terjual',
        labels={'days_to_sell': 'Rata-rata Hari', 'index': 'Kategori Produk'},
        color_discrete_sequence=px.colors.qualitative.G10
    )
    st.plotly_chart(fig_turnover, use_container_width=True)

    st.subheader('Tren Penjualan Bulanan')
    monthly_sales = df_filtered.groupby('sale_month')['is_sold'].sum().reset_index()
    monthly_sales = monthly_sales.sort_values('sale_month')
    fig_trend = px.line(
        monthly_sales,
        x='sale_month',
        y='is_sold',
        title='Jumlah Penjualan per Bulan',
        labels={'sale_month': 'Bulan', 'is_sold': 'Jumlah Terjual'},
        markers=True
    )
    st.plotly_chart(fig_trend, use_container_width=True)

st.markdown('---')