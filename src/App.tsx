import React, { useState, useMemo } from 'react';
import { Globe, MapPin, Building2, Search, X } from 'lucide-react';
import './App.css';

// 전 세계 무역진흥기관 데이터 (확장된 리스트)
const allTradePromotionAgencies = [
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
    email: 'contact@trade.gov',
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
    email: 'jetro@jetro.go.jp',
    website: 'www.jetro.go.jp',
    description: '일본 경제산업성 산하 무역진흥기관',
    featured: true
  },
  {
    id: 4,
    country: '독일',
    organizationName: 'GTAI (Germany Trade & Invest)',
    city: '베를린',
    latitude: 52.5200,
    longitude: 13.4050,
    address: 'Friedrichstrasse 60, 10117 Berlin',
    phone: '+49-30-200-099-0',
    email: 'contact@gtai.de',
    website: 'www.gtai.de',
    description: '독일 연방경제기후보호부 산하 무역투자진흥기관',
    featured: true
  },
  {
    id: 5,
    country: '영국',
    organizationName: 'DBT (Department for Business and Trade)',
    city: '런던',
    latitude: 51.5074,
    longitude: -0.1278,
    address: 'Old Admiralty Building, Admiralty Place, London SW1A 2DY',
    phone: '+44-20-4551-0011',
    email: 'DBTNA@businessandtrade.gov.uk',
    website: 'www.gov.uk/government/organisations/department-for-business-and-trade',
    description: '영국 정부 비즈니스 무역부',
    featured: true
  },
  {
    id: 6,
    country: '싱가포르',
    organizationName: 'Enterprise Singapore',
    city: '싱가포르',
    latitude: 1.3000,
    longitude: 103.8565,
    address: '230 Victoria St, #10-00, Singapore 188024',
    phone: '+65-6898-1800',
    email: 'enquiry@enterprisesg.gov.sg',
    website: 'www.enterprisesg.gov.sg',
    description: '싱가포르 기업청 - 기업 성장 및 국제화 지원',
    featured: true,
    region: 'ASEAN'
  },
  {
    id: 7,
    country: '호주',
    organizationName: 'Austrade (Australian Trade and Investment Commission)',
    city: '시드니',
    latitude: -33.8688,
    longitude: 151.2093,
    address: 'Level 11, 47 York Street, Sydney NSW 2000',
    phone: '+61-2-9262-4011',
    email: 'info@austrade.gov.au',
    website: 'www.austrade.gov.au',
    description: '호주 정부 무역투자진흥위원회',
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

  // 유럽 추가 국가들
  {
    id: 9,
    country: '프랑스',
    organizationName: 'Business France',
    city: '파리',
    latitude: 48.8566,
    longitude: 2.3522,
    address: '77 boulevard Saint-Jacques, 75014 Paris',
    phone: '+33-1-40-73-30-00',
    email: 'info@businessfrance.fr',
    website: 'www.businessfrance.fr',
    description: '프랑스 대외무역투자진흥청',
    featured: false
  },
  {
    id: 10,
    country: '이탈리아',
    organizationName: 'ITA (Italian Trade Agency)',
    city: '로마',
    latitude: 41.9028,
    longitude: 12.4964,
    address: 'Via Liszt, 21, 00144 Roma',
    phone: '+39-06-5992-1',
    email: 'info@ice.it',
    website: 'www.ice.it',
    description: '이탈리아 대외무역진흥청',
    featured: false
  },
  {
    id: 11,
    country: '스페인',
    organizationName: 'ICEX España',
    city: '마드리드',
    latitude: 40.4168,
    longitude: -3.7038,
    address: 'Paseo de la Castellana, 14-16, 28046 Madrid',
    phone: '+34-91-349-6100',
    email: 'info@icex.es',
    website: 'www.icex.es',
    description: '스페인 대외무역투자진흥원',
    featured: false
  },
  {
    id: 12,
    country: '네덜란드',
    organizationName: 'Netherlands Enterprise Agency',
    city: '암스테르담',
    latitude: 52.3676,
    longitude: 4.9041,
    address: 'Prinses Beatrixlaan 2, The Hague',
    phone: '+31-88-042-42-42',
    email: 'info@rvo.nl',
    website: 'www.rvo.nl',
    description: '네덜란드 기업청',
    featured: false
  },
  {
    id: 13,
    country: '스위스',
    organizationName: 'Switzerland Global Enterprise',
    city: '취리히',
    latitude: 47.3769,
    longitude: 8.5417,
    address: 'Stampfenbachstrasse 85, 8006 Zurich',
    phone: '+41-44-365-51-51',
    email: 'info@s-ge.com',
    website: 'www.s-ge.com',
    description: '스위스 글로벌 기업청',
    featured: false
  },
  {
    id: 14,
    country: '스웨덴',
    organizationName: 'Business Sweden',
    city: '스톡홀름',
    latitude: 59.3293,
    longitude: 18.0686,
    address: 'Box 240, SE-101 24 Stockholm',
    phone: '+46-8-588-660-00',
    email: 'info@business-sweden.se',
    website: 'www.business-sweden.se',
    description: '스웨덴 무역투자진흥청',
    featured: false
  },
  {
    id: 15,
    country: '노르웨이',
    organizationName: 'Innovation Norway',
    city: '오슬로',
    latitude: 59.9139,
    longitude: 10.7522,
    address: 'Akersgata 13, 0158 Oslo',
    phone: '+47-22-00-25-00',
    email: 'post@innovasjonnorge.no',
    website: 'www.innovasjonnorge.no',
    description: '노르웨이 혁신청',
    featured: false
  },
  {
    id: 16,
    country: '덴마크',
    organizationName: 'Danish Agency for Trade Promotion',
    city: '코펜하겐',
    latitude: 55.6761,
    longitude: 12.5683,
    address: 'Toldbodgade 29, 1253 Copenhagen',
    phone: '+45-33-92-00-00',
    email: 'info@um.dk',
    website: 'www.um.dk',
    description: '덴마크 무역진흥청',
    featured: false
  },
  {
    id: 17,
    country: '핀란드',
    organizationName: 'Business Finland',
    city: '헬싱키',
    latitude: 60.1699,
    longitude: 24.9384,
    address: 'Porkkalankatu 1, 00180 Helsinki',
    phone: '+358-29-505-5000',
    email: 'info@businessfinland.fi',
    website: 'www.businessfinland.fi',
    description: '핀란드 비즈니스청',
    featured: false
  },
  {
    id: 18,
    country: '오스트리아',
    organizationName: 'ADVANTAGE AUSTRIA',
    city: '비엔나',
    latitude: 48.2082,
    longitude: 16.3738,
    address: 'Wiedner Hauptstrasse 63, 1045 Vienna',
    phone: '+43-5-90-900-4099',
    email: 'office@advantageaustria.org',
    website: 'www.advantageaustria.org',
    description: '오스트리아 대외무역진흥청',
    featured: false
  },
  {
    id: 19,
    country: '벨기에',
    organizationName: 'AWEX-WALLONIA',
    city: '브뤼셀',
    latitude: 50.8503,
    longitude: 4.3517,
    address: 'Place Sainctelette 2, 1080 Brussels',
    phone: '+32-2-421-82-11',
    email: 'info@awex.be',
    website: 'www.awex.be',
    description: '벨기에 왈로니아 수출투자청',
    featured: false
  },
  {
    id: 20,
    country: '폴란드',
    organizationName: 'Polish Investment and Trade Agency',
    city: '바르샤바',
    latitude: 52.2297,
    longitude: 21.0122,
    address: 'ul. Krucza 50, 00-025 Warsaw',
    phone: '+48-22-334-98-00',
    email: 'info@paih.gov.pl',
    website: 'www.paih.gov.pl',
    description: '폴란드 투자무역청',
    featured: false
  },

  // 아시아 추가 국가들
  {
    id: 21,
    country: '베트남',
    organizationName: 'Vietnam Trade Promotion Agency (VIETRADE)',
    city: '하노이',
    latitude: 21.0285,
    longitude: 105.8542,
    address: '20 Ly Thuong Kiet, Hanoi',
    phone: '+84-24-3934-7621',
    email: 'vietrade@moit.gov.vn',
    website: 'www.vietrade.gov.vn',
    description: '베트남 무역진흥청',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 22,
    country: '태국',
    organizationName: 'Department of International Trade Promotion (DITP)',
    city: '방콕',
    latitude: 13.7367,
    longitude: 100.5231,
    address: 'Ratchadaphisek Rd, Bangkok',
    phone: '+66-2-507-7999',
    email: 'ditp@ditp.go.th',
    website: 'www.ditp.go.th',
    description: '태국 국제무역진흥청',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 23,
    country: '말레이시아',
    organizationName: 'MATRADE',
    city: '쿠알라룸푸르',
    latitude: 3.1587,
    longitude: 101.7090,
    address: 'Jalan Sultan Haji Ahmad Shah, Kuala Lumpur',
    phone: '+60-3-6207-7077',
    email: 'info@matrade.gov.my',
    website: 'www.matrade.gov.my',
    description: '말레이시아 대외무역진흥공사',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 24,
    country: '인도네시아',
    organizationName: 'Indonesia Investment Coordinating Board (BKPM)',
    city: '자카르타',
    latitude: -6.2294,
    longitude: 106.8295,
    address: 'Jl. Jenderal Gatot Subroto, Jakarta',
    phone: '+62-21-5252008',
    email: 'info@bkpm.go.id',
    website: 'www.bkpm.go.id',
    description: '인도네시아 투자조정청',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 25,
    country: '필리핀',
    organizationName: 'Department of Trade and Industry (DTI)',
    city: '마닐라',
    latitude: 14.5547,
    longitude: 121.0244,
    address: '361 Sen. Gil J. Puyat Ave, Makati City',
    phone: '+63-2-7791-3100',
    email: 'contactus@dti.gov.ph',
    website: 'www.dti.gov.ph',
    description: '필리핀 무역산업부',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 26,
    country: '한국',
    organizationName: 'KOTRA (대한무역투자진흥공사)',
    city: '서울',
    latitude: 37.5665,
    longitude: 126.9780,
    address: '서울특별시 서초구 헌릉로 13',
    phone: '+82-2-3460-7114',
    email: 'info@kotra.or.kr',
    website: 'www.kotra.or.kr',
    description: '대한민국 무역투자진흥공사',
    featured: false
  },
  {
    id: 27,
    country: '홍콩',
    organizationName: 'InvestHK (홍콩투자진흥청)',
    city: '홍콩',
    latitude: 22.3193,
    longitude: 114.1694,
    address: '26/F, One Island East, Taikoo Place, Hong Kong',
    phone: '+852-3107-1000',
    email: 'enquiry@investhk.gov.hk',
    website: 'www.investhk.gov.hk',
    description: '홍콩특별행정구 투자진흥청',
    featured: false
  },
  {
    id: 28,
    country: '대만',
    organizationName: 'TAITRA (대만무역진흥공사)',
    city: '타이페이',
    latitude: 25.0330,
    longitude: 121.5654,
    address: '5F, 333 Keelung Rd. Sec.1, Taipei',
    phone: '+886-2-2725-5200',
    email: 'service@taitra.org.tw',
    website: 'www.taitra.org.tw',
    description: '대만 무역진흥공사',
    featured: false
  },
  {
    id: 29,
    country: '몽골',
    organizationName: 'Foreign Investment and Foreign Trade Agency',
    city: '울란바토르',
    latitude: 47.8864,
    longitude: 106.9057,
    address: 'Government Building 2, Ulaanbaatar',
    phone: '+976-11-263-469',
    email: 'info@investmongolia.gov.mn',
    website: 'www.investmongolia.gov.mn',
    description: '몽골 외국인투자무역청',
    featured: false
  },
  {
    id: 30,
    country: '라오스',
    organizationName: 'Department of Trade Promotion',
    city: '비엔티안',
    latitude: 17.9757,
    longitude: 102.6331,
    address: 'Ministry of Commerce, Vientiane',
    phone: '+856-21-410017',
    email: 'trade@laosgov.la',
    website: 'www.moc.gov.la',
    description: '라오스 무역진흥청',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 31,
    country: '캄보디아',
    organizationName: 'Cambodia Investment Board',
    city: '프놈펜',
    latitude: 11.5621,
    longitude: 104.8885,
    address: 'Government Palace, Phnom Penh',
    phone: '+855-23-981-154',
    email: 'info@cambodiainvestment.gov.kh',
    website: 'www.cambodiainvestment.gov.kh',
    description: '캄보디아 투자위원회',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 32,
    country: '미얀마',
    organizationName: 'Directorate of Investment and Company Administration (DICA)',
    city: '양곤',
    latitude: 16.8661,
    longitude: 96.1951,
    address: 'Building 1, Yangon',
    phone: '+95-1-657891',
    email: 'dica@myanmar.gov.mm',
    website: 'www.dica.gov.mm',
    description: '미얀마 투자기업청',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 33,
    country: '브루나이',
    organizationName: 'Darussalam Enterprise (DARe)',
    city: '반다르스리브가완',
    latitude: 4.9031,
    longitude: 114.9398,
    address: 'Level 3, BIBD Square, Bandar Seri Begawan',
    phone: '+673-836-3448',
    email: 'dare@ei.gov.bn',
    website: 'www.dare.gov.bn',
    description: '브루나이 기업청',
    featured: false,
    region: 'ASEAN'
  },
  {
    id: 34,
    country: '파키스탄',
    organizationName: 'Board of Investment Pakistan',
    city: '이슬라마바드',
    latitude: 33.6844,
    longitude: 73.0479,
    address: 'Plot 2-A, Sector G-5/2, Islamabad',
    phone: '+92-51-921-8121',
    email: 'info@boi.gov.pk',
    website: 'www.boi.gov.pk',
    description: '파키스탄 투자위원회',
    featured: false
  },
  {
    id: 35,
    country: '방글라데시',
    organizationName: 'BIDA (방글라데시 투자개발청)',
    city: '다카',
    latitude: 23.8103,
    longitude: 90.4125,
    address: 'Agargaon Administrative Area, Dhaka',
    phone: '+880-2-8181-8120',
    email: 'info@bida.gov.bd',
    website: 'www.bida.gov.bd',
    description: '방글라데시 투자개발청',
    featured: false
  },
  {
    id: 36,
    country: '스리랑카',
    organizationName: 'Board of Investment Sri Lanka',
    city: '콜롬보',
    latitude: 6.9271,
    longitude: 79.8612,
    address: 'Level 26, West Tower, World Trade Center, Colombo',
    phone: '+94-11-2-437-770',
    email: 'info@investsrilanka.com',
    website: 'www.investsrilanka.com',
    description: '스리랑카 투자위원회',
    featured: false
  },
  {
    id: 37,
    country: '네팔',
    organizationName: 'Investment Promotion Board Nepal',
    city: '카트만두',
    latitude: 27.7172,
    longitude: 85.3240,
    address: 'ICC Complex, New Baneshwor, Kathmandu',
    phone: '+977-1-4-475-277',
    email: 'info@ibpn.gov.np',
    website: 'www.ibpn.gov.np',
    description: '네팔 투자진흥위원회',
    featured: false
  },
  {
    id: 38,
    country: '부탄',
    organizationName: 'Foreign Direct Investment Division',
    city: '팀푸',
    latitude: 27.4728,
    longitude: 89.6393,
    address: 'Ministry of Economic Affairs, Thimphu',
    phone: '+975-2-322-579',
    email: 'info@moea.gov.bt',
    website: 'www.moea.gov.bt',
    description: '부탄 경제부 외국인투자과',
    featured: false
  },
  {
    id: 39,
    country: '아프가니스탄',
    organizationName: 'Afghanistan Investment Support Agency',
    city: '카불',
    latitude: 34.5553,
    longitude: 69.2075,
    address: 'Darulaman Road, Kabul',
    phone: '+93-20-220-0897',
    email: 'info@aisa.gov.af',
    website: 'www.aisa.gov.af',
    description: '아프가니스탄 투자지원청',
    featured: false
  },
  {
    id: 40,
    country: '우즈베키스탄',
    organizationName: 'Agency for Foreign Investment',
    city: '타슈켄트',
    latitude: 41.2995,
    longitude: 69.2401,
    address: 'Shakhrisabz Street 5, Tashkent',
    phone: '+998-71-233-47-91',
    email: 'info@invest.gov.uz',
    website: 'www.invest.gov.uz',
    description: '우즈베키스탄 외국인투자청',
    featured: false
  },
  {
    id: 41,
    country: '카자흐스탄',
    organizationName: 'KAZAKH INVEST',
    city: '누르술탄',
    latitude: 51.1694,
    longitude: 71.4491,
    address: 'Building A-24/2, Mangilik El Avenue, Nur-Sultan',
    phone: '+7-7172-62-04-04',
    email: 'info@invest.gov.kz',
    website: 'www.invest.gov.kz',
    description: '카자흐스탄 국가투자위원회',
    featured: false
  },
  {
    id: 42,
    country: '키르기스스탄',
    organizationName: 'Invest in Kyrgyzstan',
    city: '비슈케크',
    latitude: 42.8746,
    longitude: 74.5698,
    address: 'Chui Avenue 106, Bishkek',
    phone: '+996-312-62-16-37',
    email: 'info@invest.gov.kg',
    website: 'www.invest.gov.kg',
    description: '키르기스스탄 투자진흥청',
    featured: false
  },
  {
    id: 43,
    country: '타지키스탄',
    organizationName: 'State Committee on Investment',
    city: '두샨베',
    latitude: 38.5598,
    longitude: 68.7870,
    address: 'Rudaki Avenue 37, Dushanbe',
    phone: '+992-37-221-2411',
    email: 'info@investment.tj',
    website: 'www.investment.tj',
    description: '타지키스탄 국가투자위원회',
    featured: false
  },
  {
    id: 44,
    country: '투르크메니스탄',
    organizationName: 'State Agency for Foreign Investment',
    city: '아시가바트',
    latitude: 37.9601,
    longitude: 58.3261,
    address: 'Bitarap Turkmenistan Avenue, Ashgabat',
    phone: '+993-12-35-15-15',
    email: 'info@minfin.gov.tm',
    website: 'www.minfin.gov.tm',
    description: '투르크메니스탄 외국인투자청',
    featured: false
  },
  {
    id: 45,
    country: '아제르바이잔',
    organizationName: 'Azerbaijan Investment Company',
    city: '바쿠',
    latitude: 40.4093,
    longitude: 49.8671,
    address: 'Nizami Street 203, Baku',
    phone: '+994-12-493-58-68',
    email: 'info@aic.az',
    website: 'www.aic.az',
    description: '아제르바이잔 투자회사',
    featured: false
  },
  {
    id: 46,
    country: '아르메니아',
    organizationName: 'InvestInArmenia',
    city: '예레반',
    latitude: 40.1792,
    longitude: 44.4991,
    address: 'Vazgen Sargsyan Street 5, Yerevan',
    phone: '+374-10-54-69-48',
    email: 'info@investinarmenia.am',
    website: 'www.investinarmenia.am',
    description: '아르메니아 투자진흥청',
    featured: false
  },
  {
    id: 47,
    country: '조지아',
    organizationName: 'Invest in Georgia',
    city: '트빌리시',
    latitude: 41.7151,
    longitude: 44.8271,
    address: 'Rustaveli Avenue 12, Tbilisi',
    phone: '+995-32-200-20-09',
    email: 'info@investingeorgia.org',
    website: 'www.investingeorgia.org',
    description: '조지아 투자진흥청',
    featured: false
  },
  {
    id: 48,
    country: '이란',
    organizationName: 'Organization for Investment',
    city: '테헤란',
    latitude: 35.6892,
    longitude: 51.3890,
    address: 'Taleghani Street, Tehran',
    phone: '+98-21-8831-5001',
    email: 'info@oietai.ir',
    website: 'www.oietai.ir',
    description: '이란 투자진흥기구',
    featured: false
  },
  {
    id: 49,
    country: '이라크',
    organizationName: 'National Investment Commission',
    city: '바그다드',
    latitude: 33.3152,
    longitude: 44.3661,
    address: 'International Zone, Baghdad',
    phone: '+964-1-537-8417',
    email: 'info@investpromo.gov.iq',
    website: 'www.investpromo.gov.iq',
    description: '이라크 국가투자위원회',
    featured: false
  },
  {
    id: 50,
    country: '쿠웨이트',
    organizationName: 'Kuwait Direct Investment Promotion Authority',
    city: '쿠웨이트시티',
    latitude: 29.3759,
    longitude: 47.9774,
    address: 'Abdullah Al Salem Street, Kuwait City',
    phone: '+965-2245-6555',
    email: 'info@kdipa.gov.kw',
    website: 'www.kdipa.gov.kw',
    description: '쿠웨이트 직접투자진흥청',
    featured: false
  },
  {
    id: 51,
    country: '바레인',
    organizationName: 'Bahrain Economic Development Board',
    city: '마나마',
    latitude: 26.2285,
    longitude: 50.5860,
    address: 'Seef District, Manama',
    phone: '+973-1758-9999',
    email: 'info@bahrainedb.com',
    website: 'www.bahrainedb.com',
    description: '바레인 경제개발위원회',
    featured: false
  },
  {
    id: 52,
    country: '카타르',
    organizationName: 'Invest Qatar',
    city: '도하',
    latitude: 25.2760,
    longitude: 51.5200,
    address: 'Qatar Financial Centre, Doha',
    phone: '+974-4495-8888',
    email: 'info@investqatar.qa',
    website: 'www.investqatar.qa',
    description: '카타르 투자진흥청',
    featured: false
  },
  {
    id: 53,
    country: '오만',
    organizationName: 'Oman Investment Authority',
    city: '무스카트',
    latitude: 23.5859,
    longitude: 58.4059,
    address: 'Way 4016, Muscat',
    phone: '+968-2468-2000',
    email: 'info@oia.gov.om',
    website: 'www.oia.gov.om',
    description: '오만 투자청',
    featured: false
  },
  {
    id: 54,
    country: '요단',
    organizationName: 'Jordan Investment Commission',
    city: '암만',
    latitude: 31.9454,
    longitude: 35.9284,
    address: 'Queen Noor Street, Amman',
    phone: '+962-6-560-0330',
    email: 'info@jic.gov.jo',
    website: 'www.jic.gov.jo',
    description: '요단 투자위원회',
    featured: false
  },
  {
    id: 55,
    country: '레바논',
    organizationName: 'IDAL (Investment Development Authority)',
    city: '베이루트',
    latitude: 33.8938,
    longitude: 35.5018,
    address: 'Solidere District, Beirut',
    phone: '+961-1-983-306',
    email: 'invest@idal.com.lb',
    website: 'www.investinlebanon.gov.lb',
    description: '레바논 투자개발청',
    featured: false
  },
  {
    id: 56,
    country: '시리아',
    organizationName: 'Syrian Investment Agency',
    city: '다마스쿠스',
    latitude: 33.5138,
    longitude: 36.2765,
    address: 'Umayyad Square, Damascus',
    phone: '+963-11-373-5750',
    email: 'info@syriainvestment.gov.sy',
    website: 'www.syriainvestment.gov.sy',
    description: '시리아 투자청',
    featured: false
  },
  {
    id: 57,
    country: '예멘',
    organizationName: 'General Investment Authority',
    city: '사나',
    latitude: 15.3694,
    longitude: 44.1910,
    address: 'Al-Zubairi Street, Sanaa',
    phone: '+967-1-274-219',
    email: 'info@giay.org',
    website: 'www.giay.org',
    description: '예멘 일반투자청',
    featured: false
  },
  {
    id: 58,
    country: '몰디브',
    organizationName: 'Maldives Association of Tourism Industry',
    city: '말레',
    latitude: 4.1755,
    longitude: 73.5093,
    address: 'Marine Drive, Male',
    phone: '+960-330-0294',
    email: 'info@visitmaldives.com',
    website: 'www.visitmaldives.com',
    description: '몰디브 관광산업협회',
    featured: false
  },
  {
    id: 59,
    country: '동티모르',
    organizationName: 'TradeInvest Timor-Leste',
    city: '딜리',
    latitude: -8.5569,
    longitude: 125.5603,
    address: 'Avenida de Portugal, Dili',
    phone: '+670-332-1040',
    email: 'info@tradeinvest.tl',
    website: 'www.tradeinvest.tl',
    description: '동티모르 무역투자청',
    featured: false
  },
  {
    id: 60,
    country: '북한',
    organizationName: 'Committee for the Promotion of International Trade',
    city: '평양',
    latitude: 39.0392,
    longitude: 125.7625,
    address: 'Potong District, Pyongyang',
    phone: '+850-2-381-2345',
    email: 'info@kpit.com.kp',
    website: 'www.kpit.com.kp',
    description: '조선국제무역촉진위원회',
    featured: false
  },

  // 북미 추가 국가들
  {
    id: 61,
    country: '캐나다',
    organizationName: 'Trade Commissioner Service',
    city: '오타와',
    latitude: 45.4215,
    longitude: -75.6972,
    address: '125 Sussex Drive, Ottawa, ON K1A 0G2',
    phone: '+1-613-944-4000',
    email: 'info@international.gc.ca',
    website: 'www.tradecommissioner.gc.ca',
    description: '캐나다 글로벌사업진흥청',
    featured: false
  },
  {
    id: 62,
    country: '멕시코',
    organizationName: 'ProMéxico',
    city: '멕시코시티',
    latitude: 19.4326,
    longitude: -99.1332,
    address: 'Camino a Santa Teresa 1679, Mexico City',
    phone: '+52-55-5447-7000',
    email: 'info@promexico.gob.mx',
    website: 'www.promexico.gob.mx',
    description: '멕시코 투자무역진흥청',
    featured: false
  },

  // 남미 국가들
  {
    id: 63,
    country: '브라질',
    organizationName: 'APEX-Brasil',
    city: '브라질리아',
    latitude: -15.8267,
    longitude: -47.9218,
    address: 'Setor Bancário Norte, Quadra 2, Lote 11, Brasília',
    phone: '+55-61-3426-0202',
    email: 'apex@apexbrasil.com.br',
    website: 'www.apexbrasil.com.br',
    description: '브라질 수출투자진흥청',
    featured: false
  },
  {
    id: 64,
    country: '아르헨티나',
    organizationName: 'Argentine Investment and Trade Promotion Agency',
    city: '부에노스아이레스',
    latitude: -34.6118,
    longitude: -58.3960,
    address: 'Av. Julio A. Roca 651, Buenos Aires',
    phone: '+54-11-4319-8600',
    email: 'info@investinargentina.gov.ar',
    website: 'www.investinargentina.gov.ar',
    description: '아르헨티나 투자무역진흥청',
    featured: false
  },
  {
    id: 65,
    country: '칠레',
    organizationName: 'ProChile',
    city: '산티아고',
    latitude: -33.4489,
    longitude: -70.6693,
    address: 'Teatinos 180, Santiago',
    phone: '+56-2-2827-5100',
    email: 'info@prochile.gob.cl',
    website: 'www.prochile.gob.cl',
    description: '칠레 수출진흥청',
    featured: false
  },
  {
    id: 66,
    country: '콜롬비아',
    organizationName: 'ProColombia',
    city: '보고타',
    latitude: 4.7110,
    longitude: -74.0721,
    address: 'Calle 28 No. 13A-15, Bogotá',
    phone: '+57-1-560-0100',
    email: 'info@procolombia.co',
    website: 'www.procolombia.co',
    description: '콜롬비아 수출투자관광진흥청',
    featured: false
  },
  {
    id: 67,
    country: '페루',
    organizationName: 'PromPerú',
    city: '리마',
    latitude: -12.0464,
    longitude: -77.0428,
    address: 'Calle Uno Oeste No. 50, Lima',
    phone: '+51-1-616-7300',
    email: 'postmaster@promperu.gob.pe',
    website: 'www.promperu.gob.pe',
    description: '페루 수출관광진흥위원회',
    featured: false
  },

  // 중동 국가들
  {
    id: 68,
    country: '아랍에미리트',
    organizationName: 'UAE Ministry of Economy',
    city: '두바이',
    latitude: 25.2048,
    longitude: 55.2708,
    address: 'Dubai World Trade Centre, Dubai',
    phone: '+971-4-362-9922',
    email: 'info@economy.ae',
    website: 'www.economy.ae',
    description: '아랍에미리트 경제부',
    featured: false
  },
  {
    id: 69,
    country: '사우디아라비아',
    organizationName: 'SAGIA (투자청)',
    city: '리야드',
    latitude: 24.7136,
    longitude: 46.6753,
    address: 'King Fahad Road, Riyadh',
    phone: '+966-11-203-5555',
    email: 'info@invest.gov.sa',
    website: 'www.invest.gov.sa',
    description: '사우디아라비아 투자청',
    featured: false
  },
  {
    id: 70,
    country: '이스라엘',
    organizationName: 'IEICI (이스라엘 수출투자센터)',
    city: '텔아비브',
    latitude: 32.0853,
    longitude: 34.7818,
    address: '29 Hamered Street, Tel Aviv',
    phone: '+972-3-514-2888',
    email: 'info@export.gov.il',
    website: 'www.export.gov.il',
    description: '이스라엘 수출투자센터',
    featured: false
  },
  {
    id: 71,
    country: '터키',
    organizationName: 'Investment Office Turkey',
    city: '이스탄불',
    latitude: 41.0082,
    longitude: 28.9784,
    address: 'Kore Şehitleri Caddesi No:17, Istanbul',
    phone: '+90-212-335-0500',
    email: 'info@invest.gov.tr',
    website: 'www.invest.gov.tr',
    description: '터키 투자진흥청',
    featured: false
  },

  // 아프리카 국가들
  {
    id: 72,
    country: '남아프리카공화국',
    organizationName: 'InvestSA',
    city: '케이프타운',
    latitude: -33.9249,
    longitude: 18.4241,
    address: 'DTI Campus, Pretoria',
    phone: '+27-12-394-9500',
    email: 'info@investsa.gov.za',
    website: 'www.investsa.gov.za',
    description: '남아프리카공화국 투자진흥청',
    featured: false
  },
  {
    id: 73,
    country: '이집트',
    organizationName: 'GAFI (이집트 투자청)',
    city: '카이로',
    latitude: 30.0444,
    longitude: 31.2357,
    address: '3 Salah Salem Road, Cairo',
    phone: '+20-2-2405-9316',
    email: 'info@gafi.gov.eg',
    website: 'www.gafi.gov.eg',
    description: '이집트 일반투자청',
    featured: false
  },
  {
    id: 74,
    country: '나이지리아',
    organizationName: 'NIPC (나이지리아 투자진흥위원회)',
    city: '아부자',
    latitude: 9.0765,
    longitude: 7.3986,
    address: 'Plot 1181A Aguiyi Ironsi Street, Abuja',
    phone: '+234-9-461-3000',
    email: 'info@nipc.gov.ng',
    website: 'www.nipc.gov.ng',
    description: '나이지리아 투자진흥위원회',
    featured: false
  },


  // 기타 유럽 국가들
  {
    id: 75,
    country: '러시아',
    organizationName: 'Russian Export Center',
    city: '모스크바',
    latitude: 55.7558,
    longitude: 37.6173,
    address: 'Krasnopresnenskaya nab., 12, Moscow 123610',
    phone: '+7-495-937-4220',
    email: 'info@exportcenter.ru',
    website: 'www.exportcenter.ru',
    description: '러시아 수출지원센터',
    featured: false
  },
  {
    id: 76,
    country: '체코',
    organizationName: 'CzechInvest',
    city: '프라하',
    latitude: 50.0755,
    longitude: 14.4378,
    address: 'Štěpánská 15, 120 00 Prague',
    phone: '+420-296-342-500',
    email: 'info@czechinvest.org',
    website: 'www.czechinvest.org',
    description: '체코 투자진흥청',
    featured: false
  },
  {
    id: 77,
    country: '헝가리',
    organizationName: 'HIPA (헝가리 투자진흥청)',
    city: '부다페스트',
    latitude: 47.4979,
    longitude: 19.0402,
    address: 'Bank Center, Budapest',
    phone: '+36-1-872-9700',
    email: 'info@hipa.hu',
    website: 'www.hipa.hu',
    description: '헝가리 투자진흥청',
    featured: false
  },

  // 오세아니아 추가 국가들
  {
    id: 78,
    country: '뉴질랜드',
    organizationName: 'New Zealand Trade and Enterprise',
    city: '오클랜드',
    latitude: -36.8485,
    longitude: 174.7633,
    address: 'Level 15, The Zurich Building, Auckland',
    phone: '+64-9-816-8100',
    email: 'info@nzte.govt.nz',
    website: 'www.nzte.govt.nz',
    description: '뉴질랜드 무역기업청',
    featured: false
  },

  // 추가 유럽 국가들
  {
    id: 96,
    country: '스위스',
    organizationName: 'Switzerland Global Enterprise',
    city: '취리히',
    latitude: 47.3769,
    longitude: 8.5417,
    address: 'Stampfenbachstrasse 85, Zurich',
    phone: '+41-44-365-5151',
    email: 'info@s-ge.com',
    website: 'www.s-ge.com',
    description: '스위스 글로벌 엔터프라이즈',
    featured: false
  },
  {
    id: 97,
    country: '오스트리아',
    organizationName: 'Austrian Business Agency',
    city: '비엔나',
    latitude: 48.2082,
    longitude: 16.3738,
    address: 'Opernring 3, Vienna',
    phone: '+43-1-588-58-0',
    email: 'office@aba.gv.at',
    website: 'www.investinaustria.at',
    description: '오스트리아 비즈니스 에이전시',
    featured: false
  },
  {
    id: 98,
    country: '벨기에',
    organizationName: 'Flanders Investment & Trade',
    city: '브뤼셀',
    latitude: 50.8503,
    longitude: 4.3517,
    address: 'Koning Albert II-laan 37, Brussels',
    phone: '+32-2-504-8711',
    email: 'info@flandersinvestmentandtrade.com',
    website: 'www.flandersinvestmentandtrade.com',
    description: '플랑드르 투자무역청',
    featured: false
  },
  {
    id: 99,
    country: '덴마크',
    organizationName: 'Invest in Denmark',
    city: '코펜하겐',
    latitude: 55.6761,
    longitude: 12.5683,
    address: 'Kongens Nytorv 26, Copenhagen',
    phone: '+45-33-92-70-00',
    email: 'invest@investindk.dk',
    website: 'www.investindk.com',
    description: '덴마크 투자청',
    featured: false
  },
  {
    id: 100,
    country: '핀란드',
    organizationName: 'Business Finland',
    city: '헬싱키',
    latitude: 60.1699,
    longitude: 24.9384,
    address: 'Porkkalankatu 1, Helsinki',
    phone: '+358-29-505-5000',
    email: 'info@businessfinland.fi',
    website: 'www.businessfinland.fi',
    description: '비즈니스 핀란드',
    featured: false
  },
  {
    id: 101,
    country: '아이슬란드',
    organizationName: 'Promote Iceland',
    city: '레이캬비크',
    latitude: 64.1466,
    longitude: -21.9426,
    address: 'Borgartún 35, Reykjavik',
    phone: '+354-511-4000',
    email: 'info@promoteiceland.is',
    website: 'www.promoteiceland.is',
    description: '아이슬란드 진흥청',
    featured: false
  },
  {
    id: 102,
    country: '노르웨이',
    organizationName: 'Innovation Norway',
    city: '오슬로',
    latitude: 59.9139,
    longitude: 10.7522,
    address: 'Akersgata 13, Oslo',
    phone: '+47-22-00-25-00',
    email: 'post@innovasjonnorge.no',
    website: 'www.innovasjonnorge.no',
    description: '이노베이션 노르웨이',
    featured: false
  },
  {
    id: 103,
    country: '포르투갈',
    organizationName: 'AICEP Portugal Global',
    city: '리스본',
    latitude: 38.7223,
    longitude: -9.1393,
    address: 'Avenida 5 de Outubro 101, Lisbon',
    phone: '+351-217-909-500',
    email: 'aicep@portugalglobal.pt',
    website: 'www.portugalglobal.pt',
    description: '포르투갈 글로벌 투자진흥청',
    featured: false
  },
  {
    id: 104,
    country: '체코',
    organizationName: 'CzechInvest',
    city: '프라하',
    latitude: 50.0755,
    longitude: 14.4378,
    address: 'Štěpánská 15, Prague',
    phone: '+420-296-342-500',
    email: 'info@czechinvest.org',
    website: 'www.czechinvest.org',
    description: '체코 투자진흥청',
    featured: false
  },
  {
    id: 105,
    country: '헝가리',
    organizationName: 'Hungarian Investment and Trade Agency',
    city: '부다페스트',
    latitude: 47.4979,
    longitude: 19.0402,
    address: 'Lendvay utca 22, Budapest',
    phone: '+36-1-872-6700',
    email: 'info@hipa.hu',
    website: 'www.hipa.hu',
    description: '헝가리 투자무역청',
    featured: false
  },
  {
    id: 106,
    country: '슬로바키아',
    organizationName: 'Slovak Investment and Trade Development Agency',
    city: '브라티슬라바',
    latitude: 48.1486,
    longitude: 17.1077,
    address: 'Mlynské nivy 44, Bratislava',
    phone: '+421-2-5822-1000',
    email: 'sario@sario.sk',
    website: 'www.sario.sk',
    description: '슬로바키아 투자무역개발청',
    featured: false
  },
  {
    id: 107,
    country: '슬로베니아',
    organizationName: 'SPIRIT Slovenia',
    city: '류블랴나',
    latitude: 46.0569,
    longitude: 14.5058,
    address: 'Dunajska cesta 156, Ljubljana',
    phone: '+386-1-589-1870',
    email: 'info@spiritslovenia.si',
    website: 'www.spiritslovenia.si',
    description: '스피리트 슬로베니아',
    featured: false
  },
  {
    id: 108,
    country: '크로아티아',
    organizationName: 'Croatian Investment Promotion Agency',
    city: '자그레브',
    latitude: 45.8150,
    longitude: 15.9819,
    address: 'Prilaz Gjure Deželića 7, Zagreb',
    phone: '+385-1-4569-946',
    email: 'info@investcroatia.hr',
    website: 'www.investcroatia.hr',
    description: '크로아티아 투자진흥청',
    featured: false
  },
  {
    id: 109,
    country: '세르비아',
    organizationName: 'Development Agency of Serbia',
    city: '베오그라드',
    latitude: 44.7866,
    longitude: 20.4489,
    address: 'Makedonska 25, Belgrade',
    phone: '+381-11-3398-350',
    email: 'office@ras.gov.rs',
    website: 'www.ras.gov.rs',
    description: '세르비아 개발청',
    featured: false
  },
  {
    id: 110,
    country: '루마니아',
    organizationName: 'InvestRomania',
    city: '부쿠레슈티',
    latitude: 44.4268,
    longitude: 26.1025,
    address: 'Calea Victoriei 152, Bucharest',
    phone: '+40-21-203-1437',
    email: 'office@investromania.gov.ro',
    website: 'www.investromania.gov.ro',
    description: '루마니아 투자청',
    featured: false
  },
  {
    id: 111,
    country: '불가리아',
    organizationName: 'InvestBulgaria Agency',
    city: '소피아',
    latitude: 42.6977,
    longitude: 23.3219,
    address: '36-38 Dragan Tsankov Blvd, Sofia',
    phone: '+359-2-975-3939',
    email: 'iba@investbg.government.bg',
    website: 'www.investbulgaria.com',
    description: '불가리아 투자청',
    featured: false
  },
  {
    id: 112,
    country: '그리스',
    organizationName: 'Enterprise Greece',
    city: '아테네',
    latitude: 37.9755,
    longitude: 23.7348,
    address: 'Panepistimiou 46, Athens',
    phone: '+30-210-335-8301',
    email: 'info@enterprisegreece.gov.gr',
    website: 'www.enterprisegreece.gov.gr',
    description: '엔터프라이즈 그리스',
    featured: false
  },
  {
    id: 113,
    country: '몰타',
    organizationName: 'Malta Enterprise',
    city: '발레타',
    latitude: 35.8989,
    longitude: 14.5146,
    address: 'Industrial Estate, Kordin, Malta',
    phone: '+356-2278-0000',
    email: 'info@maltaenterprise.com',
    website: 'www.maltaenterprise.com',
    description: '몰타 엔터프라이즈',
    featured: false
  },
  {
    id: 114,
    country: '키프로스',
    organizationName: 'Cyprus Investment Promotion Agency',
    city: '니코시아',
    latitude: 35.1856,
    longitude: 33.3823,
    address: '19 Prodromou Street, Nicosia',
    phone: '+357-22-441-188',
    email: 'invest@cipa.org.cy',
    website: 'www.cipa.org.cy',
    description: '키프로스 투자진흥청',
    featured: false
  },
  {
    id: 115,
    country: '에스토니아',
    organizationName: 'Invest in Estonia',
    city: '탈린',
    latitude: 59.4370,
    longitude: 24.7536,
    address: 'Harju maakond, Tallinn',
    phone: '+372-627-9700',
    email: 'info@investinestonia.com',
    website: 'www.investinestonia.com',
    description: '에스토니아 투자청',
    featured: false
  },
  {
    id: 116,
    country: '라트비아',
    organizationName: 'Investment and Development Agency of Latvia',
    city: '리가',
    latitude: 56.9496,
    longitude: 24.1052,
    address: 'Pērses iela 2, Riga',
    phone: '+371-6703-9400',
    email: 'info@liaa.gov.lv',
    website: 'www.liaa.gov.lv',
    description: '라트비아 투자개발청',
    featured: false
  },
  {
    id: 117,
    country: '리투아니아',
    organizationName: 'Invest Lithuania',
    city: '빌뉴스',
    latitude: 54.6872,
    longitude: 25.2797,
    address: 'Konstitucijos pr. 7, Vilnius',
    phone: '+370-5-262-7438',
    email: 'info@investlithuania.com',
    website: 'www.investlithuania.com',
    description: '리투아니아 투자청',
    featured: false
  },
  // 아메리카 대륙 추가 국가들
  {
    id: 118,
    country: '아르헨티나',
    organizationName: 'Argentina Investment and Trade Promotion Agency',
    city: '부에노스아이레스',
    latitude: -34.6118,
    longitude: -58.3960,
    address: 'Avenida Córdoba 950, Buenos Aires',
    phone: '+54-11-4819-7000',
    email: 'info@investinargentina.gov.ar',
    website: 'www.investinargentina.gov.ar',
    description: '아르헨티나 투자무역진흥청',
    featured: false
  },
  {
    id: 119,
    country: '브라질',
    organizationName: 'APEX-Brasil',
    city: '브라질리아',
    latitude: -15.7801,
    longitude: -47.9292,
    address: 'SBN Quadra 2, Brasília',
    phone: '+55-61-3426-0202',
    email: 'apex@apexbrasil.com.br',
    website: 'www.apexbrasil.com.br',
    description: '브라질 수출투자진흥청',
    featured: false
  },
  {
    id: 120,
    country: '콜롬비아',
    organizationName: 'ProColombia',
    city: '보고타',
    latitude: 4.7110,
    longitude: -74.0721,
    address: 'Calle 28 #13A-15, Bogotá',
    phone: '+57-1-560-0100',
    email: 'contacto@procolombia.co',
    website: 'www.procolombia.co',
    description: '프로콜롬비아',
    featured: false
  },
  {
    id: 121,
    country: '페루',
    organizationName: 'ProInversión',
    city: '리마',
    latitude: -12.0464,
    longitude: -77.0428,
    address: 'Av. Enrique Canaval Moreyra 150, Lima',
    phone: '+51-1-200-1200',
    email: 'webmaster@proinversion.gob.pe',
    website: 'www.proinversion.gob.pe',
    description: '페루 민간투자진흥청',
    featured: false
  },
  {
    id: 122,
    country: '에콰도르',
    organizationName: 'ProEcuador',
    city: '키토',
    latitude: -0.1807,
    longitude: -78.4678,
    address: 'Av. Amazonas N39-123, Quito',
    phone: '+593-2-2567-400',
    email: 'info@proecuador.gob.ec',
    website: 'www.proecuador.gob.ec',
    description: '프로에콰도르',
    featured: false
  },
  {
    id: 123,
    country: '우루과이',
    organizationName: 'Uruguay XXI',
    city: '몬테비데오',
    latitude: -34.9011,
    longitude: -56.1645,
    address: 'Rambla 25 de Agosto de 1825, Montevideo',
    phone: '+598-2-1903-2030',
    email: 'info@uruguayxxi.gob.uy',
    website: 'www.uruguayxxi.gob.uy',
    description: '우루과이 XXI',
    featured: false
  },
  {
    id: 124,
    country: '파라과이',
    organizationName: 'REDIEX',
    city: '아순시온',
    latitude: -25.2637,
    longitude: -57.5759,
    address: 'Eligio Ayala 1728, Asunción',
    phone: '+595-21-414-2000',
    email: 'info@rediex.gov.py',
    website: 'www.rediex.gov.py',
    description: '파라과이 수출투자진흥청',
    featured: false
  },
  {
    id: 125,
    country: '볼리비아',
    organizationName: 'CEPROBOL',
    city: '라파스',
    latitude: -16.5000,
    longitude: -68.1500,
    address: 'Av. Mariscal Santa Cruz, La Paz',
    phone: '+591-2-231-0082',
    email: 'info@ceprobol.gov.bo',
    website: 'www.ceprobol.gov.bo',
    description: '볼리비아 수출진흥센터',
    featured: false
  },
  {
    id: 126,
    country: '베네수엘라',
    organizationName: 'CONAPRI',
    city: '카라카스',
    latitude: 10.4806,
    longitude: -66.9036,
    address: 'Torre Banco Lara, Caracas',
    phone: '+58-212-207-8511',
    email: 'info@conapri.org',
    website: 'www.conapri.org',
    description: '베네수엘라 투자진흥위원회',
    featured: false
  },
  {
    id: 127,
    country: '가이아나',
    organizationName: 'Guyana Office for Investment',
    city: '조지타운',
    latitude: 6.8013,
    longitude: -58.1551,
    address: '190 Camp Street, Georgetown',
    phone: '+592-225-0658',
    email: 'goinvest@goinvest.gov.gy',
    website: 'www.goinvest.gov.gy',
    description: '가이아나 투자청',
    featured: false
  },
  {
    id: 128,
    country: '수리남',
    organizationName: 'Investment and Development Corporation Suriname',
    city: '파라마리보',
    latitude: 5.8520,
    longitude: -55.2038,
    address: 'Dr. Sophie Redmondstraat 118, Paramaribo',
    phone: '+597-499-649',
    email: 'info@idcs.sr',
    website: 'www.idcs.sr',
    description: '수리남 투자개발공사',
    featured: false
  },
  {
    id: 129,
    country: '프랑스령 기아나',
    organizationName: 'Guyane Développement',
    city: '카옌',
    latitude: 4.9280,
    longitude: -52.3260,
    address: 'Route de Montabo, Cayenne',
    phone: '+594-594-296-969',
    email: 'contact@guyane-developpement.fr',
    website: 'www.guyane-developpement.fr',
    description: '프랑스령 기아나 개발청',
    featured: false
  },

  // 중미 국가들
  {
    id: 130,
    country: '과테말라',
    organizationName: 'INVEST IN GUATEMALA',
    city: '과테말라시티',
    latitude: 14.6349,
    longitude: -90.5069,
    address: '5a Avenida 5-55, Guatemala City',
    phone: '+502-2422-3600',
    email: 'info@investinguatemala.org',
    website: 'www.investinguatemala.org',
    description: '과테말라 투자진흥청',
    featured: false
  },
  {
    id: 131,
    country: '벨리즈',
    organizationName: 'Belize Trade and Investment Development Service',
    city: '벨모판',
    latitude: 17.2510,
    longitude: -88.7590,
    address: '14 Orchid Garden Street, Belmopan',
    phone: '+501-822-3737',
    email: 'info@belizeinvest.org.bz',
    website: 'www.belizeinvest.org.bz',
    description: '벨리즈 무역투자개발청',
    featured: false
  },
  {
    id: 132,
    country: '엘살바도르',
    organizationName: 'PROESA',
    city: '산살바도르',
    latitude: 13.6929,
    longitude: -89.2182,
    address: 'Edificio World Trade Center, San Salvador',
    phone: '+503-2267-7000',
    email: 'info@proesa.gob.sv',
    website: 'www.proesa.gob.sv',
    description: '엘살바도르 수출투자진흥청',
    featured: false
  },
  {
    id: 133,
    country: '온두라스',
    organizationName: 'Honduras Investment Promotion Agency',
    city: '테구시갈파',
    latitude: 14.0723,
    longitude: -87.1921,
    address: 'Boulevard Morazán, Tegucigalpa',
    phone: '+504-2235-3625',
    email: 'info@hondurasinvest.hn',
    website: 'www.hondurasinvest.hn',
    description: '온두라스 투자진흥청',
    featured: false
  },
  {
    id: 134,
    country: '니카라과',
    organizationName: 'ProNicaragua',
    city: '마나과',
    latitude: 12.1150,
    longitude: -86.2362,
    address: 'Km 4.5 Carretera Masaya, Managua',
    phone: '+505-2278-9080',
    email: 'info@pronicaragua.gob.ni',
    website: 'www.pronicaragua.gob.ni',
    description: '프로니카라과',
    featured: false
  },
  {
    id: 135,
    country: '코스타리카',
    organizationName: 'CINDE',
    city: '산호세',
    latitude: 9.9281,
    longitude: -84.0907,
    address: 'CINDE Building, San José',
    phone: '+506-2299-2800',
    email: 'info@cinde.org',
    website: 'www.cinde.org',
    description: '코스타리카 투자개발연합',
    featured: false
  },
  {
    id: 136,
    country: '파나마',
    organizationName: 'ProPanamá',
    city: '파나마시티',
    latitude: 8.9824,
    longitude: -79.5199,
    address: 'Via Israel, Panama City',
    phone: '+507-526-2600',
    email: 'info@propanama.gob.pa',
    website: 'www.propanama.gob.pa',
    description: '프로파나마',
    featured: false
  },

  // 카리브해 국가들
  {
    id: 137,
    country: '도미니카공화국',
    organizationName: 'ProDominicana',
    city: '산토도밍고',
    latitude: 18.4861,
    longitude: -69.9312,
    address: 'Avenida 27 de Febrero, Santo Domingo',
    phone: '+1-809-530-8121',
    email: 'info@prodominicana.gob.do',
    website: 'www.prodominicana.gob.do',
    description: '도미니카공화국 수출투자센터',
    featured: false
  },
  {
    id: 138,
    country: '아이티',
    organizationName: 'Centre de Facilitation des Investissements',
    city: '포르토프랭스',
    latitude: 18.5944,
    longitude: -72.3074,
    address: 'Boulevard Harry Truman, Port-au-Prince',
    phone: '+509-2229-6000',
    email: 'info@cfi.ht',
    website: 'www.cfi.ht',
    description: '아이티 투자촉진센터',
    featured: false
  },
  {
    id: 139,
    country: '자메이카',
    organizationName: 'JAMPRO',
    city: '킹스턴',
    latitude: 17.9970,
    longitude: -76.7936,
    address: '18 Trafalgar Road, Kingston',
    phone: '+1-876-978-7755',
    email: 'info@jamprocorp.com',
    website: 'www.jamprocorp.com',
    description: '자메이카 무역투자진흥청',
    featured: false
  },
  {
    id: 140,
    country: '쿠바',
    organizationName: 'Zona Especial de Desarrollo Mariel',
    city: '아바나',
    latitude: 23.1136,
    longitude: -82.3666,
    address: 'Zona Especial Mariel, Havana',
    phone: '+53-7-204-2516',
    email: 'info@zedmariel.cu',
    website: 'www.zedmariel.cu',
    description: '쿠바 마리엘특별개발구',
    featured: false
  },
  {
    id: 141,
    country: '바하마',
    organizationName: 'Bahamas Investment Authority',
    city: '나소',
    latitude: 25.0443,
    longitude: -77.3504,
    address: 'UBS Annex Building, Nassau',
    phone: '+1-242-327-5826',
    email: 'bia@bahamas.gov.bs',
    website: 'www.bia.gov.bs',
    description: '바하마 투자청',
    featured: false
  },
  {
    id: 142,
    country: '바베이도스',
    organizationName: 'Invest Barbados',
    city: '브리지타운',
    latitude: 13.1939,
    longitude: -59.5432,
    address: 'Pelican House, Bridgetown',
    phone: '+1-246-626-2000',
    email: 'invest@investbarbados.org',
    website: 'www.investbarbados.org',
    description: '바베이도스 투자청',
    featured: false
  },
  {
    id: 143,
    country: '트리니다드토바고',
    organizationName: 'InvesTT',
    city: '포트오브스페인',
    latitude: 10.6918,
    longitude: -61.2225,
    address: 'Level 1, NESC Building, Port of Spain',
    phone: '+1-868-623-2022',
    email: 'info@investt.co.tt',
    website: 'www.investt.co.tt',
    description: '트리니다드토바고 투자청',
    featured: false
  },

  // 오세아니아 추가 국가들
  {
    id: 144,
    country: '피지',
    organizationName: 'Investment Fiji',
    city: '수바',
    latitude: -18.1248,
    longitude: 178.4501,
    address: 'Level 2, Civic Tower, Suva',
    phone: '+679-331-5988',
    email: 'info@investmentfiji.org.fj',
    website: 'www.investmentfiji.org.fj',
    description: '피지 투자청',
    featured: false
  },
  {
    id: 145,
    country: '바누아투',
    organizationName: 'Vanuatu Investment Promotion Authority',
    city: '포트빌라',
    latitude: -17.7404,
    longitude: 168.3186,
    address: 'PMB 9051, Port Vila',
    phone: '+678-29842',
    email: 'info@vipa.vu',
    website: 'www.vipa.vu',
    description: '바누아투 투자진흥청',
    featured: false
  },
  {
    id: 146,
    country: '파푸아뉴기니',
    organizationName: 'PNG Investment Promotion Authority',
    city: '포트모르즈비',
    latitude: -9.4438,
    longitude: 147.1803,
    address: 'Level 1, FTZL Building, Port Moresby',
    phone: '+675-308-4400',
    email: 'info@ipa.gov.pg',
    website: 'www.ipa.gov.pg',
    description: '파푸아뉴기니 투자진흥청',
    featured: false
  },
  {
    id: 147,
    country: '솔로몬제도',
    organizationName: 'Solomon Islands Investment Corporation',
    city: '호니아라',
    latitude: -9.4280,
    longitude: 159.9729,
    address: 'Investment House, Honiara',
    phone: '+677-21839',
    email: 'info@siic.com.sb',
    website: 'www.siic.com.sb',
    description: '솔로몬제도 투자공사',
    featured: false
  },
  {
    id: 148,
    country: '사모아',
    organizationName: 'Samoa Investment Corporation',
    city: '아피아',
    latitude: -13.8333,
    longitude: -171.7667,
    address: 'Level 6, SNPF Plaza, Apia',
    phone: '+685-21405',
    email: 'info@sic.ws',
    website: 'www.sic.ws',
    description: '사모아 투자공사',
    featured: false
  },
  {
    id: 149,
    country: '통가',
    organizationName: 'Tonga Development Bank',
    city: '누쿠알로파',
    latitude: -21.1789,
    longitude: -175.1982,
    address: 'Salote Road, Nuku\'alofa',
    phone: '+676-24-051',
    email: 'info@tdb.to',
    website: 'www.tdb.to',
    description: '통가 개발은행',
    featured: false
  },
  {
    id: 150,
    country: '키리바시',
    organizationName: 'Kiribati Investment Corporation',
    city: '타라와',
    latitude: 1.4518,
    longitude: 172.9717,
    address: 'Bairiki, Tarawa',
    phone: '+686-21092',
    email: 'info@kic.ki',
    website: 'www.kic.ki',
    description: '키리바시 투자공사',
    featured: false
  },
  {
    id: 151,
    country: '투발루',
    organizationName: 'Tuvalu Investment Office',
    city: '푸나푸티',
    latitude: -8.5167,
    longitude: 179.2167,
    address: 'Government Building, Funafuti',
    phone: '+688-20100',
    email: 'info@tuvaluinvest.tv',
    website: 'www.tuvaluinvest.tv',
    description: '투발루 투자청',
    featured: false
  },
  {
    id: 152,
    country: '나우루',
    organizationName: 'Nauru Investment Corporation',
    city: '야렌',
    latitude: -0.5477,
    longitude: 166.9209,
    address: 'Government Offices, Yaren',
    phone: '+674-444-3333',
    email: 'info@nic.nr',
    website: 'www.nic.nr',
    description: '나우루 투자공사',
    featured: false
  },
  {
    id: 153,
    country: '팔라우',
    organizationName: 'Palau Investment Development Bank',
    city: '코로르',
    latitude: 7.3439,
    longitude: 134.4733,
    address: 'PIDB Building, Koror',
    phone: '+680-488-2772',
    email: 'info@pidb.pw',
    website: 'www.pidb.pw',
    description: '팔라우 투자개발은행',
    featured: false
  },
  {
    id: 154,
    country: '마셜제도',
    organizationName: 'Marshall Islands Development Bank',
    city: '마주로',
    latitude: 7.1315,
    longitude: 171.1845,
    address: 'MIDB Building, Majuro',
    phone: '+692-625-3636',
    email: 'info@midb.org',
    website: 'www.midb.org',
    description: '마셜제도 개발은행',
    featured: false
  },
  {
    id: 155,
    country: '미크로네시아',
    organizationName: 'FSM Development Bank',
    city: '팔리키르',
    latitude: 6.9248,
    longitude: 158.1610,
    address: 'P.O. Box PS-38, Palikir',
    phone: '+691-320-2480',
    email: 'info@fsmdb.fm',
    website: 'www.fsmdb.fm',
    description: '미크로네시아 개발은행',
    featured: false
  },

  // 유럽 추가 국가들
  {
    id: 156,
    country: '안도라',
    organizationName: 'ACTUA',
    city: '안도라라베야',
    latitude: 42.5063,
    longitude: 1.5218,
    address: 'Carrer Prat de la Creu 62-64, Andorra la Vella',
    phone: '+376-873-100',
    email: 'info@actua.ad',
    website: 'www.actua.ad',
    description: '안도라 기업진흥청',
    featured: false
  },
  {
    id: 157,
    country: '모나코',
    organizationName: 'Monaco Economic Board',
    city: '모나코',
    latitude: 43.7384,
    longitude: 7.4246,
    address: '20 Avenue de Fontvieille, Monaco',
    phone: '+377-92-05-73-73',
    email: 'info@monacoeconomicboard.mc',
    website: 'www.monacoeconomicboard.mc',
    description: '모나코 경제위원회',
    featured: false
  },
  {
    id: 158,
    country: '산마리노',
    organizationName: 'San Marino Development Agency',
    city: '산마리노',
    latitude: 43.9424,
    longitude: 12.4578,
    address: 'Via 28 Luglio 199, San Marino',
    phone: '+378-0549-882-328',
    email: 'info@aass.sm',
    website: 'www.aass.sm',
    description: '산마리노 개발청',
    featured: false
  },
  {
    id: 159,
    country: '바티칸',
    organizationName: 'Vatican Investment Office',
    city: '바티칸',
    latitude: 41.9029,
    longitude: 12.4534,
    address: 'Vatican City State',
    phone: '+39-06-6982',
    email: 'info@vatican.va',
    website: 'www.vatican.va',
    description: '바티칸 투자청',
    featured: false
  },
  {
    id: 160,
    country: '리히텐슈타인',
    organizationName: 'Liechtenstein Development Service',
    city: '파두츠',
    latitude: 47.1410,
    longitude: 9.5209,
    address: 'Äulestrasse 30, Vaduz',
    phone: '+423-236-6863',
    email: 'info@lds.li',
    website: 'www.lds.li',
    description: '리히텐슈타인 개발청',
    featured: false
  },
  {
    id: 161,
    country: '알바니아',
    organizationName: 'Albanian Investment Development Agency',
    city: '티라나',
    latitude: 41.3275,
    longitude: 19.8187,
    address: 'Bulevardi Deshmoret e Kombit, Tirana',
    phone: '+355-4-2275-778',
    email: 'info@aida.gov.al',
    website: 'www.aida.gov.al',
    description: '알바니아 투자개발청',
    featured: false
  },
  {
    id: 162,
    country: '북마케도니아',
    organizationName: 'Invest North Macedonia',
    city: '스코페',
    latitude: 41.9973,
    longitude: 21.4280,
    address: 'Bul. Goce Delchev 18, Skopje',
    phone: '+389-2-3093-726',
    email: 'info@investnorthmacedonia.gov.mk',
    website: 'www.investnorthmacedonia.gov.mk',
    description: '북마케도니아 투자청',
    featured: false
  },
  {
    id: 163,
    country: '몬테네그로',
    organizationName: 'Montenegrin Investment Promotion Agency',
    city: '포드고리차',
    latitude: 42.4304,
    longitude: 19.2594,
    address: 'Rimski trg 46, Podgorica',
    phone: '+382-20-482-211',
    email: 'info@mipa.co.me',
    website: 'www.mipa.co.me',
    description: '몬테네그로 투자진흥청',
    featured: false
  },
  {
    id: 164,
    country: '보스니아헤르체고비나',
    organizationName: 'Foreign Investment Promotion Agency',
    city: '사라예보',
    latitude: 43.8563,
    longitude: 18.4131,
    address: 'Branilaca Sarajeva 21, Sarajevo',
    phone: '+387-33-278-080',
    email: 'fipa@fipa.gov.ba',
    website: 'www.fipa.gov.ba',
    description: '보스니아헤르체고비나 외국인투자진흥청',
    featured: false
  },
  {
    id: 165,
    country: '코소보',
    organizationName: 'Kosovo Investment and Enterprise Support Agency',
    city: '프리슈티나',
    latitude: 42.6629,
    longitude: 21.1655,
    address: 'Zona Industriale, Pristina',
    phone: '+383-38-609-013',
    email: 'info@kiesa-ks.org',
    website: 'www.kiesa-ks.org',
    description: '코소보 투자기업지원청',
    featured: false
  },
  {
    id: 166,
    country: '몰도바',
    organizationName: 'Moldova Investment and Export Promotion Organization',
    city: '키시나우',
    latitude: 47.0105,
    longitude: 28.8638,
    address: 'Bd. Ștefan cel Mare 134, Chișinău',
    phone: '+373-22-221-425',
    email: 'info@miepo.md',
    website: 'www.miepo.md',
    description: '몰도바 투자수출진흥기구',
    featured: false
  },
  {
    id: 167,
    country: '우크라이나',
    organizationName: 'UkraineInvest',
    city: '키예프',
    latitude: 50.4501,
    longitude: 30.5234,
    address: '12/2 Arsenalna Str., Kyiv',
    phone: '+380-44-253-9570',
    email: 'info@ukraineinvest.gov.ua',
    website: 'www.ukraineinvest.gov.ua',
    description: '우크라이나 투자청',
    featured: false
  },
  {
    id: 168,
    country: '벨라루스',
    organizationName: 'National Investment and Privatization Agency',
    city: '민스크',
    latitude: 53.9045,
    longitude: 27.5615,
    address: 'Moskvina Str. 38, Minsk',
    phone: '+375-17-222-0517',
    email: 'info@nipa.by',
    website: 'www.nipa.by',
    description: '벨라루스 국가투자민영화청',
    featured: false
  }
];

