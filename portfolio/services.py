from typing import Any, Dict, List

from .data import AUTHOR, CASE_STUDIES, PROJECTS, SKILLS


class AskAIService:
    @staticmethod
    def build_answer(message: str) -> Dict[str, Any]:
        normalized_message = (message or "").strip().lower()
        if not normalized_message:
            return {
                "answer": "Ask about my projects, skills, case studies, or backend/AI experience.",
                "intent": "fallback",
            }

        if any(keyword in normalized_message for keyword in ["project", "projects", "built", "build"]):
            project_titles = ", ".join(project["title"] for project in PROJECTS)
            return {
                "answer": f"I built {project_titles}.",
                "intent": "projects",
            }

        if any(keyword in normalized_message for keyword in ["skill", "stack", "technology", "technologies"]):
            skill_names = ", ".join(skill["name"] for skill in SKILLS[:8])
            return {
                "answer": f"My core stack includes {skill_names}.",
                "intent": "skills",
            }

        if any(keyword in normalized_message for keyword in ["case", "architecture", "rag", "latency"]):
            case_titles = ", ".join(case_study["title"] for case_study in CASE_STUDIES)
            return {
                "answer": f"My main engineering case studies are {case_titles}.",
                "intent": "case_studies",
            }

        return {
            "answer": AUTHOR["hero_summary"]["en"],
            "intent": "fallback",
        }


class ExperimentService:
    @staticmethod
    def list_experiments() -> Dict[str, List[Dict[str, Any]]]:
        return {
            "experiments": [
                {
                    "name": "logistics-price-model",
                    "accuracy": 0.91,
                    "model_version": "v1.3",
                    "stage": "staging",
                },
                {
                    "name": "project-complexity-estimator",
                    "accuracy": 0.87,
                    "model_version": "v0.9",
                    "stage": "demo",
                },
            ]
        }


class PredictService:
    @staticmethod
    def predict_complexity(team_size: int, duration_months: int, ai_features: bool) -> Dict[str, Any]:
        score = 0.2
        score += min(team_size, 10) * 0.05
        score += min(duration_months, 12) * 0.03
        if ai_features:
            score += 0.25

        complexity_score = round(min(score, 0.99), 2)
        if complexity_score < 0.45:
            risk_level = "low"
        elif complexity_score < 0.75:
            risk_level = "medium"
        else:
            risk_level = "high"

        return {
            "complexity_score": complexity_score,
            "risk_level": risk_level,
            "recommended_team": max(team_size, 2 if complexity_score < 0.45 else 4 if complexity_score < 0.75 else 6),
        }
