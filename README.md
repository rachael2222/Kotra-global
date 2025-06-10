# KOTRA Global Trade Network Platform

글로벌 무역진흥기관 네트워크 플랫폼 - ASEAN 중심의 무역진흥기관 정보 서비스

## 🌏 프로젝트 소개

전 세계 각국의 무역진흥기관 정보를 제공하는 React 기반 웹 플랫폼입니다. 특히 ASEAN 10개국의 무역진흥기관에 중점을 두어, 한국 기업들의 해외 진출을 지원합니다.

## ✨ 주요 기능

- **🗺️ ASEAN 지도 시각화**: 10개국 무역진흥기관 인터랙티브 지도
- **🔍 스마트 검색**: 국가명, 기관명, 도시명으로 검색
- **📊 ASEAN 통계**: 회원국, 인구, GDP 정보
- **📧 이메일 템플릿**: 수출문의 이메일 자동 생성
- **📱 반응형 디자인**: 모바일 친화적 인터페이스
- **🌍 전세계 151개국**: 무역진흥기관 정보 데이터베이스

## 🚀 시작하기

### 필수 요구사항
- Node.js 14.0 이상
- npm 6.0 이상

### 설치 및 실행

```bash
# 프로젝트 클론
git clone https://github.com/rachael2222/Kotra-global.git

# 디렉터리 이동
cd Kotra-global

# 의존성 설치
npm install

# 개발 서버 실행
npm start
```

브라우저에서 [http://localhost:3000](http://localhost:3000)으로 접속하여 확인하세요.

## 🛠️ 기술 스택

- **Frontend**: React 18, TypeScript
- **Styling**: CSS3, Flexbox, Grid
- **Icons**: Lucide React
- **Build Tool**: Create React App
- **Version Control**: Git

## 📦 프로젝트 구조

```
src/
├── components/          # React 컴포넌트
├── data/               # 무역진흥기관 데이터
│   ├── tradeAgencies.ts
│   └── regions/
│       └── asia.ts
├── App.tsx             # 메인 애플리케이션
├── App.css             # 스타일시트
└── index.tsx           # 진입점
```

## 🌏 지원 지역

### ASEAN 10개국
- 🇸🇬 싱가포르 - Enterprise Singapore
- 🇻🇳 베트남 - Vietnam Trade Promotion
- 🇹🇭 태국 - Department of International Trade Promotion
- 🇲🇾 말레이시아 - MATRADE
- 🇮🇩 인도네시아 - Indonesia Investment Coordinating Board
- 🇵🇭 필리핀 - Department of Trade and Industry
- 🇱🇦 라오스 - Department of Trade Promotion
- 🇰🇭 캄보디아 - Cambodia Investment Board
- 🇲🇲 미얀마 - Directorate of Investment and Company Administration
- 🇧🇳 브루나이 - Darussalam Enterprise

### 기타 주요 국가
- 🇺🇸 미국, 🇨🇳 중국, 🇯🇵 일본, 🇩🇪 독일, 🇬🇧 영국, 🇦🇺 호주, 🇮🇳 인도
- 유럽, 남미, 중동, 아프리카 등 전세계 151개국

## 📧 이메일 템플릿 기능

ASEAN 국가 무역진흥기관에 대해 자동으로 생성되는 이메일 템플릿:
- 한국 기술 솔루션 소개
- 공항 보안 및 국경 관리 시스템
- 파트너십 제안 내용
- 연락처 정보 자동 삽입

## 🚀 배포

### 프로덕션 빌드
```bash
npm run build
```

### GitHub Pages 배포 (선택사항)
```bash
npm install --save-dev gh-pages

# package.json에 homepage 추가
"homepage": "https://rachael2222.github.io/Kotra-global"

# 배포 스크립트 추가
"scripts": {
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
}

# 배포 실행
npm run deploy
```

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 있습니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 연락처

프로젝트 관련 문의: [GitHub Issues](https://github.com/rachael2222/Kotra-global/issues)

## 🙏 감사의 말

- [KOTRA](https://www.kotra.or.kr) - 무역진흥공사
- [React](https://reactjs.org/) - UI 라이브러리
- [Lucide React](https://lucide.dev/) - 아이콘 라이브러리