interface TradeAgency {
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

function App() {
  const [selectedAgency, setSelectedAgency] = useState<TradeAgency | null>(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [showAllCountries, setShowAllCountries] = useState(false);



  const featuredAgencies = allTradePromotionAgencies.filter(agency => agency.featured);
  const aseanAgencies = allTradePromotionAgencies.filter(agency => agency.region === 'ASEAN');

  const filteredAgencies = useMemo(() => {
    if (!searchTerm) return allTradePromotionAgencies;
    
    return allTradePromotionAgencies.filter(agency =>
      agency.country.toLowerCase().includes(searchTerm.toLowerCase()) ||
      agency.organizationName.toLowerCase().includes(searchTerm.toLowerCase()) ||
      agency.city.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }, [searchTerm]);

  const clearSearch = () => {
    setSearchTerm('');
    setShowAllCountries(false);
  };

  const generateEmailTemplate = (agency: TradeAgency) => {
    const subject = `Partnership Inquiry - Korean OCR Technology Solutions`;
    const body = `Dear ${agency.organizationName} Team,

I hope this email finds you well. I am writing to introduce our company and explore potential collaboration opportunities in ${agency.country}.

Our Company:
- Korean technology company specializing in OCR (Optical Character Recognition) solutions
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

We would greatly appreciate the opportunity to discuss how our technology can support ${agency.country}'s digital transformation initiatives.

Thank you for your time and consideration. I look forward to your response.

Best regards,
[Your Name]
[Your Title]
[Company Name]
[Contact Information]

---
Generated via KOTRA Global Trade Network Platform`;

    return { subject, body };
  };

  const handleEmailTemplate = (agency: TradeAgency) => {
    const { subject, body } = generateEmailTemplate(agency);
    const mailtoLink = `mailto:${agency.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    window.open(mailtoLink, '_blank');
  };

  return (
    <div className="App">
      <header className="app-header">
        <div className="header-content">
          <div className="logo-section">
            <Globe className="logo-icon" />
            <h1>글로벌 무역진흥기관 네트워크</h1>
          </div>
          <p className="subtitle">전 세계 각국의 무역진흥기관을 클릭하여 연락처 정보를 확인하세요</p>
          
          {/* 검색 기능 */}
          <div className="search-container">
            <div className="search-box">
              <Search className="search-icon" size={20} />
              <input
                type="text"
                placeholder="국가명, 기관명, 도시명으로 검색..."
                value={searchTerm}
                onChange={(e) => {
                  setSearchTerm(e.target.value);
                  setShowAllCountries(true);
                }}
                className="search-input"
              />
              {searchTerm && (
                <button onClick={clearSearch} className="clear-search">
                  <X size={16} />
                </button>
              )}
            </div>
            {!showAllCountries && (
              <div className="filter-buttons">
                <button 
                  className="show-all-btn"
                  onClick={() => setShowAllCountries(true)}
                >
                  전세계 모든 국가 보기 ({allTradePromotionAgencies.length}개국)
                </button>
              </div>
            )}
          </div>
        </div>
      </header>

      <main className="main-content">
        {!showAllCountries && !searchTerm && (
          <div className="asean-map-container">
            <div className="asean-map">
              <h2>ASEAN 수출지원기관 지도</h2>
              <div className="asean-stats">
                <div className="stat-card">
                  <h3>총 회원국</h3>
                  <p className="stat-number">10개국</p>
                </div>
                <div className="stat-card">
                  <h3>총 인구</h3>
                  <p className="stat-number">6.6억명</p>
                </div>
                <div className="stat-card">
                  <h3>GDP 규모</h3>
                  <p className="stat-number">3.7조 달러</p>
                </div>
              </div>
              <div className="asean-countries-grid">
                {aseanAgencies.map((agency) => (
                  <div 
                    key={agency.id}
                    className="asean-country-marker"
                    onClick={() => setSelectedAgency(agency)}
                  >
                    <Building2 size={18} />
                    <span>{agency.country}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
        


        {selectedAgency && (
          <div className="selected-office-info">
            <div className="office-details">
              <h3>{selectedAgency.country} - {selectedAgency.organizationName}</h3>
              <p className="description">{selectedAgency.description}</p>
              <div className="office-info">
                <p><MapPin size={16} /> {selectedAgency.address}</p>
                <p>📞 <a href={`tel:${selectedAgency.phone}`}>{selectedAgency.phone}</a></p>
                <p>✉️ <a href={`mailto:${selectedAgency.email}`}>{selectedAgency.email}</a></p>
                <p>🌐 <a href={`https://${selectedAgency.website}`} target="_blank" rel="noopener noreferrer">{selectedAgency.website}</a></p>
              </div>
              <button 
                className="close-btn"
                onClick={() => setSelectedAgency(null)}
              >
                닫기
              </button>
            </div>
          </div>
        )}

        {(searchTerm || showAllCountries) && (
          <div className="office-list">
            <div className="office-list-header">
              <h2>
                {searchTerm ? `"${searchTerm}" 검색 결과 (${filteredAgencies.length}개)` :
                 showAllCountries ? `전체 무역진흥기관 목록 (${allTradePromotionAgencies.length}개국)` :
                 '주요 무역진흥기관 목록'}
              </h2>
              {showAllCountries && (
                <button 
                  className="back-to-home-btn"
                  onClick={() => setShowAllCountries(false)}
                >
                  ← 홈으로
                </button>
              )}
            </div>
            
            {searchTerm && filteredAgencies.length === 0 && (
              <div className="no-results">
                <p>검색 결과가 없습니다. 다른 키워드로 검색해보세요.</p>
              </div>
            )}
            
            <div className="office-grid">
              {(searchTerm ? filteredAgencies : showAllCountries ? allTradePromotionAgencies : featuredAgencies)
                .map((agency) => (
                <div 
                  key={agency.id} 
                  className={`office-card ${selectedAgency?.id === agency.id ? 'selected' : ''}`}
                  data-region={agency.region || ''}
                  onClick={() => setSelectedAgency(agency)}
                >
                  <h3>{agency.country}</h3>
                  <h4>{agency.organizationName}</h4>
                  <p>{agency.city}</p>
                  <p className="office-address">{agency.address}</p>
                  <div className="contact-info">
                    <p>📞 {agency.phone}</p>
                    <p>✉️ {agency.email}</p>
                    {agency.region === 'ASEAN' && (
                      <button 
                        className="email-template-btn"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleEmailTemplate(agency);
                        }}
                      >
                        📧 수출문의 이메일 작성
                      </button>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
