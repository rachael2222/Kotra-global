export interface Agency {
  id: number;
  country: string;
  countryCode: string;
  agencyName: string;
  email: string;
  phone: string;
  website: string;
  address: string;
  lat: number;
  lng: number;
  description: string;
}

export const agencies: Agency[] = [
  // 동남아시아
  {
    id: 1,
    country: "Singapore",
    countryCode: "SG",
    agencyName: "Enterprise Singapore",
    email: "enquiry@enterprisesg.gov.sg",
    phone: "+65 6898 1800",
    website: "https://www.enterprisesg.gov.sg",
    address: "230 Victoria St, #10-00, Singapore 188024",
    lat: 1.3000,
    lng: 103.8565,
    description: "싱가포르의 기업 발전 및 국제화를 지원하는 정부기관"
  },
  {
    id: 2,
    country: "Malaysia",
    countryCode: "MY",
    agencyName: "MATRADE",
    email: "info@matrade.gov.my",
    phone: "+60 3-6207 7077",
    website: "https://www.matrade.gov.my",
    address: "Jalan Sultan Haji Ahmad Shah, Kuala Lumpur",
    lat: 3.1587,
    lng: 101.7090,
    description: "말레이시아 대외무역개발공사"
  },
  {
    id: 3,
    country: "Indonesia",
    countryCode: "ID",
    agencyName: "BKPM (Indonesia Investment Board)",
    email: "info@bkpm.go.id",
    phone: "+62 21-5252008",
    website: "https://www.bkpm.go.id",
    address: "Jl. Jenderal Gatot Subroto, Jakarta",
    lat: -6.2294,
    lng: 106.8295,
    description: "인도네시아 투자조정청"
  },
  {
    id: 4,
    country: "Thailand",
    countryCode: "TH",
    agencyName: "DITP (Department of International Trade Promotion)",
    email: "ditp@ditp.go.th",
    phone: "+66 2507 7999",
    website: "https://www.ditp.go.th",
    address: "Ratchadaphisek Rd, Bangkok",
    lat: 13.7367,
    lng: 100.5231,
    description: "태국 국제무역진흥부"
  },
  {
    id: 5,
    country: "Vietnam",
    countryCode: "VN",
    agencyName: "VIETRADE",
    email: "vietrade@moit.gov.vn",
    phone: "+84 24 3934 7621",
    website: "http://www.vietrade.gov.vn",
    address: "20 Ly Thuong Kiet, Hanoi",
    lat: 21.0285,
    lng: 105.8542,
    description: "베트남 무역진흥청"
  },
  {
    id: 6,
    country: "Philippines",
    countryCode: "PH",
    agencyName: "DTI (Department of Trade and Industry)",
    email: "contactus@dti.gov.ph",
    phone: "+63 2 7791 3100",
    website: "https://www.dti.gov.ph",
    address: "361 Sen. Gil J. Puyat Ave, Manila",
    lat: 14.5547,
    lng: 121.0244,
    description: "필리핀 무역산업부"
  },
  
  // 동아시아
  {
    id: 7,
    country: "Japan",
    countryCode: "JP",
    agencyName: "JETRO (Japan External Trade Organization)",
    email: "info@jetro.go.jp",
    phone: "+81 3-3582-5511",
    website: "https://www.jetro.go.jp",
    address: "Ark Mori Building, Tokyo",
    lat: 35.6762,
    lng: 139.6503,
    description: "일본 무역진흥기구"
  },
  {
    id: 8,
    country: "China",
    countryCode: "CN",
    agencyName: "CCPIT (China Council for Promotion of International Trade)",
    email: "info@ccpit.org",
    phone: "+86 10-8807-5000",
    website: "http://www.ccpit.org",
    address: "1 Fuxingmenwai Street, Beijing",
    lat: 39.9042,
    lng: 116.4074,
    description: "중국국제무역촉진위원회"
  },
  
  // 유럽
  {
    id: 9,
    country: "Germany",
    countryCode: "DE",
    agencyName: "GTAI (Germany Trade & Invest)",
    email: "info@gtai.de",
    phone: "+49 30 200 099-0",
    website: "https://www.gtai.de",
    address: "Friedrichstraße 60, Berlin",
    lat: 52.5200,
    lng: 13.4050,
    description: "독일 무역투자진흥기관"
  },
  {
    id: 10,
    country: "United Kingdom",
    countryCode: "GB",
    agencyName: "DIT (Department for International Trade)",
    email: "enquiries@trade.gov.uk",
    phone: "+44 20 7215 5000",
    website: "https://www.gov.uk/dit",
    address: "Old Admiralty Building, London",
    lat: 51.5074,
    lng: -0.1278,
    description: "영국 국제무역부"
  },
  {
    id: 11,
    country: "France",
    countryCode: "FR",
    agencyName: "Business France",
    email: "info@businessfrance.fr",
    phone: "+33 1 40 73 30 00",
    website: "https://www.businessfrance.fr",
    address: "77 Boulevard Saint-Jacques, Paris",
    lat: 48.8566,
    lng: 2.3522,
    description: "프랑스 대외무역투자청"
  },
  
  // 북미
  {
    id: 12,
    country: "United States",
    countryCode: "US",
    agencyName: "ITA (International Trade Administration)",
    email: "ita.info@trade.gov",
    phone: "+1 202-482-2000",
    website: "https://www.trade.gov",
    address: "1401 Constitution Ave NW, Washington DC",
    lat: 38.9072,
    lng: -77.0369,
    description: "미국 국제무역청"
  },
  {
    id: 13,
    country: "Canada",
    countryCode: "CA",
    agencyName: "TCS (Trade Commissioner Service)",
    email: "info@international.gc.ca",
    phone: "+1 613-996-2000",
    website: "https://www.tradecommissioner.gc.ca",
    address: "125 Sussex Drive, Ottawa",
    lat: 45.4215,
    lng: -75.6972,
    description: "캐나다 무역위원회"
  },
  
  // 중동
  {
    id: 14,
    country: "UAE",
    countryCode: "AE",
    agencyName: "Dubai Chamber of Commerce",
    email: "info@dubaichamber.com",
    phone: "+971 4-228-0000",
    website: "https://www.dubaichamber.com",
    address: "Dubai Chamber Building, Dubai",
    lat: 25.2048,
    lng: 55.2708,
    description: "두바이 상공회의소"
  },
  
  // 남미
  {
    id: 15,
    country: "Brazil",
    countryCode: "BR",
    agencyName: "APEX-Brasil",
    email: "apex@apexbrasil.com.br",
    phone: "+55 61 3426-0202",
    website: "http://www.apexbrasil.com.br",
    address: "Setor Bancário Norte, Brasília",
    lat: -15.7942,
    lng: -47.8822,
    description: "브라질 수출투자진흥청"
  },
  
  // 아프리카
  {
    id: 16,
    country: "South Africa",
    countryCode: "ZA",
    agencyName: "WESGRO",
    email: "info@wesgro.co.za",
    phone: "+27 21-487-8600",
    website: "https://www.wesgro.co.za",
    address: "19th Floor, ABSA Centre, Cape Town",
    lat: -33.9249,
    lng: 18.4241,
    description: "남아프리카공화국 서부케이프 무역투자진흥청"
  },
  
  // 오세아니아
  {
    id: 17,
    country: "Australia",
    countryCode: "AU",
    agencyName: "Austrade",
    email: "info@austrade.gov.au",
    phone: "+61 13-28-78",
    website: "https://www.austrade.gov.au",
    address: "Level 13, 201 Kent Street, Sydney",
    lat: -33.8688,
    lng: 151.2093,
    description: "호주 무역투자진흥청"
  },
  
  // 인도
  {
    id: 18,
    country: "India",
    countryCode: "IN",
    agencyName: "India Trade Portal",
    email: "info@indiatradeportal.in",
    phone: "+91 11-2338-4714",
    website: "https://www.indiatradeportal.in",
    address: "Udyog Bhawan, New Delhi",
    lat: 28.6139,
    lng: 77.2090,
    description: "인도 무역진흥기구"
  }
]; 