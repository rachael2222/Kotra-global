import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import json
from typing import Dict, List

# 페이지 설정
st.set_page_config(
    page_title="Global Trade-Investment Promotion Agency",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일링
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .agency-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .search-box {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# 샘플 데이터 (실제 KOTRA 데이터로 교체 가능)
@st.cache_data
def load_agencies_data():
    agencies = [
        {
            "country": "South Korea",
            "city": "Seoul",
            "name": "KOTRA Headquarters",
            "address": "13, Heolleung-ro, Seocho-gu, Seoul",
            "phone": "+82-2-3460-7114",
            "email": "info@kotra.or.kr",
            "website": "https://www.kotra.or.kr",
            "services": ["Trade Promotion", "Investment Support", "Market Research"],
            "lat": 37.5665,
            "lng": 126.9780
        },
        {
            "country": "United States",
            "city": "New York",
            "name": "KOTRA New York",
            "address": "460 Park Avenue, New York, NY 10022",
            "phone": "+1-212-826-0900",
            "email": "newyork@kotra.or.kr",
            "website": "https://www.kotra.or.kr/usa",
            "services": ["Trade Promotion", "Investment Support"],
            "lat": 40.7128,
            "lng": -74.0060
        },
        {
            "country": "Germany",
            "city": "Frankfurt",
            "name": "KOTRA Frankfurt",
            "address": "Kaiserstraße 11, 60311 Frankfurt",
            "phone": "+49-69-920-7170",
            "email": "frankfurt@kotra.or.kr",
            "website": "https://www.kotra.or.kr/germany",
            "services": ["Trade Promotion", "Market Research"],
            "lat": 50.1109,
            "lng": 8.6821
        },
        {
            "country": "Japan",
            "city": "Tokyo",
            "name": "KOTRA Tokyo",
            "address": "2-2-2 Marunouchi, Chiyoda-ku, Tokyo",
            "phone": "+81-3-3211-1900",
            "email": "tokyo@kotra.or.kr",
            "website": "https://www.kotra.or.kr/japan",
            "services": ["Trade Promotion", "Investment Support"],
            "lat": 35.6762,
            "lng": 139.6503
        },
        {
            "country": "China",
            "city": "Beijing",
            "name": "KOTRA Beijing",
            "address": "No. 1 Jianguomenwai Avenue, Beijing",
            "phone": "+86-10-6505-1188",
            "email": "beijing@kotra.or.kr",
            "website": "https://www.kotra.or.kr/china",
            "services": ["Trade Promotion", "Market Research"],
            "lat": 39.9042,
            "lng": 116.4074
        }
    ]
    return pd.DataFrame(agencies)

def create_world_map(agencies_df):
    """세계 지도 생성"""
    # 중심을 서울로 설정
    m = folium.Map(
        location=[37.5665, 126.9780],
        zoom_start=3,
        tiles='OpenStreetMap'
    )
    
    # 각 기관에 마커 추가
    for idx, row in agencies_df.iterrows():
        folium.Marker(
            location=[row['lat'], row['lng']],
            popup=f"""
            <div style="width: 200px;">
                <h4>{row['name']}</h4>
                <p><strong>Country:</strong> {row['country']}</p>
                <p><strong>City:</strong> {row['city']}</p>
                <p><strong>Phone:</strong> {row['phone']}</p>
                <p><strong>Email:</strong> {row['email']}</p>
                <p><strong>Website:</strong> <a href="{row['website']}" target="_blank">Visit</a></p>
            </div>
            """,
            tooltip=row['name'],
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    
    return m

def main():
    # 메인 헤더
    st.markdown('<h1 class="main-header">🌍 Global Trade-Investment Promotion Agency</h1>', unsafe_allow_html=True)
    st.markdown("### Connecting Global Businesses with Korean Trade Opportunities")
    
    # 데이터 로드
    agencies_df = load_agencies_data()
    
    # 사이드바 - 검색 및 필터
    st.sidebar.markdown("## 🔍 Search & Filter")
    
    # 국가별 필터
    countries = ['All'] + sorted(agencies_df['country'].unique().tolist())
    selected_country = st.sidebar.selectbox("Select Country", countries)
    
    # 서비스별 필터
    all_services = []
    for services in agencies_df['services']:
        all_services.extend(services)
    unique_services = ['All'] + sorted(list(set(all_services)))
    selected_service = st.sidebar.selectbox("Select Service", unique_services)
    
    # 검색어
    search_term = st.sidebar.text_input("Search by name or city", "").lower()
    
    # 필터링 적용
    filtered_df = agencies_df.copy()
    
    if selected_country != 'All':
        filtered_df = filtered_df[filtered_df['country'] == selected_country]
    
    if selected_service != 'All':
        filtered_df = filtered_df[filtered_df['services'].apply(lambda x: selected_service in x)]
    
    if search_term:
        filtered_df = filtered_df[
            filtered_df['name'].str.lower().str.contains(search_term) |
            filtered_df['city'].str.lower().str.contains(search_term)
        ]
    
    # 메인 컨텐츠
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="sub-header">🗺️ Global Network Map</h2>', unsafe_allow_html=True)
        
        if not filtered_df.empty:
            world_map = create_world_map(filtered_df)
            folium_static(world_map, width=700, height=500)
        else:
            st.warning("No agencies found matching your criteria.")
    
    with col2:
        st.markdown('<h2 class="sub-header">📊 Statistics</h2>', unsafe_allow_html=True)
        
        # 통계 정보
        st.metric("Total Agencies", len(agencies_df))
        st.metric("Countries Covered", len(agencies_df['country'].unique()))
        st.metric("Filtered Results", len(filtered_df))
        
        # 국가별 분포
        st.markdown("### Countries Distribution")
        country_counts = agencies_df['country'].value_counts()
        st.bar_chart(country_counts)
    
    # 기관 목록
    st.markdown('<h2 class="sub-header">🏢 Agency Directory</h2>', unsafe_allow_html=True)
    
    if not filtered_df.empty:
        for idx, row in filtered_df.iterrows():
            with st.expander(f"📍 {row['name']} - {row['city']}, {row['country']}"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Address:** {row['address']}")
                    st.markdown(f"**Phone:** {row['phone']}")
                    st.markdown(f"**Email:** {row['email']}")
                    st.markdown(f"**Website:** [{row['website']}]({row['website']})")
                
                with col2:
                    st.markdown("**Services:**")
                    for service in row['services']:
                        st.markdown(f"• {service}")
    
    # 푸터
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>© 2024 Global Trade-Investment Promotion Agency Platform</p>
        <p>Powered by Streamlit | Data provided by KOTRA</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 