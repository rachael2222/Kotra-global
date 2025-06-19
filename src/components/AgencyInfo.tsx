import React from 'react';
import { Agency } from '../data/agencies';
import { Building, Mail, Phone, Globe, MapPin, Copy, ExternalLink } from 'lucide-react';

interface AgencyInfoProps {
  agency: Agency | null;
  onClose: () => void;
}

const AgencyInfo: React.FC<AgencyInfoProps> = ({ agency, onClose }) => {
  if (!agency) return null;

  const copyToClipboard = (text: string, type: string) => {
    navigator.clipboard.writeText(text).then(() => {
      // 간단한 알림 (실제 프로덕션에서는 toast 라이브러리 사용 권장)
      alert(`${type}이(가) 클립보드에 복사되었습니다.`);
    });
  };

  return (
    <div className="w-96 bg-white shadow-xl border-l border-gray-200 h-full overflow-y-auto">
      <div className="p-6">
        {/* 헤더 */}
        <div className="flex items-start justify-between mb-6">
          <div className="flex items-start gap-3">
            <Building className="text-blue-600 mt-1" size={24} />
            <div>
              <h2 className="text-xl font-bold text-gray-800 leading-tight">
                {agency.agencyName}
              </h2>
              <p className="text-sm text-gray-600 font-medium mt-1">
                {agency.country} ({agency.countryCode})
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 p-1"
          >
            ✕
          </button>
        </div>

        {/* 설명 */}
        <div className="mb-6">
          <p className="text-gray-700 leading-relaxed">
            {agency.description}
          </p>
        </div>

        {/* 연락처 정보 */}
        <div className="space-y-4">
          <h3 className="text-lg font-semibold text-gray-800 border-b border-gray-200 pb-2">
            연락처 정보
          </h3>

          {/* 이메일 */}
          <div className="bg-gray-50 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <Mail size={18} className="text-gray-600" />
              <span className="font-medium text-gray-700">이메일</span>
            </div>
            <div className="flex items-center justify-between">
              <a 
                href={`mailto:${agency.email}`}
                className="text-blue-600 hover:text-blue-800 font-medium"
              >
                {agency.email}
              </a>
              <button
                onClick={() => copyToClipboard(agency.email, '이메일')}
                className="text-gray-400 hover:text-gray-600 p-1"
                title="이메일 복사"
              >
                <Copy size={16} />
              </button>
            </div>
          </div>

          {/* 전화번호 */}
          <div className="bg-gray-50 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <Phone size={18} className="text-gray-600" />
              <span className="font-medium text-gray-700">전화번호</span>
            </div>
            <div className="flex items-center justify-between">
              <a 
                href={`tel:${agency.phone}`}
                className="text-blue-600 hover:text-blue-800 font-medium"
              >
                {agency.phone}
              </a>
              <button
                onClick={() => copyToClipboard(agency.phone, '전화번호')}
                className="text-gray-400 hover:text-gray-600 p-1"
                title="전화번호 복사"
              >
                <Copy size={16} />
              </button>
            </div>
          </div>

          {/* 웹사이트 */}
          <div className="bg-gray-50 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <Globe size={18} className="text-gray-600" />
              <span className="font-medium text-gray-700">웹사이트</span>
            </div>
            <div className="flex items-center justify-between">
              <a 
                href={agency.website}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:text-blue-800 font-medium flex items-center gap-1"
              >
                웹사이트 방문
                <ExternalLink size={14} />
              </a>
              <button
                onClick={() => copyToClipboard(agency.website, '웹사이트 URL')}
                className="text-gray-400 hover:text-gray-600 p-1"
                title="URL 복사"
              >
                <Copy size={16} />
              </button>
            </div>
          </div>

          {/* 주소 */}
          <div className="bg-gray-50 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <MapPin size={18} className="text-gray-600" />
              <span className="font-medium text-gray-700">주소</span>
            </div>
            <div className="flex items-start justify-between">
              <p className="text-gray-700 leading-relaxed flex-1">
                {agency.address}
              </p>
              <button
                onClick={() => copyToClipboard(agency.address, '주소')}
                className="text-gray-400 hover:text-gray-600 p-1 ml-2"
                title="주소 복사"
              >
                <Copy size={16} />
              </button>
            </div>
          </div>
        </div>

        {/* 액션 버튼들 */}
        <div className="mt-8 space-y-3">
          <button
            onClick={() => window.open(`mailto:${agency.email}?subject=수출 문의&body=안녕하세요, ${agency.agencyName}입니다.%0A%0A수출 관련 문의사항이 있어 연락드립니다.`, '_blank')}
            className="w-full bg-blue-600 text-white py-3 px-4 rounded-lg hover:bg-blue-700 transition-colors font-medium flex items-center justify-center gap-2"
          >
            <Mail size={18} />
            이메일 문의하기
          </button>
          
          <button
            onClick={() => window.open(agency.website, '_blank')}
            className="w-full bg-gray-100 text-gray-700 py-3 px-4 rounded-lg hover:bg-gray-200 transition-colors font-medium flex items-center justify-center gap-2"
          >
            <Globe size={18} />
            공식 웹사이트 방문
          </button>
        </div>
      </div>
    </div>
  );
};

export default AgencyInfo; 