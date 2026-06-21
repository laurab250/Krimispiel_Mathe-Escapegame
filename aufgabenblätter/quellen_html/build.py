# -*- coding: utf-8 -*-
import os
OUT = "/home/tim/Downloads/tst/wsbuild"

CSS = r'''
@page { size:A4; margin:13mm 14mm 11mm 14mm; }
*{box-sizing:border-box;}
body{font-family:'Helvetica Neue',Arial,sans-serif;font-size:10.5pt;color:#111;line-height:1.42;margin:0;}
.hdr{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2.2pt solid #111;padding-bottom:1.5mm;}
.hdr .t{font-size:15pt;font-weight:bold;letter-spacing:.2pt;}
.hdr .b{font-size:9pt;color:#555;text-align:right;}
.meta{display:flex;justify-content:space-between;font-size:9pt;color:#333;margin:2mm 0 3mm;}
.given{border:1pt solid #111;background:#eef1f4;padding:2.5mm 3mm;margin:2mm 0 3mm;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.given .gl{font-weight:bold;font-size:9pt;letter-spacing:.4pt;text-transform:uppercase;color:#333;margin-bottom:1mm;}
.task{margin:3.5mm 0 1mm;break-inside:avoid;}
.task h2{font-size:11pt;margin:0 0 1.2mm;}
.q{margin:0 0 1.5mm;}
.wline{border-bottom:1px solid #999;height:6.6mm;}
.blank{display:inline-block;min-width:30mm;border-bottom:1px solid #555;}
.formula{font-family:'Courier New',monospace;font-weight:bold;}
table.data{border-collapse:collapse;width:100%;font-size:9.5pt;margin:2mm 0;}
table.data th,table.data td{border:1px solid #444;padding:1.5mm 2mm;text-align:left;vertical-align:top;}
table.data th{background:#e3e3e3;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.tall td{height:8.5mm;}
.grid{border:1pt solid #444;background-image:repeating-linear-gradient(#bcd4ec 0 .35mm,transparent .35mm 5mm),repeating-linear-gradient(90deg,#bcd4ec 0 .35mm,transparent .35mm 5mm);-webkit-print-color-adjust:exact;print-color-adjust:exact;break-inside:avoid;margin:1.5mm 0 2mm;}
.gl2{font-size:8.5pt;color:#666;margin:0 0 .5mm;}
.hint{font-size:9pt;color:#555;font-style:italic;}
.result{border:1.3pt solid #111;padding:2mm 3mm;margin:1.5mm 0;background:#eef1f4;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
ul.c{margin:.5mm 0 1.5mm 5mm;padding:0;} ul.c li{margin:.4mm 0;}
.sub{font-size:9pt;color:#555;}
'''

def head(title, bezug):
    return ("<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'><style>"+CSS+"</style></head><body>"
        f"<div class='hdr'><div class='t'>{title}</div><div class='b'>Fall #2024-0311<br>{bezug}</div></div>"
        "<div class='meta'><span>Name(n): _______________________________</span><span>Klasse: __________</span><span>Datum: __________</span></div>")
def foot(): return "</body></html>"
def given(label, inner): return f"<div class='given'><div class='gl'>{label}</div>{inner}</div>"
def task(h, inner): return f"<div class='task'><h2>{h}</h2>{inner}</div>"
def grid(h, label="Rechnung / Lösungsweg"): return f"<div class='gl2'>{label}:</div><div class='grid' style='height:{h}mm'></div>"
def wlines(n): return "".join("<div class='wline'></div>" for _ in range(n))
def bl(w=30): return f"<span class='blank' style='min-width:{w}mm'></span>"

sheets = {}

# ---------------- SPUR 1 ----------------
s = head("SPUR 1 — TATORTANALYSE", "Polizeibericht · Überwachungsbild")
s += given("Auftrag", "Ihr habt Zugang zum Überwachungsbild des Labors. Beantwortet die Fragen so genau wie möglich. "
    "Haltet euch <b>ausschließlich an das, was ihr im Bild seht</b>. Diese Beobachtungen braucht ihr in späteren Hinweisen wieder.")
q1=("<b>1.</b> Uhrzeit, zu der die Leiche aufgefunden wurde (Wanduhr): "+bl(45)+"<br>"
    "<b>2.</b> Gesicherte Tür im hinteren Bereich — Aufschrift auf dem Schild und Bedeutung:"+wlines(2)+
    "<b>3.</b> Drei Zugangschips auf Dr. Felds Schreibtisch — welche Nummer deutet auf wen?"
    "<br>Chip #"+bl(8)+" → "+bl(55)+"<br>Chip #"+bl(8)+" → "+bl(55)+"<br>Chip #"+bl(8)+" → "+bl(55)+
    "<br>Welcher Chip liegt nicht am richtigen Ort? "+bl(55))
