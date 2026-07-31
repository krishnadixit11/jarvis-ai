from ollama import chat

from core.logger import JarvisLogger


class ChatAI:

    def __init__(self):
        self.model = "qwen2.5:1.5b"

    def ask(self, question):

        try:
            JarvisLogger.info(f"AI Question: {question}")

            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as e:
            JarvisLogger.error(f"AI Error: {e}")
            return "Sorry Krishna, I am unable to answer right now."