from core.logger import JarvisLogger


class WakeWord:

    def __init__(self):

        self.aliases = [

            "jarvis",

            "hey jarvis",

            "hi jarvis",

            "hello jarvis",

            "ok jarvis",

            "okay jarvis",

            "yo jarvis",

            "hey jars",

            "jarvis please",

            "jarvis listen"

        ]

        self.last_detection = ""


    # =====================================

    def normalize(self, text):

        if not text:

            return ""

        text = text.lower().strip()

        text = " ".join(text.split())

        return text


    # =====================================

    def detect(self, text):

        text = self.normalize(text)

        if not text:

            return False

        if text == self.last_detection:

            return False

        for wake in self.aliases:

            if wake in text:

                self.last_detection = text

                JarvisLogger.success(

                    f"Wake Word Detected : {wake}"

                )

                return True

        return False


    # =====================================

    def remove_wake_word(self, text):

        text = self.normalize(text)

        for wake in self.aliases:

            if wake in text:

                text = text.replace(

                    wake,

                    "",

                    1

                ).strip()

                break

        return text


    # =====================================

    def add_alias(self, alias):

        alias = self.normalize(alias)

        if alias and alias not in self.aliases:

            self.aliases.append(alias)

            JarvisLogger.info(

                f"Wake Alias Added : {alias}"

            )


    # =====================================

    def get_aliases(self):

        return self.aliases.copy()


    # =====================================

    def reset(self):

        self.last_detection = ""