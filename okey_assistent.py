import streamlit as st
import math
import random

# Farben und Werte
farben = ["C", "N", "Z"]
werte = [str(i) for i in range(1, 9)]
alle_karten = [w + f for f in farben for w in werte]

def bingo(aktuelle_karten):
    farben_karten = {"C": [], "N": [], "Z": []}
    for k in aktuelle_karten:
        farben_karten[k[1]].append(int(k[0]))

    for farbe, zahlen in farben_karten.items():
        zahlen = sorted(zahlen)
        for i in range(len(zahlen) - 2):
            if zahlen[i+1] - zahlen[i] == 1 and zahlen[i+2] - zahlen[i+1] == 1:
                return [f"{zahlen[i]}{farbe}", f"{zahlen[i+1]}{farbe}", f"{zahlen[i+2]}{farbe}"]
    return None

def gleiche_zahl(aktuelle_karten):
    zahlen = {}
    for k in aktuelle_karten:
        z = k[0]
        zahlen[z] = zahlen.get(z, []) + [k[1]]
    for z, farben in zahlen.items():
        if len(set(farben)) == 3:
            return [z + f for f in farben]
    return None

def mischfarbe_straight(aktuelle_karten):
    nummern = sorted([int(k[0]) for k in aktuelle_karten])
    for i in range(len(nummern) - 2):
        if nummern[i+1] - nummern[i] == 1 and nummern[i+2] - nummern[i+1] == 1:
            return [k for k in aktuelle_karten if int(k[0]) in (nummern[i], nummern[i+1], nummern[i+2])]
    return None

def empfehlung(aktuelle_karten):
    if bingo(aktuelle_karten):
        return f"✅ Bingo-Kombi gefunden: {bingo(aktuelle_karten)} (+100 Punkte)"
    elif gleiche_zahl(aktuelle_karten):
        k = gleiche_zahl(aktuelle_karten)
        return f"✅ Drei gleiche Zahlen (unterschiedliche Farben): {k} (+{10 + 10*int(k[0][0])} Punkte)"
    elif mischfarbe_straight(aktuelle_karten):
        k = mischfarbe_straight(aktuelle_karten)
        punkte = 10 + 10*min([int(x[0]) for x in k])
        return f"✅ Farb-Mix Straight: {k} (+{punkte} Punkte)"
    else:
        karte = sorted(aktuelle_karten, key=lambda x: int(x[0]))[0]
        return f"❌ Keine Kombination gefunden. Vorschlag: Wirf '{karte}' ab."

# Streamlit UI
st.title("🃏 Okey Assistent – Entscheidungshelfer")
st.write("Wähle deine 5 Karten. Klicke auf 'Empfehlung anzeigen' für einen Zugvorschlag.")

kartenwahl = st.multiselect("Wähle 5 Karten:", options=alle_karten, max_selections=5)

if st.button("Empfehlung anzeigen"):
    if len(kartenwahl) != 5:
        st.warning("Bitte genau 5 Karten auswählen.")
    else:
        st.success(empfehlung(kartenwahl))
