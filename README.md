# Global Trade Support & KOTRA Global Trade Network Platform 🌍

전세계 수출지원기관 연락처를 지도 기반으로 검색할 수 있는 SaaS 플랫폼입니다.

## 🚀 주요 기능
- **지도 기반 검색**: 세계지도에서 직관적으로 수출지원기관 위치 확인
- **국가별/기관별/도시별 검색**: 국가명, 기관명, 도시명으로 빠른 검색
- **상세 정보 제공**: 이메일, 전화번호, 웹사이트, 주소 등 완전한 연락처 정보
- **원클릭 연락**: 이메일 작성, 전화 걸기, 웹사이트 방문 등 바로 실행
- **클립보드 복사**: 연락처 정보 원클릭 복사
- **반응형 디자인**: 데스크톱과 모바일에서 모두 사용 가능
- **ASEAN 10개국 인터랙티브 지도** 및 **전세계 151개국 데이터베이스**
- **이메일 템플릿 자동 생성** (ASEAN 국가 전용)

## 🌏 지원 국가 및 기관
- ASEAN 10개국: 싱가포르, 말레이시아, 인도네시아, 태국, 베트남, 필리핀, 라오스, 캄보디아, 미얀마, 브루나이
- 동아시아: 일본, 중국, 한국 등
- 유럽: 독일, 영국, 프랑스 등
- 북미: 미국, 캐나다 등
- 기타: UAE, 브라질, 남아공, 호주, 인도 등
- 총 151개국 지원

## 🛠 기술 스택
- **Frontend**: React 18 + TypeScript
- **지도**: Mapbox GL JS + react-map-gl, 또는 Folium (Streamlit 버전)
- **스타일링**: Tailwind CSS, CSS3, Flexbox, Grid
- **아이콘**: Lucide React
- **빌드 도구**: Create React App
- **백엔드/데이터**: (옵션) Supabase, PostgreSQL, Streamlit

## 📦 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/rachael2222/Kotra-global.git
cd kotra-global
```

### 2. 의존성 설치
```bash
npm install
```

### 3. Mapbox 토큰 설정 (React 지도 버전)
1. [Mapbox](https://www.mapbox.com)에서 무료 계정 생성
2. Access Token 발급
3. 프로젝트 루트에 `.env` 파일 생성:
```
REACT_APP_MAPBOX_TOKEN=your_mapbox_token_here
```

### 4. 개발 서버 실행
```bash
npm start
```
브라우저에서 [http://localhost:3000](http://localhost:3000)으로 접속하세요.

### 5. Streamlit 버전 실행 (streamlit_app.py)
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🎯 사용 방법
1. **검색하기**: 상단 검색바에 국가명, 기관명, 도시명 입력
2. **지도에서 찾기**: 지도 마커 클릭
3. **정보 확인**: 팝업 또는 사이드바에서 상세 정보 확인
4. **연락하기**: 이메일, 전화, 웹사이트 버튼으로 바로 연락
5. **이메일 템플릿**: ASEAN 국가 카드에서 "수출문의 이메일 작성" 버튼 클릭

## 🚀 배포
- Vercel, Netlify, Streamlit Cloud 등 다양한 플랫폼 지원
- Streamlit Cloud 배포 시 `streamlit_app.py`와 `requirements.txt` 필요

## 🔮 향후 계획
- 더 많은 국가 및 기관 추가
- 다국어 지원 (영어, 중국어, 일본어 등)
- 기관별 상담 예약 기능
- 무역 관련 뉴스 및 공지사항 연동
- PDF 리포트 다운로드 기능
- 즐겨찾기 기능
- 사용자 계정 및 히스토리 관리

## �� 라이선스
MIT License
