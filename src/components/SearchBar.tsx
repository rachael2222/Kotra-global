import React, { useState, useMemo } from 'react';
import { Search, X } from 'lucide-react';
import { Agency } from '../data/agencies';

interface SearchBarProps {
  agencies: Agency[];
  onAgencySelect: (agency: Agency | null) => void;
  selectedAgency: Agency | null;
}

const SearchBar: React.FC<SearchBarProps> = ({ agencies, onAgencySelect, selectedAgency }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [isOpen, setIsOpen] = useState(false);

  const filteredAgencies = useMemo(() => {
    if (!searchTerm.trim()) return [];
    
    return agencies.filter(agency =>
      agency.country.toLowerCase().includes(searchTerm.toLowerCase()) ||
      agency.agencyName.toLowerCase().includes(searchTerm.toLowerCase())
    ).slice(0, 8); // 최대 8개 결과만 표시
  }, [agencies, searchTerm]);

  const handleSelect = (agency: Agency) => {
    setSearchTerm(agency.country);
    setIsOpen(false);
    onAgencySelect(agency);
  };

  const handleClear = () => {
    setSearchTerm('');
    setIsOpen(false);
    onAgencySelect(null);
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setSearchTerm(value);
    setIsOpen(value.trim().length > 0);
    
    if (!value.trim()) {
      onAgencySelect(null);
    }
  };

  return (
    <div className="relative w-full max-w-md">
      <div className="relative">
        <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={20} />
        <input
          type="text"
          placeholder="국가명 또는 기관명을 검색하세요..."
          value={searchTerm}
          onChange={handleInputChange}
          onFocus={() => setIsOpen(searchTerm.trim().length > 0)}
          className="w-full pl-10 pr-10 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
        />
        {searchTerm && (
          <button
            onClick={handleClear}
            className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600"
          >
            <X size={20} />
          </button>
        )}
      </div>

      {isOpen && filteredAgencies.length > 0 && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-white border border-gray-200 rounded-lg shadow-lg z-50 max-h-80 overflow-y-auto">
          {filteredAgencies.map((agency) => (
            <button
              key={agency.id}
              onClick={() => handleSelect(agency)}
              className={`w-full text-left px-4 py-3 hover:bg-gray-50 border-b border-gray-100 last:border-b-0 transition-colors ${
                selectedAgency?.id === agency.id ? 'bg-blue-50 border-blue-200' : ''
              }`}
            >
              <div className="flex items-center justify-between">
                <div>
                  <p className="font-medium text-gray-800">{agency.country}</p>
                  <p className="text-sm text-gray-600 truncate">{agency.agencyName}</p>
                </div>
                <div className="text-xs text-gray-400 ml-2">
                  {agency.countryCode}
                </div>
              </div>
            </button>
          ))}
        </div>
      )}

      {isOpen && searchTerm.trim() && filteredAgencies.length === 0 && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-white border border-gray-200 rounded-lg shadow-lg z-50 p-4">
          <p className="text-gray-500 text-center">검색 결과가 없습니다.</p>
        </div>
      )}
    </div>
  );
};

export default SearchBar; 