# Global Trade-Investment Promotion Agency - Streamlit 배포 가이드

## 🌍 프로젝트 개요
이 프로젝트는 KOTRA 글로벌 무역투자진흥원의 전 세계 기관 정보를 제공하는 Streamlit 웹 애플리케이션입니다.

## 📋 주요 기능
- 🌍 **세계 지도**: Folium을 사용한 인터랙티브 월드맵
- 🔍 **검색 및 필터**: 국가별, 서비스별, 키워드 검색
- 📊 **통계 대시보드**: 기관 분포 및 통계 정보
- 📞 **연락처 정보**: 각 기관의 상세 연락처 정보

## 🚀 배포 방법

### 1. Streamlit Cloud 배포 (권장)

1. **GitHub에 코드 업로드**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/kotra-global-streamlit.git
   git push -u origin main
   ```

2. **Streamlit Cloud에서 배포**
   - [share.streamlit.io](https://share.streamlit.io) 접속
   - GitHub 계정으로 로그인
   - "New app" 클릭
   - Repository 선택: `yourusername/kotra-global-streamlit`
   - Main file path: `streamlit_app.py`
   - "Deploy" 클릭

### 2. Heroku 배포

1. **Procfile 생성**
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Heroku CLI로 배포**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### 3. Docker 배포

1. **Dockerfile 생성**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   EXPOSE 8501
   
   CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Docker 실행**
   ```bash
   docker build -t kotra-global .
   docker run -p 8501:8501 kotra-global
   ```

## 📁 파일 구조
```
├── streamlit_app.py          # 메인 애플리케이션
├── requirements.txt          # Python 의존성
├── .streamlit/
│   └── config.toml          # Streamlit 설정
├── DEPLOYMENT.md            # 배포 가이드
└── README.md               # 프로젝트 설명
```

## 🔧 로컬 개발 환경 설정

1. **가상환경 생성**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **앱 실행**
   ```bash
   streamlit run streamlit_app.py
   ```

## 🌐 웹사이트 탭 연결

`sodapop22.dothome.co.kr`에 탭을 추가하려면:

1. **HTML 코드 생성**
   ```html
   <div class="tab">
     <a href="https://your-streamlit-app-url.streamlit.app" target="_blank">
       <div class="tab-content">
         <h3>Global Trade-Investment Promotion Agency</h3>
         <p>세계 무역투자진흥원 정보 플랫폼</p>
       </div>
     </a>
   </div>
   ```

2. **CSS 스타일링**
   ```css
   .tab {
     background: linear-gradient(135deg, #1f77b4, #2c3e50);
     border-radius: 10px;
     padding: 20px;
     margin: 10px;
     transition: transform 0.3s ease;
   }
   
   .tab:hover {
     transform: translateY(-5px);
     box-shadow: 0 10px 20px rgba(0,0,0,0.2);
   }
   
   .tab a {
     text-decoration: none;
     color: white;
   }
   
   .tab-content h3 {
     margin: 0 0 10px 0;
     font-size: 1.2em;
   }
   
   .tab-content p {
     margin: 0;
     opacity: 0.9;
   }
   ```

## 📞 지원 및 문의
- 이메일: support@kotra.or.kr
- 웹사이트: https://www.kotra.or.kr

## 📄 라이선스
© 2024 KOTRA. All rights reserved. 