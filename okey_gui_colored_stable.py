import streamlit as st
from typing import List, Tuple

COLORS = ['r', 'y', 'b']
ALL_CARDS = [f"{n}{c}" for c in COLORS for n in range(1, 9)]

def parse_card(card: str) -> Tuple[int, str]:
    return int(card[:-1]), card[-1]

card_layout = {'b': 'Blau', 'y': 'Gelb', 'r': 'Rot'}
color_map = {'b': '#ADD8E6', 'y': '#FFFF99', 'r': '#FF9999', 'disabled': '#DDDDDD'}

# Session-State initialisieren
if 'active_hand' not in st.session_state:
    st.session_state.active_hand = []
if 'removed' not in st.session_state:
    st.session_state.removed = []

st.set_page_config(page_title="Okey Deck Visual", layout="centered")
st.title("🎴 Okey Deck Visualisierung & Empfehlung")

st.subheader("🧱 Aktuelles Deck")
for color in COLORS:
    st.markdown(f"**{card_layout[color]}**")
    cols = st.columns(8)
    for i in range(1, 9):
        card = f"{i}{color}"
        used = card in st.session_state.active_hand or card in st.session_state.removed
        bg_color = color_map['disabled'] if used else color_map[color]
        with cols[i - 1]:
            if not used:
                if st.button(f"{i}", key=f"add_{card}", help=f"Karte {card}", args=(card,)):
                    if len(st.session_state.active_hand) < 5:
                        st.session_state.active_hand.append(card)
            else:
                st.markdown(
                    f"<div style='background-color:{bg_color}; text-align:center; padding:0.5em; border-radius:8px; font-weight:bold;'>{i}</div>",
                    unsafe_allow_html=True
                )

st.markdown("---")
st.subheader("🤚 Aktives Deck")
deck_cols = st.columns(5)
for i in range(5):
    if i < len(st.session_state.active_hand):
        card = st.session_state.active_hand[i]
        num, col = parse_card(card)
        color = color_map[col]
        with deck_cols[i]:
            if st.button(f"{num}", key=f"remove_{card}", help=f"{card} entfernen"):
                st.session_state.active_hand.remove(card)
                st.session_state.removed.append(card)
    else:
        with deck_cols[i]:
            st.markdown("<div style='height:2.5em'></div>", unsafe_allow_html=True)

st.markdown("---")
if st.button("🔁 Zurücksetzen"):
    st.session_state.active_hand = []
    st.session_state.removed = []
    st.rerun()