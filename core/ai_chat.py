import requests

from core.logger import JarvisLogger
from config import (
    OLLAMA_MODEL,
    OLLAMA_HOST,
    REQUEST_TIMEOUT
)


class AIChat:

    def __init__(self):

        self.model = OLLAMA_MODEL

        self.url = f"{OLLAMA_HOST}/api/generate"

    # =====================================
    # Ask Ollama
    # =====================================

    def ask(self, message):

        if not message.strip():
            return "Please ask something."

        try:

            JarvisLogger.info(
                f"AI Question : {message}"
            )

            response = requests.post(

                self.url,

                json={

                    "model": self.model,

                    "prompt": message,

                    "stream": False

                },

                timeout=AI_TIMEOUT

            )

            response.raise_for_status()

            data = response.json()

            answer = data.get(
                "response",
                ""
            ).strip()

            if not answer:

                JarvisLogger.error(
                    "Empty response received from Ollama."
                )

                return "I couldn't generate a response."

            JarvisLogger.success(
                "AI Response Generated Successfully."
            )

            return answer

        except requests.exceptions.ConnectionError:

            JarvisLogger.error(
                "Unable to connect to Ollama."
            )

            return (
                "Ollama is not running. "
                "Please start Ollama first."
            )

        except requests.exceptions.Timeout:

            JarvisLogger.error(
                "Ollama request timed out."
            )

            return (
                "The AI took too long to respond."
            )

        except requests.exceptions.HTTPError as e:

            JarvisLogger.error(
                f"HTTP Error : {e}"
            )

            return "AI server returned an error."

        except Exception as e:

            JarvisLogger.error(
                f"AI Error : {e}"
            )

            return "AI service is currently unavailable."