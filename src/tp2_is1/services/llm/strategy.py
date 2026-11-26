import json
import urllib.request
from abc import ABC, abstractmethod


class Strategy(ABC):
    """Interfaz Strategy: cada proveedor de LLM implementa generate_response."""

    #: identificador del modelo, se guarda en AgentAI.model
    model: str = ""

    @abstractmethod
    def generate_response(self, question) -> str:
        """Devuelve el texto de la respuesta para una Question."""

    @staticmethod
    def build_prompt(question) -> str:
        tags = ", ".join(t.name for t in question.tags) or "-"
        return (
            "Respondé en español, de forma clara y concisa, la siguiente pregunta "
            "de un estudiante universitario.\n"
            f"Categoría: {question.category.name}\n"
            f"Etiquetas: {tags}\n"
            f"Título: {question.title}\n"
            f"Detalle: {question.body}"
        )

    @staticmethod
    def post_json(url: str, payload: dict, headers: dict, timeout: int = 30) -> dict:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", **headers},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
