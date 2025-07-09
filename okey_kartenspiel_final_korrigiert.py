
import streamlit as st

st.set_page_config(page_title="Okey Kartenspiel", layout="centered")

# Initialisiere Session State
if "start_deck" not in st.session_state:
    st.session_state.start_deck = {
        "rot": [str(i) for i in range(1, 9)],
        "gelb": [str(i) for i in range(1, 9)],
        "blau": [str(i) for i in range(1, 9)],
    }
    st.session_state.aktuell = []
    st.session_state.out = []

# Farben für Anzeige
farbe_map = {
    "rot": "red",
    "gelb": "orange",
    "blau": "blue"
}

def karten_button(zahl, farbe, pos):
    button_key = f"{farbe}_{zahl}_{pos}"
    if st.button(zahl, key=button_key):
        if len(st.session_state.aktuell) < 5:
            st.session_state.start_deck[farbe].remove(zahl)
            st.session_state.aktuell.append((zahl, farbe))

def aktuell_button(zahl, farbe, index):
    button_key = f"{farbe}_aktuell_{zahl}_{index}"
    if st.button(zahl, key=button_key):
        st.session_state.aktuell.pop(index)
        st.session_state.out.append((zahl, farbe))

# Titel
st.title("🃏 Okey Kartenspiel")

# START Deck
st.subheader("🎯 Start")
for farbe in ["rot", "gelb", "blau"]:
    cols = st.columns(8)
    for i, zahl in enumerate(st.session_state.start_deck[farbe]):
        with cols[i]:
            st.markdown(f"<div style='text-align:center; color:{farbe_map[farbe]}; font-size:24px'>{zahl}</div>", unsafe_allow_html=True)
            karten_button(zahl, farbe, i)

# AKTUELL
st.markdown("---")
st.subheader("🖐️ Aktuell")
cols = st.columns(5)
for i, (zahl, farbe) in enumerate(st.session_state.aktuell):
    with cols[i]:
        st.markdown(f"<div style='text-align:center; color:{farbe_map[farbe]}; font-size:20px'>{zahl}</div>", unsafe_allow_html=True)
        aktuell_button(zahl, farbe, i)

# OUT
st.markdown("---")
st.subheader("🏠 Out")
st.markdown("".join([
    f"<span style='color:{farbe_map[farbe]}; font-size:20px; margin-right:8px'>{zahl}</span>"
    for zahl, farbe in st.session_state.out
]), unsafe_allow_html=True)
