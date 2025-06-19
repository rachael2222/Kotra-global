import React, { useState } from 'react';
import SearchBar from './components/SearchBar';
import AgencyInfo from './components/AgencyInfo';
import { agencies, Agency } from './data/agencies';
import { Globe, MapPin, Building } from 'lucide-react';

function App() {
  const [selectedAgency, setSelectedAgency] = useState<Agency | null>(null);

  const handleAgencySelect = (agency: Agency | null) => {
    setSelectedAgency(agency);
  };

  return (
    <div className="min-h-screen flex flex-col bg-gray-100">
      {/* 헤더 */}
      <header className="bg-white shadow-sm border-b border-gray-200 px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Globe className="text-blue-600" size={32} />
            <div>
              <h1 className="text-2xl font-bold text-gray-800">
                Global Trade Support
              </h1>
              <p className="text-sm text-gray-600">
                전세계 수출지원기관 연락처 검색 서비스
              </p>
            </div>
          </div>
          
          <SearchBar 
            agencies={agencies}
            onAgencySelect={handleAgencySelect}
            selectedAgency={selectedAgency}
          />
        </div>
      </header>

      {/* 메인 컨텐츠 */}
      <div className="flex-1 flex">
        {/* 기관 목록 영역 */}
        <div className="flex-1 p-6">
          <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
            <h2 className="text-xl font-bold text-gray-800 mb-4">
              🌍 전세계 수출지원기관 ({agencies.length}개)
            </h2>
            <p className="text-gray-600 mb-6">
              국가명을 검색하거나 아래 목록에서 기관을 선택하세요
            </p>
            
            {/* 기관 카드 목록 */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {agencies.map((agency) => (
                <div
                  key={agency.id}
                  onClick={() => handleAgencySelect(agency)}
                  className={`p-4 border rounded-lg cursor-pointer transition-all hover:shadow-md ${
                    selectedAgency?.id === agency.id 
                      ? 'border-blue-500 bg-blue-50' 
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <div className="flex items-start gap-3">
                    <div className="flex-shrink-0">
                      <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                        <Building className="text-blue-600" size={16} />
                      </div>
                    </div>
                    <div className="flex-1 min-w-0">
                      <h3 className="font-semibold text-gray-800 text-sm mb-1">
                        {agency.country}
                      </h3>
                      <p className="text-xs text-gray-600 mb-2 line-clamp-2">
                        {agency.agencyName}
                      </p>
                      <div className="flex items-center gap-1 text-xs text-gray-500">
                        <MapPin size={12} />
                        <span>{agency.countryCode}</span>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* 선택된 기관 정보 사이드바 */}
        {selectedAgency && (
          <AgencyInfo agency={selectedAgency} onClose={() => setSelectedAgency(null)} />
        )}
      </div>
    </div>
  );
}

export default App;
