
import streamlit as st

st.set_page_config(layout="centered")

# Farben & Titel
colors = {"r": "red", "y": "orange", "b": "blue"}
color_names = {"r": "Rot", "y": "Gelb", "b": "Blau"}

st.markdown("<h1>🃏 Okey Kartenspiel</h1>", unsafe_allow_html=True)

# Initialisierung
if "start_deck" not in st.session_state:
    st.session_state.start_deck = [f"{n}{c}" for c in "ryb" for n in range(1, 9)]
if "aktuell" not in st.session_state:
    st.session_state.aktuell = []
if "out" not in st.session_state:
    st.session_state.out = []

# Karten hinzufügen
def add_to_aktuell(card):
    if card not in st.session_state.aktuell and len(st.session_state.aktuell) < 5:
        st.session_state.aktuell.append(card)
        st.session_state.start_deck.remove(card)

# Karten entfernen (Aktuell → Out)
def move_to_out(card):
    if card in st.session_state.aktuell:
        st.session_state.aktuell.remove(card)
        st.session_state.out.append(card)

# Anzeige
st.markdown("### 🎯 Start")

for c in "ryb":
    st.markdown(f"<span style='color:{colors[c]}; font-weight:bold;'>{color_names[c]}</span>", unsafe_allow_html=True)
    cols = st.columns(8)
    for i, n in enumerate(range(1, 9)):
        card = f"{n}{c}"
        if card in st.session_state.start_deck:
            if cols[i].button(f"{n}", key=f"{card}_start", help=f"{card} hinzufügen"):
                add_to_aktuell(card)

st.markdown("---")
st.markdown("### 🖐️ Aktuell")

cols = st.columns(5)
for i, card in enumerate(st.session_state.aktuell):
    color = colors[card[-1]]
    number = card[:-1]
    with cols[i]:
        st.markdown(f"<span style='color:{color}; font-weight:bold;'>{number}</span>", unsafe_allow_html=True)
        if st.button(f"{number}", key=f"{card}_aktuell", help=f"{card} entfernen"):
            move_to_out(card)

st.markdown("---")
st.markdown("### 🏡 Out")

if st.session_state.out:
    out_display = ""
    for card in st.session_state.out:
        color = colors[card[-1]]
        number = card[:-1]
        out_display += f"<span style='color:{color}; font-weight:bold; margin-right:4px'>{number}</span>"
    st.markdown(out_display, unsafe_allow_html=True)
