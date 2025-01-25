#!/usr/bin/python3
# coding: utf-8

import sys
import time
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QColor

def interpolate_color(color1, color2, factor: float):
    """Interpolate between two colors with a given factor (0.0 - 1.0)."""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return QColor(r, g, b)

class ClockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clock App')
        self.setGeometry(100, 100, 600, 200)
        self.setStyleSheet("background-color: black;")

        self.layout = QVBoxLayout()
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(QFont('Arial', 100))
        self.layout.addWidget(self.time_label)
        self.setLayout(self.layout)

        self.current_color = QColor(0, 255, 255)  # Initial color (light blue)
        self.target_color = QColor(255, 0, 255)   # Initial target color (magenta)
        self.step = 0.0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_time)
        self.timer.start(100)

    def refresh_time(self):
        # Update the label text
        self.time_label.setText(time.strftime('%H:%M:%S'))

        # Interpolate the color
        new_color = interpolate_color(self.current_color.getRgb()[:3], self.target_color.getRgb()[:3], self.step)
        self.time_label.setStyleSheet(f"color: {new_color.name()};")

        # Update the step and check if we need to pick a new target color
        self.step += 0.01
        if self.step >= 1.0:
            self.step = 0.0
            self.current_color = self.target_color
            self.target_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = ClockApp()
    clock.show()
    sys.exit(app.exec_())