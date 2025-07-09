
import streamlit as st

st.set_page_config(page_title="Okey Kartenspiel", layout="centered")
st.markdown(
    """
    <style>
        body {
            background-color: #f2f2f2;
        }
        .big-number {
            font-size: 24px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🃏 Okey Kartenspiel")

# Session states
if "deck" not in st.session_state:
    st.session_state.deck = {
        "rot": [str(i) for i in range(1, 9)],
        "gelb": [str(i) for i in range(1, 9)],
        "blau": [str(i) for i in range(1, 9)],
    }

if "aktuell" not in st.session_state:
    st.session_state.aktuell = []

if "out" not in st.session_state:
    st.session_state.out = []

farben = {
    "rot": "red",
    "gelb": "orange",
    "blau": "blue",
}

st.markdown("### 🎯 Start")

for farbe in farben:
    cols = st.columns(8)
    for i, zahl in enumerate(range(1, 9)):
        zahl_str = str(zahl)
        if zahl_str in st.session_state.deck[farbe]:
            with cols[i]:
                st.markdown(f"<div class='big-number' style='color:{farben[farbe]}'>{zahl}</div>", unsafe_allow_html=True)
                if st.button(" ", key=f"{farbe}_{zahl}_start"):
                    if len(st.session_state.aktuell) < 5:
                        st.session_state.aktuell.append((zahl_str, farbe))
                        st.session_state.deck[farbe].remove(zahl_str)

st.divider()

st.markdown("### 🖐 Aktuell")
aktuell_cols = st.columns(5)
for i in range(5):
    if i < len(st.session_state.aktuell):
        zahl, farbe = st.session_state.aktuell[i]
        with aktuell_cols[i]:
            st.markdown(f"<div class='big-number' style='color:{farben[farbe]}'>{zahl}</div>", unsafe_allow_html=True)
            if st.button(" ", key=f"{farbe}_{zahl}_aktuell_{i}"):
                st.session_state.aktuell.pop(i)
                st.session_state.out.append((zahl, farbe))

st.divider()

st.markdown("### 🚫 Out")
out_cols = st.columns(5)
for i in range(5):
    if i < len(st.session_state.out):
        zahl, farbe = st.session_state.out[i]
        with out_cols[i]:
            st.markdown(f"<div class='big-number' style='color:{farben[farbe]}'>{zahl}</div>", unsafe_allow_html=True)
