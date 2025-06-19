// 무역진흥기관 인터페이스 정의
export interface TradeAgency {
  id: number;
  country: string;
  organizationName: string;
  city: string;
  latitude: number;
  longitude: number;
  address: string;
  phone: string;
  email: string;
  website: string;
  description: string;
  featured: boolean;
  region?: string;
}

// 전 세계 무역진흥기관 데이터
export const allTradePromotionAgencies: TradeAgency[] = [
  // 주요 국가들 (featured)
  {
    id: 1,
    country: '미국',
    organizationName: 'International Trade Administration (ITA)',
    city: '워싱턴 D.C.',
    latitude: 38.9072,
    longitude: -77.0369,
    address: '1401 Constitution Ave NW, Washington, DC 20230',
    phone: '+1-202-482-2000',
    email: 'info@trade.gov',
    website: 'www.trade.gov',
    description: '미국 상무부 국제무역청',
    featured: true
  },
  {
    id: 2,
    country: '중국',
    organizationName: 'CCPIT (중국국제무역촉진위원회)',
    city: '베이징',
    latitude: 39.9042,
    longitude: 116.4074,
    address: '1 Fuxingmenwai Street, Beijing 100860',
    phone: '+86-10-8807-5000',
    email: 'ccpit@ccpit.org',
    website: 'www.ccpit.org',
    description: '중국 최대 무역투자 촉진기관',
    featured: true
  },
  {
    id: 3,
    country: '일본',
    organizationName: 'JETRO (일본무역진흥기구)',
    city: '도쿄',
    latitude: 35.6762,
    longitude: 139.6503,
    address: 'Ark Mori Building, 1-12-32 Akasaka, Minato-ku, Tokyo',
    phone: '+81-3-3582-5511',
    email: 'info@jetro.go.jp',
    website: 'www.jetro.go.jp',
    description: '일본 경제산업성 산하 무역진흥기관',
    featured: true
  },
  // ... 나머지 데이터는 App.tsx에서 복사해서 여기에 넣으시면 됩니다
];

// 지역별 필터링을 위한 헬퍼 함수들
export const getFeaturedAgencies = () => 
  allTradePromotionAgencies.filter(agency => agency.featured);

export const getAgenciesByRegion = (region: string) => 
  allTradePromotionAgencies.filter(agency => agency.region === region);

export const searchAgencies = (query: string) => 
  allTradePromotionAgencies.filter(agency => 
    agency.country.toLowerCase().includes(query.toLowerCase()) ||
    agency.organizationName.toLowerCase().includes(query.toLowerCase()) ||
    agency.city.toLowerCase().includes(query.toLowerCase())
  ); 