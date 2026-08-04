import webbrowser
from urllib.parse import quote_plus

from core.logger import JarvisLogger


class BrowserAutomation:

    WEBSITES = {

        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
        "linkedin": "https://www.linkedin.com",
        "gmail": "https://mail.google.com",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "reddit": "https://www.reddit.com",
        "twitter": "https://twitter.com",
        "x": "https://twitter.com",
        "amazon": "https://www.amazon.in",

    }

    ALIASES = {

        "yt": "youtube",
        "git": "github",
        "mail": "gmail",
        "insta": "instagram",
        "fb": "facebook",

    }

    # =====================================

    @classmethod
    def open_website(cls, website):

        website = website.lower().strip()

        website = cls.ALIASES.get(
            website,
            website
        )

        if website.endswith(".com"):

            url = f"https://{website}"

        elif website in cls.WEBSITES:

            url = cls.WEBSITES[website]

        else:

            return f"I don't know the website {website}."

        try:

            JarvisLogger.info(
                f"Opening Website : {url}"
            )

            webbrowser.open(
                url,
                new=2
            )

            JarvisLogger.success(
                f"{website} opened."
            )

            return f"Opening {website.title()}."

        except Exception as e:

            JarvisLogger.error(
                f"Browser Error : {e}"
            )

            return "Unable to open the website."

    # =====================================

    @staticmethod
    def google_search(query):

        query = query.strip()

        if not query:

            return "Please tell me what to search."

        url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        try:

            JarvisLogger.info(
                f"Google Search : {query}"
            )

            webbrowser.open(
                url,
                new=2
            )

            return f"Searching Google for {query}."

        except Exception as e:

            JarvisLogger.error(
                f"Google Search Error : {e}"
            )

            return "Unable to search Google."

    # =====================================

    @staticmethod
    def youtube_search(query):

        query = query.strip()

        if not query:

            return "Please tell me what to search."

        url = (
            "https://www.youtube.com/results?"
            "search_query="
            + quote_plus(query)
        )

        try:

            JarvisLogger.info(
                f"YouTube Search : {query}"
            )

            webbrowser.open(
                url,
                new=2
            )

            return f"Searching YouTube for {query}."

        except Exception as e:

            JarvisLogger.error(
                f"YouTube Search Error : {e}"
            )

            return "Unable to search YouTube."