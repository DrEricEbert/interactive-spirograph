# Interactive spirograph implemented in Python using PyQt6 and as WebApp using Nodejs and Express

## Python-Script
Python-Programm, das PyQt6 verwendet und einen interaktiven Spirographen implementiert. Du kannst die Parameter des Spirographen:

– den großen Radius (R)
- den kleinen Radius (r)
- und den Abstand (d)

über Slider verändern. Bei jeder Anpassung wird der Spirograph neu gezeichnet.

### Erklärung
SpiroWidget:
-   Dieses QWidget übernimmt das Zeichnen des Spirographen in der paintEvent-Methode. Die Spirograph-Gleichungen
  
    $x(t) = (R - r) \cos(t) + d \cos\left(\frac{R - r}{r} t\right)$

    $y(t) = (R - r) \sin(t) - d \sin\left(\frac{R - r}{r} t\right)$

    werden verwendet, um die Punkte zu berechnen. Einfache Skalierung und Zentrierung wird durchgeführt, damit die Kurve immer schön dargestellt wird.

MainWindow:
-   Das Hauptfenster enthält neben der Zeichenfläche (SpiroWidget) drei vertikale Slider, mit denen die Parameter R, r und d interaktiv verändert werden können. Bei jeder Änderung der Slider wird das SpiroWidget aktualisiert.

Start:
-   Der Standard-PyQt6-Code sorgt dafür, dass das Fenster angezeigt wird.
