# Interactive spirograph implemented in Python using PyQt6 and as WebApp using Nodejs and Express

## Python-Script
Python-Programm, das PyQt6 verwendet und einen interaktiven Spirographen implementiert. Du kannst die Parameter des Spirographen:

- den großen Radius (R)
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

## Nodejs-WebApp
Interaktiven Spirographen als Webanwendung

Dabei wird ein Node.js-Server (mithilfe von Express) verwendet, der statische Dateien (HTML, CSS, JavaScript) ausliefert. In der Web‑App kannst du über Schieberegler (Range Inputs) die Parameter des Spirographen anpassen und die Änderung wird sofort im Canvas neu gezeichnet.

Installiere die Abhängigkeiten und navigiere dazu in das Verzeichnis der Webanwendung und führe aus:

```npm install```

Starte den Node.js-Server:

```npm start```

Öffne deinen Browser und gehe zu http://localhost:3000 und du solltest den interaktiven Spirographen sehen.

Jetzt hast du eine komplette Node.js-Webanwendung, in der ein interaktiver Spirograph dargestellt wird und dessen Parameter (großer Radius, kleiner Radius und Pen-Abstand) über Schieberegler angepasst werden können.
