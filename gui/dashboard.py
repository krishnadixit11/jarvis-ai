from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGraphicsDropShadowEffect
)

from gui.animation import OrbAnimation
from gui.orb import OrbWidget
from gui.signals import signals


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.setup_window()

        self.apply_style()

        self.setup_ui()

        self.center_window()

        self.connect_signals()

    # =====================================================

    def setup_window(self):

        self.resize(430, 560)

        self.setMinimumSize(430, 560)

        self.setWindowTitle("JARVIS AI")

        self.setWindowFlag(Qt.Window)

    # =====================================================

    def apply_style(self):

        self.setStyleSheet("""

        QWidget{

            background:#070B14;

            color:white;

            font-family:'Segoe UI';

        }

        QLabel{

            background:transparent;

            color:white;

        }

        """)

    # =====================================================

    def center_window(self):

        screen = self.screen()

        if screen:

            geometry = screen.availableGeometry()

            x = geometry.center().x() - self.width() // 2

            y = geometry.center().y() - self.height() // 2

            self.move(x, y)

    # =====================================================

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setAlignment(Qt.AlignCenter)

        layout.setSpacing(20)

        layout.setContentsMargins(30, 30, 30, 30)

        # ===========================================
        # Title
        # ===========================================

        self.title = QLabel("JARVIS")

        self.title.setAlignment(Qt.AlignCenter)

        self.title.setFont(

            QFont(

                "Segoe UI",

                30,

                QFont.Bold

            )

        )

        self.title.setStyleSheet("""

        color:#00E5FF;

        """)

        # ===========================================
        # Status
        # ===========================================

        self.status = QLabel("System Ready")

        self.status.setAlignment(Qt.AlignCenter)

        self.status.setFont(

            QFont(

                "Segoe UI",

                12

            )

        )

        self.status.setStyleSheet("""

        color:#BBBBBB;

        """)

        # ===========================================
        # Orb
        # ===========================================

        self.orb = OrbWidget()

        shadow = QGraphicsDropShadowEffect()

        shadow.setBlurRadius(50)

        shadow.setOffset(0)

        shadow.setColor(Qt.cyan)

        self.orb.setGraphicsEffect(shadow)

        # ===========================================
        # Footer
        # ===========================================

        self.footer = QLabel(

            "Artificial Intelligence Assistant"

        )

        self.footer.setAlignment(Qt.AlignCenter)

        self.footer.setFont(

            QFont(

                "Segoe UI",

                10

            )

        )

        self.footer.setStyleSheet("""

        color:#777777;

        """)

        # ===========================================

        layout.addStretch()

        layout.addWidget(self.title)

        layout.addSpacing(5)

        layout.addWidget(self.status)

        layout.addSpacing(20)

        layout.addWidget(

            self.orb,

            alignment=Qt.AlignCenter

        )

        layout.addSpacing(20)

        layout.addWidget(self.footer)

        layout.addStretch()

        # ===========================================

        self.animation = OrbAnimation(self.orb)

        self.animation.breathing()

    # =====================================================

    def connect_signals(self):

        signals.ready.connect(self.set_ready)

        signals.listening.connect(self.set_listening)

        signals.thinking.connect(self.set_thinking)

        signals.speaking.connect(self.set_speaking)

        signals.status.connect(self.update_status)

    # =====================================================

    def update_status(self, text):

        self.status.setText(text)

    # =====================================================

    def set_ready(self):

        self.status.setText("System Ready")

        self.status.setStyleSheet(

            "color:#BBBBBB;"

        )

        self.animation.breathing()

    # =====================================================

    def set_listening(self):

        self.status.setText("Listening...")

        self.status.setStyleSheet(

            "color:#00E5FF;"

        )

        self.animation.listening()

    # =====================================================

    def set_thinking(self):

        self.status.setText("Thinking...")

        self.status.setStyleSheet(

            "color:#FFB300;"

        )

        self.animation.thinking()

    # =====================================================

    def set_speaking(self):

        self.status.setText("Speaking...")

        self.status.setStyleSheet(

            "color:#4CAF50;"

        )

        self.animation.speaking()