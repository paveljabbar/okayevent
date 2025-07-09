import streamlit as st
import itertools

# Nur Bingo erlaubt: drei aufeinanderfolgende Karten gleicher Farbe

farben = ["R", "G", "B"]
werte = [str(i) for i in range(1, 9)]
alle_karten = [w + f for f in farben for w in werte]

def finde_bingo_kombi(karten):
    for kombi in itertools.combinations(karten, 3):
        farben_check = [k[1] for k in kombi]
        werte_check = sorted([int(k[0]) for k in kombi])
        if len(set(farben_check)) == 1:
            if werte_check[1] - werte_check[0] == 1 and werte_check[2] - werte_check[1] == 1:
                return list(kombi)
    return None

def finde_2er_setup(karten):
    paare = list(itertools.combinations(karten, 2))
    for k1, k2 in paare:
        if k1[1] == k2[1]:  # gleiche Farbe
            diff = abs(int(k1[0]) - int(k2[0]))
            if diff == 1 or diff == 2:
                return [k1, k2]
    return None

def bingo_only_empfehlung(karten):
    bingo = finde_bingo_kombi(karten)
    if bingo:
        return f"✅ BINGO gefunden! {bingo} (+100 Punkte)"

    setup = finde_2er_setup(karten)
    if setup:
        rest = [k for k in karten if k not in setup]
        return f"🧐 Noch kein Bingo, aber gute Voraussetzung mit {setup}. Vorschlag: Wirf eine dieser Karten ab: {rest}"

    # Kein Setup gefunden
    karte = sorted(karten, key=lambda x: int(x[0]))[0]
    return f"❌ Keine sinnvolle Bingo-Kombination. Vorschlag: Wirf '{karte}' ab."

# Streamlit UI
st.title("🃏 Okey Assistent (Nur Bingo)")
st.write("Wähle 5 Karten. Ziel ist **ausschließlich** Bingo-Kombinationen zu erzielen.")

kartenwahl = st.multiselect("Wähle 5 Karten:", options=alle_karten, max_selections=5)

if st.button("Empfehlung anzeigen"):
    if len(kartenwahl) != 5:
        st.warning("Bitte genau 5 Karten auswählen.")
    else:
        st.success(bingo_only_empfehlung(kartenwahl))
