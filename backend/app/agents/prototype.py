import json
from typing import Any, Dict
from backend.app.agents.base import BaseAgent, SharedMemory
from backend.app.agents.mock_generator import MockGenerator

class PrototypeDesignerAgent(BaseAgent):
    def __init__(self):
        system_instruction = (
            "Sen Antigravity altyapısıyla çalışan, sonsuz farklı girişim fikrini çalışan mobil prototiplere dönüştüren bir UI/UX Engine'sin.\n\n"
            "Görevin, girdi olarak gelen girişim fikrinin kullanıcı yolculuğunu (User Journey) analiz etmek ve bu fikrin EN KRİTİK 3 ekranını tasarlamaktır.\n\n"
            "Fikir ne kadar niş veya karmaşık olursa olsun, onu sadece sana verilen şu 6 atomik bileşeni kullanarak ifade etmek zorundasın:\n"
            "- 'TEXT': Başlıklar veya açıklamalar için. (Örn: { \"type\": \"text\", \"text\": \"Kalan Bakiye\", \"size\": \"large\" })\n"
            "- 'BUTTON': Aksiyonlar ve ekran geçişleri için. (Örn: { \"type\": \"button\", \"label\": \"Satın Al\", \"action\": \"navigate\", \"target\": \"success_screen\" })\n"
            "- 'INPUT': Kullanıcıdan bilgi almak için. (Örn: { \"type\": \"input\", \"placeholder\": \"Köpeğinizin adı\", \"input_type\": \"text\" })\n"
            "- 'CARD': Detaylı bilgi blokları veya listelenen ögeler için. (Örn: { \"type\": \"card\", \"title\": \"Altın Paket\", \"desc\": \"Aylık 3 yürüme hakkı\" })\n"
            "- 'LIST': Tekrarlayan verileri göstermek için. (Örn: { \"type\": \"list\", \"items\": [\"Öğe 1\", \"Öğe 2\"] })\n"
            "- 'CHART': Grafik göstermek için. (Örn: { \"type\": \"chart\", \"chart_type\": \"ring\", \"value\": 75, \"label\": \"Tamamlanma Oranı\" })\n\n"
            "Çıktı formatın her zaman şu yapıda bir JSON olmalıdır. Başka hiçbir açıklama yazma, doğrudan JSON dön:\n"
            "{\n"
            "  \"app_name\": \"[Fikre Uygun Yaratıcı Uygulama Adı]\",\n"
            "  \"branding\": {\n"
            "    \"primary_color\": \"[Hex Kodu, örn: #10b981]\",\n"
            "    \"dark_mode\": true\n"
            "  },\n"
            "  \"initial_screen\": \"main\",\n"
            "  \"screens\": {\n"
            "    \"main\": {\n"
            "      \"navigation_title\": \"Ana Sayfa\",\n"
            "      \"layout\": [\n"
            "        { \"type\": \"text\", \"text\": \"Hoş Geldiniz\", \"size\": \"large\" }\n"
            "      ]\n"
            "    }\n"
            "  }\n"
            "}"
        )
        super().__init__(name="PrototypeDesignerAgent", system_instruction=system_instruction)

    def run(self, memory: SharedMemory) -> Dict[str, Any]:
        memory.add_log(self.name, "Girişim fikrinin kullanıcı yolculuğu analiz ediliyor ve 3D ekran prototipi tasarlanıyor...")
        
        prompt = (
            f"Girişim Fikri: {memory.startup_idea}\n\n"
            "Lütfen bu fikir için en kritik 3 ekranı tasarla ve belirtilen JSON formatında çıktı ver."
        )
        raw_output = self._call_gemini(prompt)
        
        # Fallback to dynamic mock generator if API key is rate-limited or missing
        if "[MOCK MODE" in raw_output or "[ERROR" in raw_output:
            # We will generate a dynamic prototype mock structure using MockGenerator
            mock_proto = MockGenerator.generate_prototype(memory.startup_idea)
            memory.ui_prototype = mock_proto
            memory.add_log(self.name, "UI/UX Prototip tasarımı tamamlandı (Dinamik Mock Veri).", mock_proto)
            return mock_proto

        # Clean JSON markdown styling if present
        clean_json = raw_output.strip()
        if clean_json.startswith("```json"):
            clean_json = clean_json[7:]
        if clean_json.endswith("```"):
            clean_json = clean_json[:-3]
        clean_json = clean_json.strip()

        try:
            parsed_data = json.loads(clean_json)
            memory.ui_prototype = parsed_data
            memory.add_log(self.name, "UI/UX Prototip tasarımı başarıyla tamamlandı.", parsed_data)
            return parsed_data
        except Exception as e:
            # Fallback if json parsing fails
            fallback_proto = MockGenerator.generate_prototype(memory.startup_idea)
            memory.ui_prototype = fallback_proto
            memory.add_log(self.name, "UI/UX Prototip tasarımı tamamlandı (Format Hatası Nedeniyle Fallback).", fallback_proto)
            return fallback_proto
