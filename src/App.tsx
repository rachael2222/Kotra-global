import React, { useState } from 'react';
import SearchBar from './components/SearchBar';
import AgencyInfo from './components/AgencyInfo';
import WorldMap from './components/WorldMap';
import { agencies, Agency } from './data/agencies';
import { Globe, MapPin, Building } from 'lucide-react';

function App() {
  const [selectedAgency, setSelectedAgency] = useState<Agency | null>(null);

  const handleAgencySelect = (agency: Agency | null) => {
    setSelectedAgency(agency);
  };

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      {/* 헤더 */}
      <header className="bg-white shadow-sm border-b border-gray-200 px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Globe className="text-orange-500" size={32} />
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
      <div className="flex-1 flex flex-col">
        {/* 지도 영역 */}
        <div className="flex-1 relative">
          <WorldMap 
            agencies={agencies}
            selectedAgency={selectedAgency}
            onAgencySelect={handleAgencySelect}
          />
        </div>

        {/* 하단 나라 목록 */}
        <div className="bg-white border-t border-gray-200 p-6">
          <div className="max-w-7xl mx-auto">
            <h2 className="text-xl font-bold text-gray-800 mb-4">
              🌍 전세계 수출지원기관 ({agencies.length}개)
            </h2>
            <p className="text-gray-600 mb-6">
              국가명을 검색하거나 아래 목록에서 기관을 선택하세요
            </p>
            
            {/* 기관 카드 목록 */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              {agencies.map((agency) => (
                <div
                  key={agency.id}
                  onClick={() => handleAgencySelect(agency)}
                  className={`p-4 border rounded-lg cursor-pointer transition-all duration-200 shadow-sm hover:shadow-md
                    ${selectedAgency?.id === agency.id
                      ? 'border-orange-500 bg-orange-50 shadow-lg scale-105 ring-2 ring-orange-200'
                      : 'border-gray-200 bg-white hover:border-orange-400 hover:bg-orange-50'
                    }
                  `}
                  style={{ minHeight: 110 }}
                >
                  <div className="flex items-start gap-3">
                    <div className="flex-shrink-0">
                      <div className={`w-8 h-8 rounded-full flex items-center justify-center transition-colors
                        ${selectedAgency?.id === agency.id ? 'bg-orange-100' : 'bg-gray-100'}`}
                      >
                        <Building className={`transition-colors ${selectedAgency?.id === agency.id ? 'text-orange-500' : 'text-gray-400'}`} size={16} />
                      </div>
                    </div>
                    <div className="flex-1 min-w-0">
                      <h3 className={`font-semibold text-sm mb-1 transition-colors
                        ${selectedAgency?.id === agency.id ? 'text-orange-700' : 'text-gray-800'}`}
                      >
                        {agency.country}
                      </h3>
                      <p className="text-xs text-gray-600 mb-2 line-clamp-2">
                        {agency.agencyName}
                      </p>
                      <div className="flex items-center gap-1 text-xs">
                        <MapPin size={12} className={`transition-colors ${selectedAgency?.id === agency.id ? 'text-orange-400' : 'text-gray-400'}`} />
                        <span className={`transition-colors ${selectedAgency?.id === agency.id ? 'text-orange-500' : 'text-gray-500'}`}>{agency.countryCode}</span>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* 선택된 기관 정보 모달 */}
      <AgencyInfo agency={selectedAgency} onClose={() => setSelectedAgency(null)} />
    </div>
  );
}

export default App;
