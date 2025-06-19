# Global Trade Support 🌍

전세계 수출지원기관 연락처를 지도 기반으로 검색할 수 있는 SaaS 플랫폼입니다.

## 🚀 주요 기능

- **지도 기반 검색**: 세계지도에서 직관적으로 수출지원기관 위치 확인
- **국가별 검색**: 국가명 또는 기관명으로 빠른 검색
- **상세 정보 제공**: 이메일, 전화번호, 웹사이트, 주소 등 완전한 연락처 정보
- **원클릭 연락**: 이메일 작성, 전화 걸기, 웹사이트 방문 등 바로 실행
- **클립보드 복사**: 연락처 정보 원클릭 복사
- **반응형 디자인**: 데스크톱과 모바일에서 모두 사용 가능

## 🌏 지원 국가 및 기관

현재 **18개국 18개 기관**의 정보를 제공합니다:

### 동남아시아
- 🇸🇬 **싱가포르**: Enterprise Singapore
- 🇲🇾 **말레이시아**: MATRADE
- 🇮🇩 **인도네시아**: BKPM (Indonesia Investment Board)
- 🇹🇭 **태국**: DITP (Department of International Trade Promotion)
- 🇻🇳 **베트남**: VIETRADE
- 🇵🇭 **필리핀**: DTI (Department of Trade and Industry)

### 동아시아
- 🇯🇵 **일본**: JETRO (Japan External Trade Organization)
- 🇨🇳 **중국**: CCPIT (China Council for Promotion of International Trade)

### 유럽
- 🇩🇪 **독일**: GTAI (Germany Trade & Invest)
- 🇬🇧 **영국**: DIT (Department for International Trade)
- 🇫🇷 **프랑스**: Business France

### 북미
- 🇺🇸 **미국**: ITA (International Trade Administration)
- 🇨🇦 **캐나다**: TCS (Trade Commissioner Service)

### 기타 지역
- 🇦🇪 **UAE**: Dubai Chamber of Commerce
- 🇧🇷 **브라질**: APEX-Brasil
- 🇿🇦 **남아프리카공화국**: WESGRO
- 🇦🇺 **호주**: Austrade
- 🇮🇳 **인도**: India Trade Portal

## 🛠 기술 스택

- **Frontend**: React 18 + TypeScript
- **지도**: Mapbox GL JS + react-map-gl
- **스타일링**: Tailwind CSS
- **아이콘**: Lucide React
- **빌드 도구**: Create React App

## 📦 설치 및 실행

### 1. 저장소 클론
\`\`\`bash
git clone <repository-url>
cd kotra-global
\`\`\`

### 2. 의존성 설치
\`\`\`bash
npm install
\`\`\`

### 3. Mapbox 토큰 설정
1. [Mapbox](https://www.mapbox.com)에서 무료 계정 생성
2. Access Token 발급
3. 프로젝트 루트에 \`.env\` 파일 생성:
\`\`\`
REACT_APP_MAPBOX_TOKEN=your_mapbox_token_here
\`\`\`

### 4. 개발 서버 실행
\`\`\`bash
npm start
\`\`\`

브라우저에서 [http://localhost:3000](http://localhost:3000)으로 접속하세요.

## 🎯 사용 방법

1. **검색하기**: 상단 검색바에 국가명 또는 기관명 입력
2. **지도에서 찾기**: 지도의 파란색 마커 클릭
3. **정보 확인**: 팝업 또는 사이드바에서 상세 정보 확인
4. **연락하기**: 이메일, 전화, 웹사이트 버튼으로 바로 연락

## 🚀 배포

### Vercel 배포
\`\`\`bash
npm run build
npx vercel --prod
\`\`\`

### Netlify 배포
\`\`\`bash
npm run build
# build 폴더를 Netlify에 업로드
\`\`\`

## 🔮 향후 계획

- [ ] 더 많은 국가 및 기관 추가
- [ ] 다국어 지원 (영어, 중국어, 일본어 등)
- [ ] 기관별 상담 예약 기능
- [ ] 무역 관련 뉴스 및 공지사항 연동
- [ ] PDF 리포트 다운로드 기능
- [ ] 즐겨찾기 기능
- [ ] 사용자 계정 및 히스토리 관리

## 📄 라이선스

MIT License

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your Changes (\`git commit -m 'Add some AmazingFeature'\`)
4. Push to the Branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

## 📞 문의

프로젝트에 대한 문의사항이나 제안사항이 있으시면 언제든 연락주세요!

---

**Made with ❤️ for Korean exporters** 