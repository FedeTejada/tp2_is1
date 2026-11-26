from tp2_is1.services.llm.strategy import Strategy


class OpenAIStrategy(Strategy):
    URL = "https://api.openai.com/v1/chat/completions"

    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.model = model

    def generate_response(self, question) -> str:
        data = self.post_json(
            self.URL,
            {
                "model": self.model,
                "messages": [{"role": "user", "content": self.build_prompt(question)}],
            },
            {"Authorization": f"Bearer {self.api_key}"},
        )
        return data["choices"][0]["message"]["content"].strip()
