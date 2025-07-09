
import streamlit as st

st.set_page_config(layout="centered")
st.markdown("""<style>body { background-color: #f0f0f0; }</style>""", unsafe_allow_html=True)

st.title("🃏 Okey Kartenspiel")

# Farben definieren
colors = ["rot", "gelb", "blau"]
color_codes = {
    "rot": "red",
    "gelb": "orange",
    "blau": "blue"
}

# Karten generieren
all_cards = [(i, color) for color in colors for i in range(1, 9)]

# SessionState initialisieren
if "available_cards" not in st.session_state:
    st.session_state.available_cards = all_cards.copy()

if "current_cards" not in st.session_state:
    st.session_state.current_cards = []

st.markdown("### 🎯 Start")

cols = st.columns(8)

for color in colors:
    row = st.columns(8)
    for i, col in enumerate(row):
        card = (i+1, color)
        if card in st.session_state.available_cards:
            with col:
                st.markdown(
                    f"<div style='text-align: center; font-size: 22px; color: {color_codes[color]}; font-weight: bold;'>{i+1}</div>",
                    unsafe_allow_html=True
                )
                if st.button("➕", key=f"add_{color}_{i+1}"):
                    if len(st.session_state.current_cards) < 5:
                        st.session_state.available_cards.remove(card)
                        st.session_state.current_cards.append(card)

st.markdown("---")
st.markdown("### 🖐 Aktuell")

if st.session_state.current_cards:
    current_row = st.columns(5)
    for idx, card in enumerate(st.session_state.current_cards):
        num, color = card
        with current_row[idx]:
            st.markdown(
                f"<div style='text-align: center; font-size: 22px; color: {color_codes[color]}; font-weight: bold;'>{num}</div>",
                unsafe_allow_html=True
            )
else:
    st.info("Noch keine Karten ausgewählt.")
