// Hole Referenzen zum Canvas und den Schiebereglern
const canvas = document.getElementById('spiroCanvas');
const ctx = canvas.getContext('2d');
const bigRadiusInput = document.getElementById('bigRadius');
const smallRadiusInput = document.getElementById('smallRadius');
const penDistanceInput = document.getElementById('penDistance');

const bigRadiusValue = document.getElementById('bigRadiusValue');
const smallRadiusValue = document.getElementById('smallRadiusValue');
const penDistanceValue = document.getElementById('penDistanceValue');

// Größe des Canvas festlegen
canvas.width = 600;
canvas.height = 600;

// Funktion, die den Spirograph basierend auf den aktuellen Parametern zeichnet
function drawSpirograph() {
  const R = parseFloat(bigRadiusInput.value);
  const r = parseFloat(smallRadiusInput.value);
  const d = parseFloat(penDistanceInput.value);

  // Update der Anzeige der Parameterwerte
  bigRadiusValue.textContent = R;
  smallRadiusValue.textContent = r;
  penDistanceValue.textContent = d;

  // Clear Canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Setze Zeichenstil
  ctx.strokeStyle = 'blue';
  ctx.lineWidth = 2;
  
  // Mittelpunkt des Canvas
  const cx = canvas.width / 2;
  const cy = canvas.height / 2;

  // Berechne den Endwert des Winkels t.
  // Um eine vollständige Kurve zu erhalten, wird der Zeitraum unter Verwendung
  // des kleinsten gemeinsamen Vielfachen bzw. eines Vielfachen des kleineren Radius
  // bestimmt. Hier verwenden wir t_end = (2 * Math.PI * r) / gcd(R, r).
  const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
  const divisor = r === 0 ? 1 : gcd(R, r);
  const t_end = r * 2 * Math.PI / divisor;
  
  // Anzahl der Schritte festlegen
  const steps = 2000;
  const dt = t_end / steps;

  ctx.beginPath();
  // Beginne an der Startposition
  let firstPoint = true;
  for (let i = 0, t = 0; i <= steps; i++, t += dt) {
    // Spirograph-Gleichungen
    let x = (R - r) * Math.cos(t) + d * Math.cos(((R - r) / r) * t);
    let y = (R - r) * Math.sin(t) - d * Math.sin(((R - r) / r) * t);
    
    // Verschiebe die Punkte in den Canvas-Mittelpunkt
    let drawX = cx + x;
    let drawY = cy + y;
    
    if (firstPoint) {
      ctx.moveTo(drawX, drawY);
      firstPoint = false;
    } else {
      ctx.lineTo(drawX, drawY);
    }
  }
  ctx.stroke();
}

// Event-Listener für die Schieberegler
bigRadiusInput.addEventListener('input', drawSpirograph);
smallRadiusInput.addEventListener('input', drawSpirograph);
penDistanceInput.addEventListener('input', drawSpirograph);

// Initiale Zeichnung
drawSpirograph();
