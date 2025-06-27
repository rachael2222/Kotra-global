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

# 150여개국 데이터
@st.cache_data
def load_agencies_data():
    agencies = [
        # 주요 국가들 (featured)
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
        },
        {
            "id": 11,
            "country": "스페인",
            "organizationName": "ICEX España",
            "city": "마드리드",
            "latitude": 40.4168,
            "longitude": -3.7038,
            "address": "Paseo de la Castellana, 14-16, 28046 Madrid",
            "phone": "+34-91-349-6100",
            "email": "info@icex.es",
            "website": "www.icex.es",
            "description": "스페인 대외무역투자진흥원",
            "featured": False
        },
        {
            "id": 12,
            "country": "네덜란드",
            "organizationName": "Netherlands Enterprise Agency",
            "city": "헤이그",
            "latitude": 52.3676,
            "longitude": 4.9041,
            "address": "Prinses Beatrixlaan 2, The Hague",
            "phone": "+31-88-042-42-42",
            "email": "info@rvo.nl",
            "website": "www.rvo.nl",
            "description": "네덜란드 기업청",
            "featured": False
        },
        {
            "id": 13,
            "country": "스위스",
            "organizationName": "Switzerland Global Enterprise",
            "city": "취리히",
            "latitude": 47.3769,
            "longitude": 8.5417,
            "address": "Stampfenbachstrasse 85, 8006 Zurich",
            "phone": "+41-44-365-51-51",
            "email": "info@s-ge.com",
            "website": "www.s-ge.com",
            "description": "스위스 글로벌 기업청",
            "featured": False
        },
        {
            "id": 14,
            "country": "스웨덴",
            "organizationName": "Business Sweden",
            "city": "스톡홀름",
            "latitude": 59.3293,
            "longitude": 18.0686,
            "address": "Box 240, SE-101 24 Stockholm",
            "phone": "+46-8-588-660-00",
            "email": "info@business-sweden.se",
            "website": "www.business-sweden.se",
            "description": "스웨덴 무역투자진흥청",
            "featured": False
        },
        {
            "id": 15,
            "country": "노르웨이",
            "organizationName": "Innovation Norway",
            "city": "오슬로",
            "latitude": 59.9139,
            "longitude": 10.7522,
            "address": "Akersgata 13, 0158 Oslo",
            "phone": "+47-22-00-25-00",
            "email": "post@innovasjonnorge.no",
            "website": "www.innovasjonnorge.no",
            "description": "노르웨이 혁신청",
            "featured": False
        },
        {
            "id": 16,
            "country": "덴마크",
            "organizationName": "Danish Agency for Trade Promotion",
            "city": "코펜하겐",
            "latitude": 55.6761,
            "longitude": 12.5683,
            "address": "Toldbodgade 29, 1253 Copenhagen",
            "phone": "+45-33-92-00-00",
            "email": "info@um.dk",
            "website": "www.um.dk",
            "description": "덴마크 무역진흥청",
            "featured": False
        },
        {
            "id": 17,
            "country": "핀란드",
            "organizationName": "Business Finland",
            "city": "헬싱키",
            "latitude": 60.1699,
            "longitude": 24.9384,
            "address": "Porkkalankatu 1, 00180 Helsinki",
            "phone": "+358-29-505-5000",
            "email": "info@businessfinland.fi",
            "website": "www.businessfinland.fi",
            "description": "핀란드 비즈니스청",
            "featured": False
        },
        {
            "id": 18,
            "country": "오스트리아",
            "organizationName": "ABA - Invest in Austria",
            "city": "비엔나",
            "latitude": 48.2082,
            "longitude": 16.3738,
            "address": "Landstraßer Hauptstraße 71, 1030 Vienna",
            "phone": "+43-1-588-58-0",
            "email": "info@aba.gv.at",
            "website": "www.investinaustria.at",
            "description": "오스트리아 투자진흥청",
            "featured": False
        },
        {
            "id": 19,
            "country": "벨기에",
            "organizationName": "Flanders Investment & Trade",
            "city": "브뤼셀",
            "latitude": 50.8503,
            "longitude": 4.3517,
            "address": "Koning Albert II-laan 37, 1030 Brussels",
            "phone": "+32-2-504-87-11",
            "email": "info@fitagency.be",
            "website": "www.flandersinvestmentandtrade.com",
            "description": "플란더스 투자무역청",
            "featured": False
        },
        {
            "id": 20,
            "country": "폴란드",
            "organizationName": "Polish Investment and Trade Agency",
            "city": "바르샤바",
            "latitude": 52.2297,
            "longitude": 21.0122,
            "address": "ul. Bagatela 12, 00-585 Warsaw",
            "phone": "+48-22-334-98-00",
            "email": "info@paiz.gov.pl",
            "website": "www.paiz.gov.pl",
            "description": "폴란드 투자무역청",
            "featured": False
        },
        {
            "id": 21,
            "country": "베트남",
            "organizationName": "VIETRADE",
            "city": "하노이",
            "latitude": 21.0285,
            "longitude": 105.8542,
            "address": "20 Ly Thuong Kiet, Hanoi",
            "phone": "+84-24-3934-7621",
            "email": "vietrade@moit.gov.vn",
            "website": "www.vietrade.gov.vn",
            "description": "베트남 무역진흥청",
            "featured": False
        },
        {
            "id": 22,
            "country": "태국",
            "organizationName": "DITP (Department of International Trade Promotion)",
            "city": "방콕",
            "latitude": 13.7367,
            "longitude": 100.5231,
            "address": "Ratchadaphisek Rd, Bangkok",
            "phone": "+66-2507-7999",
            "email": "ditp@ditp.go.th",
            "website": "www.ditp.go.th",
            "description": "태국 국제무역진흥부",
            "featured": False
        },
        {
            "id": 23,
            "country": "말레이시아",
            "organizationName": "MATRADE",
            "city": "쿠알라룸푸르",
            "latitude": 3.1587,
            "longitude": 101.7090,
            "address": "Jalan Sultan Haji Ahmad Shah, Kuala Lumpur",
            "phone": "+60-3-6207-7077",
            "email": "info@matrade.gov.my",
            "website": "www.matrade.gov.my",
            "description": "말레이시아 대외무역개발공사",
            "featured": False
        },
        {
            "id": 24,
            "country": "인도네시아",
            "organizationName": "BKPM (Indonesia Investment Board)",
            "city": "자카르타",
            "latitude": -6.2294,
            "longitude": 106.8295,
            "address": "Jl. Jenderal Gatot Subroto, Jakarta",
            "phone": "+62-21-5252008",
            "email": "info@bkpm.go.id",
            "website": "www.bkpm.go.id",
            "description": "인도네시아 투자조정청",
            "featured": False
        },
        {
            "id": 25,
            "country": "필리핀",
            "organizationName": "DTI (Department of Trade and Industry)",
            "city": "마닐라",
            "latitude": 14.5547,
            "longitude": 121.0244,
            "address": "361 Sen. Gil J. Puyat Ave, Manila",
            "phone": "+63-2-7791-3100",
            "email": "contactus@dti.gov.ph",
            "website": "www.dti.gov.ph",
            "description": "필리핀 무역산업부",
            "featured": False
        },
        {
            "id": 26,
            "country": "한국",
            "organizationName": "KOTRA (Korea Trade-Investment Promotion Agency)",
            "city": "서울",
            "latitude": 37.5665,
            "longitude": 126.9780,
            "address": "13 Heolleung-ro, Seocho-gu, Seoul",
            "phone": "+82-2-3460-7114",
            "email": "info@kotra.or.kr",
            "website": "www.kotra.or.kr",
            "description": "대한무역투자진흥공사",
            "featured": False
        },
        {
            "id": 27,
            "country": "홍콩",
            "organizationName": "Hong Kong Trade Development Council",
            "city": "홍콩",
            "latitude": 22.3193,
            "longitude": 114.1694,
            "address": "38/F Office Tower, Convention Plaza, Hong Kong",
            "phone": "+852-1830-668",
            "email": "info@hktdc.org",
            "website": "www.hktdc.com",
            "description": "홍콩무역발전국",
            "featured": False
        },
        {
            "id": 28,
            "country": "대만",
            "organizationName": "TAITRA (Taiwan External Trade Development Council)",
            "city": "타이페이",
            "latitude": 25.0330,
            "longitude": 121.5654,
            "address": "5-7 Fl., 333 Keelung Rd., Sec. 1, Taipei",
            "phone": "+886-2-2725-5200",
            "email": "taitra@taitra.org.tw",
            "website": "www.taitra.org.tw",
            "description": "대만대외무역발전협회",
            "featured": False
        },
        {
            "id": 29,
            "country": "몽골",
            "organizationName": "Mongolian National Chamber of Commerce and Industry",
            "city": "울란바토르",
            "latitude": 47.9184,
            "longitude": 106.9177,
            "address": "Sukhbaatar District, Ulaanbaatar",
            "phone": "+976-11-318-692",
            "email": "info@mncci.mn",
            "website": "www.mncci.mn",
            "description": "몽골상공회의소",
            "featured": False
        },
        {
            "id": 30,
            "country": "라오스",
            "organizationName": "Lao National Chamber of Commerce and Industry",
            "city": "비엔티안",
            "latitude": 17.9757,
            "longitude": 102.6331,
            "address": "KM3 Thadeua Road, Vientiane",
            "phone": "+856-21-213-470",
            "email": "info@lncci.la",
            "website": "www.lncci.la",
            "description": "라오스상공회의소",
            "featured": False
        },
        {
            "id": 31,
            "country": "아랍에미리트",
            "organizationName": "Dubai Chamber of Commerce",
            "city": "두바이",
            "latitude": 25.2048,
            "longitude": 55.2708,
            "address": "Dubai Chamber Building, Dubai",
            "phone": "+971-4-228-0000",
            "email": "info@dubaichamber.com",
            "website": "www.dubaichamber.com",
            "description": "두바이 상공회의소",
            "featured": False
        },
        {
            "id": 32,
            "country": "사우디아라비아",
            "organizationName": "Saudi Export Development Authority",
            "city": "리야드",
            "latitude": 24.7136,
            "longitude": 46.6753,
            "address": "King Fahd Road, Riyadh",
            "phone": "+966-11-203-8888",
            "email": "info@sagia.gov.sa",
            "website": "www.sagia.gov.sa",
            "description": "사우디아라비아 수출개발청",
            "featured": False
        },
        {
            "id": 33,
            "country": "이스라엘",
            "organizationName": "Israel Export Institute",
            "city": "텔아비브",
            "latitude": 32.0853,
            "longitude": 34.7818,
            "address": "29 Hamered Street, Tel Aviv",
            "phone": "+972-3-514-2800",
            "email": "info@export.gov.il",
            "website": "www.export.gov.il",
            "description": "이스라엘 수출협회",
            "featured": False
        },
        {
            "id": 34,
            "country": "터키",
            "organizationName": "Turkish Exporters Assembly",
            "city": "이스탄불",
            "latitude": 41.0082,
            "longitude": 28.9784,
            "address": "Ritz Carlton Hotel, Istanbul",
            "phone": "+90-212-454-0000",
            "email": "info@turkexporter.org",
            "website": "www.turkexporter.org",
            "description": "터키 수출업자 총연합회",
            "featured": False
        },
        {
            "id": 35,
            "country": "남아프리카공화국",
            "organizationName": "WESGRO",
            "city": "케이프타운",
            "latitude": -33.9249,
            "longitude": 18.4241,
            "address": "19th Floor, ABSA Centre, Cape Town",
            "phone": "+27-21-487-8600",
            "email": "info@wesgro.co.za",
            "website": "www.wesgro.co.za",
            "description": "남아프리카공화국 서부케이프 무역투자진흥청",
            "featured": False
        },
        {
            "id": 36,
            "country": "이집트",
            "organizationName": "General Authority for Investment and Free Zones",
            "city": "카이로",
            "latitude": 30.0444,
            "longitude": 31.2357,
            "address": "Smart Village, Cairo",
            "phone": "+20-2-2794-9494",
            "email": "info@gafi.gov.eg",
            "website": "www.gafi.gov.eg",
            "description": "이집트 투자자유지역청",
            "featured": False
        },
        {
            "id": 37,
            "country": "나이지리아",
            "organizationName": "Nigerian Export Promotion Council",
            "city": "아부자",
            "latitude": 9.0820,
            "longitude": 8.6753,
            "address": "Plot 424, Aguiyi Ironsi Street, Abuja",
            "phone": "+234-1-279-0000",
            "email": "info@nepc.gov.ng",
            "website": "www.nepc.gov.ng",
            "description": "나이지리아 수출진흥위원회",
            "featured": False
        },
        {
            "id": 38,
            "country": "러시아",
            "organizationName": "Russian Export Center",
            "city": "모스크바",
            "latitude": 55.7558,
            "longitude": 37.6176,
            "address": "Presnenskaya Embankment, Moscow",
            "phone": "+7-495-937-4747",
            "email": "info@exportcenter.ru",
            "website": "www.exportcenter.ru",
            "description": "러시아 수출센터",
            "featured": False
        },
        {
            "id": 39,
            "country": "캐나다",
            "organizationName": "TCS (Trade Commissioner Service)",
            "city": "오타와",
            "latitude": 45.4215,
            "longitude": -75.6972,
            "address": "125 Sussex Drive, Ottawa",
            "phone": "+1-613-996-2000",
            "email": "info@international.gc.ca",
            "website": "www.tradecommissioner.gc.ca",
            "description": "캐나다 무역위원회",
            "featured": False
        },
        {
            "id": 40,
            "country": "멕시코",
            "organizationName": "ProMéxico",
            "city": "멕시코시티",
            "latitude": 19.4326,
            "longitude": -99.1332,
            "address": "Av. Insurgentes Sur 1940, Mexico City",
            "phone": "+52-55-5447-7000",
            "email": "info@promexico.gob.mx",
            "website": "www.promexico.gob.mx",
            "description": "멕시코 투자무역진흥청",
            "featured": False
        },
        {
            "id": 41,
            "country": "브라질",
            "organizationName": "APEX-Brasil",
            "city": "브라질리아",
            "latitude": -15.7942,
            "longitude": -47.8822,
            "address": "Setor Bancário Norte, Brasília",
            "phone": "+55-61-3426-0202",
            "email": "apex@apexbrasil.com.br",
            "website": "www.apexbrasil.com.br",
            "description": "브라질 수출투자진흥청",
            "featured": False
        },
        {
            "id": 42,
            "country": "아르헨티나",
            "organizationName": "Fundación Export.Ar",
            "city": "부에노스아이레스",
            "latitude": -34.6037,
            "longitude": -58.3816,
            "address": "Esmeralda 1302, Buenos Aires",
            "phone": "+54-11-4349-7500",
            "email": "info@exportar.org.ar",
            "website": "www.exportar.org.ar",
            "description": "아르헨티나 수출진흥재단",
            "featured": False
        },
        {
            "id": 43,
            "country": "칠레",
            "organizationName": "ProChile",
            "city": "산티아고",
            "latitude": -33.4489,
            "longitude": -70.6693,
            "address": "Teatinos 180, Santiago",
            "phone": "+56-2-2827-5100",
            "email": "prochile@prochile.cl",
            "website": "www.prochile.cl",
            "description": "칠레 수출진흥청",
            "featured": False
        },
        {
            "id": 44,
            "country": "콜롬비아",
            "organizationName": "ProColombia",
            "city": "보고타",
            "latitude": 4.7110,
            "longitude": -74.0721,
            "address": "Calle 28A # 15-31, Bogotá",
            "phone": "+57-1-560-0100",
            "email": "info@procolombia.co",
            "website": "www.procolombia.co",
            "description": "콜롬비아 수출투자진흥청",
            "featured": False
        },
        {
            "id": 45,
            "country": "페루",
            "organizationName": "PROMPERÚ",
            "city": "리마",
            "latitude": -12.0464,
            "longitude": -77.0428,
            "address": "Av. República de Chile 278, Lima",
            "phone": "+51-1-616-7300",
            "email": "info@promperu.gob.pe",
            "website": "www.promperu.gob.pe",
            "description": "페루 수출관광진흥청",
            "featured": False
        },
        {
            "id": 46,
            "country": "뉴질랜드",
            "organizationName": "New Zealand Trade and Enterprise",
            "city": "오클랜드",
            "latitude": -36.8485,
            "longitude": 174.7633,
            "address": "139 Quay Street, Auckland",
            "phone": "+64-9-915-4000",
            "email": "info@nzte.govt.nz",
            "website": "www.nzte.govt.nz",
            "description": "뉴질랜드 무역기업청",
            "featured": False
        },
        {
            "id": 47,
            "country": "체코",
            "organizationName": "CzechTrade",
            "city": "프라하",
            "latitude": 50.0755,
            "longitude": 14.4378,
            "address": "Dittrichova 21, Prague",
            "phone": "+420-224-907-111",
            "email": "info@czechtrade.cz",
            "website": "www.czechtrade.cz",
            "description": "체코 무역진흥청",
            "featured": False
        },
        {
            "id": 48,
            "country": "헝가리",
            "organizationName": "Hungarian Investment Promotion Agency",
            "city": "부다페스트",
            "latitude": 47.4979,
            "longitude": 19.0402,
            "address": "Andrássy út 12, Budapest",
            "phone": "+36-1-872-8000",
            "email": "info@hipa.hu",
            "website": "www.hipa.hu",
            "description": "헝가리 투자진흥청",
            "featured": False
        },
        {
            "id": 49,
            "country": "슬로바키아",
            "organizationName": "SARIO (Slovak Investment and Trade Development Agency)",
            "city": "브라티슬라바",
            "latitude": 48.1486,
            "longitude": 17.1077,
            "address": "Trnavská cesta 100, Bratislava",
            "phone": "+421-2-2070-0111",
            "email": "info@sario.sk",
            "website": "www.sario.sk",
            "description": "슬로바키아 투자무역개발청",
            "featured": False
        },
        {
            "id": 50,
            "country": "슬로베니아",
            "organizationName": "SPIRIT Slovenia",
            "city": "류블랴나",
            "latitude": 46.0569,
            "longitude": 14.5058,
            "address": "Dunajska cesta 156, Ljubljana",
            "phone": "+386-1-589-1800",
            "email": "info@spirit.si",
            "website": "www.spirit.si",
            "description": "슬로베니아 기업국제화청",
            "featured": False
        },
        {
            "id": 51,
            "country": "크로아티아",
            "organizationName": "Croatian Chamber of Economy",
            "city": "자그레브",
            "latitude": 45.8150,
            "longitude": 15.9819,
            "address": "Rooseveltov trg 2, Zagreb",
            "phone": "+385-1-456-1555",
            "email": "info@hgk.hr",
            "website": "www.hgk.hr",
            "description": "크로아티아 경제상공회의소",
            "featured": False
        },
        {
            "id": 52,
            "country": "세르비아",
            "organizationName": "Serbian Chamber of Commerce",
            "city": "베오그라드",
            "latitude": 44.8125,
            "longitude": 20.4612,
            "address": "Resavska 13-15, Belgrade",
            "phone": "+381-11-2645-555",
            "email": "info@pks.rs",
            "website": "www.pks.rs",
            "description": "세르비아 상공회의소",
            "featured": False
        },
        {
            "id": 53,
            "country": "루마니아",
            "organizationName": "Romanian Chamber of Commerce and Industry",
            "city": "부쿠레슈티",
            "latitude": 44.4268,
            "longitude": 26.1025,
            "address": "Bulevardul Octavian Goga 2, Bucharest",
            "phone": "+40-21-319-0088",
            "email": "info@ccir.ro",
            "website": "www.ccir.ro",
            "description": "루마니아 상공회의소",
            "featured": False
        },
        {
            "id": 54,
            "country": "불가리아",
            "organizationName": "Bulgarian Chamber of Commerce and Industry",
            "city": "소피아",
            "latitude": 42.6977,
            "longitude": 23.3219,
            "address": "Parchevich 42, Sofia",
            "phone": "+359-2-811-7490",
            "email": "info@bcci.bg",
            "website": "www.bcci.bg",
            "description": "불가리아 상공회의소",
            "featured": False
        },
        {
            "id": 55,
            "country": "그리스",
            "organizationName": "Enterprise Greece",
            "city": "아테네",
            "latitude": 37.9838,
            "longitude": 23.7275,
            "address": "Mitropoleos 15, Athens",
            "phone": "+30-210-335-5700",
            "email": "info@enterprisegreece.gov.gr",
            "website": "www.enterprisegreece.gov.gr",
            "description": "그리스 기업청",
            "featured": False
        },
        {
            "id": 56,
            "country": "몰타",
            "organizationName": "Malta Enterprise",
            "city": "피에타",
            "latitude": 35.9375,
            "longitude": 14.3754,
            "address": "Gwardamangia Hill, Pieta",
            "phone": "+356-2542-0000",
            "email": "info@maltaenterprise.com",
            "website": "www.maltaenterprise.com",
            "description": "몰타 기업청",
            "featured": False
        },
        {
            "id": 57,
            "country": "키프로스",
            "organizationName": "Cyprus Investment Promotion Agency",
            "city": "니코시아",
            "latitude": 35.1856,
            "longitude": 33.3823,
            "address": "6, Anastasi Sioukri & Olympou, Nicosia",
            "phone": "+357-22-285-000",
            "email": "info@investcyprus.org.cy",
            "website": "www.investcyprus.org.cy",
            "description": "키프로스 투자진흥청",
            "featured": False
        },
        {
            "id": 58,
            "country": "에스토니아",
            "organizationName": "Enterprise Estonia",
            "city": "탈린",
            "latitude": 59.4369,
            "longitude": 24.7536,
            "address": "Lasnamäe 2, Tallinn",
            "phone": "+372-627-9500",
            "email": "info@eas.ee",
            "website": "www.eas.ee",
            "description": "에스토니아 기업청",
            "featured": False
        },
        {
            "id": 59,
            "country": "라트비아",
            "organizationName": "Investment and Development Agency of Latvia",
            "city": "리가",
            "latitude": 56.9496,
            "longitude": 24.1052,
            "address": "Perses iela 2, Riga",
            "phone": "+371-670-394-00",
            "email": "info@liaa.gov.lv",
            "website": "www.liaa.gov.lv",
            "description": "라트비아 투자개발청",
            "featured": False
        },
        {
            "id": 60,
            "country": "리투아니아",
            "organizationName": "Invest Lithuania",
            "city": "빌뉴스",
            "latitude": 54.6872,
            "longitude": 25.2797,
            "address": "Gedimino pr. 28, Vilnius",
            "phone": "+370-5-219-4140",
            "email": "info@investlithuania.com",
            "website": "www.investlithuania.com",
            "description": "리투아니아 투자청",
            "featured": False
        },
        {
            "id": 61,
            "country": "캄보디아",
            "organizationName": "Council for the Development of Cambodia",
            "city": "프놈펜",
            "latitude": 11.5564,
            "longitude": 104.9282,
            "address": "Government Palace, Phnom Penh",
            "phone": "+855-23-981-154",
            "email": "cdc@cambodiainvestment.gov.kh",
            "website": "www.cambodiainvestment.gov.kh",
            "description": "캄보디아 개발위원회",
            "featured": False
        },
        {
            "id": 62,
            "country": "미얀마",
            "organizationName": "Myanmar Investment Commission",
            "city": "네피도",
            "latitude": 19.7633,
            "longitude": 96.0785,
            "address": "Nay Pyi Taw",
            "phone": "+95-1-667-002",
            "email": "info@dica.gov.mm",
            "website": "www.dica.gov.mm",
            "description": "미얀마 투자위원회",
            "featured": False
        },
        {
            "id": 63,
            "country": "브루나이",
            "organizationName": "Brunei Economic Development Board",
            "city": "반다르스리브가완",
            "latitude": 4.8903,
            "longitude": 114.9422,
            "address": "Unit 2.01, Block A, Bangunan Haji Sidek, Bandar Seri Begawan",
            "phone": "+673-238-2929",
            "email": "info@bedb.com.bn",
            "website": "www.bedb.com.bn",
            "description": "브루나이 경제개발청",
            "featured": False
        },
        {
            "id": 64,
            "country": "파키스탄",
            "organizationName": "Trade Development Authority of Pakistan",
            "city": "카라치",
            "latitude": 24.8607,
            "longitude": 67.0011,
            "address": "3rd Floor, Block A, Finance and Trade Centre, Karachi",
            "phone": "+92-21-992-064-00",
            "email": "info@tdap.gov.pk",
            "website": "www.tdap.gov.pk",
            "description": "파키스탄 무역개발청",
            "featured": False
        },
        {
            "id": 65,
            "country": "방글라데시",
            "organizationName": "Bangladesh Investment Development Authority",
            "city": "다카",
            "latitude": 23.8103,
            "longitude": 90.4125,
            "address": "Plot E-32, Agargaon, Dhaka",
            "phone": "+880-2-550-881-00",
            "email": "info@bida.gov.bd",
            "website": "www.bida.gov.bd",
            "description": "방글라데시 투자개발청",
            "featured": False
        },
        {
            "id": 66,
            "country": "스리랑카",
            "organizationName": "Sri Lanka Export Development Board",
            "city": "콜롬보",
            "latitude": 6.9271,
            "longitude": 79.8612,
            "address": "No. 42, Nawam Mawatha, Colombo",
            "phone": "+94-11-230-0700",
            "email": "info@srilankabusiness.com",
            "website": "www.srilankabusiness.com",
            "description": "스리랑카 수출개발청",
            "featured": False
        },
        {
            "id": 67,
            "country": "네팔",
            "organizationName": "Nepal Trade Integration Strategy",
            "city": "카트만두",
            "latitude": 27.7172,
            "longitude": 85.3240,
            "address": "Singha Durbar, Kathmandu",
            "phone": "+977-1-421-1600",
            "email": "info@ntis.gov.np",
            "website": "www.ntis.gov.np",
            "description": "네팔 무역통합전략",
            "featured": False
        },
        {
            "id": 68,
            "country": "부탄",
            "organizationName": "Bhutan Chamber of Commerce and Industry",
            "city": "팀푸",
            "latitude": 27.4716,
            "longitude": 89.6386,
            "address": "Doebum Lam, Thimphu",
            "phone": "+975-2-323-528",
            "email": "info@bhutanchamber.bt",
            "website": "www.bhutanchamber.bt",
            "description": "부탄 상공회의소",
            "featured": False
        },
        {
            "id": 69,
            "country": "아프가니스탄",
            "organizationName": "Afghanistan Investment Support Agency",
            "city": "카불",
            "latitude": 34.5553,
            "longitude": 69.2075,
            "address": "Kabul",
            "phone": "+93-20-210-1000",
            "email": "info@aisa.org.af",
            "website": "www.aisa.org.af",
            "description": "아프가니스탄 투자지원청",
            "featured": False
        },
        {
            "id": 70,
            "country": "우즈베키스탄",
            "organizationName": "Uzbekistan Investment Committee",
            "city": "타슈켄트",
            "latitude": 41.2995,
            "longitude": 69.2401,
            "address": "Tashkent",
            "phone": "+998-71-238-5400",
            "email": "info@invest.gov.uz",
            "website": "www.invest.gov.uz",
            "description": "우즈베키스탄 투자위원회",
            "featured": False
        },
        {
            "id": 71,
            "country": "카자흐스탄",
            "organizationName": "Kazakhstan Investment Development Fund",
            "city": "아스타나",
            "latitude": 51.1694,
            "longitude": 71.4491,
            "address": "Astana",
            "phone": "+7-717-255-0000",
            "email": "info@invest.gov.kz",
            "website": "www.invest.gov.kz",
            "description": "카자흐스탄 투자개발기금",
            "featured": False
        },
        {
            "id": 72,
            "country": "키르기스스탄",
            "organizationName": "Kyrgyz Investment and Export Promotion Agency",
            "city": "비슈케크",
            "latitude": 42.8746,
            "longitude": 74.5698,
            "address": "Bishkek",
            "phone": "+996-312-620-000",
            "email": "info@kiepa.gov.kg",
            "website": "www.kiepa.gov.kg",
            "description": "키르기스스탄 투자수출진흥청",
            "featured": False
        },
        {
            "id": 73,
            "country": "타지키스탄",
            "organizationName": "Tajikistan Investment and State Property Management Committee",
            "city": "두샨베",
            "latitude": 38.5358,
            "longitude": 68.7791,
            "address": "Dushanbe",
            "phone": "+992-48-701-0000",
            "email": "info@invest.gov.tj",
            "website": "www.invest.gov.tj",
            "description": "타지키스탄 투자국유재산관리위원회",
            "featured": False
        },
        {
            "id": 74,
            "country": "투르크메니스탄",
            "organizationName": "Turkmenistan State Committee for Foreign Investment",
            "city": "아시가바트",
            "latitude": 37.9601,
            "longitude": 58.3261,
            "address": "Ashgabat",
            "phone": "+993-12-940-000",
            "email": "info@invest.gov.tm",
            "website": "www.invest.gov.tm",
            "description": "투르크메니스탄 외국투자국가위원회",
            "featured": False
        },
        {
            "id": 75,
            "country": "아제르바이잔",
            "organizationName": "Azerbaijan Export and Investment Promotion Foundation",
            "city": "바쿠",
            "latitude": 40.4093,
            "longitude": 49.8671,
            "address": "Baku",
            "phone": "+994-12-497-6300",
            "email": "info@azpromo.az",
            "website": "www.azpromo.az",
            "description": "아제르바이잔 수출투자진흥재단",
            "featured": False
        },
        {
            "id": 76,
            "country": "아르메니아",
            "organizationName": "Armenian Development Agency",
            "city": "예레반",
            "latitude": 40.1872,
            "longitude": 44.5152,
            "address": "Yerevan",
            "phone": "+374-10-520-000",
            "email": "info@ada.am",
            "website": "www.ada.am",
            "description": "아르메니아 개발청",
            "featured": False
        },
        {
            "id": 77,
            "country": "조지아",
            "organizationName": "Georgian National Investment Agency",
            "city": "트빌리시",
            "latitude": 41.7151,
            "longitude": 44.8271,
            "address": "Tbilisi",
            "phone": "+995-32-243-0000",
            "email": "info@gnia.ge",
            "website": "www.gnia.ge",
            "description": "조지아 국가투자청",
            "featured": False
        },
        {
            "id": 78,
            "country": "이란",
            "organizationName": "Iran Trade Promotion Organization",
            "city": "테헤란",
            "latitude": 35.6892,
            "longitude": 51.3890,
            "address": "Tehran",
            "phone": "+98-21-667-4000",
            "email": "info@tpo.ir",
            "website": "www.tpo.ir",
            "description": "이란 무역진흥기구",
            "featured": False
        },
        {
            "id": 79,
            "country": "이라크",
            "organizationName": "Iraq Investment and Export Promotion Agency",
            "city": "바그다드",
            "latitude": 33.3152,
            "longitude": 44.3661,
            "address": "Baghdad",
            "phone": "+964-1-717-0000",
            "email": "info@investiraq.gov.iq",
            "website": "www.investiraq.gov.iq",
            "description": "이라크 투자수출진흥청",
            "featured": False
        },
        {
            "id": 80,
            "country": "쿠웨이트",
            "organizationName": "Kuwait Direct Investment Promotion Authority",
            "city": "쿠웨이트시티",
            "latitude": 29.3759,
            "longitude": 47.9774,
            "address": "Kuwait City",
            "phone": "+965-1-888-000",
            "email": "info@kdipa.gov.kw",
            "website": "www.kdipa.gov.kw",
            "description": "쿠웨이트 직접투자진흥청",
            "featured": False
        },
        {
            "id": 81,
            "country": "바레인",
            "organizationName": "Bahrain Economic Development Board",
            "city": "마나마",
            "latitude": 26.2285,
            "longitude": 50.5860,
            "address": "Manama",
            "phone": "+973-17-589-999",
            "email": "info@bedb.com",
            "website": "www.bedb.com",
            "description": "바레인 경제개발청",
            "featured": False
        },
        {
            "id": 82,
            "country": "카타르",
            "organizationName": "Qatar Investment Promotion Agency",
            "city": "도하",
            "latitude": 25.2854,
            "longitude": 51.5310,
            "address": "Doha",
            "phone": "+974-4-499-0000",
            "email": "info@invest.qa",
            "website": "www.invest.qa",
            "description": "카타르 투자진흥청",
            "featured": False
        },
        {
            "id": 83,
            "country": "오만",
            "organizationName": "Oman Investment Authority",
            "city": "무스카트",
            "latitude": 23.5880,
            "longitude": 58.3829,
            "address": "Muscat",
            "phone": "+968-24-649-000",
            "email": "info@oia.gov.om",
            "website": "www.oia.gov.om",
            "description": "오만 투자청",
            "featured": False
        },
        {
            "id": 84,
            "country": "요르단",
            "organizationName": "Jordan Investment Commission",
            "city": "암만",
            "latitude": 31.9539,
            "longitude": 35.9106,
            "address": "Amman",
            "phone": "+962-6-520-0000",
            "email": "info@jic.gov.jo",
            "website": "www.jic.gov.jo",
            "description": "요르단 투자위원회",
            "featured": False
        },
        {
            "id": 85,
            "country": "레바논",
            "organizationName": "Investment Development Authority of Lebanon",
            "city": "베이루트",
            "latitude": 33.8935,
            "longitude": 35.5018,
            "address": "Beirut",
            "phone": "+961-1-585-000",
            "email": "info@idalebanon.com",
            "website": "www.idalebanon.com",
            "description": "레바논 투자개발청",
            "featured": False
        },
        {
            "id": 86,
            "country": "시리아",
            "organizationName": "Syrian Investment Agency",
            "city": "다마스쿠스",
            "latitude": 33.5138,
            "longitude": 36.2765,
            "address": "Damascus",
            "phone": "+963-11-232-0000",
            "email": "info@sia.gov.sy",
            "website": "www.sia.gov.sy",
            "description": "시리아 투자청",
            "featured": False
        },
        {
            "id": 87,
            "country": "예멘",
            "organizationName": "Yemen Investment Authority",
            "city": "사나",
            "latitude": 15.3694,
            "longitude": 44.1910,
            "address": "Sana'a",
            "phone": "+967-1-200-000",
            "email": "info@yia.gov.ye",
            "website": "www.yia.gov.ye",
            "description": "예멘 투자청",
            "featured": False
        },
        {
            "id": 88,
            "country": "케냐",
            "organizationName": "Kenya Investment Authority",
            "city": "나이로비",
            "latitude": -1.2921,
            "longitude": 36.8219,
            "address": "Nairobi",
            "phone": "+254-20-494-0000",
            "email": "info@kenyainvest.org",
            "website": "www.kenyainvest.org",
            "description": "케냐 투자청",
            "featured": False
        },
        {
            "id": 89,
            "country": "모로코",
            "organizationName": "Moroccan Investment Development Agency",
            "city": "라바트",
            "latitude": 34.0209,
            "longitude": -6.8416,
            "address": "Rabat",
            "phone": "+212-5-377-0000",
            "email": "info@mida.gov.ma",
            "website": "www.mida.gov.ma",
            "description": "모로코 투자개발청",
            "featured": False
        },
        {
            "id": 90,
            "country": "튀니지",
            "organizationName": "Tunisia Investment Authority",
            "city": "튀니스",
            "latitude": 36.8065,
            "longitude": 10.1815,
            "address": "Tunis",
            "phone": "+216-71-234-000",
            "email": "info@tia.gov.tn",
            "website": "www.tia.gov.tn",
            "description": "튀니지 투자청",
            "featured": False
        },
        {
            "id": 91,
            "country": "알제리",
            "organizationName": "Algerian Investment Development Agency",
            "city": "알제",
            "latitude": 36.7538,
            "longitude": 3.0588,
            "address": "Algiers",
            "phone": "+213-21-710-000",
            "email": "info@andz.dz",
            "website": "www.andz.dz",
            "description": "알제리 투자개발청",
            "featured": False
        },
        {
            "id": 92,
            "country": "가나",
            "organizationName": "Ghana Investment Promotion Centre",
            "city": "아크라",
            "latitude": 5.5600,
            "longitude": -0.2057,
            "address": "Accra",
            "phone": "+233-30-266-0000",
            "email": "info@gipc.gov.gh",
            "website": "www.gipc.gov.gh",
            "description": "가나 투자진흥센터",
            "featured": False
        },
        {
            "id": 93,
            "country": "우간다",
            "organizationName": "Uganda Investment Authority",
            "city": "캄팔라",
            "latitude": 0.3476,
            "longitude": 32.5825,
            "address": "Kampala",
            "phone": "+256-41-434-0000",
            "email": "info@ugandainvest.go.ug",
            "website": "www.ugandainvest.go.ug",
            "description": "우간다 투자청",
            "featured": False
        },
        {
            "id": 94,
            "country": "탄자니아",
            "organizationName": "Tanzania Investment Centre",
            "city": "다르에스살람",
            "latitude": -6.8230,
            "longitude": 39.2695,
            "address": "Dar es Salaam",
            "phone": "+255-22-286-0000",
            "email": "info@tic.co.tz",
            "website": "www.tic.co.tz",
            "description": "탄자니아 투자센터",
            "featured": False
        },
        {
            "id": 95,
            "country": "에티오피아",
            "organizationName": "Ethiopian Investment Commission",
            "city": "아디스아바바",
            "latitude": 9.0320,
            "longitude": 38.7488,
            "address": "Addis Ababa",
            "phone": "+251-11-551-0000",
            "email": "info@eic.gov.et",
            "website": "www.eic.gov.et",
            "description": "에티오피아 투자위원회",
            "featured": False
        },
        {
            "id": 96,
            "country": "우루과이",
            "organizationName": "Uruguay XXI",
            "city": "몬테비데오",
            "latitude": -34.9011,
            "longitude": -56.1645,
            "address": "Montevideo",
            "phone": "+598-2-916-0000",
            "email": "info@uruguayxxi.gub.uy",
            "website": "www.uruguayxxi.gub.uy",
            "description": "우루과이 투자수출진흥청",
            "featured": False
        },
        {
            "id": 97,
            "country": "파라과이",
            "organizationName": "Red de Inversiones y Exportaciones",
            "city": "아순시온",
            "latitude": -25.2637,
            "longitude": -57.5759,
            "address": "Asunción",
            "phone": "+595-21-450-000",
            "email": "info@rediex.gov.py",
            "website": "www.rediex.gov.py",
            "description": "파라과이 투자수출네트워크",
            "featured": False
        },
        {
            "id": 98,
            "country": "볼리비아",
            "organizationName": "Bolivia Export",
            "city": "라파스",
            "latitude": -16.4897,
            "longitude": -68.1193,
            "address": "La Paz",
            "phone": "+591-2-212-0000",
            "email": "info@boliviaexport.com.bo",
            "website": "www.boliviaexport.com.bo",
            "description": "볼리비아 수출진흥청",
            "featured": False
        },
        {
            "id": 99,
            "country": "에콰도르",
            "organizationName": "Corporación de Promoción de Exportaciones e Inversiones",
            "city": "키토",
            "latitude": -0.1807,
            "longitude": -78.4678,
            "address": "Quito",
            "phone": "+593-2-256-0000",
            "email": "info@corpei.org.ec",
            "website": "www.corpei.org.ec",
            "description": "에콰도르 수출투자진흥공사",
            "featured": False
        },
        {
            "id": 100,
            "country": "베네수엘라",
            "organizationName": "Venezuela Investment Promotion Agency",
            "city": "카라카스",
            "latitude": 10.4806,
            "longitude": -66.9036,
            "address": "Caracas",
            "phone": "+58-212-201-0000",
            "email": "info@venezuelainvest.com",
            "website": "www.venezuelainvest.com",
            "description": "베네수엘라 투자진흥청",
            "featured": False
        },
        {
            "id": 101,
            "country": "아이슬란드",
            "organizationName": "Business Iceland",
            "city": "레이캬비크",
            "latitude": 64.1466,
            "longitude": -21.9426,
            "address": "Reykjavik",
            "phone": "+354-512-4000",
            "email": "info@businessiceland.is",
            "website": "www.businessiceland.is",
            "description": "아이슬란드 비즈니스청",
            "featured": False
        },
        {
            "id": 102,
            "country": "아일랜드",
            "organizationName": "Enterprise Ireland",
            "city": "더블린",
            "latitude": 53.3498,
            "longitude": -6.2603,
            "address": "Dublin",
            "phone": "+353-1-727-2000",
            "email": "info@enterprise-ireland.com",
            "website": "www.enterprise-ireland.com",
            "description": "아일랜드 기업청",
            "featured": False
        },
        {
            "id": 103,
            "country": "포르투갈",
            "organizationName": "AICEP Portugal Global",
            "city": "리스본",
            "latitude": 38.7223,
            "longitude": -9.1393,
            "address": "Lisbon",
            "phone": "+351-21-790-9500",
            "email": "info@portugalglobal.pt",
            "website": "www.portugalglobal.pt",
            "description": "포르투갈 글로벌 무역투자청",
            "featured": False
        },
        {
            "id": 104,
            "country": "룩셈부르크",
            "organizationName": "Luxembourg for Business",
            "city": "룩셈부르크",
            "latitude": 49.6116,
            "longitude": 6.1319,
            "address": "Luxembourg",
            "phone": "+352-42-39-39-1",
            "email": "info@luxembourgforbusiness.lu",
            "website": "www.luxembourgforbusiness.lu",
            "description": "룩셈부르크 비즈니스청",
            "featured": False
        },
        {
            "id": 105,
            "country": "몰도바",
            "organizationName": "Moldova Investment and Export Promotion Organization",
            "city": "키시너우",
            "latitude": 47.0105,
            "longitude": 28.8638,
            "address": "Chisinau",
            "phone": "+373-22-250-000",
            "email": "info@miepo.md",
            "website": "www.miepo.md",
            "description": "몰도바 투자수출진흥기구",
            "featured": False
        },
        {
            "id": 106,
            "country": "알바니아",
            "organizationName": "Albanian Investment Development Agency",
            "city": "티라나",
            "latitude": 41.3275,
            "longitude": 19.8187,
            "address": "Tirana",
            "phone": "+355-4-227-0000",
            "email": "info@aida.gov.al",
            "website": "www.aida.gov.al",
            "description": "알바니아 투자개발청",
            "featured": False
        },
        {
            "id": 107,
            "country": "북마케도니아",
            "organizationName": "Invest North Macedonia",
            "city": "스코페",
            "latitude": 42.0027,
            "longitude": 21.4267,
            "address": "Skopje",
            "phone": "+389-2-310-0000",
            "email": "info@investnorthmacedonia.gov.mk",
            "website": "www.investnorthmacedonia.gov.mk",
            "description": "북마케도니아 투자청",
            "featured": False
        },
        {
            "id": 108,
            "country": "보스니아헤르체고비나",
            "organizationName": "Foreign Investment Promotion Agency",
            "city": "사라예보",
            "latitude": 43.8564,
            "longitude": 18.4131,
            "address": "Sarajevo",
            "phone": "+387-33-278-000",
            "email": "info@fipa.gov.ba",
            "website": "www.fipa.gov.ba",
            "description": "보스니아헤르체고비나 외국투자진흥청",
            "featured": False
        },
        {
            "id": 109,
            "country": "몬테네그로",
            "organizationName": "Montenegro Investment Promotion Agency",
            "city": "포드고리차",
            "latitude": 42.4304,
            "longitude": 19.2594,
            "address": "Podgorica",
            "phone": "+382-20-203-000",
            "email": "info@mipa.me",
            "website": "www.mipa.me",
            "description": "몬테네그로 투자진흥청",
            "featured": False
        },
        {
            "id": 110,
            "country": "코소보",
            "organizationName": "Kosovo Investment and Enterprise Support Agency",
            "city": "프리슈티나",
            "latitude": 42.6629,
            "longitude": 21.1655,
            "address": "Pristina",
            "phone": "+383-38-200-000",
            "email": "info@kiesa.rks-gov.net",
            "website": "www.kiesa.rks-gov.net",
            "description": "코소보 투자기업지원청",
            "featured": False
        },
        {
            "id": 111,
            "country": "몰디브",
            "organizationName": "Maldives Investment and Trade Zone",
            "city": "말레",
            "latitude": 4.1755,
            "longitude": 73.5093,
            "address": "Male",
            "phone": "+960-332-0000",
            "email": "info@mitz.gov.mv",
            "website": "www.mitz.gov.mv",
            "description": "몰디브 투자무역지대",
            "featured": False
        },
        {
            "id": 112,
            "country": "피지",
            "organizationName": "Investment Fiji",
            "city": "수바",
            "latitude": -18.1416,
            "longitude": 178.4419,
            "address": "Suva",
            "phone": "+679-331-5988",
            "email": "info@investmentfiji.org.fj",
            "website": "www.investmentfiji.org.fj",
            "description": "피지 투자청",
            "featured": False
        },
        {
            "id": 113,
            "country": "파푸아뉴기니",
            "organizationName": "Papua New Guinea Investment Promotion Authority",
            "city": "포트모르즈비",
            "latitude": -9.4438,
            "longitude": 147.1803,
            "address": "Port Moresby",
            "phone": "+675-321-0000",
            "email": "info@ipa.gov.pg",
            "website": "www.ipa.gov.pg",
            "description": "파푸아뉴기니 투자진흥청",
            "featured": False
        },
        {
            "id": 114,
            "country": "솔로몬제도",
            "organizationName": "Solomon Islands Investment Corporation",
            "city": "호니아라",
            "latitude": -9.4438,
            "longitude": 159.9498,
            "address": "Honiara",
            "phone": "+677-215-0000",
            "email": "info@siic.gov.sb",
            "website": "www.siic.gov.sb",
            "description": "솔로몬제도 투자공사",
            "featured": False
        },
        {
            "id": 115,
            "country": "바누아투",
            "organizationName": "Vanuatu Investment Promotion Authority",
            "city": "포트빌라",
            "latitude": -17.7333,
            "longitude": 168.3167,
            "address": "Port Vila",
            "phone": "+678-233-0000",
            "email": "info@vipa.gov.vu",
            "website": "www.vipa.gov.vu",
            "description": "바누아투 투자진흥청",
            "featured": False
        },
        {
            "id": 116,
            "country": "사모아",
            "organizationName": "Samoa Trade and Investment Commission",
            "city": "아피아",
            "latitude": -13.8506,
            "longitude": -171.7514,
            "address": "Apia",
            "phone": "+685-204-0000",
            "email": "info@stic.gov.ws",
            "website": "www.stic.gov.ws",
            "description": "사모아 무역투자위원회",
            "featured": False
        },
        {
            "id": 117,
            "country": "통가",
            "organizationName": "Tonga Trade and Investment Commission",
            "city": "누쿠알로파",
            "latitude": -21.1390,
            "longitude": -175.2020,
            "address": "Nuku'alofa",
            "phone": "+676-231-0000",
            "email": "info@ttic.gov.to",
            "website": "www.ttic.gov.to",
            "description": "통가 무역투자위원회",
            "featured": False
        },
        {
            "id": 118,
            "country": "키리바시",
            "organizationName": "Kiribati Investment and Development Authority",
            "city": "타라와",
            "latitude": 1.3382,
            "longitude": 173.0176,
            "address": "Tarawa",
            "phone": "+686-750-0000",
            "email": "info@kida.gov.ki",
            "website": "www.kida.gov.ki",
            "description": "키리바시 투자개발청",
            "featured": False
        },
        {
            "id": 119,
            "country": "투발루",
            "organizationName": "Tuvalu Investment Corporation",
            "city": "푸나푸티",
            "latitude": -8.5217,
            "longitude": 179.1982,
            "address": "Funafuti",
            "phone": "+688-201-0000",
            "email": "info@tic.gov.tv",
            "website": "www.tic.gov.tv",
            "description": "투발루 투자공사",
            "featured": False
        },
        {
            "id": 120,
            "country": "나우루",
            "organizationName": "Nauru Investment Corporation",
            "city": "야렌",
            "latitude": -0.5228,
            "longitude": 166.9315,
            "address": "Yaren",
            "phone": "+674-557-0000",
            "email": "info@nic.gov.nr",
            "website": "www.nic.gov.nr",
            "description": "나우루 투자공사",
            "featured": False
        },
        {
            "id": 121,
            "country": "팔라우",
            "organizationName": "Palau Investment and Development Authority",
            "city": "코로르",
            "latitude": 7.3419,
            "longitude": 134.4791,
            "address": "Koror",
            "phone": "+680-488-0000",
            "email": "info@pida.gov.pw",
            "website": "www.pida.gov.pw",
            "description": "팔라우 투자개발청",
            "featured": False
        },
        {
            "id": 122,
            "country": "마셜제도",
            "organizationName": "Marshall Islands Investment Development Authority",
            "city": "마주로",
            "latitude": 7.0897,
            "longitude": 171.3803,
            "address": "Majuro",
            "phone": "+692-625-0000",
            "email": "info@mida.gov.mh",
            "website": "www.mida.gov.mh",
            "description": "마셜제도 투자개발청",
            "featured": False
        },
        {
            "id": 123,
            "country": "미크로네시아",
            "organizationName": "Micronesia Investment and Development Authority",
            "city": "팔리키르",
            "latitude": 6.9244,
            "longitude": 158.1618,
            "address": "Palikir",
            "phone": "+691-320-0000",
            "email": "info@mida.gov.fm",
            "website": "www.mida.gov.fm",
            "description": "미크로네시아 투자개발청",
            "featured": False
        },
        {
            "id": 124,
            "country": "적도기니",
            "organizationName": "Equatorial Guinea Investment Promotion Agency",
            "city": "말라보",
            "latitude": 3.7523,
            "longitude": 8.7833,
            "address": "Malabo",
            "phone": "+240-333-0000",
            "email": "info@egipa.gov.gq",
            "website": "www.egipa.gov.gq",
            "description": "적도기니 투자진흥청",
            "featured": False
        },
        {
            "id": 125,
            "country": "상투메프린시페",
            "organizationName": "São Tomé and Príncipe Investment and Trade Center",
            "city": "상투메",
            "latitude": 0.1864,
            "longitude": 6.6131,
            "address": "São Tomé",
            "phone": "+239-222-0000",
            "email": "info@citp.gov.st",
            "website": "www.citp.gov.st",
            "description": "상투메프린시페 투자무역센터",
            "featured": False
        },
        {
            "id": 126,
            "country": "카보베르데",
            "organizationName": "Cape Verde Investment Promotion Agency",
            "city": "프라이아",
            "latitude": 14.9317,
            "longitude": -23.5087,
            "address": "Praia",
            "phone": "+238-260-0000",
            "email": "info@cipa.gov.cv",
            "website": "www.cipa.gov.cv",
            "description": "카보베르데 투자진흥청",
            "featured": False
        },
        {
            "id": 127,
            "country": "기니비사우",
            "organizationName": "Guinea-Bissau Investment Promotion Agency",
            "city": "비사우",
            "latitude": 11.8636,
            "longitude": -15.5846,
            "address": "Bissau",
            "phone": "+245-320-0000",
            "email": "info@gipa.gov.gw",
            "website": "www.gipa.gov.gw",
            "description": "기니비사우 투자진흥청",
            "featured": False
        },
        {
            "id": 128,
            "country": "기니",
            "organizationName": "Guinea Investment Promotion Agency",
            "city": "코나크리",
            "latitude": 9.5370,
            "longitude": -13.6785,
            "address": "Conakry",
            "phone": "+224-304-0000",
            "email": "info@gipa.gov.gn",
            "website": "www.gipa.gov.gn",
            "description": "기니 투자진흥청",
            "featured": False
        },
        {
            "id": 129,
            "country": "시에라리온",
            "organizationName": "Sierra Leone Investment and Export Promotion Agency",
            "city": "프리타운",
            "latitude": 8.4606,
            "longitude": -13.2317,
            "address": "Freetown",
            "phone": "+232-222-0000",
            "email": "info@sliepa.gov.sl",
            "website": "www.sliepa.gov.sl",
            "description": "시에라리온 투자수출진흥청",
            "featured": False
        },
        {
            "id": 130,
            "country": "라이베리아",
            "organizationName": "Liberia Investment and Export Promotion Agency",
            "city": "몬로비아",
            "latitude": 6.3004,
            "longitude": -10.7969,
            "address": "Monrovia",
            "phone": "+231-444-0000",
            "email": "info@liepa.gov.lr",
            "website": "www.liepa.gov.lr",
            "description": "라이베리아 투자수출진흥청",
            "featured": False
        },
        {
            "id": 131,
            "country": "코트디부아르",
            "organizationName": "Côte d'Ivoire Investment Promotion Center",
            "city": "아비장",
            "latitude": 5.3600,
            "longitude": -4.0083,
            "address": "Abidjan",
            "phone": "+225-272-0000",
            "email": "info@cipa.ci",
            "website": "www.cipa.ci",
            "description": "코트디부아르 투자진흥센터",
            "featured": False
        },
        {
            "id": 132,
            "country": "부르키나파소",
            "organizationName": "Burkina Faso Investment Promotion Agency",
            "city": "와가두구",
            "latitude": 12.3714,
            "longitude": -1.5197,
            "address": "Ouagadougou",
            "phone": "+226-503-0000",
            "email": "info@api.bf",
            "website": "www.api.bf",
            "description": "부르키나파소 투자진흥청",
            "featured": False
        },
        {
            "id": 133,
            "country": "말리",
            "organizationName": "Mali Investment Promotion Agency",
            "city": "바마코",
            "latitude": 12.6392,
            "longitude": -8.0029,
            "address": "Bamako",
            "phone": "+223-202-0000",
            "email": "info@api-mali.org",
            "website": "www.api-mali.org",
            "description": "말리 투자진흥청",
            "featured": False
        },
        {
            "id": 134,
            "country": "니제르",
            "organizationName": "Niger Investment Promotion Agency",
            "city": "니아메",
            "latitude": 13.5116,
            "longitude": 2.1254,
            "address": "Niamey",
            "phone": "+227-207-0000",
            "email": "info@anpi.ne",
            "website": "www.anpi.ne",
            "description": "니제르 투자진흥청",
            "featured": False
        },
        {
            "id": 135,
            "country": "차드",
            "organizationName": "Chad Investment and Export Promotion Agency",
            "city": "은자메나",
            "latitude": 12.1348,
            "longitude": 15.0557,
            "address": "N'Djamena",
            "phone": "+235-252-0000",
            "email": "info@aiep-tchad.org",
            "website": "www.aiep-tchad.org",
            "description": "차드 투자수출진흥청",
            "featured": False
        },
        {
            "id": 136,
            "country": "수단",
            "organizationName": "Sudan Investment Authority",
            "city": "하르툼",
            "latitude": 15.5007,
            "longitude": 32.5599,
            "address": "Khartoum",
            "phone": "+249-183-0000",
            "email": "info@sia.gov.sd",
            "website": "www.sia.gov.sd",
            "description": "수단 투자청",
            "featured": False
        },
        {
            "id": 137,
            "country": "남수단",
            "organizationName": "South Sudan Investment Authority",
            "city": "주바",
            "latitude": 4.8594,
            "longitude": 31.5713,
            "address": "Juba",
            "phone": "+211-912-0000",
            "email": "info@ssia.gov.ss",
            "website": "www.ssia.gov.ss",
            "description": "남수단 투자청",
            "featured": False
        },
        {
            "id": 138,
            "country": "에리트레아",
            "organizationName": "Eritrea Investment Center",
            "city": "아스마라",
            "latitude": 15.3229,
            "longitude": 38.9251,
            "address": "Asmara",
            "phone": "+291-120-0000",
            "email": "info@eic.gov.er",
            "website": "www.eic.gov.er",
            "description": "에리트레아 투자센터",
            "featured": False
        },
        {
            "id": 139,
            "country": "지부티",
            "organizationName": "Djibouti Investment Promotion Agency",
            "city": "지부티",
            "latitude": 11.8251,
            "longitude": 42.5903,
            "address": "Djibouti",
            "phone": "+253-213-0000",
            "email": "info@dipa.dj",
            "website": "www.dipa.dj",
            "description": "지부티 투자진흥청",
            "featured": False
        },
        {
            "id": 140,
            "country": "소말리아",
            "organizationName": "Somalia Investment Promotion Office",
            "city": "모가디슈",
            "latitude": 2.0469,
            "longitude": 45.3182,
            "address": "Mogadishu",
            "phone": "+252-612-0000",
            "email": "info@sipo.gov.so",
            "website": "www.sipo.gov.so",
            "description": "소말리아 투자진흥청",
            "featured": False
        },
        {
            "id": 141,
            "country": "코모로",
            "organizationName": "Comoros Investment Promotion Agency",
            "city": "모로니",
            "latitude": -11.6455,
            "longitude": 43.3333,
            "address": "Moroni",
            "phone": "+269-773-0000",
            "email": "info@cipa.km",
            "website": "www.cipa.km",
            "description": "코모로 투자진흥청",
            "featured": False
        },
        {
            "id": 142,
            "country": "세이셸",
            "organizationName": "Seychelles Investment Board",
            "city": "빅토리아",
            "latitude": -4.6203,
            "longitude": 55.4513,
            "address": "Victoria",
            "phone": "+248-429-0000",
            "email": "info@sib.gov.sc",
            "website": "www.sib.gov.sc",
            "description": "세이셸 투자위원회",
            "featured": False
        },
        {
            "id": 143,
            "country": "모리셔스",
            "organizationName": "Mauritius Investment Promotion Authority",
            "city": "포트루이스",
            "latitude": -20.1609,
            "longitude": 57.5012,
            "address": "Port Louis",
            "phone": "+230-203-0000",
            "email": "info@edbmauritius.org",
            "website": "www.edbmauritius.org",
            "description": "모리셔스 투자진흥청",
            "featured": False
        },
        {
            "id": 144,
            "country": "마다가스카르",
            "organizationName": "Madagascar Investment Promotion Agency",
            "city": "안타나나리보",
            "latitude": -18.8792,
            "longitude": 47.5079,
            "address": "Antananarivo",
            "phone": "+261-202-0000",
            "email": "info@edbm.mg",
            "website": "www.edbm.mg",
            "description": "마다가스카르 투자진흥청",
            "featured": False
        },
        {
            "id": 145,
            "country": "모잠비크",
            "organizationName": "Mozambique Investment and Export Promotion Agency",
            "city": "마푸투",
            "latitude": -25.9692,
            "longitude": 32.5732,
            "address": "Maputo",
            "phone": "+258-213-0000",
            "email": "info@api.gov.mz",
            "website": "www.api.gov.mz",
            "description": "모잠비크 투자수출진흥청",
            "featured": False
        },
        {
            "id": 146,
            "country": "짐바브웨",
            "organizationName": "Zimbabwe Investment and Development Agency",
            "city": "하라레",
            "latitude": -17.8252,
            "longitude": 31.0335,
            "address": "Harare",
            "phone": "+263-242-0000",
            "email": "info@zida.org.zw",
            "website": "www.zida.org.zw",
            "description": "짐바브웨 투자개발청",
            "featured": False
        },
        {
            "id": 147,
            "country": "잠비아",
            "organizationName": "Zambia Development Agency",
            "city": "루사카",
            "latitude": -15.3875,
            "longitude": 28.3228,
            "address": "Lusaka",
            "phone": "+260-211-0000",
            "email": "info@zda.org.zm",
            "website": "www.zda.org.zm",
            "description": "잠비아 개발청",
            "featured": False
        },
        {
            "id": 148,
            "country": "말라위",
            "organizationName": "Malawi Investment and Trade Centre",
            "city": "릴롱궤",
            "latitude": -13.9626,
            "longitude": 33.7741,
            "address": "Lilongwe",
            "phone": "+265-177-0000",
            "email": "info@mitc.mw",
            "website": "www.mitc.mw",
            "description": "말라위 투자무역센터",
            "featured": False
        },
        {
            "id": 149,
            "country": "보츠와나",
            "organizationName": "Botswana Investment and Trade Centre",
            "city": "가보로네",
            "latitude": -24.6282,
            "longitude": 25.9231,
            "address": "Gaborone",
            "phone": "+267-363-0000",
            "email": "info@bitc.co.bw",
            "website": "www.bitc.co.bw",
            "description": "보츠와나 투자무역센터",
            "featured": False
        },
        {
            "id": 150,
            "country": "나미비아",
            "organizationName": "Namibia Investment Promotion and Development Board",
            "city": "빈트후크",
            "latitude": -22.5609,
            "longitude": 17.0658,
            "address": "Windhoek",
            "phone": "+264-61-0000",
            "email": "info@nipdb.com.na",
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
    
    # 각 기관을 지도에 마커로 표시
    for idx, row in agencies_df.iterrows():
        # featured 기관은 다른 색상으로 표시
        if row['featured']:
            icon_color = 'red'
            icon_size = [25, 25]
        else:
            icon_color = 'blue'
            icon_size = [20, 20]
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"""
            <b>{row['country']}</b><br>
            {row['organizationName']}<br>
            📧 <a href="mailto:{row['email']}">{row['email']}</a><br>
            📞 {row['phone']}<br>
            🌐 <a href="https://{row['website']}" target="_blank">{row['website']}</a>
            """,
            icon=folium.Icon(color=icon_color, icon='info-sign'),
            tooltip=row['country']
        ).add_to(m)
    
    return m

