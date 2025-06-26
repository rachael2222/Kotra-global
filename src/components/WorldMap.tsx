import React, { useState, useRef, useEffect } from 'react';
import mapboxgl from 'mapbox-gl';
import { Agency } from '../data/agencies';
import { MapPin, Mail, Phone, Globe, Building } from 'lucide-react';
import 'mapbox-gl/dist/mapbox-gl.css';

interface WorldMapProps {
  agencies: Agency[];
  selectedAgency: Agency | null;
  onAgencySelect: (agency: Agency | null) => void;
}

const WorldMap: React.FC<WorldMapProps> = ({ agencies, selectedAgency, onAgencySelect }) => {
  const mapContainer = useRef<HTMLDivElement>(null);
  const map = useRef<mapboxgl.Map | null>(null);
  const [popupInfo, setPopupInfo] = useState<Agency | null>(null);

  useEffect(() => {
    if (map.current) return;

    mapboxgl.accessToken = process.env.REACT_APP_MAPBOX_TOKEN || 'pk.eyJ1IjoidGVzdCIsImEiOiJjbGV0ZXN0In0.test';
    
    map.current = new mapboxgl.Map({
      container: mapContainer.current!,
      style: 'mapbox://styles/mapbox/light-v11',
      center: [30, 20],
      zoom: 2
    });

    map.current.on('load', () => {
      if (!map.current) return;

      // Add markers for each agency
      agencies.forEach((agency) => {
        // Create marker element
        const markerEl = document.createElement('div');
        markerEl.className = 'cursor-pointer transform transition-transform hover:scale-110';
        markerEl.innerHTML = `
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blue-600 fill-blue-100 drop-shadow-lg">
            <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
            <circle cx="12" cy="10" r="3"/>
          </svg>
        `;

        // Create popup
        const popup = new mapboxgl.Popup({ offset: 25 }).setHTML(`
          <div class="p-4 min-w-80">
            <div class="flex items-start gap-3 mb-3">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blue-600 mt-1">
                <path d="M2 7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2Z"/>
                <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
              </svg>
              <div>
                <h3 class="font-bold text-lg text-gray-800">${agency.agencyName}</h3>
                <p class="text-sm text-gray-600 font-medium">${agency.country}</p>
              </div>
            </div>
            
            <p class="text-sm text-gray-700 mb-4 leading-relaxed">
              ${agency.description}
            </p>
            
            <div class="space-y-3">
              <div class="flex items-center gap-2">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-500">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                  <polyline points="22,6 12,13 2,6"/>
                </svg>
                <a href="mailto:${agency.email}" class="text-blue-600 hover:text-blue-800 text-sm font-medium">
                  ${agency.email}
                </a>
              </div>
              
              <div class="flex items-center gap-2">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-500">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                </svg>
                <a href="tel:${agency.phone}" class="text-blue-600 hover:text-blue-800 text-sm font-medium">
                  ${agency.phone}
                </a>
              </div>
              
              <div class="flex items-center gap-2">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-500">
                  <circle cx="12" cy="12" r="10"/>
                  <path d="m15 9-6 6"/>
                  <path d="m9 9 6 6"/>
                </svg>
                <a href="${agency.website}" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-800 text-sm font-medium">
                  웹사이트 방문
                </a>
              </div>
              
              <div class="flex items-start gap-2 pt-2 border-t border-gray-200">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-500 mt-0.5">
                  <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                <p class="text-xs text-gray-600 leading-relaxed">
                  ${agency.address}
                </p>
              </div>
            </div>
          </div>
        `);

        // Add marker to map
        if (map.current) {
          new mapboxgl.Marker(markerEl)
            .setLngLat([agency.lng, agency.lat])
            .setPopup(popup)
            .addTo(map.current);
        }

        // Add click event
        markerEl.addEventListener('click', () => {
          onAgencySelect(agency);
          setPopupInfo(agency);
        });
      });
    });

    return () => {
      if (map.current) {
        map.current.remove();
        map.current = null;
      }
    };
  }, [agencies, onAgencySelect]);

  return (
    <div className="w-full h-full">
      <div ref={mapContainer} className="w-full h-full" />
    </div>
  );
};

export default WorldMap; 