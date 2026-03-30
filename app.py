import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AirFly Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AirFly Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("data/Airline_Dataset_Updated_Final.xlsx")
        return df
    except FileNotFoundError:
        st.error("❌ Data file not found! Please check the file path.")
        st.stop()

df = load_data()

# ----------------------------
# HEADER
# ----------------------------
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>✈️ AirFly Insights Dashboard</h1>
    <p style='text-align: center; color: #666;'>Analyze airline performance, delays, and trends</p>
""", unsafe_allow_html=True)

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------
st.sidebar.header("🔍 Filters")

country = st.sidebar.multiselect(
    "🌍 Country",
    options=sorted(df['Country Name'].unique()),
    default=sorted(df['Country Name'].unique())
)

month = st.sidebar.multiselect(
    "📅 Month",
    options=sorted(df['Month'].unique()),
    default=sorted(df['Month'].unique())
)

# Apply filters
filtered_df = df[
    (df['Country Name'].isin(country)) &
    (df['Month'].isin(month))
].copy()

# ----------------------------
# KPI CARDS
# ----------------------------
st.markdown("## 📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="background-color:#E8F0FE;padding:20px;border-radius:10px;text-align:center">
    <h3>Total Flights</h3>
    <h2 style='color:#1f77b4;'>{len(filtered_df):,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    delayed_count = filtered_df['IsDelayed'].sum() if 'IsDelayed' in filtered_df.columns else 0
    st.markdown(f"""
    <div style="background-color:#FFE8E8;padding:20px;border-radius:10px;text-align:center">
    <h3>Delayed Flights</h3>
    <h2 style='color:#ff4444;'>{delayed_count:,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    cancelled_count = filtered_df['IsCancelled'].sum() if 'IsCancelled' in filtered_df.columns else 0
    st.markdown(f"""
    <div style="background-color:#E8FFE8;padding:20px;border-radius:10px;text-align:center">
    <h3>Cancelled Flights</h3>
    <h2 style='color:#2ca02c;'>{cancelled_count:,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    delay_rate = (delayed_count / len(filtered_df) * 100) if len(filtered_df) > 0 else 0
    st.markdown(f"""
    <div style="background-color:#FFF3E8;padding:20px;border-radius:10px;text-align:center">
    <h3>Delay Rate</h3>
    <h2 style='color:#ff7f0e;'>{delay_rate:.1f}%</h2>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# TABS
# ----------------------------
tab1, tab2, tab3 = st.tabs(["📌 Overview", "⏱️ Delay Analysis", "🌍 Route & Airport"])

# ----------------------------
# TAB 1: OVERVIEW
# ----------------------------
with tab1:
    st.subheader("📌 Flight Status Distribution")
    
    # ✅ CORRECTED - This fixes your error!
    if 'Flight Status' in filtered_df.columns and len(filtered_df) > 0:
        status_data = filtered_df['Flight Status'].value_counts().reset_index()
        status_data.columns = ['Flight Status', 'Count']
        
        fig1 = px.pie(
            status_data,
            names='Flight Status',  # ✅ CORRECT column name
            values='Count',         # ✅ CORRECT column name
            title='Flight Status Distribution',
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig1.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("No Flight Status data available")

    st.subheader("📅 Monthly Flight Trend")
    if len(filtered_df) > 0:
        monthly = filtered_df.groupby('Month').size().reset_index(name='Flights')
        fig2 = px.line(
            monthly, x='Month', y='Flights',
            markers=True,
            title='Flights by Month',
            color_discrete_sequence=['#1f77b4']
        )
        st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# TAB 2: DELAY ANALYSIS
# ----------------------------
with tab2:
    st.subheader("⚖️ Delay vs Cancellation")
    
    delay_cancel = pd.DataFrame({
        'Type': ['Delayed', 'Cancelled'],
        'Count': [
            filtered_df['IsDelayed'].sum() if 'IsDelayed' in filtered_df.columns else 0,
            filtered_df['IsCancelled'].sum() if 'IsCancelled' in filtered_df.columns else 0
        ]
    })
    
    fig3 = px.bar(
        delay_cancel, x='Type', y='Count',
        title='Delay vs Cancellation',
        color='Type',
        color_discrete_sequence=['#ff7f0e', '#2ca02c']
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("👥 Gender Distribution")
    if 'Gender' in filtered_df.columns:
        gender_data = filtered_df['Gender'].value_counts().reset_index()
        gender_data.columns = ['Gender', 'Count']
        
        fig4 = px.pie(
            gender_data,
            names='Gender',
            values='Count',
            title='Gender Distribution',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig4, use_container_width=True)

# ----------------------------
# TAB 3: ROUTE & AIRPORT
# ----------------------------
with tab3:
    st.subheader("🌍 Top 10 Routes")
    if 'Route' in filtered_df.columns:
        routes = filtered_df['Route'].value_counts().head(10).reset_index()
        routes.columns = ['Route', 'Flights']
        
        fig5 = px.bar(
            routes, x='Flights', y='Route',
            title='Top Routes by Flight Count',
            color='Flights',
            color_continuous_scale='Blues',
            orientation='h'
        )
        st.plotly_chart(fig5, use_container_width=True)

    st.subheader("🏢 Top 10 Airports")
    if 'Airport Name' in filtered_df.columns:
        airports = filtered_df['Airport Name'].value_counts().head(10).reset_index()
        airports.columns = ['Airport', 'Flights']
        
        fig6 = px.bar(
            airports, x='Flights', y='Airport',
            title='Top Airports by Flight Count',
            color='Flights',
            color_continuous_scale='Viridis',
            orientation='h'
        )
        st.plotly_chart(fig6, use_container_width=True)

# ----------------------------
# DATA PREVIEW
# ----------------------------
with st.expander("📄 Data Preview (First 100 rows)"):
    st.dataframe(filtered_df.head(100), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Made with ❤️ using Streamlit & Plotly</p>", unsafe_allow_html=True)
# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("data/Airline_Dataset_Updated_Final.xlsx")
        return df
    except FileNotFoundError:
        st.error("❌ Data file not found! Please check the file path.")
        st.stop()

df = load_data()

# ----------------------------
# HEADER
# ----------------------------
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>✈️ AirFly Insights Dashboard</h1>
    <p style='text-align: center; color: #666;'>Analyze airline performance, delays, and trends</p>
""", unsafe_allow_html=True)

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------
st.sidebar.header("🔍 Filters")

country = st.sidebar.multiselect(
    "🌍 Country",
    options=sorted(df['Country Name'].unique()),
    default=sorted(df['Country Name'].unique())
)

month = st.sidebar.multiselect(
    "📅 Month",
    options=sorted(df['Month'].unique()),
    default=sorted(df['Month'].unique())
)

# Apply filters
filtered_df = df[
    (df['Country Name'].isin(country)) &
    (df['Month'].isin(month))
].copy()

# ----------------------------
# KPI CARDS
# ----------------------------
st.markdown("## 📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="background-color:#E8F0FE;padding:20px;border-radius:10px;text-align:center">
    <h3>Total Flights</h3>
    <h2 style='color:#1f77b4;'>{len(filtered_df):,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    delayed_count = filtered_df['IsDelayed'].sum() if 'IsDelayed' in filtered_df.columns else 0
    st.markdown(f"""
    <div style="background-color:#FFE8E8;padding:20px;border-radius:10px;text-align:center">
    <h3>Delayed Flights</h3>
    <h2 style='color:#ff4444;'>{delayed_count:,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    cancelled_count = filtered_df['IsCancelled'].sum() if 'IsCancelled' in filtered_df.columns else 0
    st.markdown(f"""
    <div style="background-color:#E8FFE8;padding:20px;border-radius:10px;text-align:center">
    <h3>Cancelled Flights</h3>
    <h2 style='color:#2ca02c;'>{cancelled_count:,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    delay_rate = (delayed_count / len(filtered_df) * 100) if len(filtered_df) > 0 else 0
    st.markdown(f"""
    <div style="background-color:#FFF3E8;padding:20px;border-radius:10px;text-align:center">
    <h3>Delay Rate</h3>
    <h2 style='color:#ff7f0e;'>{delay_rate:.1f}%</h2>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# TABS
# ----------------------------
tab1, tab2, tab3 = st.tabs(["📌 Overview", "⏱️ Delay Analysis", "🌍 Route & Airport"])

# ----------------------------
# TAB 1: OVERVIEW
# ----------------------------
with tab1:
    st.subheader("📌 Flight Status Distribution")
    
    # ✅ CORRECTED - This fixes your error!
    if 'Flight Status' in filtered_df.columns and len(filtered_df) > 0:
        status_data = filtered_df['Flight Status'].value_counts().reset_index()
        status_data.columns = ['Flight Status', 'Count']
        
        fig1 = px.pie(
            status_data,
            names='Flight Status',  # ✅ CORRECT column name
            values='Count',         # ✅ CORRECT column name
            title='Flight Status Distribution',
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig1.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("No Flight Status data available")

    st.subheader("📅 Monthly Flight Trend")
    if len(filtered_df) > 0:
        monthly = filtered_df.groupby('Month').size().reset_index(name='Flights')
        fig2 = px.line(
            monthly, x='Month', y='Flights',
            markers=True,
            title='Flights by Month',
            color_discrete_sequence=['#1f77b4']
        )
        st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# TAB 2: DELAY ANALYSIS
# ----------------------------
with tab2:
    st.subheader("⚖️ Delay vs Cancellation")
    
    delay_cancel = pd.DataFrame({
        'Type': ['Delayed', 'Cancelled'],
        'Count': [
            filtered_df['IsDelayed'].sum() if 'IsDelayed' in filtered_df.columns else 0,
            filtered_df['IsCancelled'].sum() if 'IsCancelled' in filtered_df.columns else 0
        ]
    })
    
    fig3 = px.bar(
        delay_cancel, x='Type', y='Count',
        title='Delay vs Cancellation',
        color='Type',
        color_discrete_sequence=['#ff7f0e', '#2ca02c']
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("👥 Gender Distribution")
    if 'Gender' in filtered_df.columns:
        gender_data = filtered_df['Gender'].value_counts().reset_index()
        gender_data.columns = ['Gender', 'Count']
        
        fig4 = px.pie(
            gender_data,
            names='Gender',
            values='Count',
            title='Gender Distribution',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig4, use_container_width=True)

# ----------------------------
# TAB 3: ROUTE & AIRPORT
# ----------------------------
with tab3:
    st.subheader("🌍 Top 10 Routes")
    if 'Route' in filtered_df.columns:
        routes = filtered_df['Route'].value_counts().head(10).reset_index()
        routes.columns = ['Route', 'Flights']
        
        fig5 = px.bar(
            routes, x='Flights', y='Route',
            title='Top Routes by Flight Count',
            color='Flights',
            color_continuous_scale='Blues',
            orientation='h'
        )
        st.plotly_chart(fig5, use_container_width=True)

    st.subheader("🏢 Top 10 Airports")
    if 'Airport Name' in filtered_df.columns:
        airports = filtered_df['Airport Name'].value_counts().head(10).reset_index()
        airports.columns = ['Airport', 'Flights']
        
        fig6 = px.bar(
            airports, x='Flights', y='Airport',
            title='Top Airports by Flight Count',
            color='Flights',
            color_continuous_scale='Viridis',
            orientation='h'
        )
        st.plotly_chart(fig6, use_container_width=True)

# ----------------------------
# DATA PREVIEW
# ----------------------------
with st.expander("📄 Data Preview (First 100 rows)"):
    st.dataframe(filtered_df.head(100), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Made with ❤️ using Streamlit & Plotly</p>", unsafe_allow_html=True)