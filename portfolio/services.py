from typing import Any, Dict


class AskAIService:
    @staticmethod
    def get_status_payload() -> Dict[str, Any]:
        return {
            "detail": "AI chatbot integration is not implemented yet.",
            "status": "not_implemented",
            "planned_provider": "OpenAI or local model",
            "knowledge_base_scope": [
                "projects",
                "skills",
                "experience",
                "case studies",
            ],
        }


class PredictService:
    @staticmethod
    def get_status_payload() -> Dict[str, Any]:
        return {
            "detail": "MLflow prediction demo is not implemented yet.",
            "status": "not_implemented",
            "planned_model": "simple logistics model",
            "planned_endpoint": "/api/predict",
        }
