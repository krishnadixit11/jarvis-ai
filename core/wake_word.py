from core.logger import JarvisLogger


class WakeWord:

    def __init__(self):
        self.word = "jarvis"


    def detect(self, text):

        text = text.lower()

        if self.word in text:

            JarvisLogger.success(
                "Wake word detected"
            )

            return True

        return False