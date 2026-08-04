import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication

from core.logger import JarvisLogger
from gui.dashboard import Dashboard


class JarvisGUI:

    def __init__(self):

        QApplication.setAttribute(
            Qt.AA_EnableHighDpiScaling,
            True
        )

        QApplication.setAttribute(
            Qt.AA_UseHighDpiPixmaps,
            True
        )

        self.app = QApplication(sys.argv)

        self.configure_application()

        self.dashboard = Dashboard()

    # =====================================================

    def configure_application(self):

        self.app.setApplicationName(
            "JARVIS AI"
        )

        self.app.setApplicationDisplayName(
            "JARVIS AI Assistant"
        )

        self.app.setOrganizationName(
            "Krishna AI Labs"
        )

        self.app.setOrganizationDomain(
            "krishnaai.local"
        )

        self.app.setStyle("Fusion")

        self.app.setQuitOnLastWindowClosed(True)

        self.app.setFont(
            QFont(
                "Segoe UI",
                10
            )
        )

        icon_path = os.path.join(
            "assets",
            "icons",
            "jarvis.ico"
        )

        if os.path.exists(icon_path):

            self.app.setWindowIcon(
                QIcon(icon_path)
            )

        self.load_stylesheet()

        JarvisLogger.success(
            "GUI Initialized Successfully."
        )

    # =====================================================

    def load_stylesheet(self):

        self.app.setStyleSheet("""

            *{
                outline:none;
                color:white;
                font-family:'Segoe UI';
            }

            QWidget{
                background:#090B10;
                color:white;
            }

            QLabel{
                background:transparent;
                color:white;
            }

            QPushButton{

                background:#1A1F28;

                border:1px solid #303848;

                border-radius:10px;

                padding:8px 16px;

                font-size:10pt;
            }

            QPushButton:hover{

                background:#273244;

                border:1px solid #5B8CFF;

            }

            QPushButton:pressed{

                background:#10141C;

            }

            QLineEdit{

                background:#11161F;

                border:1px solid #2E3440;

                border-radius:8px;

                padding:6px;

            }

            QTextEdit{

                background:#11161F;

                border:1px solid #2E3440;

                border-radius:8px;

                padding:6px;

            }

            QScrollBar:vertical{

                background:#090B10;

                width:8px;

                margin:0px;

            }

            QScrollBar::handle:vertical{

                background:#3A4353;

                border-radius:4px;

            }

            QScrollBar::handle:vertical:hover{

                background:#5B8CFF;

            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical{

                height:0px;

            }

        """)

    # =====================================================

    def run(self):

        try:

            self.dashboard.show()

            JarvisLogger.success(
                "Dashboard Loaded."
            )

            sys.exit(
                self.app.exec()
            )

        except Exception as e:

            JarvisLogger.error(
                f"GUI Error : {e}"
            )


if __name__ == "__main__":

    JarvisGUI().run()