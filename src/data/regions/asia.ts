import { TradeAgency } from '../tradeAgencies';

export const asiaAgencies: TradeAgency[] = [
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
    id: 8,
    country: '인도',
    organizationName: 'FIEO - Federation of Indian Export Organisations',
    city: '뉴델리',
    latitude: 28.6139,
    longitude: 77.2090,
    address: 'Vanijya Bhawan, International Trade Centre, New Delhi 110001',
    phone: '+91-11-2331-4171',
    email: 'fieo@fieo.org',
    website: 'www.indiantradeportal.in',
    description: '인도 수출기구연합회 - 무역진흥 및 수출촉진',
    featured: true
  },
  // ... 나머지 아시아 국가들
]; 