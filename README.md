# 🃏 Okey Assistent (Streamlit)

Ein einfacher Entscheidungshelfer für das Okey-ähnliche Kartenspiel. Wähle 5 Karten aus und erhalte eine Empfehlung, welche Karte du behalten oder abwerfen solltest.

## 🚀 Online-Version

Diese App läuft auf [Streamlit Cloud](https://streamlit.io/cloud).

## 🧩 Spielregeln (vereinfacht)

- **Bingo (100 Punkte)**: Drei aufeinanderfolgende Zahlen gleicher Farbe (z. B. 3C,4C,5C)
- **Gleichwertig (20–90 Punkte)**: Drei gleiche Zahlen in verschiedenen Farben (z. B. 8C,8N,8Z = 90)
- **Mixed-Farben-Folge (20–80 Punkte)**: Drei aufeinanderfolgende Zahlen in beliebiger Farbe (z. B. 3C,4N,5Z)

## 📦 Lokale Installation

```bash
pip install streamlit
streamlit run okey_assistent.py
```

## 🌍 Deployment via Streamlit Cloud

1. Code auf GitHub hochladen
2. [streamlit.io/cloud](https://streamlit.io/cloud) öffnen
3. Repository + Datei auswählen
4. Deploy 🎉