s += task("Beobachtungen", q1)
q2=("<b>4.</b> Aufgeschlagenes Notizbuch — Text und mögliche Person:"+wlines(2)+
    "<b>5.</b> Geplantes Gespräch mit Dr. Feld am Tattag — Person und Uhrzeit: Person "+bl(40)+" Uhrzeit "+bl(25)+
    "<br><b>6.</b> Frische Kaffeetasse mit Namenskürzel — Kürzel "+bl(25)+", Person "+bl(35)+", warum auffällig:"+wlines(1)+
    "<b>7.</b> Handgeschriebene Notiz an diesem Platz — Inhalt:"+wlines(1)+
    "<b>8.</b> Abkürzung „TTX“ taucht an zwei Stellen auf — Stelle/Person/Kontext jeweils:"+wlines(2)+
    "<b>9.</b> Beschädigtes Sicherheitssystem — Name auf dem Wartungsschild: "+bl(55)+
    "<br><b>10.</b> Behauptetes Vorlesungs-Alibi — welcher Hinweis im Bild bestätigt es? Person "+bl(35)+wlines(1))
s += task("Beobachtungen (Fortsetzung)", q2)
q3=("<b>11.</b> Sicherheitskamera an der Südwand — Typenschild vollständig notieren (wird in Spur 5 gebraucht):"
    "<br>Montagehöhe "+bl(35)+"  Neigungswinkel "+bl(35)+"  Standort laut Schild "+bl(40))
s += task("Technische Daten", q3)
s += task("Erste Einschätzung",
    "Welche zwei Personen erscheinen euch nach dieser Analyse am verdächtigsten? Jeweils mit konkreter Begründung aus dem Bild."
    +wlines(4))
s += foot(); sheets["1_Polizeibericht"]=s

# ---------------- SPUR 2 ----------------
s = head("SPUR 2 — HANDGRÖSSEN", "Normalverteilung · Handschuhfund")
s += given("Gegeben",
    "Vergleichsstudie überführter Täter: Mittelwert <span class='formula'>μ = 19,2 cm</span>, "
    "Standardabweichung <span class='formula'>σ = 1,5 cm</span>.<br>"
    "Die am Tatort gesicherten Handschuhe passen zu einer Handgröße von <b>18,5 cm bis 21,5 cm</b>.")
tbl=("<table class='data'><tr><th>Person</th><th>Handgröße x [cm]</th><th>z-Wert z = (x−μ)/σ</th></tr>"
 + "".join(f"<tr class='tall'><td>{n}</td><td>{x}</td><td></td></tr>" for n,x in
   [("Jonas Kern","19,8"),("Miriam Scholz","19,3"),("Dr. Elena Voss","18,9"),("Prof. Anton Richter","20,5"),
    ("Sarah Mayer","18,7"),("Felix Hauser","20,4"),("Lena Brandt","18,6"),("David Okonkwo","22,0")])
 + "</table>")
s += task("a) Standardisierung", "Berechnet für jede Person den z-Wert und tragt ihn in die Tabelle ein."+tbl+grid(40))
s += task("b) Auswertung",
    "Wer liegt mit seiner Handgröße <b>außerhalb</b> des Handschuh-Bereichs (18,5–21,5 cm)? "
    "Wer weicht am stärksten vom Mittelwert ab (größter Betrag von z)?"+wlines(2)+grid(35))
s += task("c) Schlussfolgerung",
    "<div class='result'>Welche Person kann den Handschuh nicht getragen haben und scheidet damit aus? Begründung:</div>"+wlines(3))
s += foot(); sheets["2_Handgroessen"]=s

# ---------------- SPUR 3a ----------------
s = head("SPUR 3a — TODESZEITPUNKT", "Abkühlungsgesetz · Exponentialfunktion")
s += given("Gegeben",
    "Körpertemperatur in Abhängigkeit von der Zeit seit dem Tod:<br>"
    "<span class='formula'>T(t) = 20 + 17 · e^(−0,16·t)</span><br>"
    "<span class='sub'>T in °C, t in Stunden seit dem Tod</span><br>"
    "Bei der Leichenbeschau um <b>18:00 Uhr</b> wurde <b>T = 30,0 °C</b> gemessen. Raumtemperatur konstant 20 °C.")
