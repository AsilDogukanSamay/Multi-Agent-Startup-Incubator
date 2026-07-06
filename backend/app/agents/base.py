import datetime
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import google.generativeai as genai
from backend.app.config import settings

# Initialize Gemini API
if settings.gemini_api_key and settings.gemini_api_key != "your_gemini_api_key_here":
    genai.configure(api_key=settings.gemini_api_key)

class SharedMemory(BaseModel):
    """
    Ortak Hafıza (Shared Memory) sınıfı.
    Ajanlar arası veri paylaşımını ve tüm analiz adımlarını saklar.
    """
    startup_idea: str
    market_research: Optional[Dict[str, Any]] = None
    financial_plan: Optional[Dict[str, Any]] = None
    technical_architecture: Optional[Dict[str, Any]] = None
    final_report: Optional[str] = None
    agent_logs: List[Dict[str, Any]] = Field(default_factory=list)

    def add_log(self, agent_name: str, message: str, data: Optional[Any] = None):
        self.agent_logs.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "agent": agent_name,
            "message": message,
            "data": data
        })

class BaseAgent:
    """
    Tüm özelleştirilmiş yapay zeka ajanlarının türeyeceği temel sınıf.
    """
    def __init__(self, name: str, system_instruction: str, model_name: str = "gemini-2.5-flash"):
        self.name = name
        self.system_instruction = system_instruction
        self.model_name = model_name

    def _call_gemini(self, prompt: str) -> str:
        """
        Gemini API'sini güvenli bir şekilde çağırır.
        API anahtarı eksik veya hatalıysa mock veri veya açıklayıcı hata döner.
        """
        if not settings.gemini_api_key or settings.gemini_api_key == "your_gemini_api_key_here":
            return f"[MOCK MODE - API KEY MISSING] {self.name} için analiz simüle ediliyor...\n(Lütfen .env dosyasına geçerli bir GEMINI_API_KEY ekleyin.)"
        
        try:
            model = genai.GenerativeModel(
                model_name=self.model_name,
                system_instruction=self.system_instruction
            )
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"[ERROR - API CALL FAILED] {self.name} çalışırken hata oluştu: {str(e)}"

    def run(self, memory: SharedMemory) -> Any:
        """
        Her ajanın kendi özel mantığına göre uygulayacağı ana metod.
        """
        raise NotImplementedError("Ajanlar 'run' metodunu uygulamalıdır.")
