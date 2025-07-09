import streamlit as st
from typing import List, Tuple, Dict

COLORS = ['r', 'y', 'b']
ALL_CARDS = [f"{n}{c}" for c in COLORS for n in range(1, 9)]

def parse_card(card: str) -> Tuple[int, str]:
    return int(card[:-1]), card[-1]

# Farbdefinition
card_layout = {'b': 'Blau', 'y': 'Gelb', 'r': 'Rot'}
color_map = {'b': '#ADD8E6', 'y': '#FFFF99', 'r': '#FF9999', 'disabled': '#DDDDDD'}

# Init Session State
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
        clickable = not used
        html = f'''
        <div style="background-color:{bg_color}; text-align:center; padding:0.5em; border-radius:8px; font-weight:bold; cursor:pointer;" onclick="fetch('/?add={card}')">{i}</div>
        '''
        with cols[i-1]:
            if clickable:
                st.markdown(
                    f"<a href='?add={card}' style='text-decoration:none'>{html}</a>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(html, unsafe_allow_html=True)

# URL-Parameter auswerten (z.B. wenn jemand eine Karte hinzugefügt hat)
query_params = st.query_params
if 'add' in query_params:
    card_to_add = query_params.get("add")
    if isinstance(card_to_add, list):
        card_to_add = card_to_add[0]
    if card_to_add not in st.session_state.active_hand and len(st.session_state.active_hand) < 5:
        st.session_state.active_hand.append(card_to_add)
    st.query_params.clear()

st.markdown("---")

st.subheader("🤚 Aktives Deck")
deck_cols = st.columns(5)
for i in range(5):
    if i < len(st.session_state.active_hand):
        card = st.session_state.active_hand[i]
        num, col = parse_card(card)
        color = color_map[col]
        with deck_cols[i]:
            st.markdown(f"<a href='?remove={card}' style='text-decoration:none'><div style='background-color:{color}; text-align:center; padding:0.5em; border-radius:10px; font-size:24px; font-weight:bold; color:black;'>{num}</div></a>", unsafe_allow_html=True)

# Entfernen via URL
query_params = st.query_params
if 'remove' in query_params:
    card_to_remove = query_params.get("remove")
    if isinstance(card_to_remove, list):
        card_to_remove = card_to_remove[0]
    if card_to_remove in st.session_state.active_hand:
        st.session_state.active_hand.remove(card_to_remove)
        st.session_state.removed.append(card_to_remove)
    st.query_params.clear()

# Reset
st.markdown("---")
if st.button("🔁 Zurücksetzen"):
    st.session_state.active_hand = []
    st.session_state.removed = []
    st.rerun()