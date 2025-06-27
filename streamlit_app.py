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

# 지역별 분류 함수

def get_region(country):
    asia = ['싱가포르', '말레이시아', '인도네시아', '태국', '베트남', '필리핀', '캄보디아', '미얀마', '브루나이', '라오스', '몽골', '홍콩', '대만', '일본', '중국', '인도', '파키스탄', '방글라데시', '스리랑카', '네팔', '부탄', '아프가니스탄']
    europe = ['독일', '영국', '프랑스', '이탈리아', '스페인', '네덜란드', '스위스', '스웨덴', '노르웨이', '덴마크', '핀란드', '오스트리아', '벨기에', '폴란드', '체코', '헝가리', '슬로바키아', '슬로베니아', '크로아티아', '세르비아', '루마니아', '불가리아', '그리스', '몰타', '키프로스', '에스토니아', '라트비아', '리투아니아']
    northAmerica = ['미국', '캐나다', '멕시코']
    southAmerica = ['브라질', '아르헨티나', '칠레', '콜롬비아', '페루', '우루과이', '파라과이', '볼리비아', '에콰도르', '베네수엘라']
    africa = ['남아프리카공화국', '이집트', '나이지리아', '케냐', '모로코', '튀니지', '알제리', '가나', '우간다', '탄자니아', '에티오피아']
    middleEast = ['아랍에미리트', '사우디아라비아', '이스라엘', '터키', '이란', '이라크', '쿠웨이트', '바레인', '카타르', '오만', '요르단', '레바논', '시리아', '예멘']
    centralAsia = ['러시아', '우즈베키스탄', '카자흐스탄', '키르기스스탄', '타지키스탄', '투르크메니스탄', '아제르바이잔', '아르메니아', '조지아']
    oceania = ['호주', '뉴질랜드']
    if country in asia:
        return 'asia'
    elif country in europe:
        return 'europe'
    elif country in northAmerica:
        return 'northAmerica'
    elif country in southAmerica:
        return 'southAmerica'
    elif country in africa:
        return 'africa'
    elif country in middleEast:
        return 'middleEast'
    elif country in centralAsia:
        return 'centralAsia'
    elif country in oceania:
        return 'oceania'
    return 'global'