s += task("Aufgabe",
    "Bestimmt rechnerisch den Todeszeitpunkt. Löst dazu die Gleichung T(t) = 30 nach t auf (natürlicher Logarithmus) "
    "und rechnet das Ergebnis in eine Uhrzeit um."+grid(95))
s += task("Ergebnis",
    "<div class='result'>t = "+bl(30)+" Stunden vor 18:00 Uhr &nbsp;⟹&nbsp; Todeszeitpunkt ≈ "+bl(30)+" Uhr</div>"
    "<div class='hint'>Dieses Ergebnis legt das Tatzeitfenster fest — ihr braucht es in Spur 6 und Spur 7 wieder.</div>")
s += foot(); sheets["3a_Todeszeit"]=s

# ---------------- SPUR 3b ----------------
s = head("SPUR 3b — HERZFREQUENZ", "Änderungsrate · Differenzialrechnung")
s += given("Gegeben",
    "Die Smartwatches zeichnen die Herzfrequenz <span class='formula'>f(t)</span> in Schlägen pro Minute auf "
    "(t in Stunden ab 13:00 Uhr). Tatzeitpunkt: <b>t = 1,7</b> (entspricht 14:42 Uhr).<br>"
    "Wer zur Tatzeit körperlich aktiv/nervös war, zeigt eine deutliche Änderungsrate; wer ruhig war, eine Rate nahe 0.")
ftab=("<table class='data'><tr><th>Person</th><th>f(t)</th><th>f′(t)</th><th>f′(1,7)</th></tr>"
 + "".join(f"<tr class='tall'><td>{n}</td><td class='formula'>{f}</td><td></td><td></td></tr>" for n,f in
   [("Jonas Kern","2,5t<sup>4</sup> − 15t<sup>3</sup> + 25t<sup>2</sup> + 70"),
    ("Dr. Elena Voss","5,15t<sup>4</sup> − 29,52t<sup>3</sup> + 46,35t<sup>2</sup> + 72"),
    ("Prof. A. Richter","13,35t<sup>4</sup> − 73,0t<sup>3</sup> + 106,8t<sup>2</sup> + 68"),
    ("Sarah Mayer","7,475t<sup>4</sup> − 43,86t<sup>3</sup> + 71,01t<sup>2</sup> + 65"),
    ("Felix Hauser","0,3t<sup>3</sup> − 1,2t<sup>2</sup> + 1,2t + 71,7")])
 + "</table>")
s += task("a) Ableitungen", "Bildet f′(t) und berechnet f′(1,7) für die fünf Personen."+ftab+grid(60))
s += task("b) Sonderfall Miriam Scholz",
    "Miriams Gerät ist beschädigt; nur vier Werte ihrer Funktion <span class='formula'>g(t) = a·t³ + b·t² + c·t + d</span> sind gesichert:"
    "<ul class='c'><li>g(0) = 65 &nbsp;(Herzfrequenz um 13:00 Uhr)</li>"
    "<li>g(2) = 85 &nbsp;(Herzfrequenz um 15:00 Uhr)</li>"
    "<li>g′(2) = 0 &nbsp;(Rate um 15:00 Uhr — stabilisiert)</li>"
    "<li>g″(2) = −8 &nbsp;(zweite Ableitung um 15:00 Uhr)</li></ul>"
    "Stellt das Gleichungssystem für a, b, c, d auf, bestimmt die Funktion und berechnet g′(1,7)."+grid(90))
s += task("c) Schlussfolgerung",
    "<div class='result'>Wessen Herzfrequenz zeigte zur Tatzeit praktisch <b>keine</b> Änderung (Rate ≈ 0)? "
    "Diese Person war ruhig — nicht am Tatort — und scheidet aus:</div>"+wlines(2))
s += foot(); sheets["3b_Herzfrequenz"]=s

# ---------------- SPUR 4 ----------------
s = head("SPUR 4 — GPS-AUSWERTUNG", "Bestimmtes Integral · Alibiüberprüfung")
s += given("Gegeben",
    "Aus den Smartwatch-Daten wurden Geschwindigkeitsfunktionen <span class='formula'>v(t)</span> rekonstruiert "
    "(in m/min, t in Minuten ab 14:00 Uhr). Das Integral der Geschwindigkeit über den Zeitraum ergibt die "
    "<b>zurückgelegte Strecke</b>. Die Distanz laut Lageplan ist die Strecke, die der behauptete Aufenthaltsort erfordern würde.")
