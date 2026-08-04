import math

from PySide6.QtCore import (
    Qt,
    QRectF,
    QPointF,
    QTimer
)

from PySide6.QtGui import (
    QColor,
    QPainter,
    QPen,
    QBrush,
    QRadialGradient
)

from PySide6.QtWidgets import QWidget


class OrbWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedSize(270, 270)

        # ===========================
        # Animation Variables
        # ===========================

        self.rotation = 0.0

        self.inner_rotation = 0.0

        self.outer_rotation = 0.0

        self.pulse = 0.0

        self.glow = 30

        self.glow_direction = 1

        self.wave = 0

        # ===========================
        # Timer (60 FPS)
        # ===========================

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(16)

    # =====================================================

    def animate(self):

        self.rotation += 1.5

        self.inner_rotation += 2.5

        self.outer_rotation -= 0.8

        self.pulse += 0.08

        self.wave += 0.04

        self.glow += self.glow_direction * 1.2

        if self.glow >= 80:

            self.glow_direction = -1

        elif self.glow <= 20:

            self.glow_direction = 1

        if self.rotation >= 360:

            self.rotation = 0

        if self.inner_rotation >= 360:

            self.inner_rotation = 0

        if self.outer_rotation <= -360:

            self.outer_rotation = 0

        self.update()

    # =====================================================

    def draw_glow(self, painter):

        for i in range(14):

            alpha = max(
                2,
                18 - i
            )

            pen = QPen(

                QColor(

                    0,

                    255,

                    255,

                    alpha

                )

            )

            pen.setWidth(

                42 - i * 3

            )

            painter.setPen(pen)

            painter.setBrush(Qt.NoBrush)

            painter.drawEllipse(

                QRectF(

                    20,

                    20,

                    230,

                    230

                )

            )

    # =====================================================

    def draw_main_orb(self, painter):

        pulse = math.sin(self.pulse) * 3

        radius = 108 + pulse

        gradient = QRadialGradient(

            QPointF(135, 135),

            radius

        )

        gradient.setColorAt(

            0,

            QColor(

                90,

                255,

                255

            )

        )

        gradient.setColorAt(

            0.40,

            QColor(

                0,

                210,

                255

            )

        )

        gradient.setColorAt(

            0.80,

            QColor(

                0,

                70,

                120

            )

        )

        gradient.setColorAt(

            1,

            QColor(

                5,

                15,

                30

            )

        )

        painter.setBrush(

            QBrush(

                gradient

            )

        )

        pen = QPen(

            QColor(

                0,

                255,

                255,

                180 + int(self.glow)

            )

        )

        pen.setWidth(4)

        painter.setPen(pen)

        painter.drawEllipse(

            QRectF(

                27,

                27,

                216,

                216

            )

        )

    # =====================================================

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        painter.setRenderHint(
            QPainter.SmoothPixmapTransform
        )

        self.draw_glow(painter)

        self.draw_main_orb(painter)

                # =====================================================
        # OUTER HUD RING
        # =====================================================

        hud_pen = QPen(
            QColor(0, 255, 255, 150)
        )
        hud_pen.setWidth(3)

        painter.setPen(hud_pen)

        painter.setBrush(Qt.NoBrush)

        for i in range(8):

            start = self.outer_rotation + (i * 45)

            painter.drawArc(

                QRectF(
                    10,
                    10,
                    250,
                    250
                ),

                int(start * 16),

                int(20 * 16)

            )

        # =====================================================
        # INNER ROTATING RING
        # =====================================================

        inner_pen = QPen(
            QColor(0, 200, 255, 180)
        )

        inner_pen.setWidth(2)

        painter.setPen(inner_pen)

        for i in range(12):

            start = self.inner_rotation + (i * 30)

            painter.drawArc(

                QRectF(
                    38,
                    38,
                    194,
                    194
                ),

                int(start * 16),

                int(12 * 16)

            )

        # =====================================================
        # CENTER ENERGY CORE
        # =====================================================

        core_size = 34 + math.sin(self.wave) * 3

        core_gradient = QRadialGradient(
            QPointF(135, 135),
            core_size
        )

        core_gradient.setColorAt(
            0,
            QColor(255, 255, 255)
        )

        core_gradient.setColorAt(
            0.4,
            QColor(0, 255, 255)
        )

        core_gradient.setColorAt(
            1,
            QColor(0, 120, 255)
        )

        painter.setPen(Qt.NoPen)

        painter.setBrush(
            QBrush(core_gradient)
        )

        painter.drawEllipse(

            QPointF(
                135,
                135
            ),

            core_size,

            core_size

        )

        # =====================================================
        # ROTATING DOT
        # =====================================================

        angle = math.radians(self.rotation)

        radius = 118

        x = 135 + math.cos(angle) * radius

        y = 135 + math.sin(angle) * radius

        painter.setBrush(
            QColor(
                0,
                255,
                255
            )
        )

        painter.drawEllipse(

            QPointF(x, y),

            6,

            6

        )

        # =====================================================
        # SMALL PARTICLES
        # =====================================================

        particle_pen = QPen(
            QColor(
                0,
                255,
                255,
                170
            )
        )

        painter.setPen(Qt.NoPen)

        painter.setBrush(
            QColor(
                0,
                255,
                255,
                120
            )
        )

        for i in range(18):

            a = math.radians(
                self.rotation * 1.5 + i * 20
            )

            r = 78 + math.sin(
                self.wave + i
            ) * 6

            px = 135 + math.cos(a) * r

            py = 135 + math.sin(a) * r

            painter.drawEllipse(

                QPointF(
                    px,
                    py
                ),

                2.5,

                2.5

            )

        # =====================================================
        # CROSS LINES
        # =====================================================

        cross_pen = QPen(
            QColor(
                0,
                255,
                255,
                45
            )
        )

        cross_pen.setWidth(1)

        painter.setPen(cross_pen)

        painter.drawLine(
            135,
            18,
            135,
            252
        )

        painter.drawLine(
            18,
            135,
            252,
            135
        )

        # =====================================================
        # FINAL GLOW
        # =====================================================

        glow_pen = QPen(
            QColor(
                0,
                255,
                255,
                90
            )
        )

        glow_pen.setWidth(2)

        painter.setPen(glow_pen)

        painter.drawEllipse(
            QRectF(
                24,
                24,
                222,
                222
            )
        )