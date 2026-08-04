from PySide6.QtCore import (
    QObject,
    QEasingCurve,
    QPropertyAnimation,
    QSize,
    QSequentialAnimationGroup
)


class OrbAnimation(QObject):

    def __init__(self, orb):

        super().__init__()

        self.orb = orb

        self.group = None

        self.default_size = QSize(260, 260)

    # =====================================================

    def stop(self):

        if self.group:

            self.group.stop()

            self.group.deleteLater()

            self.group = None

        self.orb.setMinimumSize(self.default_size)

        self.orb.setMaximumSize(self.default_size)

    # =====================================================

    def start_animation(

            self,

            minimum,

            maximum,

            duration

    ):

        self.stop()

        grow = QPropertyAnimation(

            self.orb,

            b"minimumSize"

        )

        grow.setDuration(duration)

        grow.setStartValue(

            QSize(minimum, minimum)

        )

        grow.setEndValue(

            QSize(maximum, maximum)

        )

        grow.setEasingCurve(

            QEasingCurve.InOutSine

        )

        shrink = QPropertyAnimation(

            self.orb,

            b"minimumSize"

        )

        shrink.setDuration(duration)

        shrink.setStartValue(

            QSize(maximum, maximum)

        )

        shrink.setEndValue(

            QSize(minimum, minimum)

        )

        shrink.setEasingCurve(

            QEasingCurve.InOutSine

        )

        self.group = QSequentialAnimationGroup()

        self.group.addAnimation(grow)

        self.group.addAnimation(shrink)

        self.group.setLoopCount(-1)

        self.group.start()

    # =====================================================
    # Idle
    # =====================================================

    def breathing(self):

        self.start_animation(

            minimum=258,

            maximum=262,

            duration=1200

        )

    # =====================================================
    # Listening
    # =====================================================

    def listening(self):

        self.start_animation(

            minimum=255,

            maximum=268,

            duration=550

        )

    # =====================================================
    # Thinking
    # =====================================================

    def thinking(self):

        self.start_animation(

            minimum=250,

            maximum=272,

            duration=350

        )

    # =====================================================
    # Speaking
    # =====================================================

    def speaking(self):

        self.start_animation(

            minimum=256,

            maximum=266,

            duration=220

        )