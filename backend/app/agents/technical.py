import json
from typing import Any, Dict
from backend.app.agents.base import BaseAgent, SharedMemory
from backend.app.agents.mock_generator import MockGenerator

class TechnicalArchitectAgent(BaseAgent):
    def __init__(self):
        system_instruction = (
            "Sen kıdemli bir Yazılım Mimarı (Software Architect) ve CTO'sun. Görevin, verilen girişim fikri, "
            "pazar araştırması ve finansal sınırlamalara uygun olarak modern, ölçeklenebilir bir teknik mimari, "
            "teknoloji yığını, veritabanı şeması ve API yapısı tasarlamaktır.\n\n"
            "Çıktını MUTLAKA aşağıdaki JSON formatında vermelisin. Başka hiçbir açıklama metni yazma, doğrudan JSON objesini dön.\n"
            "JSON Formatı:\n"
            "{\n"
            "  \"tech_stack\": {\n"
            "    \"frontend\": [\"Öğe 1\"],\n"
            "    \"backend\": [\"Öğe 1\"],\n"
            "    \"database\": [\"Öğe 1\"],\n"
            "    \"cloud_hosting\": [\"Öğe 1\"],\n"
            "    \"ai_models\": [\"Öğe 1\"]\n"
            "  },\n"
            "  \"database_schema\": [\n"
            "    {\"table_name\": \"Tablo Adı\", \"columns\": [\"Kolon Adı (Tip) - Açıklama\"]}\n"
            "  ],\n"
            "  \"api_endpoints\": [\n"
            "    {\"method\": \"GET/POST\", \"path\": \"/api/v1/resource\", \"description\": \"Açıklama\"}\n"
            "  ],\n"
            "  \"architecture_summary\": \"Genel mimari açıklama ve sistem akışı özet metni.\"\n"
            "}"
        )
        super().__init__(name="TechnicalArchitectAgent", system_instruction=system_instruction)

    def run(self, memory: SharedMemory) -> Dict[str, Any]:
        memory.add_log(self.name, "Yazılım mimarisi ve teknoloji yığını seçimi başlatılıyor...")
        
        # Pull context from memory (demonstrates multiple agent memory retrieval)
        market_context = json.dumps(memory.market_research or {}, indent=2, ensure_ascii=False)
        finance_context = json.dumps(memory.financial_plan or {}, indent=2, ensure_ascii=False)
        
        prompt = (
            f"Girişim Fikri: {memory.startup_idea}\n\n"
            f"Pazar Araştırma Sonuçları:\n{market_context}\n\n"
            f"Finansal Planlama Sonuçları:\n{finance_context}\n\n"
            "Lütfen bu verileri analiz ederek, girişim için en uygun teknoloji yığınını ve mimariyi tasarla ve JSON formatında çıktı ver."
        )
        raw_output = self._call_gemini(prompt)
        
        # Handle mock mode or API key error
        if "[MOCK MODE" in raw_output or "[ERROR" in raw_output:
            mock_data = MockGenerator.generate_tech(memory.startup_idea, memory.market_research or {}, memory.financial_plan or {})
            mock_data["is_mock"] = True
            mock_data["message"] = raw_output
            memory.technical_architecture = mock_data
            memory.add_log(self.name, "Yazılım mimarisi planlaması simüle edildi (Dinamik Mock Veri).", mock_data)
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
            memory.technical_architecture = parsed_data
            memory.add_log(self.name, "Yazılım mimarisi tasarımı başarıyla tamamlandı.", parsed_data)
            return parsed_data
        except Exception as e:
            # Fallback if json parsing fails
            fallback_data = {
                "error": f"JSON parsing failed: {str(e)}",
                "raw_text": raw_output
            }
            memory.technical_architecture = fallback_data
            memory.add_log(self.name, "Yazılım mimarisi tamamlandı ancak çıktı formatlanırken hata oluştu.", fallback_data)
            return fallback_data