vtab=("<table class='data'><tr><th>Person</th><th>v(t) [m/min]</th><th>t-Bereich</th><th>Distanz (Lageplan)</th><th>Strecke ∫v(t)dt [m]</th></tr>"
 + "".join(f"<tr class='tall'><td>{n}</td><td class='formula'>{v}</td><td>{r}</td><td>{d}</td><td></td></tr>" for n,v,r,d in
   [("Jonas Kern","−0,016t<sup>2</sup> + 1,2t − 20","[25, 50]","80 m"),
    ("Miriam Scholz","−0,025t<sup>2</sup> + 1,875t − 27,5","[20, 55]","380 m"),
    ("Dr. E. Voss","−0,05t<sup>2</sup> + 2,95t − 36,9","[18, 41]","220 m"),
    ("Prof. Richter","−0,095t<sup>2</sup> + 2,85t − 11,875","[5, 25]","600 m"),
    ("Lena Brandt","−0,04t<sup>2</sup> + 0,6t","[0, 15]","120 m"),
    ("Sarah Mayer","−0,1t<sup>2</sup> + 9t − 180","[30, 60]","450 m")])
 + "</table>")
s += task("a) Strecken berechnen", "Berechnet für jede Person das bestimmte Integral über den t-Bereich und tragt die Strecke ein."+vtab+grid(85))
s += task("b) Vergleich & Schlussfolgerung",
    "Bei wem stimmt die berechnete Strecke mit der Distanz aus dem Lageplan überein? Dessen Alibi ist bestätigt."
    "<div class='result'>Wessen Aussage wird durch die GPS-Daten bestätigt (scheidet aus)? "+bl(55)+
    "<br>Bei wem passt die Strecke <b>nicht</b> zum behaupteten Ort?</div>"+wlines(2))
s += foot(); sheets["4_GPS"]=s

# ---------------- SPUR 5 ----------------
s = head("SPUR 5 — KÖRPERGRÖSSE", "Trigonometrie · Kameraauswertung")
s += given("Gegeben",
    "Die Südwand-Kamera hat zur Tatzeit eine Person in Bereich B erfasst. Technische Daten (aus Spur 1):<br>"
    "Montagehöhe der Kamera <span class='formula'>h = 3,20 m</span> &nbsp;·&nbsp; "
    "Neigungswinkel unter der Horizontalen <span class='formula'>α = 16°</span> &nbsp;·&nbsp; "
    "horizontaler Abstand zur Person <span class='formula'>d = 5,0 m</span>.<br>"
    "Die Kamera erfasst den Scheitelpunkt (Kopf) der Person. Messungenauigkeit: <b>± 10 cm</b>.")
s += task("a) Körpergröße berechnen",
    "Fertigt eine Skizze an (Kamera, Sichtlinie, Person) und berechnet die Körpergröße der gefilmten Person."
    "<div class='hint'>Hinweis: Die Sichtlinie fällt über die Strecke d um d·tan(α) ab.</div>"+grid(80,"Skizze & Rechnung"))
htab=("<table class='data'><tr><th>Person</th><th>Körpergröße [cm]</th><th>im Bereich 177 ± 10 cm?</th></tr>"
 + "".join(f"<tr class='tall'><td>{n}</td><td>{h}</td><td></td></tr>" for n,h in
   [("Jonas Kern","178"),("Dr. Elena Voss","169"),("Prof. Anton Richter","181"),
    ("Lena Brandt","162"),("Miriam Scholz","174")])
 + "</table>")
s += task("b) Abgleich",
    "Vergleicht euer Ergebnis (mit ± 10 cm Toleranz) mit den Körpergrößen der noch verbliebenen Verdächtigen."+htab)
s += task("c) Schlussfolgerung",
    "<div class='result'>Welche Person liegt außerhalb des Toleranzbereichs und scheidet damit aus? Begründung:</div>"+wlines(2))
s += foot(); sheets["5_Koerpergroesse"]=s

# ---------------- SPUR 6 ----------------
s = head("SPUR 6 — BLUTZUCKER", "Exponentialfunktion · Glukosesensor")
s += given("Gegeben",
    "Blutzuckerverlauf von Prof. Richter ab 14:00 Uhr:<br>"
    "<span class='formula'>B(t) = 95 · e^(−0,03·t) + 85</span> &nbsp; "
    "<span class='sub'>B in mg/dL, t in Minuten ab 14:00 Uhr</span><br>"
    "Grenzwert <b>135 mg/dL</b>: darüber = kürzlich gegessen. Institutsküche geöffnet 11:30–14:30 Uhr. "
    "Tatzeitfenster: 14:28–14:47 Uhr.")
