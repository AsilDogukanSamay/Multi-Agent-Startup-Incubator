import unittest
import asyncio
from backend.app.agents.base import SharedMemory, BaseAgent
from backend.app.orchestrator import Orchestrator

class MockAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=name, system_instruction="Mock")

    def run(self, memory: SharedMemory):
        memory.add_log(self.name, f"{self.name} çalıştı.")
        return f"{self.name} sonucu"

class TestAgentsAndMemory(unittest.TestCase):
    def test_shared_memory_logging(self):
        """SharedMemory log ekleme özelliğini doğrular."""
        memory = SharedMemory(startup_idea="Test Fikri")
        self.assertEqual(memory.startup_idea, "Test Fikri")
        self.assertEqual(len(memory.agent_logs), 0)

        memory.add_log("TestAgent", "Log mesajı", {"data_key": "data_val"})
        self.assertEqual(len(memory.agent_logs), 1)
        self.assertEqual(memory.agent_logs[0]["agent"], "TestAgent")
        self.assertEqual(memory.agent_logs[0]["message"], "Log mesajı")
        self.assertEqual(memory.agent_logs[0]["data"]["data_key"], "data_val")

    def test_base_agent_mock_output(self):
        """API anahtarı eksik olduğunda BaseAgent'ın mock/hata döndürdüğünü doğrular."""
        agent = MockAgent("TestMockAgent")
        memory = SharedMemory(startup_idea="Test Fikri")
        
        # Test direct gemini call fallback behavior
        output = agent._call_gemini("Merhaba")
        self.assertIn("MOCK MODE", output)

    def test_orchestrator_compilation(self):
        """Orchestrator'ın nihai raporu derleme (formatting) fonksiyonunu doğrular."""
        orchestrator = Orchestrator()
        memory = SharedMemory(startup_idea="Kahve Otomatı")
        
        # Set mock results
        memory.market_research = {
            "target_audience": ["Kahveseverler"],
            "market_trends": ["Hızlı tüketim"],
            "competitors": [{"name": "Kahve Zincirleri", "advantage": "Marka", "disadvantage": "Hız"}],
            "swot": {"strengths": ["Hızlı"], "weaknesses": ["Pahalı"], "opportunities": ["Yeni pazarlar"], "threats": ["Rakipler"]}
        }
        memory.financial_plan = {
            "monetization_models": ["Satış"],
            "pricing_tiers": [{"tier_name": "Espresso", "price": "50 TL", "features": ["Sıcak"]}],
            "estimated_costs": [{"item": "Sunucu", "amount": "100 TL", "frequency": "Aylık"}],
            "financial_tips": ["İpucu"]
        }
        memory.technical_architecture = {
            "tech_stack": {"frontend": ["HTML"], "backend": ["Python"], "database": ["SQL"], "cloud_hosting": ["Cloud"], "ai_models": ["Model"]},
            "database_schema": [{"table_name": "test_table", "columns": ["id"]}],
            "api_endpoints": [{"method": "GET", "path": "/test", "description": "test desc"}],
            "architecture_summary": "Test mimari"
        }

        report = orchestrator._generate_final_report(memory)
        
        self.assertIn("Kahve Otomatı", report)
        self.assertIn("Pazar Araştırması", report)
        self.assertIn("Kahveseverler", report)
        self.assertIn("Espresso", report)
        self.assertIn("Test mimari", report)

if __name__ == "__main__":
    unittest.main()
