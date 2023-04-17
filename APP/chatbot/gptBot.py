import openai
from APP.dataModels.dataModels import GptResponse


class GptBot:

    def __init__(self, engine, max_tokens, temperature, api_key):
        self.engine = engine
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.api_key = api_key

    def generate_response(self, prompt):
        try:
            openai.api_key = self.api_key
            response = openai.Completion.create(
                engine=self.engine,
                prompt=prompt,
                max_tokens=self.max_tokens,
                n=1,
                stop=None,
                temperature=self.temperature
            )
            GptResponse.error = False
            GptResponse.response = response['choices'][0]['text']
            GptResponse.tokens = response['usage']['total_tokens']

        except Exception:
            GptResponse.error = True

        return GptResponse