s += task("a) Funktionswerte",
    "Berechnet B(0) und B(30) und deutet die Werte.<br>"
    "B(0) = "+bl(25)+" Bedeutung: "+bl(60)+"<br>B(30) = "+bl(25)+" Bedeutung: "+bl(60)+grid(35))
s += task("b) Grenzwert",
    "Ab welchem Zeitpunkt t liegt der Blutzucker unter 135 mg/dL? Stellt die Gleichung auf und löst nach t (ln)."+grid(70)+
    "<div class='result'>t = "+bl(25)+" Minuten ab 14:00 Uhr = "+bl(25)+" Uhr</div>")
s += task("c) Schlussfolgerung",
    "Kombiniert das Ergebnis mit den Küchen-Öffnungszeiten, den GPS-Daten (Spur 4) und dem Tatzeitfenster. "
    "Was folgt für Prof. Richters Aufenthaltsort — und warum scheidet er aus?"+wlines(3))
s += foot(); sheets["6_Blutzucker"]=s

# ---------------- SPUR 7 ----------------
s = head("SPUR 7 — ZUGANGSSYSTEM", "Lineares Gleichungssystem · Bereich B")
s += given("Auftrag",
    "Hört euch den Anruf der Polizei (KHK Brenner) aufmerksam an. Alle nötigen Angaben — die Bedeutung von p und t, "
    "die beiden Formeln und die Prüfwerte — entnehmt ihr dem Gespräch. Tipp: Lasst den Anruf bei Bedarf erneut abspielen.")
s += task("1) Mitschrift während des Anrufs",
    "p (Chip-Nummer) bedeutet: "+bl(70)+"<br>t (Zeitwert) bedeutet: "+bl(70)+
    "<br>Formel 1: "+bl(90)+"<br>Formel 2: "+bl(90)+
    "<br>Prüfwerte: C1 = "+bl(20)+"  C2 = "+bl(20))
chip=("<table class='data'><tr><th>Chip-Nr.</th><th>Person</th><th>Sonderausweis Bereich B?</th><th>noch verdächtig?</th></tr>"
 "<tr class='tall'><td>#1</td><td>Dr. Markus Feld (Opfer)</td><td>Ja</td><td>Tatopfer — entfällt</td></tr>"
 "<tr class='tall'><td>#3</td><td></td><td></td><td></td></tr>"
 "<tr class='tall'><td>#7</td><td></td><td></td><td></td></tr>"
 "<tr class='tall'><td>keiner</td><td>Dr. Elena Voss</td><td></td><td></td></tr></table>")
s += task("2) Wer hatte überhaupt Zugang zu Bereich B?",
    "Die Chips auf Dr. Felds Schreibtisch (Spur 1) waren die Sonderausweise. Tragt ein, wer welchen Chip trägt."
    +chip+"Wer scheidet allein durch den fehlenden Sonderausweis aus? "+bl(55))
s += task("3) Gleichungssystem aufstellen",
    "Setzt die Prüfwerte ein:<br>(I) &nbsp; "+bl(60)+"<br>(II) &nbsp; "+bl(60))
s += task("4) Gleichungssystem lösen", grid(95))
s += task("5) Ergebnis deuten",
    "<div class='result'>p = "+bl(15)+" ⟹ Chip #"+bl(10)+" gehört "+bl(40)+
    "<br>t = "+bl(15)+" ⟹ 14:00 Uhr + "+bl(12)+" min = "+bl(20)+" Uhr"
    "<br>Liegt diese Uhrzeit im Tatzeitfenster (14:28–14:47 Uhr)? "+bl(20)+"</div>")
s += task("6) Täter benennen und begründen",
    "Benennt den Täter und begründet mit mindestens <b>drei</b> mathematischen Argumenten aus verschiedenen Hinweisen."
    "<br>Täter: "+bl(55)+wlines(5))
s += foot(); sheets["7_Zugangssystem"]=s

for name, html in sheets.items():
    with open(os.path.join(OUT, name+".html"), "w", encoding="utf-8") as f:
        f.write(html)
print("HTML geschrieben:", ", ".join(sorted(sheets)))
