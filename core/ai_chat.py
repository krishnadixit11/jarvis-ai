import requests

from core.logger import JarvisLogger


class AIChat:

    def __init__(self):

        self.model = "qwen2.5:1.5b"

        self.url = "http://localhost:11434/api/generate"


    def ask(self, message):

        try:

            JarvisLogger.info(
                "Asking Ollama AI..."
            )

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": message,
                    "stream": False
                }
            )


            data = response.json()


            answer = data.get(
                "response",
                "I could not understand."
            )


            return answer.strip()


        except Exception as e:

            JarvisLogger.error(
                str(e)
            )

            return "AI service is not available."