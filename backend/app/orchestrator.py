import asyncio
from backend.app.agents.base import SharedMemory
from backend.app.agents.market import MarketResearchAgent
from backend.app.agents.finance import FinancePlannerAgent
from backend.app.agents.technical import TechnicalArchitectAgent

class Orchestrator:
    def __init__(self):
        self.market_agent = MarketResearchAgent()
        self.finance_agent = FinancePlannerAgent()
        self.tech_agent = TechnicalArchitectAgent()

    async def run_incubator(self, startup_idea: str) -> SharedMemory:
        """
        Tüm kuluçka sürecini yönetir. Ajanları sıralı olarak çalıştırır
        ve ortak hafızayı güncelleyerek nihai raporu üretir.
        """
        memory = SharedMemory(startup_idea=startup_idea)
        memory.add_log("Orchestrator", "Girişim kuluçka süreci başlatıldı. Ajanlar sırayla devreye giriyor...")
        
        # 1. Pazar Araştırma Ajanı
        memory.add_log("Orchestrator", "Pazar Araştırma Ajanı (MarketResearchAgent) tetiklendi.")
        await asyncio.to_thread(self.market_agent.run, memory)
        await asyncio.sleep(1)  # Ajan geçişi simülasyonu / UX
        
        # 2. Finans Ajanı
        memory.add_log("Orchestrator", "Finans Planlama Ajanı (FinancePlannerAgent) tetiklendi.")
        await asyncio.to_thread(self.finance_agent.run, memory)
        await asyncio.sleep(1)
        
        # 3. Teknik Mimar Ajanı
        memory.add_log("Orchestrator", "Teknik Mimari Ajanı (TechnicalArchitectAgent) tetiklendi.")
        await asyncio.to_thread(self.tech_agent.run, memory)
        await asyncio.sleep(1)
        
        # 4. Nihai Markdown Raporu Oluşturma
        memory.add_log("Orchestrator", "Nihai Girişim Raporu derleniyor...")
        memory.final_report = self._generate_final_report(memory)
        memory.add_log("Orchestrator", "Süreç tamamlandı. Rapor başarıyla oluşturuldu!")
        
        return memory

    def _generate_final_report(self, memory: SharedMemory) -> str:
        """
        Tüm ajanlardan gelen verileri birleştirerek şık bir Markdown raporu oluşturur.
        """
        market = memory.market_research or {}
        finance = memory.financial_plan or {}
        tech = memory.technical_architecture or {}

        # Safe list retrievals
        audience = "\n".join([f"- {item}" for item in market.get("target_audience", [])]) or "- Bilgi yok"
        trends = "\n".join([f"- {item}" for item in market.get("market_trends", [])]) or "- Bilgi yok"
        
        competitors_list = []
        for c in market.get("competitors", []):
            competitors_list.append(f"| **{c.get('name', 'Bilinmeyen')}** | {c.get('advantage', '-')} | {c.get('disadvantage', '-')} |")
        competitors = "\n".join(competitors_list) or "| Rakipler belirlenemedi | - | - |"

        swot = market.get("swot", {})
        swot_s = "\n".join([f"- {item}" for item in swot.get("strengths", [])]) or "- Bilgi yok"
        swot_w = "\n".join([f"- {item}" for item in swot.get("weaknesses", [])]) or "- Bilgi yok"
        swot_o = "\n".join([f"- {item}" for item in swot.get("opportunities", [])]) or "- Bilgi yok"
        swot_t = "\n".join([f"- {item}" for item in swot.get("threats", [])]) or "- Bilgi yok"

        # Finance formatting
        monetization = "\n".join([f"- {item}" for item in finance.get("monetization_models", [])]) or "- Bilgi yok"
        
        pricing_list = []
        for p in finance.get("pricing_tiers", []):
            feats = ", ".join(p.get("features", []))
            pricing_list.append(f"- **{p.get('tier_name', 'Plan')}**: {p.get('price', '-')} ({feats})")
        pricing = "\n".join(pricing_list) or "- Fiyatlandırma belirlenemedi"

        costs_list = []
        for cost in finance.get("estimated_costs", []):
            costs_list.append(f"| {cost.get('item', '-')} | {cost.get('amount', '-')} | {cost.get('frequency', '-')} |")
        costs = "\n".join(costs_list) or "| Gider kalemi bulunamadı | - | - |"

        fin_tips = "\n".join([f"- {item}" for item in finance.get("financial_tips", [])]) or "- Bilgi yok"

        # Tech formatting
        tech_stack_dict = tech.get("tech_stack", {})
        frontend_tech = ", ".join(tech_stack_dict.get("frontend", [])) or "-"
        backend_tech = ", ".join(tech_stack_dict.get("backend", [])) or "-"
        db_tech = ", ".join(tech_stack_dict.get("database", [])) or "-"
        host_tech = ", ".join(tech_stack_dict.get("cloud_hosting", [])) or "-"
        ai_tech = ", ".join(tech_stack_dict.get("ai_models", [])) or "-"

        endpoints_list = []
        for ep in tech.get("api_endpoints", []):
            endpoints_list.append(f"- `[{ep.get('method', 'GET')}]` **{ep.get('path', '/')}** : {ep.get('description', '-')}")
        endpoints = "\n".join(endpoints_list) or "- API uç noktaları belirlenemedi"

        report = f"""# 🚀 Girişim Analiz ve Yol Haritası Raporu

Girişim Fikri: **{memory.startup_idea}**

---

## 📊 1. Pazar Araştırması ve SWOT Analizi

### 👥 Hedef Kitle
{audience}

### 📈 Pazar Trendleri
{trends}

### ⚔️ Rekabet Analizi
| Rakip Adı | Rakip Güçlü Yön | Bizim Üstünlüğümüz |
| :--- | :--- | :--- |
{competitors}

### 🔄 SWOT Analizi
| 🟢 Güçlü Yönler (Strengths) | 🔴 Zayıf Yönler (Weaknesses) |
| :--- | :--- |
| {swot_s.replace('- ', '')} | {swot_w.replace('- ', '')} |

| 🔵 Fırsatlar (Opportunities) | ⚠️ Tehditler (Threats) |
| :--- | :--- |
| {swot_o.replace('- ', '')} | {swot_t.replace('- ', '')} |

---

## 💰 2. Finansal Planlama ve Gelir Modelleri

### 💵 Gelir Kanalları
{monetization}

### 🏷️ Fiyatlandırma Modeli
{pricing}

### 📊 Tahmini Operasyonel Giderler
| Gider Kalemi | Tutar | Sıklık |
| :--- | :--- | :--- |
{costs}

### 💡 Finansal İpuçları
{fin_tips}

---

## 🏗️ 3. Teknik Mimari ve Teknoloji Yığını

### 🛠️ Teknoloji Seçimleri (Tech Stack)
* **Frontend:** {frontend_tech}
* **Backend:** {backend_tech}
* **Database:** {db_tech}
* **Cloud & Hosting:** {host_tech}
* **AI & LLM Services:** {ai_tech}

### 🔌 Kritik API Uç Noktaları (Endpoints)
{endpoints}

### 📈 Mimari Özet
{tech.get('architecture_summary', 'Genel mimari şablonu hazırlanıyor.')}
"""
        return report
