from ollama import chat

from core.logger import JarvisLogger


class ChatAI:

    def __init__(self):

        self.model = "qwen2.5:1.5b"

        self.system_prompt = """
You are JARVIS.

You are Krishna's personal AI assistant.

Rules:

- Be intelligent.
- Be concise.
- Be friendly.
- Answer naturally.
- Never mention you are ChatGPT.
- Call the user Krishna whenever appropriate.
- If you don't know something, say so honestly.
- Give practical answers.
"""

        self.history = [

            {
                "role": "system",
                "content": self.system_prompt
            }

        ]

        JarvisLogger.success(
            f"AI Model Loaded : {self.model}"
        )

    # ======================================

    def ask(self, question: str):

        try:

            JarvisLogger.info(
                f"AI Question : {question}"
            )

            self.history.append(

                {
                    "role": "user",
                    "content": question
                }

            )

            response = chat(

                model=self.model,

                messages=self.history

            )

            answer = response["message"]["content"].strip()

            self.history.append(

                {
                    "role": "assistant",
                    "content": answer
                }

            )

            # Prevent unlimited history growth

            if len(self.history) > 20:

                self.history = [

                    self.history[0]

                ] + self.history[-18:]

            JarvisLogger.success(
                "AI Response Generated."
            )

            return answer

        except Exception as e:

            JarvisLogger.error(
                f"AI Error : {e}"
            )

            return (
                "Sorry Krishna, I am unable to answer right now."
            )

    # ======================================

    def clear_history(self):

        self.history = [

            {
                "role": "system",
                "content": self.system_prompt
            }

        ]

        JarvisLogger.info(
            "AI Conversation Cleared."
        )