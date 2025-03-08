import sys
import math

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSlider,
    QLabel,
)
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QRectF


class SpiroWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Standard-Parameter (als ganze Zahlen für einfache GCD-Berechnung)
        self.big_radius = 150    # R
        self.small_radius = 50   # r
        self.pen_distance = 70   # d

        # Für bessere Darstellung wird ein Rand hinzugefügt
        self.margin = 20

    def set_big_radius(self, value: int):
        self.big_radius = value
        self.update()

    def set_small_radius(self, value: int):
        self.small_radius = value
        self.update()

    def set_pen_distance(self, value: int):
        self.pen_distance = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Hintergrund weiß füllen
        painter.fillRect(self.rect(), Qt.GlobalColor.white)

        # Stift konfigurieren
        pen = QPen(Qt.GlobalColor.darkBlue)
        pen.setWidth(2)
        painter.setPen(pen)

        # Mittelpunkt des Widgets bestimmen
        center_x = self.width() // 2
        center_y = self.height() // 2

        # Berechne den Spirograph
        R = self.big_radius
        r = self.small_radius
        d = self.pen_distance

        # Um den Spirograph vollständig zu zeichnen, benutzen wir die Periode:
        # t_end = 2*pi * (kleiner Radius / gcd(R, r))
        # Wir konvertieren R und r zu int für die Bestimmung des ggT.
        gcd_val = math.gcd(int(R), int(r))
        # Schützen gegen Division durch 0, falls r == 0 sein sollte:
        if r == 0:
            t_end = 2 * math.pi
        else:
            t_end = 2 * math.pi * r / gcd_val

        # Wir bestimmen die Anzahl der Schritte, um eine glatte Kurve zu erhalten.
        steps = 2000
        dt = t_end / steps

        # Liste der Punkte berechnen
        points = []
        t = 0.0
        while t <= t_end:
            # Spirograph-Gleichungen
            # x = (R - r) * cos(t) + d * cos(((R - r) / r) * t)
            # y = (R - r) * sin(t) - d * sin(((R - r) / r) * t)
            x = (R - r) * math.cos(t) + d * math.cos(((R - r) / r) * t)
            y = (R - r) * math.sin(t) - d * math.sin(((R - r) / r) * t)
            points.append((x, y))
            t += dt

        # Finde den Bereich der Punkte, um ggf. zu skalieren (optional)
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        # Berechne Skalierung (optional, hier nicht zwingend nötig, da wir den Mittelpunkt nutzen)
        # Wir passen die Punkte so an, dass sie im Widget gut dargestellt werden.
        scale_x = (self.width() - 2 * self.margin) / (max_x - min_x) if max_x != min_x else 1
        scale_y = (self.height() - 2 * self.margin) / (max_y - min_y) if max_y != min_y else 1
        scale = min(scale_x, scale_y)

        # Verschiebe und skaliere die Punkte, sodass der Mittelpunkt in der Mitte liegt
        transformed_points = []
        for x, y in points:
            tx = (x - min_x) * scale + self.margin - ((max_x - min_x) * scale - (self.width() - 2 * self.margin)) / 2
            ty = (y - min_y) * scale + self.margin - ((max_y - min_y) * scale - (self.height() - 2 * self.margin)) / 2
            transformed_points.append((tx, ty))

        # Zeichne die Kurve
        if transformed_points:
            path = transformed_points
            prev_point = path[0]
            for point in path[1:]:
                painter.drawLine(int(prev_point[0] + center_x - self.width()//2),
                                 int(prev_point[1] + center_y - self.height()//2),
                                 int(point[0] + center_x - self.width()//2),
                                 int(point[1] + center_y - self.height()//2))
                prev_point = point


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interaktiver Spirograph mit PyQt6")

        # Zentrales Widget und Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Spirograph-Zeichenfläche
        self.spiro_widget = SpiroWidget()
        self.spiro_widget.setMinimumSize(400, 400)
        main_layout.addWidget(self.spiro_widget)

        # Erzeuge Slider zur Steuerung der Parameter
        sliders_layout = QHBoxLayout()

        # Slider für großen Radius (R)
        self.slider_big = QSlider(Qt.Orientation.Vertical)
        self.slider_big.setRange(50, 300)
        self.slider_big.setValue(self.spiro_widget.big_radius)
        self.slider_big.valueChanged.connect(self.spiro_widget.set_big_radius)
        slider_big_layout = QVBoxLayout()
        slider_big_layout.addWidget(QLabel("Großer Radius (R)"))
        slider_big_layout.addWidget(self.slider_big)
        sliders_layout.addLayout(slider_big_layout)

        # Slider für kleinen Radius (r)
        self.slider_small = QSlider(Qt.Orientation.Vertical)
        self.slider_small.setRange(10, 150)
        self.slider_small.setValue(self.spiro_widget.small_radius)
        self.slider_small.valueChanged.connect(self.spiro_widget.set_small_radius)
        slider_small_layout = QVBoxLayout()
        slider_small_layout.addWidget(QLabel("Kleiner Radius (r)"))
        slider_small_layout.addWidget(self.slider_small)
        sliders_layout.addLayout(slider_small_layout)

        # Slider für den Abstand (d)
        self.slider_d = QSlider(Qt.Orientation.Vertical)
        self.slider_d.setRange(0, 200)
        self.slider_d.setValue(self.spiro_widget.pen_distance)
        self.slider_d.valueChanged.connect(self.spiro_widget.set_pen_distance)
        slider_d_layout = QVBoxLayout()
        slider_d_layout.addWidget(QLabel("Abstand (d)"))
        slider_d_layout.addWidget(self.slider_d)
        sliders_layout.addLayout(slider_d_layout)

        main_layout.addLayout(sliders_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 600)
    window.show()
    sys.exit(app.exec())
