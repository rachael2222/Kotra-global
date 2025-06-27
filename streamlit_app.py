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

# 100개국 데이터로 agencies 리스트를 대체합니다.
@st.cache_data
def load_agencies_data():
    agencies = [
        {
            "id": 1,
            "country": "미국",
            "organizationName": "International Trade Administration (ITA)",
            "city": "워싱턴 D.C.",
            "latitude": 38.9072,
            "longitude": -77.0369,
            "address": "1401 Constitution Ave NW, Washington, DC 20230",
            "phone": "+1-202-482-2000",
            "email": "contact@trade.gov",
            "website": "www.trade.gov",
            "description": "미국 상무부 국제무역청",
            "featured": True
        },
        {
            "id": 2,
            "country": "중국",
            "organizationName": "CCPIT (중국국제무역촉진위원회)",
            "city": "베이징",
            "latitude": 39.9042,
            "longitude": 116.4074,
            "address": "1 Fuxingmenwai Street, Beijing 100860",
            "phone": "+86-10-8807-5000",
            "email": "ccpit@ccpit.org",
            "website": "www.ccpit.org",
            "description": "중국 최대 무역투자 촉진기관",
            "featured": True
        },
        {
            "id": 3,
            "country": "일본",
            "organizationName": "JETRO (일본무역진흥기구)",
            "city": "도쿄",
            "latitude": 35.6762,
            "longitude": 139.6503,
            "address": "Ark Mori Building, 1-12-32 Akasaka, Minato-ku, Tokyo",
            "phone": "+81-3-3582-5511",
            "email": "jetro@jetro.go.jp",
            "website": "www.jetro.go.jp",
            "description": "일본 경제산업성 산하 무역진흥기관",
            "featured": True
        },
        {
            "id": 4,
            "country": "독일",
            "organizationName": "GTAI (Germany Trade & Invest)",
            "city": "베를린",
            "latitude": 52.5200,
            "longitude": 13.4050,
            "address": "Friedrichstrasse 60, 10117 Berlin",
            "phone": "+49-30-200-099-0",
            "email": "contact@gtai.de",
            "website": "www.gtai.de",
            "description": "독일 연방경제기후보호부 산하 무역투자진흥기관",
            "featured": True
        },
        {
            "id": 5,
            "country": "영국",
            "organizationName": "DBT (Department for Business and Trade)",
            "city": "런던",
            "latitude": 51.5074,
            "longitude": -0.1278,
            "address": "Old Admiralty Building, Admiralty Place, London SW1A 2DY",
            "phone": "+44-20-4551-0011",
            "email": "DBTNA@businessandtrade.gov.uk",
            "website": "www.gov.uk/government/organisations/department-for-business-and-trade",
            "description": "영국 정부 비즈니스 무역부",
            "featured": True
        },
        {
            "id": 6,
            "country": "싱가포르",
            "organizationName": "Enterprise Singapore",
            "city": "싱가포르",
            "latitude": 1.3000,
            "longitude": 103.8565,
            "address": "230 Victoria St, #10-00, Singapore 188024",
            "phone": "+65-6898-1800",
            "email": "enquiry@enterprisesg.gov.sg",
            "website": "www.enterprisesg.gov.sg",
            "description": "싱가포르 기업청 - 기업 성장 및 국제화 지원",
            "featured": True
        },
        {
            "id": 7,
            "country": "호주",
            "organizationName": "Austrade (Australian Trade and Investment Commission)",
            "city": "시드니",
            "latitude": -33.8688,
            "longitude": 151.2093,
            "address": "Level 11, 47 York Street, Sydney NSW 2000",
            "phone": "+61-2-9262-4011",
            "email": "info@austrade.gov.au",
            "website": "www.austrade.gov.au",
            "description": "호주 정부 무역투자진흥위원회",
            "featured": True
        },
        {
            "id": 8,
            "country": "인도",
            "organizationName": "FIEO - Federation of Indian Export Organisations",
            "city": "뉴델리",
            "latitude": 28.6139,
            "longitude": 77.2090,
            "address": "Vanijya Bhawan, International Trade Centre, New Delhi 110001",
            "phone": "+91-11-2331-4171",
            "email": "fieo@fieo.org",
            "website": "www.indiantradeportal.in",
            "description": "인도 수출기구연합회 - 무역진흥 및 수출촉진",
            "featured": True
        },
        {
            "id": 9,
            "country": "프랑스",
            "organizationName": "Business France",
            "city": "파리",
            "latitude": 48.8566,
            "longitude": 2.3522,
            "address": "77 boulevard Saint-Jacques, 75014 Paris",
            "phone": "+33-1-40-73-30-00",
            "email": "info@businessfrance.fr",
            "website": "www.businessfrance.fr",
            "description": "프랑스 대외무역투자진흥청",
            "featured": False
        },
        {
            "id": 10,
            "country": "이탈리아",
            "organizationName": "ITA (Italian Trade Agency)",
            "city": "로마",
            "latitude": 41.9028,
            "longitude": 12.4964,
            "address": "Via Liszt, 21, 00144 Roma",
            "phone": "+39-06-5992-1",
            "email": "info@ice.it",
            "website": "www.ice.it",
            "description": "이탈리아 대외무역진흥청",
            "featured": False
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
            location=[row['latitude'], row['longitude']],
            popup=f"""
            <div style="width: 250px;">
                <h4>{row['organizationName']}</h4>
                <p><strong>Country:</strong> {row['country']}</p>
                <p><strong>City:</strong> {row['city']}</p>
                <p><strong>Phone:</strong> {row['phone']}</p>
                <p><strong>Email:</strong> <a href="mailto:{row['email']}">{row['email']}</a></p>
                <p><strong>Website:</strong> <a href="https://{row['website']}" target="_blank">Visit</a></p>
            </div>
            """,
            tooltip=row['organizationName'],
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
    
    # 검색어
    search_term = st.sidebar.text_input("Search by name or city", "").lower()
    
    # 필터링 적용
    filtered_df = agencies_df.copy()
    
    if selected_country != 'All':
        filtered_df = filtered_df[filtered_df['country'] == selected_country]
    
    if search_term:
        filtered_df = filtered_df[
            filtered_df['organizationName'].str.lower().str.contains(search_term) |
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
        st.metric("Featured Agencies", len(agencies_df[agencies_df['featured'] == True]))
        st.metric("Countries Covered", len(agencies_df['country'].unique()))
        
        # 국가별 분포
        st.markdown("### Countries Distribution")
        country_counts = agencies_df['country'].value_counts()
        st.bar_chart(country_counts)
    
    # 기관 목록
    st.markdown('<h2 class="sub-header">📋 Agency List</h2>', unsafe_allow_html=True)
    
    for idx, row in filtered_df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="agency-card">
                <h3>{row['organizationName']}</h3>
                <p><strong>Country:</strong> {row['country']} | <strong>City:</strong> {row['city']}</p>
                <p><strong>Phone:</strong> {row['phone']} | <strong>Email:</strong> <a href="mailto:{row['email']}">{row['email']}</a></p>
                <p><strong>Website:</strong> <a href="https://{row['website']}" target="_blank">{row['website']}</a></p>
                <p><strong>Description:</strong> {row['description']}</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 