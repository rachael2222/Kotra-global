import React from 'react';
import { Agency } from '../data/agencies';
import { Mail, Phone, Globe, Building, MapPin, Send } from 'lucide-react';
import Modal from './Modal';

interface AgencyInfoProps {
  agency: Agency | null;
  onClose: () => void;
}

const AgencyInfo: React.FC<AgencyInfoProps> = ({ agency, onClose }) => {
  if (!agency) return null;

  // 지역별 국가 분류
  const regions = {
    asia: ['싱가포르', '말레이시아', '인도네시아', '태국', '베트남', '필리핀', '캄보디아', '미얀마', '브루나이', '라오스', '몽골', '홍콩', '대만', '일본', '중국', '인도', '파키스탄', '방글라데시', '스리랑카', '네팔', '부탄', '아프가니스탄'],
    europe: ['독일', '영국', '프랑스', '이탈리아', '스페인', '네덜란드', '스위스', '스웨덴', '노르웨이', '덴마크', '핀란드', '오스트리아', '벨기에', '폴란드', '체코', '헝가리', '슬로바키아', '슬로베니아', '크로아티아', '세르비아', '루마니아', '불가리아', '그리스', '몰타', '키프로스', '에스토니아', '라트비아', '리투아니아'],
    northAmerica: ['미국', '캐나다', '멕시코'],
    southAmerica: ['브라질', '아르헨티나', '칠레', '콜롬비아', '페루', '우루과이', '파라과이', '볼리비아', '에콰도르', '베네수엘라'],
    africa: ['남아프리카공화국', '이집트', '나이지리아', '케냐', '모로코', '튀니지', '알제리', '가나', '우간다', '탄자니아', '에티오피아'],
    middleEast: ['아랍에미리트', '사우디아라비아', '이스라엘', '터키', '이란', '이라크', '쿠웨이트', '바레인', '카타르', '오만', '요르단', '레바논', '시리아', '예멘'],
    centralAsia: ['러시아', '우즈베키스탄', '카자흐스탄', '키르기스스탄', '타지키스탄', '투르크메니스탄', '아제르바이잔', '아르메니아', '조지아'],
    oceania: ['호주', '뉴질랜드']
  };

  // 국가의 지역 확인
  const getRegion = (country: string) => {
    for (const [region, countries] of Object.entries(regions)) {
      if (countries.includes(country)) {
        return region;
      }
    }
    return 'global';
  };

  const region = getRegion(agency.country);

  // 지역별 이메일 템플릿 생성
  const generateEmailTemplate = () => {
    const subject = encodeURIComponent(`[수출 문의] ${agency.country} 시장 진출 관련 상담 요청`);
    
    let body = '';
    
    switch (region) {
      case 'asia':
        body = `안녕하세요, ${agency.agencyName} 담당자님,

저는 한국의 [회사명]에서 근무하고 있는 [이름]입니다.

${agency.country} 시장 진출을 고려하고 있어서, ${agency.agencyName}의 지원 서비스에 대해 문의드립니다.

주요 문의사항:
1. ${agency.country} 시장 진출을 위한 지원 프로그램
2. 현지 파트너사 연결 서비스
3. 시장 조사 및 컨설팅 서비스
4. 투자 관련 정보 및 절차
5. 현지 법규 및 규제 정보

추가로 궁금한 점:
- 지원 서비스 이용 절차
- 필요한 서류 및 준비사항
- 서비스 이용 비용
- 예상 소요 기간
- 현지 문화 및 비즈니스 관습

연락 가능한 시간: [연락 가능 시간]
연락처: [전화번호]

상세한 상담을 위해 회신 부탁드립니다.

감사합니다.

[이름]
[회사명]
[직책]
[연락처]`;
        break;

      case 'europe':
        body = `Dear ${agency.agencyName} Team,

I am [Name] from [Company Name] in South Korea.

We are considering expanding our business to ${agency.country} and would like to inquire about the support services provided by ${agency.agencyName}.

Main inquiries:
1. Market entry support programs for ${agency.country}
2. Local partner connection services
3. Market research and consulting services
4. Investment information and procedures
5. EU regulations and compliance (if applicable)

Additional questions:
- Service application procedures
- Required documents and preparations
- Service costs
- Expected processing time
- Local business culture and practices

Available contact time: [Available time]
Contact: [Phone number]

We look forward to your response for detailed consultation.

Best regards,

[Name]
[Company Name]
[Position]
[Contact]`;
        break;

      case 'northAmerica':
        body = `Dear ${agency.agencyName} Team,

I am [Name] from [Company Name] in South Korea.

We are interested in expanding our business to ${agency.country} and would like to learn more about the support services offered by ${agency.agencyName}.

Key inquiries:
1. Market entry support programs for ${agency.country}
2. Local partner network services
3. Market research and consulting services
4. Investment facilitation and procedures
5. Regulatory compliance information

Additional questions:
- Service application process
- Required documentation
- Service fees and costs
- Expected timeline
- Local market insights

Available for contact: [Available time]
Phone: [Phone number]

We would appreciate your response for detailed consultation.

Thank you.

[Name]
[Company Name]
[Position]
[Contact]`;
        break;

      case 'southAmerica':
        body = `Estimado equipo de ${agency.agencyName},

Soy [Nombre] de [Nombre de la empresa] en Corea del Sur.

Estamos considerando expandir nuestro negocio a ${agency.country} y nos gustaría consultar sobre los servicios de apoyo proporcionados por ${agency.agencyName}.

Consultas principales:
1. Programas de apoyo para entrada al mercado de ${agency.country}
2. Servicios de conexión con socios locales
3. Servicios de investigación de mercado y consultoría
4. Información y procedimientos de inversión
5. Información sobre regulaciones locales

Preguntas adicionales:
- Procedimientos de aplicación de servicios
- Documentos requeridos y preparaciones
- Costos de servicios
- Tiempo de procesamiento esperado
- Cultura empresarial local

Tiempo disponible para contacto: [Tiempo disponible]
Teléfono: [Número de teléfono]

Esperamos su respuesta para una consulta detallada.

Saludos cordiales,

[Nombre]
[Nombre de la empresa]
[Cargo]
[Contacto]`;
        break;

      case 'africa':
        body = `Dear ${agency.agencyName} Team,

I am [Name] from [Company Name] in South Korea.

We are exploring business opportunities in ${agency.country} and would like to inquire about the support services provided by ${agency.agencyName}.

Main inquiries:
1. Market entry support programs for ${agency.country}
2. Local partner connection services
3. Market research and consulting services
4. Investment information and procedures
5. Local business environment and regulations

Additional questions:
- Service application procedures
- Required documents and preparations
- Service costs and fees
- Expected processing time
- Local business culture and practices

Available contact time: [Available time]
Phone: [Phone number]

We look forward to your response for detailed consultation.

Best regards,

[Name]
[Company Name]
[Position]
[Contact]`;
        break;

      case 'middleEast':
        body = `عزيزي فريق ${agency.agencyName}،

أنا [الاسم] من [اسم الشركة] في كوريا الجنوبية.

نحن نفكر في التوسع في أعمالنا إلى ${agency.country} ونود الاستفسار عن خدمات الدعم المقدمة من ${agency.agencyName}.

الاستفسارات الرئيسية:
1. برامج دعم دخول السوق لـ ${agency.country}
2. خدمات ربط الشركاء المحليين
3. خدمات أبحاث السوق والاستشارات
4. معلومات الاستثمار والإجراءات
5. معلومات اللوائح المحلية

أسئلة إضافية:
- إجراءات طلب الخدمة
- المستندات المطلوبة والتحضيرات
- تكاليف الخدمة
- الوقت المتوقع للمعالجة
- ثقافة الأعمال المحلية

الوقت المتاح للاتصال: [الوقت المتاح]
الهاتف: [رقم الهاتف]

نتطلع إلى ردكم للاستشارة التفصيلية.

مع أطيب التحيات،

[الاسم]
[اسم الشركة]
[المنصب]
[معلومات الاتصال]`;
        break;

      case 'centralAsia':
        body = `Уважаемая команда ${agency.agencyName},

Я [Имя] из [Название компании] в Южной Корее.

Мы рассматриваем возможность расширения нашего бизнеса в ${agency.country} и хотели бы узнать о услугах поддержки, предоставляемых ${agency.agencyName}.

Основные вопросы:
1. Программы поддержки выхода на рынок ${agency.country}
2. Услуги по подключению местных партнеров
3. Услуги по исследованию рынка и консультированию
4. Информация об инвестициях и процедурах
5. Информация о местных правилах

Дополнительные вопросы:
- Процедуры подачи заявки на услуги
- Необходимые документы и подготовка
- Стоимость услуг
- Ожидаемое время обработки
- Местная деловая культура

Доступное время для связи: [Доступное время]
Телефон: [Номер телефона]

Мы с нетерпением ждем вашего ответа для подробной консультации.

С наилучшими пожеланиями,

[Имя]
[Название компании]
[Должность]
[Контакт]`;
        break;

      case 'oceania':
        body = `Dear ${agency.agencyName} Team,

I am [Name] from [Company Name] in South Korea.

We are interested in expanding our business to ${agency.country} and would like to inquire about the support services provided by ${agency.agencyName}.

Main inquiries:
1. Market entry support programs for ${agency.country}
2. Local partner connection services
3. Market research and consulting services
4. Investment information and procedures
5. Local business environment and regulations

Additional questions:
- Service application procedures
- Required documents and preparations
- Service costs and fees
- Expected processing time
- Local business culture and practices

Available contact time: [Available time]
Phone: [Phone number]

We look forward to your response for detailed consultation.

Best regards,

[Name]
[Company Name]
[Position]
[Contact]`;
        break;

      default:
        body = `Dear ${agency.agencyName} Team,

I am [Name] from [Company Name] in South Korea.

We are considering expanding our business to ${agency.country} and would like to inquire about the support services provided by ${agency.agencyName}.

Main inquiries:
1. Market entry support programs for ${agency.country}
2. Local partner connection services
3. Market research and consulting services
4. Investment information and procedures
5. Local business environment and regulations

Additional questions:
- Service application procedures
- Required documents and preparations
- Service costs and fees
- Expected processing time
- Local business culture and practices

Available contact time: [Available time]
Phone: [Phone number]

We look forward to your response for detailed consultation.

Best regards,

[Name]
[Company Name]
[Position]
[Contact]`;
    }

    return `mailto:${agency.email}?subject=${subject}&body=${encodeURIComponent(body)}`;
  };

  // 지역별 색상 및 아이콘
  const getRegionStyle = () => {
    switch (region) {
      case 'asia':
        return { color: 'text-blue-600', bg: 'bg-blue-50', border: 'border-blue-200', icon: '🌏' };
      case 'europe':
        return { color: 'text-purple-600', bg: 'bg-purple-50', border: 'border-purple-200', icon: '🇪🇺' };
      case 'northAmerica':
        return { color: 'text-red-600', bg: 'bg-red-50', border: 'border-red-200', icon: '🇺🇸' };
      case 'southAmerica':
        return { color: 'text-green-600', bg: 'bg-green-50', border: 'border-green-200', icon: '🇧🇷' };
      case 'africa':
        return { color: 'text-yellow-600', bg: 'bg-yellow-50', border: 'border-yellow-200', icon: '🌍' };
      case 'middleEast':
        return { color: 'text-orange-600', bg: 'bg-orange-50', border: 'border-orange-200', icon: '🕌' };
      case 'centralAsia':
        return { color: 'text-indigo-600', bg: 'bg-indigo-50', border: 'border-indigo-200', icon: '🏔️' };
      case 'oceania':
        return { color: 'text-teal-600', bg: 'bg-teal-50', border: 'border-teal-200', icon: '🌊' };
      default:
        return { color: 'text-gray-600', bg: 'bg-gray-50', border: 'border-gray-200', icon: '🌐' };
    }
  };

  const regionStyle = getRegionStyle();

  return (
    <Modal isOpen={!!agency} onClose={onClose} title="기관 정보">
      <div className="space-y-4">
        {/* 기관 헤더 */}
        <div className="flex items-start gap-3 mb-4">
          <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
            <Building className="text-orange-600" size={24} />
          </div>
          <div>
            <h2 className="text-xl font-bold text-gray-800">{agency.agencyName}</h2>
            <p className="text-sm text-gray-600 font-medium">{agency.country}</p>
            <div className="flex items-center gap-1 mt-1">
              <MapPin size={14} className="text-gray-400" />
              <span className="text-xs text-gray-500">{agency.countryCode}</span>
            </div>
          </div>
        </div>
        
        {/* 설명 */}
        <div className="bg-gray-50 rounded-lg p-3">
          <p className="text-sm text-gray-700 leading-relaxed">
            {agency.description}
          </p>
        </div>
        
        {/* 연락처 정보 */}
        <div className="space-y-3">
          <h3 className="font-semibold text-gray-800 text-sm">연락처 정보</h3>
          
          <div className="space-y-2">
            <div className="flex items-center gap-3 p-2 rounded-lg hover:bg-gray-50 transition-colors">
              <Mail size={16} className="text-orange-500" />
              <div className="flex-1">
                <a 
                  href={generateEmailTemplate()}
                  className="text-blue-600 hover:text-blue-800 text-sm font-medium"
                >
                  {agency.email}
                </a>
                <div className="flex items-center gap-1 mt-1">
                  <Send size={12} className="text-green-500" />
                  <span className="text-xs text-green-600 font-medium">
                    자동 이메일 템플릿 제공
                  </span>
                </div>
              </div>
            </div>
            
            <div className="flex items-center gap-3 p-2 rounded-lg hover:bg-gray-50 transition-colors">
              <Phone size={16} className="text-orange-500" />
              <a 
                href={`tel:${agency.phone}`}
                className="text-blue-600 hover:text-blue-800 text-sm font-medium"
              >
                {agency.phone}
              </a>
            </div>
            
            <div className="flex items-center gap-3 p-2 rounded-lg hover:bg-gray-50 transition-colors">
              <Globe size={16} className="text-orange-500" />
              <a 
                href={agency.website}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:text-blue-800 text-sm font-medium"
              >
                웹사이트 방문
              </a>
            </div>
          </div>
        </div>
        
        {/* 지역별 자동 이메일 템플릿 안내 */}
        <div className={`${regionStyle.bg} border ${regionStyle.border} rounded-lg p-3`}>
          <div className="flex items-start gap-2">
            <span className="text-lg">{regionStyle.icon}</span>
            <div>
              <p className={`text-sm font-medium ${regionStyle.color} mb-1`}>
                🚀 지역별 맞춤 이메일 템플릿
              </p>
              <p className="text-xs text-gray-700 leading-relaxed">
                이메일을 클릭하면 {agency.country} 시장 진출을 위한 전문적인 문의 템플릿이 자동으로 작성됩니다. 
                지역별 맞춤 내용으로 제목과 내용을 수정하여 바로 발송하실 수 있습니다.
              </p>
            </div>
          </div>
        </div>
        
        {/* 주소 */}
        <div className="pt-3 border-t border-gray-200">
          <div className="flex items-start gap-3">
            <MapPin size={16} className="text-gray-500 mt-0.5" />
            <div>
              <p className="text-xs font-medium text-gray-600 mb-1">주소</p>
              <p className="text-xs text-gray-600 leading-relaxed">
                {agency.address}
              </p>
            </div>
          </div>
        </div>
      </div>
    </Modal>
  );
};

export default AgencyInfo; 