from tp2_is1.services.llm.strategy import Strategy


class GeminiStrategy(Strategy):
    URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        self.api_key = api_key
        self.model = model

    def generate_response(self, question) -> str:
        data = self.post_json(
            self.URL.format(model=self.model),
            {"contents": [{"parts": [{"text": self.build_prompt(question)}]}]},
            {"x-goog-api-key": self.api_key},
        )
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
