import React from 'react';
import { Agency } from '../data/agencies';
import { Mail, Phone, Globe, Building, MapPin } from 'lucide-react';
import Modal from './Modal';

interface AgencyInfoProps {
  agency: Agency | null;
  onClose: () => void;
}

const AgencyInfo: React.FC<AgencyInfoProps> = ({ agency, onClose }) => {
  if (!agency) return null;

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
              <a 
                href={`mailto:${agency.email}`}
                className="text-blue-600 hover:text-blue-800 text-sm font-medium"
              >
                {agency.email}
              </a>
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