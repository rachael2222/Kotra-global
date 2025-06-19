import React, { useState, useCallback } from 'react';
import Map, { Marker, Popup } from 'react-map-gl';
import { Agency } from '../data/agencies';
import { MapPin, Mail, Phone, Globe, Building } from 'lucide-react';

interface WorldMapProps {
  agencies: Agency[];
  selectedAgency: Agency | null;
  onAgencySelect: (agency: Agency | null) => void;
}

const WorldMap: React.FC<WorldMapProps> = ({ agencies, selectedAgency, onAgencySelect }) => {
  const [viewState, setViewState] = useState({
    longitude: 30,
    latitude: 20,
    zoom: 2
  });

  const [popupInfo, setPopupInfo] = useState<Agency | null>(null);

  const onMarkerClick = useCallback((agency: Agency) => {
    setPopupInfo(agency);
    onAgencySelect(agency);
  }, [onAgencySelect]);

  const onPopupClose = useCallback(() => {
    setPopupInfo(null);
    onAgencySelect(null);
  }, [onAgencySelect]);

  return (
    <div className="w-full h-full">
      <Map
        {...viewState}
        onMove={evt => setViewState(evt.viewState)}
        style={{ width: '100%', height: '100%' }}
        mapStyle="mapbox://styles/mapbox/light-v11"
        mapboxAccessToken={process.env.REACT_APP_MAPBOX_TOKEN || 'pk.eyJ1IjoidGVzdCIsImEiOiJjbGV0ZXN0In0.test'}
      >
        {agencies.map((agency) => (
          <Marker
            key={agency.id}
            longitude={agency.lng}
            latitude={agency.lat}
            anchor="bottom"
            onClick={(e) => {
              e.originalEvent.stopPropagation();
              onMarkerClick(agency);
            }}
          >
            <div className={`cursor-pointer transform transition-transform hover:scale-110 ${
              selectedAgency?.id === agency.id ? 'scale-125' : ''
            }`}>
              <MapPin 
                size={32} 
                className={`${
                  selectedAgency?.id === agency.id 
                    ? 'text-red-600 fill-red-100' 
                    : 'text-blue-600 fill-blue-100'
                } drop-shadow-lg`}
              />
            </div>
          </Marker>
        ))}

        {popupInfo && (
          <Popup
            anchor="top"
            longitude={popupInfo.lng}
            latitude={popupInfo.lat}
            onClose={onPopupClose}
            closeButton={true}
            closeOnClick={false}
            className="max-w-sm"
          >
            <div className="p-4 min-w-80">
              <div className="flex items-start gap-3 mb-3">
                <Building className="text-blue-600 mt-1" size={20} />
                <div>
                  <h3 className="font-bold text-lg text-gray-800">{popupInfo.agencyName}</h3>
                  <p className="text-sm text-gray-600 font-medium">{popupInfo.country}</p>
                </div>
              </div>
              
              <p className="text-sm text-gray-700 mb-4 leading-relaxed">
                {popupInfo.description}
              </p>
              
              <div className="space-y-3">
                <div className="flex items-center gap-2">
                  <Mail size={16} className="text-gray-500" />
                  <a 
                    href={`mailto:${popupInfo.email}`}
                    className="text-blue-600 hover:text-blue-800 text-sm font-medium"
                  >
                    {popupInfo.email}
                  </a>
                </div>
                
                <div className="flex items-center gap-2">
                  <Phone size={16} className="text-gray-500" />
                  <a 
                    href={`tel:${popupInfo.phone}`}
                    className="text-blue-600 hover:text-blue-800 text-sm font-medium"
                  >
                    {popupInfo.phone}
                  </a>
                </div>
                
                <div className="flex items-center gap-2">
                  <Globe size={16} className="text-gray-500" />
                  <a 
                    href={popupInfo.website}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-600 hover:text-blue-800 text-sm font-medium"
                  >
                    웹사이트 방문
                  </a>
                </div>
                
                <div className="flex items-start gap-2 pt-2 border-t border-gray-200">
                  <MapPin size={16} className="text-gray-500 mt-0.5" />
                  <p className="text-xs text-gray-600 leading-relaxed">
                    {popupInfo.address}
                  </p>
                </div>
              </div>
            </div>
          </Popup>
        )}
      </Map>
    </div>
  );
};

export default WorldMap; 