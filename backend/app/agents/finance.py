import json
from typing import Any, Dict
from backend.app.agents.base import BaseAgent, SharedMemory

class FinancePlannerAgent(BaseAgent):
    def __init__(self):
        system_instruction = (
            "Sen uzman bir Finans Planlama ve Girişimcilik Mentörüsün. Görevin, verilen girişim fikri "
            "ve pazar analizi verilerini kullanarak gelir modelleri, fiyatlandırma stratejileri ve "
            "tahmini operasyonel giderleri planlamaktır.\n\n"
            "Çıktını MUTLAKA aşağıdaki JSON formatında vermelisin. Başka hiçbir açıklama metni yazma, doğrudan JSON objesini dön.\n"
            "JSON Formatı:\n"
            "{\n"
            "  \"monetization_models\": [\"Gelir modeli 1\", \"Gelir modeli 2\"],\n"
            "  \"pricing_tiers\": [\n"
            "    {\"tier_name\": \"Plan Adı\", \"price\": \"Fiyat / Ay\", \"features\": [\"Özellik 1\", \"Özellik 2\"]}\n"
            "  ],\n"
            "  \"estimated_costs\": [\n"
            "    {\"item\": \"Gider kalemi\", \"amount\": \"Tahmini Tutar\", \"frequency\": \"Tek seferlik / Aylık\"}\n"
            "  ],\n"
            "  \"financial_tips\": [\"Finansal ipucu 1\", \"Finansal ipucu 2\"]\n"
            "}"
        )
        super().__init__(name="FinancePlannerAgent", system_instruction=system_instruction)

    def run(self, memory: SharedMemory) -> Dict[str, Any]:
        memory.add_log(self.name, "Gelir modeli ve maliyet hesaplamaları başlatılıyor...")
        
        # Pull context from memory (demonstrates agent memory usage)
        market_context = json.dumps(memory.market_research or {}, indent=2, ensure_ascii=False)
        
        prompt = (
            f"Girişim Fikri: {memory.startup_idea}\n\n"
            f"Pazar Araştırma Sonuçları (Önceki Ajanın Bulguları):\n{market_context}\n\n"
            "Lütfen bu pazar verilerini göz önünde bulundurarak finansal planı hazırla ve JSON çıktısı ver."
        )
        raw_output = self._call_gemini(prompt)
        
        # Handle mock mode or API key error
        if "[MOCK MODE" in raw_output or "[ERROR" in raw_output:
            mock_data = {
                "monetization_models": ["SaaS Abonelik", "Kullanım Başına Ödeme (Pay-as-you-go)", "B2B Lisanslama"],
                "pricing_tiers": [
                    {"tier_name": "Başlangıç (Basic)", "price": "$9 / Ay", "features": ["Temel AI Analizleri", "Sınırlı Bellek", "E-posta Desteği"]},
                    {"tier_name": "Profesyonel (Pro)", "price": "$29 / Ay", "features": ["Gelişmiş AI Ajanları", "Sınırsız Hafıza Entegrasyonu", "7/24 Destek", "API Erişimi"]}
                ],
                "estimated_costs": [
                    {"item": "Bulut Sunucu & API Kullanım Giderleri", "amount": "$150 / Ay", "frequency": "Aylık"},
                    {"item": "Pazarlama ve Reklam Giderleri", "amount": "$500 / Ay", "frequency": "Aylık"},
                    {"item": "Marka Tescili ve Hukuki Kurulum", "amount": "$1000", "frequency": "Tek seferlik"}
                ],
                "financial_tips": [
                    "Başlangıçta sunucu maliyetlerini optimize etmek için ücretsiz/uygun fiyatlı API paketlerini kullanın.",
                    "Pazarlama bütçesini doğrudan hedef kitle analizindeki niş gruplara yönelik harcayın."
                ],
                "is_mock": True,
                "message": raw_output
            }
            memory.financial_plan = mock_data
            memory.add_log(self.name, "Finansal planlama simüle edildi (Mock Veri).", mock_data)
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
            memory.financial_plan = parsed_data
            memory.add_log(self.name, "Finansal planlama başarıyla tamamlandı.", parsed_data)
            return parsed_data
        except Exception as e:
            # Fallback if json parsing fails
            fallback_data = {
                "error": f"JSON parsing failed: {str(e)}",
                "raw_text": raw_output
            }
            memory.financial_plan = fallback_data
            memory.add_log(self.name, "Finansal planlama tamamlandı ancak çıktı formatlanırken hata oluştu.", fallback_data)
            return fallback_data
