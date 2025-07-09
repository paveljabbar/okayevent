
import streamlit as st

st.set_page_config(page_title="Okey Kartenspiel", layout="centered")

# Hintergrundfarbe setzen (grau)
st.markdown(
    """
    <style>
        body {
            background-color: #f0f0f0;
        }
        .big-button {
            font-size: 24px !important;
            font-weight: bold !important;
            width: 50px;
            height: 50px;
            margin: 4px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialisierung des Session States
if "start_deck" not in st.session_state:
    st.session_state.start_deck = {
        "rot": list(range(1, 9)),
        "gelb": list(range(1, 9)),
        "blau": list(range(1, 9))
    }

if "aktuell" not in st.session_state:
    st.session_state.aktuell = []

st.title("🃏 Okey Kartenspiel")

st.header("🎯 Start")

# Farben und deren Anzeige
farben = {
    "rot": "red",
    "gelb": "orange",
    "blau": "blue"
}

# Anzeige der Start-Karten
for farbe, color_code in farben.items():
    cols = st.columns(8)
    for i, zahl in enumerate(st.session_state.start_deck[farbe]):
        with cols[i]:
            if len(st.session_state.aktuell) < 5:
                if st.button(str(zahl), key=f"start_{farbe}_{zahl}", help=f"{farbe} {zahl}"):
                    st.session_state.aktuell.append((farbe, zahl))
                    st.session_state.start_deck[farbe].remove(zahl)
            st.markdown(f"<span style='color:{color_code}; font-size:24px; font-weight:bold;'>{zahl}</span>", unsafe_allow_html=True)

st.markdown("---")
st.header("🖐️ Aktuell")

# Anzeige der aktuell ausgewählten Karten
if st.session_state.aktuell:
    cols = st.columns(5)
    for i, (farbe, zahl) in enumerate(st.session_state.aktuell):
        with cols[i]:
            st.markdown(f"<span style='color:{farben[farbe]}; font-size:24px; font-weight:bold;'>{zahl}</span>", unsafe_allow_html=True)
else:
    st.info("Wähle bis zu 5 Karten aus dem Startbereich.")
