import streamlit as st

COLORS = ['r', 'y', 'b']
color_map = {'r': '#FF9999', 'y': '#FFFF99', 'b': '#ADD8E6', 'disabled': '#DDDDDD'}
label_map = {'r': 'Rot', 'y': 'Gelb', 'b': 'Blau'}

if 'active_hand' not in st.session_state:
    st.session_state.active_hand = []

st.title("🃏 Okey Deck Visualisierung & Empfehlung")
st.subheader("🧱 Aktuelles Deck")

for color in COLORS:
    st.markdown(f"**{label_map[color]}**")
    cols = st.columns(8)
    for i in range(1, 9):
        card = f"{i}{color}"
        bg = color_map[color]
        html = f"""
        <div style='background-color: {bg}; padding: 0.5em; border-radius: 8px; text-align: center; font-weight: bold; cursor: pointer;'
             onclick="window.location.href='?add={card}'">
            {i}
        </div>
        """
        with cols[i - 1]:
            st.markdown(html, unsafe_allow_html=True)

# Handle Auswahl
query_params = st.query_params
if 'add' in query_params:
    card = query_params['add'][0]
    if card not in st.session_state.active_hand and len(st.session_state.active_hand) < 5:
        st.session_state.active_hand.append(card)
    st.query_params.clear()

st.markdown("---")
st.subheader("✋ Aktives Deck")
active_cols = st.columns(5)
for i in range(5):
    if i < len(st.session_state.active_hand):
        card = st.session_state.active_hand[i]
        num, col = int(card[:-1]), card[-1]
        bg = color_map[col]
        html = f"""
        <div style='background-color: {bg}; padding: 0.5em; border-radius: 8px; text-align: center; font-weight: bold; cursor: pointer;'
             onclick="window.location.href='?remove={card}'">
            {num}
        </div>
        """
        with active_cols[i]:
            st.markdown(html, unsafe_allow_html=True)

# Handle Entfernen
query_params = st.query_params
if 'remove' in query_params:
    card = query_params['remove'][0]
    if card in st.session_state.active_hand:
        st.session_state.active_hand.remove(card)
    st.query_params.clear()

st.markdown("---")
if st.button("🔄 Zurücksetzen"):
    st.session_state.active_hand = []
    st.query_params.clear()
    st.rerun()