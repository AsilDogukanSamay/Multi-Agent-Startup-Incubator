import json
from typing import Any, Dict
from backend.app.agents.base import BaseAgent, SharedMemory

class MarketResearchAgent(BaseAgent):
    def __init__(self):
        system_instruction = (
            "Sen uzman bir Pazar Araştırma Analistisin. Görevin, verilen girişim fikirlerini analiz etmek, "
            "hedef kitleyi, pazar büyüklüğünü/trendlerini, rakipleri ve SWOT analizini belirlemektir.\n\n"
            "Çıktını MUTLAKA aşağıdaki JSON formatında vermelisin. Başka hiçbir açıklama metni yazma, doğrudan JSON objesini dön.\n"
            "JSON Formatı:\n"
            "{\n"
            "  \"target_audience\": [\"Hedef kitle segmenti 1\", \"Hedef kitle segmenti 2\"],\n"
            "  \"competitors\": [\n"
            "    {\"name\": \"Rakip 1\", \"advantage\": \"Onların güçlü yönü\", \"disadvantage\": \"Bizim onlara karşı üstünlüğümüz\"}\n"
            "  ],\n"
            "  \"market_trends\": [\"Trend 1\", \"Trend 2\"],\n"
            "  \"swot\": {\n"
            "    \"strengths\": [\"Güçlü yön 1\"],\n"
            "    \"weaknesses\": [\"Zayıf yön 1\"],\n"
            "    \"opportunities\": [\"Fırsat 1\"],\n"
            "    \"threats\": [\"Tehdit 1\"]\n"
            "  }\n"
            "}"
        )
        super().__init__(name="MarketResearchAgent", system_instruction=system_instruction)

    def run(self, memory: SharedMemory) -> Dict[str, Any]:
        memory.add_log(self.name, "Pazar araştırması ve rakip analizi başlatılıyor...")
        
        prompt = f"Girişim Fikri: {memory.startup_idea}\n\nLütfen bu fikir için detaylı pazar analizi yap ve yukarıda belirtilen JSON formatında çıktı ver."
        raw_output = self._call_gemini(prompt)
        
        # Handle mock mode or API key error
        if "[MOCK MODE" in raw_output or "[ERROR" in raw_output:
            mock_data = {
                "target_audience": ["Genç profesyoneller", "Teknoloji meraklıları", "Ev kullanıcıları"],
                "competitors": [
                    {"name": "Mevcut Geleneksel Çözümler", "advantage": "Pazarda bilinirlik ve güven", "disadvantage": "Hız ve yapay zeka entegrasyonu eksikliği"},
                    {"name": "Benzer Alternatif Uygulamalar", "advantage": "Basit arayüz", "disadvantage": "Kişiselleştirme ve otonom ajan desteğinin olmaması"}
                ],
                "market_trends": ["Yapay zeka ile kişiselleştirme", "Mobil öncelikli çözümler", "Abonelik tabanlı hizmet modelleri"],
                "swot": {
                    "strengths": ["Esnek ve dinamik mimari", "Gelişmiş AI entegrasyonu", "Düşük operasyonel maliyet"],
                    "weaknesses": ["Yeni marka bilinirliği", "Başlangıç verisi eksikliği"],
                    "opportunities": ["Büyüyen yapay zeka pazarı", "Niş kullanıcı kitlelerine ulaşma kolaylığı"],
                    "threats": ["Büyük rakiplerin benzer özellikleri hızlıca kopyalaması", "Bulut servis maliyetlerinin artışı"]
                },
                "is_mock": True,
                "message": raw_output
            }
            memory.market_research = mock_data
            memory.add_log(self.name, "Pazar araştırması simüle edildi (Mock Veri).", mock_data)
            return mock_data

        # Clean JSON markdown styling if present
        clean_json = raw_output.strip()
        if clean_json.startswith("```json"):
            clean_json = clean_json[7:]
        if clean_json.endswith("```"):
            clean_json = clean_json[:-3]
        clean_json = clean_json.strip()

        try:
            parsed_data = json.loads(clean_json)
            memory.market_research = parsed_data
            memory.add_log(self.name, "Pazar araştırması ve SWOT analizi başarıyla tamamlandı.", parsed_data)
            return parsed_data
        except Exception as e:
            # Fallback if json parsing fails
            fallback_data = {
                "error": f"JSON parsing failed: {str(e)}",
                "raw_text": raw_output
            }
            memory.market_research = fallback_data
            memory.add_log(self.name, "Pazar araştırması tamamlandı ancak çıktı formatlanırken hata oluştu.", fallback_data)
            return fallback_data
