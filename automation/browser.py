import webbrowser
from urllib.parse import quote_plus

from core.logger import JarvisLogger


class BrowserAutomation:

    WEBSITES = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
        "linkedin": "https://www.linkedin.com",
        "gmail": "https://mail.google.com",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "reddit": "https://www.reddit.com",
    }

    @classmethod
    def open_website(cls, website):
        website = website.lower().strip()

        if website not in cls.WEBSITES:
            return f"Sorry, I don't know {website}."

        url = cls.WEBSITES[website]

        JarvisLogger.info(f"Opening {website}")
        print(f"Opening URL: {url}")

        result = webbrowser.open(url)

        print(f"Browser Result: {result}")

        return f"Opening {website.title()}."

    @staticmethod
    def google_search(query):
        query = query.strip()

        url = f"https://www.google.com/search?q={quote_plus(query)}"

        JarvisLogger.info(f"Google Search: {query}")
        print(f"Opening URL: {url}")

        result = webbrowser.open(url)

        print(f"Browser Result: {result}")

        return f"Searching Google for {query}."

    @staticmethod
    def youtube_search(query):
        query = query.strip()

        url = (
            f"https://www.youtube.com/results?"
            f"search_query={quote_plus(query)}"
        )

        JarvisLogger.info(f"YouTube Search: {query}")
        print(f"Opening URL: {url}")

        result = webbrowser.open(url)

        print(f"Browser Result: {result}")

        return f"Searching YouTube for {query}."