def generate_email_template(row):
    region = get_region(row['country'])
    if region == 'asia':
        subject = f"[수출 문의] {row['country']} 시장 진출 관련 상담 요청"
        body = f"""안녕하세요, {row['organizationName']} 담당자님,\n\n저는 한국의 [회사명]에서 근무하고 있는 [이름]입니다.\n\n{row['country']} 시장 진출을 고려하고 있어서, {row['organizationName']}의 지원 서비스에 대해 문의드립니다.\n\n주요 문의사항:\n1. {row['country']} 시장 진출을 위한 지원 프로그램\n2. 현지 파트너사 연결 서비스\n3. 시장 조사 및 컨설팅 서비스\n4. 투자 관련 정보 및 절차\n5. 현지 법규 및 규제 정보\n\n추가로 궁금한 점:\n- 지원 서비스 이용 절차\n- 필요한 서류 및 준비사항\n- 서비스 이용 비용\n- 예상 소요 기간\n- 현지 문화 및 비즈니스 관습\n\n연락 가능한 시간: [연락 가능 시간]\n연락처: [전화번호]\n\n상세한 상담을 위해 회신 부탁드립니다.\n\n감사합니다.\n\n[이름]\n[회사명]\n[직책]\n[연락처]"""
    elif region == 'europe':
        subject = f"[Export Inquiry] Request for Consultation on Entering {row['country']} Market"
        body = f"""Dear {row['organizationName']} Team,\n\nI am [Name] from [Company Name] in South Korea.\n\nWe are considering expanding our business to {row['country']} and would like to inquire about the support services provided by {row['organizationName']}.\n\nMain inquiries:\n1. Market entry support programs for {row['country']}\n2. Local partner connection services\n3. Market research and consulting services\n4. Investment information and procedures\n5. EU regulations and compliance (if applicable)\n\nAdditional questions:\n- Service application procedures\n- Required documents and preparations\n- Service costs\n- Expected processing time\n- Local business culture and practices\n\nAvailable contact time: [Available time]\nContact: [Phone number]\n\nWe look forward to your response for detailed consultation.\n\nBest regards,\n\n[Name]\n[Company Name]\n[Position]\n[Contact]"""
    elif region == 'northAmerica':
        subject = f"[Export Inquiry] Request for Consultation on Entering {row['country']} Market"
        body = f"""Dear {row['organizationName']} Team,\n\nI am [Name] from [Company Name] in South Korea.\n\nWe are interested in expanding our business to {row['country']} and would like to learn more about the support services offered by {row['organizationName']}.\n\nKey inquiries:\n1. Market entry support programs for {row['country']}\n2. Local partner network services\n3. Market research and consulting services\n4. Investment facilitation and procedures\n5. Regulatory compliance information\n\nAdditional questions:\n- Service application process\n- Required documentation\n- Service fees and costs\n- Expected timeline\n- Local market insights\n\nAvailable for contact: [Available time]\nPhone: [Phone number]\n\nWe would appreciate your response for detailed consultation.\n\nThank you.\n\n[Name]\n[Company Name]\n[Position]\n[Contact]"""
    elif region == 'southAmerica':
        subject = f"[Consulta de Exportación] Solicitud de Asesoría para Ingresar al Mercado de {row['country']}"
        body = f"""Estimado equipo de {row['organizationName']},\n\nSoy [Nombre] de [Nombre de la empresa] en Corea del Sur.\n\nEstamos considerando expandir nuestro negocio a {row['country']} y nos gustaría consultar sobre los servicios de apoyo proporcionados por {row['organizationName']}.\n\nConsultas principales:\n1. Programas de apoyo para entrada al mercado de {row['country']}\n2. Servicios de conexión con socios locales\n3. Servicios de investigación de mercado y consultoría\n4. Información y procedimientos de inversión\n5. Información sobre regulaciones locales\n\nPreguntas adicionales:\n- Procedimientos de aplicación de servicios\n- Documentos requeridos y preparaciones\n- Costos de servicios\n- Tiempo de procesamiento esperado\n- Cultura empresarial local\n\nTiempo disponible para contacto: [Tiempo disponible]\nTeléfono: [Número de teléfono]\n\nEsperamos su respuesta para una consulta detallada.\n\nSaludos cordiales,\n\n[Nombre]\n[Nombre de la empresa]\n[Cargo]\n[Contacto]"""
    elif region == 'africa':
        subject = f"[Export Inquiry] Request for Consultation on Entering {row['country']} Market"
        body = f"""Dear {row['organizationName']} Team,\n\nI am [Name] from [Company Name] in South Korea.\n\nWe are exploring business opportunities in {row['country']} and would like to inquire about the support services provided by {row['organizationName']}.\n\nMain inquiries:\n1. Market entry support programs for {row['country']}\n2. Local partner connection services\n3. Market research and consulting services\n4. Investment information and procedures\n5. Local business environment and regulations\n\nAdditional questions:\n- Service application procedures\n- Required documents and preparations\n- Service costs and fees\n- Expected processing time\n- Local business culture and practices\n\nAvailable contact time: [Available time]\nPhone: [Phone number]\n\nWe look forward to your response for detailed consultation.\n\nBest regards,\n\n[Name]\n[Company Name]\n[Position]\n[Contact]"""
    elif region == 'middleEast':
        subject = f"[استفسار تصدير] طلب استشارة حول دخول سوق {row['country']}"
        body = f"""عزيزي فريق {row['organizationName']}،\n\nأنا [الاسم] من [اسم الشركة] في كوريا الجنوبية.\n\nنحن نفكر في التوسع في أعمالنا إلى {row['country']} ونود الاستفسار عن خدمات الدعم المقدمة من {row['organizationName']}.\n\nالاستفسارات الرئيسية:\n1. برامج دعم دخول السوق لـ {row['country']}\n2. خدمات ربط الشركاء المحليين\n3. خدمات أبحاث السوق والاستشارات\n4. معلومات الاستثمار والإجراءات\n5. معلومات اللوائح المحلية\n\nأسئلة إضافية:\n- إجراءات طلب الخدمة\n- المستندات المطلوبة والتحضيرات\n- تكاليف الخدمة\n- الوقت المتوقع للمعالجة\n- ثقافة الأعمال المحلية\n\nالوقت المتاح للاتصال: [الوقت المتاح]\nالهاتف: [رقم الهاتف]\n\nنتطلع إلى ردكم للاستشارة التفصيلية.\n\nمع أطيب التحيات،\n\n[الاسم]\n[اسم الشركة]\n[المنصب]\n[معلومات الاتصال]"""
    elif region == 'centralAsia':
        subject = f"[Экспортный запрос] Запрос консультации по выходу на рынок {row['country']}"
        body = f"""Уважаемая команда {row['organizationName']},\n\nЯ [Имя] из [Название компании] в Южной Корее.\n\nМы рассматриваем возможность расширения нашего бизнеса в {row['country']} и хотели бы узнать о услугах поддержки, предоставляемых {row['organizationName']}.\n\nОсновные вопросы:\n1. Программы поддержки выхода на рынок {row['country']}\n2. Услуги по подключению местных партнеров\n3. Услуги по исследованию рынка и консультированию\n4. Информация об инвестициях и процедурах\n5. Информация о местных правилах\n\nДополнительные вопросы:\n- Процедуры подачи заявки на услуги\n- Необходимые документы и подготовка\n- Стоимость услуг\n- Ожидаемое время обработки\n- Местная деловая культура\n\nДоступное время для связи: [Доступное время]\nТелефон: [Номер телефона]\n\nМы с нетерпением ждем вашего ответа для подробной консультации.\n\nС наилучшими пожеланиями,\n\n[Имя]\n[Название компании]\n[Должность]\n[Контакт]"""
    elif region == 'oceania':
        subject = f"[Export Inquiry] Request for Consultation on Entering {row['country']} Market"
        body = f"""Dear {row['organizationName']} Team,\n\nI am [Name] from [Company Name] in South Korea.\n\nWe are interested in expanding our business to {row['country']} and would like to inquire about the support services provided by {row['organizationName']}.\n\nMain inquiries:\n1. Market entry support programs for {row['country']}\n2. Local partner connection services\n3. Market research and consulting services\n4. Investment information and procedures\n5. Local business environment and regulations\n\nAdditional questions:\n- Service application procedures\n- Required documents and preparations\n- Service costs and fees\n- Expected processing time\n- Local business culture and practices\n\nAvailable contact time: [Available time]\nPhone: [Phone number]\n\nWe look forward to your response for detailed consultation.\n\nBest regards,\n\n[Name]\n[Company Name]\n[Position]\n[Contact]"""
    else:
        subject = f"[Export Inquiry] Request for Consultation"
        body = f"Dear {row['organizationName']} Team, ..."
    return f"mailto:{row['email']}?subject={subject}&body={body}"

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
            "address": "Vientiane",
            "phone": "+856-21-213-470",
            "email": "info@lncci.la",
            "website": "www.lncci.la",
            "description": "라오스상공회의소",
            "featured": False
        },
        {
            "id": 31,
            "country": "캄보디아",
            "organizationName": "Cambodia Chamber of Commerce",
            "city": "프놈펜",
            "latitude": 11.5564,
            "longitude": 104.9282,
            "address": "Phnom Penh",
            "phone": "+855-23-426-148",
            "email": "info@ccc.org.kh",
            "website": "www.ccc.org.kh",
            "description": "캄보디아상공회의소",
            "featured": False
        },
        {
            "id": 32,
            "country": "미얀마",
            "organizationName": "Myanmar Investment Commission",
            "city": "양곤",
            "latitude": 16.8661,
            "longitude": 96.1951,
            "address": "Yangon",
            "phone": "+95-1-657-000",
            "email": "info@dica.gov.mm",
            "website": "www.dica.gov.mm",
            "description": "미얀마투자위원회",
            "featured": False
        },
        {
            "id": 33,
            "country": "브루나이",
            "organizationName": "Brunei Economic Development Board",
            "city": "반다르스리브가완",
            "latitude": 4.8903,
            "longitude": 114.9422,
            "address": "Bandar Seri Begawan",
            "phone": "+673-223-0000",
            "email": "info@bedb.com.bn",
            "website": "www.bedb.com.bn",
            "description": "브루나이경제개발청",
            "featured": False
        },
        {
            "id": 34,
            "country": "파키스탄",
            "organizationName": "Pakistan Board of Investment",
            "city": "이슬라마바드",
            "latitude": 33.7294,
            "longitude": 73.0931,
            "address": "Islamabad",
            "phone": "+92-51-920-0000",
            "email": "info@boi.gov.pk",
            "website": "www.boi.gov.pk",
            "description": "파키스탄투자청",
            "featured": False
        },
        {
            "id": 35,
            "country": "방글라데시",
            "organizationName": "Bangladesh Investment Development Authority",
            "city": "다카",
            "latitude": 23.8103,
            "longitude": 90.4125,
            "address": "Dhaka",
            "phone": "+880-2-550-0000",
            "email": "info@bida.gov.bd",
            "website": "www.bida.gov.bd",
            "description": "방글라데시투자개발청",
            "featured": False
        },
        {
            "id": 36,
            "country": "스리랑카",
            "organizationName": "Sri Lanka Board of Investment",
            "city": "콜롬보",
            "latitude": 6.9271,
            "longitude": 79.8612,
            "address": "Colombo",
            "phone": "+94-11-242-0000",
            "email": "info@boi.lk",
            "website": "www.boi.lk",
            "description": "스리랑카투자청",
            "featured": False
        },
        {
            "id": 37,
            "country": "네팔",
            "organizationName": "Nepal Investment Board",
            "city": "카트만두",
            "latitude": 27.7172,
            "longitude": 85.3240,
            "address": "Kathmandu",
            "phone": "+977-1-422-0000",
            "email": "info@nib.gov.np",
            "website": "www.nib.gov.np",
            "description": "네팔투자청",
            "featured": False
        },
        {
            "id": 38,
            "country": "부탄",
            "organizationName": "Bhutan Chamber of Commerce and Industry",
            "city": "팀푸",
            "latitude": 27.4716,
            "longitude": 89.6386,
            "address": "Thimphu",
            "phone": "+975-2-322-000",
            "email": "info@bcci.org.bt",
            "website": "www.bcci.org.bt",
            "description": "부탄상공회의소",
            "featured": False
        },
        {
            "id": 39,
            "country": "아프가니스탄",
            "organizationName": "Afghanistan Investment Support Agency",
            "city": "카불",
            "latitude": 34.5553,
            "longitude": 69.2075,
            "address": "Kabul",
            "phone": "+93-20-210-0000",
            "email": "info@aisa.org.af",
            "website": "www.aisa.org.af",
            "description": "아프가니스탄투자지원청",
            "featured": False
        },
        {
            "id": 40,
            "country": "캐나다",
            "organizationName": "Global Affairs Canada",
            "city": "오타와",
            "latitude": 45.4215,
            "longitude": -75.6972,
            "address": "Ottawa",
            "phone": "+1-613-944-4000",
            "email": "info@international.gc.ca",
            "website": "www.international.gc.ca",
            "description": "캐나다 글로벌정책부",
            "featured": False
        },
        {
            "id": 41,
            "country": "멕시코",
            "organizationName": "ProMéxico",
            "city": "멕시코시티",
            "latitude": 19.4326,
            "longitude": -99.1332,
            "address": "Mexico City",
            "phone": "+52-55-5447-7000",
            "email": "info@promexico.gob.mx",
            "website": "www.promexico.gob.mx",
            "description": "멕시코 무역투자진흥청",
            "featured": False
        },
        {
            "id": 42,
            "country": "브라질",
            "organizationName": "Apex-Brasil",
            "city": "브라질리아",
            "latitude": -15.7942,
            "longitude": -47.8822,
            "address": "Brasília",
            "phone": "+55-61-3426-0000",
            "email": "info@apexbrasil.com.br",
            "website": "www.apexbrasil.com.br",
            "description": "브라질 수출투자진흥청",
            "featured": False
        },
        {
            "id": 43,
            "country": "아르헨티나",
            "organizationName": "Fundación Export.Ar",
            "city": "부에노스아이레스",
            "latitude": -34.6118,
            "longitude": -58.3960,
            "address": "Buenos Aires",
            "phone": "+54-11-4349-0000",
            "email": "info@exportar.org.ar",
            "website": "www.exportar.org.ar",
            "description": "아르헨티나 수출진흥재단",
            "featured": False
        },
        {
            "id": 44,
            "country": "칠레",
            "organizationName": "ProChile",
            "city": "산티아고",
            "latitude": -33.4489,
            "longitude": -70.6693,
            "address": "Santiago",
            "phone": "+56-2-2827-0000",
            "email": "info@prochile.gob.cl",
            "website": "www.prochile.gob.cl",
            "description": "칠레 수출진흥청",
            "featured": False
        },
        {
            "id": 45,
            "country": "콜롬비아",
            "organizationName": "ProColombia",
            "city": "보고타",
            "latitude": 4.7110,
            "longitude": -74.0721,
            "address": "Bogotá",
            "phone": "+57-1-560-0000",
            "email": "info@procolombia.co",
            "website": "www.procolombia.co",
            "description": "콜롬비아 수출투자진흥청",
            "featured": False
        },
        {
            "id": 46,
            "country": "페루",
            "organizationName": "PromPerú",
            "city": "리마",
            "latitude": -12.0464,
            "longitude": -77.0428,
            "address": "Lima",
            "phone": "+51-1-616-0000",
            "email": "info@promperu.gob.pe",
            "website": "www.promperu.gob.pe",
            "description": "페루 수출투자진흥청",
            "featured": False
        },
        {
            "id": 47,
            "country": "남아프리카공화국",
            "organizationName": "Trade and Investment South Africa",
            "city": "프리토리아",
            "latitude": -25.7479,
            "longitude": 28.2293,
            "address": "Pretoria",
            "phone": "+27-12-394-0000",
            "email": "info@tisa.org.za",
            "website": "www.tisa.org.za",
            "description": "남아공 무역투자청",
            "featured": False
        },
        {
            "id": 48,
            "country": "이집트",
            "organizationName": "General Authority for Investment and Free Zones",
            "city": "카이로",
            "latitude": 30.0444,
            "longitude": 31.2357,
            "address": "Cairo",
            "phone": "+20-2-279-0000",
            "email": "info@gafinet.org",
            "website": "www.gafinet.org",
            "description": "이집트 투자자유무역구청",
            "featured": False
        },
        {
            "id": 49,
            "country": "나이지리아",
            "organizationName": "Nigerian Investment Promotion Commission",
            "city": "아부자",
            "latitude": 9.0820,
            "longitude": 8.6753,
            "address": "Abuja",
            "phone": "+234-9-461-0000",
            "email": "info@nipc.gov.ng",
            "website": "www.nipc.gov.ng",
            "description": "나이지리아 투자진흥위원회",
            "featured": False
        },
        {
            "id": 50,
            "country": "아랍에미리트",
            "organizationName": "Dubai Investment Development Agency",
            "city": "두바이",
            "latitude": 25.2048,
            "longitude": 55.2708,
            "address": "Dubai",
            "phone": "+971-4-330-0000",
            "email": "info@dubaidia.gov.ae",
            "website": "www.dubaidia.gov.ae",
            "description": "두바이 투자개발청",
            "featured": False
        },
        {
            "id": 51,
            "country": "사우디아라비아",
            "organizationName": "Saudi Arabian General Investment Authority",
            "city": "리야드",
            "latitude": 24.7136,
            "longitude": 46.6753,
            "address": "Riyadh",
            "phone": "+966-11-520-0000",
            "email": "info@sagia.gov.sa",
            "website": "www.sagia.gov.sa",
            "description": "사우디아라비아 총투자청",
            "featured": False
        },
        {
            "id": 52,
            "country": "이스라엘",
            "organizationName": "Israel Export Institute",
            "city": "텔아비브",
            "latitude": 32.0853,
            "longitude": 34.7818,
            "address": "Tel Aviv",
            "phone": "+972-3-514-0000",
            "email": "info@export.gov.il",
            "website": "www.export.gov.il",
            "description": "이스라엘 수출협회",
            "featured": False
        },
        {
            "id": 53,
            "country": "터키",
            "organizationName": "Investment Support and Promotion Agency of Turkey",
            "city": "앙카라",
            "latitude": 39.9334,
            "longitude": 32.8597,
            "address": "Ankara",
            "phone": "+90-312-413-0000",
            "email": "info@invest.gov.tr",
            "website": "www.invest.gov.tr",
            "description": "터키 투자지원진흥청",
            "featured": False
        },
        {
            "id": 54,
            "country": "이란",
            "organizationName": "Organization for Investment, Economic and Technical Assistance of Iran",
            "city": "테헤란",
            "latitude": 35.6892,
            "longitude": 51.3890,
            "address": "Tehran",
            "phone": "+98-21-667-0000",
            "email": "info@oiea.ir",
            "website": "www.oiea.ir",
            "description": "이란 투자경제기술지원청",
            "featured": False
        },
        {
            "id": 55,
            "country": "이라크",
            "organizationName": "National Investment Commission",
            "city": "바그다드",
            "latitude": 33.3152,
            "longitude": 44.3661,
            "address": "Baghdad",
            "phone": "+964-1-537-0000",
            "email": "info@nic.gov.iq",
            "website": "www.nic.gov.iq",
            "description": "이라크 국가투자위원회",
            "featured": False
        },
        {
            "id": 56,
            "country": "쿠웨이트",
            "organizationName": "Kuwait Direct Investment Promotion Authority",
            "city": "쿠웨이트시티",
            "latitude": 29.3759,
            "longitude": 47.9774,
            "address": "Kuwait City",
            "phone": "+965-1-800-0000",
            "email": "info@kdipa.gov.kw",
            "website": "www.kdipa.gov.kw",
            "description": "쿠웨이트 직접투자진흥청",
            "featured": False
        },
        {
            "id": 57,
            "country": "바레인",
            "organizationName": "Bahrain Economic Development Board",
            "city": "마나마",
            "latitude": 26.2285,
            "longitude": 50.5860,
            "address": "Manama",
            "phone": "+973-17-589-000",
            "email": "info@bedb.com",
            "website": "www.bedb.com",
            "description": "바레인 경제개발청",
            "featured": False
        },
        {
            "id": 58,
            "country": "카타르",
            "organizationName": "Qatar Investment Authority",
            "city": "도하",
            "latitude": 25.2854,
            "longitude": 51.5310,
            "address": "Doha",
            "phone": "+974-4-499-0000",
            "email": "info@qia.qa",
            "website": "www.qia.qa",
            "description": "카타르 투자청",
            "featured": False
        },
        {
            "id": 59,
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
            "id": 60,
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
            "id": 61,
            "country": "레바논",
            "organizationName": "Investment Development Authority of Lebanon",
            "city": "베이루트",
            "latitude": 33.8935,
            "longitude": 35.5018,
            "address": "Beirut",
            "phone": "+961-1-335-000",
            "email": "info@idalebanon.com",
            "website": "www.idalebanon.com",
            "description": "레바논 투자개발청",
            "featured": False
        },
        {
            "id": 62,
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
            "id": 63,
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
            "id": 64,
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
            "id": 65,
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
            "id": 66,
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
            "id": 67,
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
            "id": 68,
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
            "id": 69,
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
            "id": 70,
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
            "id": 71,
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
            "id": 72,
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
            "id": 73,
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
            "id": 74,
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
            "id": 75,
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
            "id": 76,
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
            "id": 77,
            "country": "러시아",
            "organizationName": "Russian Export Center",
            "city": "모스크바",
            "latitude": 55.7558,
            "longitude": 37.6176,
            "address": "Moscow",
            "phone": "+7-495-937-0000",
            "email": "info@exportcenter.ru",
            "website": "www.exportcenter.ru",
            "description": "러시아 수출센터",
            "featured": False
        },
        {
            "id": 78,
            "country": "우즈베키스탄",
            "organizationName": "Uzbekistan Investment Committee",
            "city": "타슈켄트",
            "latitude": 41.2995,
            "longitude": 69.2401,
            "address": "Tashkent",
            "phone": "+998-71-200-0000",
            "email": "info@invest.gov.uz",
            "website": "www.invest.gov.uz",
            "description": "우즈베키스탄 투자위원회",
            "featured": False
        },
        {
            "id": 79,
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
            "id": 80,
            "country": "키르기스스탄",
            "organizationName": "Kyrgyz Investment and Export Agency",
            "city": "비슈케크",
            "latitude": 42.8746,
            "longitude": 74.5698,
            "address": "Bishkek",
            "phone": "+996-312-610-000",
            "email": "info@invest.gov.kg",
            "website": "www.invest.gov.kg",
            "description": "키르기스투자수출청",
            "featured": False
        },
        {
            "id": 81,
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
            "id": 82,
            "country": "투르크메니스탄",
            "organizationName": "Turkmenistan Investment Agency",
            "city": "아시가바트",
            "latitude": 37.9601,
            "longitude": 58.3261,
            "address": "Ashgabat",
            "phone": "+993-12-440-000",
            "email": "info@invest.gov.tm",
            "website": "www.invest.gov.tm",
            "description": "투르크메니스탄 투자청",
            "featured": False
        },
        {
            "id": 83,
            "country": "아제르바이잔",
            "organizationName": "Azerbaijan Investment and Export Promotion Foundation",
            "city": "바쿠",
            "latitude": 40.3777,
            "longitude": 49.8920,
            "address": "Baku",
            "phone": "+994-12-598-0000",
            "email": "info@azpromo.az",
            "website": "www.azpromo.az",
            "description": "아제르바이잔 투자수출진흥재단",
            "featured": False
        },
        {
            "id": 84,
            "country": "아르메니아",
            "organizationName": "Armenia Development Foundation",
            "city": "예레반",
            "latitude": 40.1872,
            "longitude": 44.5152,
            "address": "Yerevan",
            "phone": "+374-10-520-000",
            "email": "info@adf.am",
            "website": "www.adf.am",
            "description": "아르메니아 개발재단",
            "featured": False
        },
        {
            "id": 85,
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
            "id": 86,
            "country": "체코",
            "organizationName": "CzechInvest",
            "city": "프라하",
            "latitude": 50.0755,
            "longitude": 14.4378,
            "address": "Prague",
            "phone": "+420-296-342-000",
            "email": "info@czechinvest.org",
            "website": "www.czechinvest.org",
            "description": "체코 투자진흥청",
            "featured": False
        },
        {
            "id": 87,
            "country": "헝가리",
            "organizationName": "Hungarian Investment Promotion Agency",
            "city": "부다페스트",
            "latitude": 47.4979,
            "longitude": 19.0402,
            "address": "Budapest",
            "phone": "+36-1-872-0000",
            "email": "info@hipa.hu",
            "website": "www.hipa.hu",
            "description": "헝가리 투자진흥청",
            "featured": False
        },
        {
            "id": 88,
            "country": "슬로바키아",
            "organizationName": "Slovak Investment and Trade Development Agency",
            "city": "브라티슬라바",
            "latitude": 48.1486,
            "longitude": 17.1077,
            "address": "Bratislava",
            "phone": "+421-2-583-00000",
            "email": "info@sario.sk",
            "website": "www.sario.sk",
            "description": "슬로바키아 투자무역개발청",
            "featured": False
        },
        {
            "id": 89,
            "country": "슬로베니아",
            "organizationName": "Slovenian Public Agency for Entrepreneurship and Foreign Investments",
            "city": "류블랴나",
            "latitude": 46.0569,
            "longitude": 14.5058,
            "address": "Ljubljana",
            "phone": "+386-1-589-0000",
            "email": "info@spiritslovenia.si",
            "website": "www.spiritslovenia.si",
            "description": "슬로베니아 기업가정신해외투자공공청",
            "featured": False
        },
        {
            "id": 90,
            "country": "크로아티아",
            "organizationName": "Croatian Agency for SMEs, Innovations and Investments",
            "city": "자그레브",
            "latitude": 45.8150,
            "longitude": 15.9819,
            "address": "Zagreb",
            "phone": "+385-1-640-0000",
            "email": "info@hamag.hr",
            "website": "www.hamag.hr",
            "description": "크로아티아 중소기업혁신투자청",
            "featured": False
        },
        {
            "id": 91,
            "country": "세르비아",
            "organizationName": "Serbia Investment and Export Promotion Agency",
            "city": "베오그라드",
            "latitude": 44.7866,
            "longitude": 20.4489,
            "address": "Belgrade",
            "phone": "+381-11-339-0000",
            "email": "info@sierpa.gov.rs",
            "website": "www.sierpa.gov.rs",
            "description": "세르비아 투자수출진흥청",
            "featured": False
        },
        {
            "id": 92,
            "country": "루마니아",
            "organizationName": "Romanian Agency for Foreign Investments",
            "city": "부쿠레슈티",
            "latitude": 44.4268,
            "longitude": 26.1025,
            "address": "Bucharest",
            "phone": "+40-21-207-0000",
            "email": "info@arisinvest.ro",
            "website": "www.arisinvest.ro",
            "description": "루마니아 해외투자청",
            "featured": False
        },
        {
            "id": 93,
            "country": "불가리아",
            "organizationName": "Bulgarian Investment Agency",
            "city": "소피아",
            "latitude": 42.6977,
            "longitude": 23.3219,
            "address": "Sofia",
            "phone": "+359-2-985-0000",
            "email": "info@investbg.government.bg",
            "website": "www.investbg.government.bg",
            "description": "불가리아 투자청",
            "featured": False
        },
        {
            "id": 94,
            "country": "그리스",
            "organizationName": "Enterprise Greece",
            "city": "아테네",
            "latitude": 37.9838,
            "longitude": 23.7275,
            "address": "Athens",
            "phone": "+30-210-335-0000",
            "email": "info@enterprisegreece.gov.gr",
            "website": "www.enterprisegreece.gov.gr",
            "description": "그리스 기업청",
            "featured": False
        },
        {
            "id": 95,
            "country": "몰타",
            "organizationName": "Malta Enterprise",
            "city": "발레타",
            "latitude": 35.8989,
            "longitude": 14.5146,
            "address": "Valletta",
            "phone": "+356-2542-0000",
            "email": "info@maltaenterprise.com",
            "website": "www.maltaenterprise.com",
            "description": "몰타 기업청",
            "featured": False
        },
        {
            "id": 96,
            "country": "키프로스",
            "organizationName": "Cyprus Investment Promotion Agency",
            "city": "니코시아",
            "latitude": 35.1856,
            "longitude": 33.3823,
            "address": "Nicosia",
            "phone": "+357-22-285-000",
            "email": "info@cipa.org.cy",
            "website": "www.cipa.org.cy",
            "description": "키프로스 투자진흥청",
            "featured": False
        },
        {
            "id": 97,
            "country": "에스토니아",
            "organizationName": "Enterprise Estonia",
            "city": "탈린",
            "latitude": 59.4370,
            "longitude": 24.7536,
            "address": "Tallinn",
            "phone": "+372-627-0000",
            "email": "info@eas.ee",
            "website": "www.eas.ee",
            "description": "에스토니아 기업청",
            "featured": False
        },
        {
            "id": 98,
            "country": "라트비아",
            "organizationName": "Investment and Development Agency of Latvia",
            "city": "리가",
            "latitude": 56.9496,
            "longitude": 24.1052,
            "address": "Riga",
            "phone": "+371-670-00000",
            "email": "info@liaa.gov.lv",
            "website": "www.liaa.gov.lv",
            "description": "라트비아 투자개발청",
            "featured": False
        },
        {
            "id": 99,
            "country": "리투아니아",
            "organizationName": "Invest Lithuania",
            "city": "빌뉴스",
            "latitude": 54.6872,
            "longitude": 25.2797,
            "address": "Vilnius",
            "phone": "+370-5-250-0000",
            "email": "info@investlithuania.com",
            "website": "www.investlithuania.com",
            "description": "리투아니아 투자청",
            "featured": False
        },
        {
            "id": 100,
            "country": "뉴질랜드",
            "organizationName": "New Zealand Trade and Enterprise",
            "city": "오클랜드",
            "latitude": -36.8485,
            "longitude": 174.7633,
            "address": "Auckland",
            "phone": "+64-9-915-4000",
            "email": "info@nzte.govt.nz",
            "website": "www.nzte.govt.nz",
            "description": "뉴질랜드 무역기업청",
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
                <p><strong>Email:</strong> <a href="{generate_email_template(row)}"><strong>Email:</strong> {row['email']} (자동 템플릿)</a></p>
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
                <p><strong>Phone:</strong> {row['phone']} | <strong>Email:</strong> <a href="{generate_email_template(row)}"><strong>Email:</strong> {row['email']} (자동 템플릿)</a></p>
                <p><strong>Website:</strong> <a href="https://{row['website']}" target="_blank">{row['website']}</a></p>
                <p><strong>Description:</strong> {row['description']}</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 