def main():
    # 메인 헤더
    st.markdown('<h1 class="main-header">🌍 Global Trade-Investment Promotion Agency</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">전세계 수출지원기관 연락처 검색 서비스</p>', unsafe_allow_html=True)
    
    # 데이터 로드
    agencies_df = load_agencies_data()
    
    # 통계 정보
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("총 기관 수", f"{len(agencies_df)}개")
    with col2:
        featured_count = len(agencies_df[agencies_df['featured'] == True])
        st.metric("주요 기관", f"{featured_count}개")
    with col3:
        st.metric("국가 수", f"{len(agencies_df)}개")
    
    # 검색 기능
    st.markdown('<div class="search-box">', unsafe_allow_html=True)
    st.subheader("🔍 기관 검색")
    
    search_term = st.text_input(
        "국가명, 기관명, 또는 도시명을 입력하세요:",
        placeholder="예: 미국, 중국, 도쿄..."
    )
    
    if search_term:
        filtered_df = agencies_df[
            agencies_df['country'].str.contains(search_term, case=False, na=False) |
            agencies_df['organizationName'].str.contains(search_term, case=False, na=False) |
            agencies_df['city'].str.contains(search_term, case=False, na=False)
        ]
    else:
        filtered_df = agencies_df
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 지도 표시
    st.subheader("🗺️ 세계 지도")
    world_map = create_world_map(filtered_df)
    folium_static(world_map, width=1200, height=600)
    
    # 검색 결과 표시
    st.subheader(f"📋 검색 결과 ({len(filtered_df)}개)")
    
    if len(filtered_df) > 0:
        for idx, row in filtered_df.iterrows():
            st.markdown(f"""
            <div class="agency-card">
                <h3>{row['country']} - {row['organizationName']}</h3>
                <p><strong>도시:</strong> {row['city']}</p>
                <p><strong>주소:</strong> {row['address']}</p>
                <p><strong>전화:</strong> {row['phone']}</p>
                <p><strong>이메일:</strong> <a href="mailto:{row['email']}">{row['email']}</a></p>
                <p><strong>웹사이트:</strong> <a href="https://{row['website']}" target="_blank">{row['website']}</a></p>
                <p><strong>설명:</strong> {row['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("검색 결과가 없습니다.")
    
    # 전체 기관 목록
    st.subheader("📊 전체 기관 목록")
    
    # 데이터프레임으로 표시
    display_df = filtered_df[['country', 'organizationName', 'city', 'phone', 'email', 'website']].copy()
    st.dataframe(display_df, use_container_width=True)

if __name__ == "__main__":
    main() 