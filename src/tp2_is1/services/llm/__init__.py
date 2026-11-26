from tp2_is1.services.llm.gemini_strategy import GeminiStrategy
from tp2_is1.services.llm.openai_strategy import OpenAIStrategy
from tp2_is1.services.llm.strategy import Strategy

__all__ = ["GeminiStrategy", "OpenAIStrategy", "Strategy", "strategy_from_config"]


def strategy_from_config(cfg) -> Strategy:
    """Elige el proveedor según LLM_PROVIDER; la lógica de dominio no conoce la clase concreta."""
    provider = cfg.get('LLM_PROVIDER', 'openai')
    if provider == 'openai':
        return OpenAIStrategy(cfg['OPENAI_API_KEY'])
    if provider == 'gemini':
        return GeminiStrategy(cfg['GEMINI_API_KEY'])
    raise ValueError(f"LLM_PROVIDER desconocido: {provider}")
