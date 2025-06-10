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

## 📧 **이메일 템플릿 기능 상세 설명**

### **🔧 작동 방식**
1. **버튼 위치**: ASEAN 국가 카드 하단에 **"📧 수출문의 이메일 작성"** 버튼
2. **클릭 시**: 자동으로 **미리 작성된 이메일**이 기본 메일 프로그램에서 열림
3. **자동 입력**: 받는 사람(해당 기관 이메일)과 제목, 본문이 **자동으로 채워짐**

### **📝 실제 생성되는 이메일 템플릿**

#### **이메일 제목**
```
Partnership Inquiry - Korean Technology Solutions
```

#### **이메일 본문** (예: 싱가포르 Enterprise Singapore)
```
Dear Enterprise Singapore Team,

I hope this email finds you well. I am writing to introduce our company and explore potential collaboration opportunities in 싱가포르.

Our Company:
- Korean technology company specializing in innovative solutions
- Proven track record in airport security and border control systems
- Looking to expand operations in the ASEAN region

Our Solutions:
📋 Airport document verification systems
🛂 Immigration and border control technology
🔒 Government security solutions
📄 Document digitization and processing

We would be very interested in:
✅ Learning about current government ICT procurement opportunities
✅ Connecting with local system integrators
✅ Understanding regulatory requirements for our technology
✅ Exploring potential pilot projects

Attached Materials:
- Company introduction (English)
- Technical specifications
- Airport implementation case studies

We would greatly appreciate the opportunity to discuss how our technology can support 싱가포르's digital transformation initiatives.

Thank you for your time and consideration. I look forward to your response.

Best regards,
[Your Name]
[Your Title]
[Company Name]
[Contact Information]

---
Generated via KOTRA Global Trade Network Platform
```

### **🎯 자동 삽입되는 정보**
- ✅ **기관명**: `${agency.organizationName}` (예: Enterprise Singapore)
- ✅ **국가명**: `${agency.country}` (예: 싱가포르)
- ✅ **받는 사람**: `${agency.email}` (예: enquiry@enterprisesg.gov.sg)

### **📱 사용 방법**
1. **ASEAN 지도에서 국가 클릭** 또는 **전체 목록에서 ASEAN 국가 찾기**
2. 해당 국가 카드에서 **"📧 수출문의 이메일 작성"** 버튼 클릭
3. **기본 메일 프로그램**(Outlook, Gmail 등)이 자동으로 열림
4. **이미 작성된 템플릿**을 확인하고 필요에 따라 수정
5. **[Your Name] 등 개인정보 입력** 후 전송

### **💡 특징**
- **완전 자동화**: 클릭 한 번으로 전문적인 비즈니스 이메일 생성
- **개인화**: 각 국가와 기관에 맞게 자동으로 정보 삽입
- **전문적 내용**: 한국 기업의 해외진출에 특화된 내용
- **ASEAN 전용**: ASEAN 10개국에만 제공되는 특별 기능

이 기능으로 ASEAN 무역진흥기관에 체계적이고 전문적인 문의를 쉽게 보낼 수 있습니다! 🚀
