import { Agency } from '../data/agencies';

// API 설정
const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://api.globaltrade.com';
const API_KEY = process.env.REACT_APP_API_KEY;

// API 응답 타입
interface ApiResponse<T> {
  success: boolean;
  data: T;
  message?: string;
}

// API 서비스 클래스
export class ApiService {
  private static headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${API_KEY}`,
  };

  // 모든 수출지원기관 조회
  static async getAllAgencies(): Promise<Agency[]> {
    try {
      const response = await fetch(`${API_BASE_URL}/agencies`, {
        headers: this.headers,
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const result: ApiResponse<Agency[]> = await response.json();
      return result.data;
    } catch (error) {
      console.error('Failed to fetch agencies:', error);
      // 실패 시 로컬 데이터 반환
      return this.getFallbackData();
    }
  }

  // 국가별 기관 검색
  static async getAgenciesByCountry(country: string): Promise<Agency[]> {
    try {
      const response = await fetch(
        `${API_BASE_URL}/agencies/search?country=${encodeURIComponent(country)}`,
        { headers: this.headers }
      );
      
      const result: ApiResponse<Agency[]> = await response.json();
      return result.data;
    } catch (error) {
      console.error('Failed to search agencies:', error);
      return [];
    }
  }

  // 실시간 기관 정보 업데이트
  static async updateAgencyInfo(agencyId: number): Promise<Agency | null> {
    try {
      const response = await fetch(`${API_BASE_URL}/agencies/${agencyId}/refresh`, {
        method: 'POST',
        headers: this.headers,
      });
      
      const result: ApiResponse<Agency> = await response.json();
      return result.data;
    } catch (error) {
      console.error('Failed to update agency info:', error);
      return null;
    }
  }

  // KOTRA 공식 API 연동 (예시)
  static async getKotraOffices(): Promise<Agency[]> {
    try {
      // 실제 KOTRA API 엔드포인트 (가상)
      const response = await fetch(
        'https://api.kotra.or.kr/v1/offices?apikey=' + process.env.REACT_APP_KOTRA_API_KEY
      );
      
      const kotraData = await response.json();
      
      // KOTRA 데이터를 우리 형식으로 변환
      return kotraData.offices.map((office: any) => ({
        id: office.id,
        country: office.country_name,
        countryCode: office.country_code,
        agencyName: `KOTRA ${office.city}`,
        email: office.email,
        phone: office.phone,
        website: office.website,
        address: office.address,
        lat: office.latitude,
        lng: office.longitude,
        description: `KOTRA ${office.city} 지사`
      }));
    } catch (error) {
      console.error('Failed to fetch KOTRA data:', error);
      return [];
    }
  }

  // 각국 무역진흥기관 정보 수집 (웹 스크래핑 결과)
  static async getTradePromotionAgencies(): Promise<Agency[]> {
    try {
      // 자체 구축한 스크래핑 API
      const response = await fetch(`${API_BASE_URL}/scraping/trade-agencies`, {
        headers: this.headers,
      });
      
      const result: ApiResponse<Agency[]> = await response.json();
      return result.data;
    } catch (error) {
      console.error('Failed to fetch trade agencies:', error);
      return [];
    }
  }

  // 실시간 환율 정보 (추가 기능)
  static async getExchangeRates(): Promise<any> {
    try {
      const response = await fetch(
        'https://api.exchangerate-api.com/v4/latest/KRW'
      );
      return response.json();
    } catch (error) {
      console.error('Failed to fetch exchange rates:', error);
      return null;
    }
  }

  // 무역 통계 정보 (추가 기능)
  static async getTradeStatistics(country: string): Promise<any> {
    try {
      // 한국무역협회 API 또는 관세청 API 연동
      const response = await fetch(
        `https://api.kita.net/trade-stats?country=${country}&apikey=${process.env.REACT_APP_KITA_API_KEY}`
      );
      return response.json();
    } catch (error) {
      console.error('Failed to fetch trade statistics:', error);
      return null;
    }
  }

  // 폴백 데이터 (API 실패 시)
  private static getFallbackData(): Agency[] {
    // 현재 정적 데이터 반환
    return require('../data/agencies').agencies;
  }
}

// 실시간 데이터 동기화 훅
export const useRealtimeAgencies = () => {
  const [agencies, setAgencies] = React.useState<Agency[]>([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<string | null>(null);

  React.useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const data = await ApiService.getAllAgencies();
        setAgencies(data);
        setError(null);
      } catch (err) {
        setError('데이터를 불러오는데 실패했습니다.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();

    // 5분마다 데이터 갱신
    const interval = setInterval(fetchData, 5 * 60 * 1000);
    return () => clearInterval(interval);
  }, []);

  return { agencies, loading, error };
}; 