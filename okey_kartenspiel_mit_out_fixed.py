
import streamlit as st

st.set_page_config(page_title="Okey Kartenspiel", layout="centered")
st.markdown(
    """
    <style>
        body {
            background-color: #f0f0f0;
        }
        .card-number {
            font-size: 22px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🃏 Okey Kartenspiel")

colors = {
    "Rot": "red",
    "Gelb": "orange",
    "Blau": "blue"
}

# Initialisiere Session States
if "start_deck" not in st.session_state:
    st.session_state.start_deck = {
        "Rot": list(range(1, 9)),
        "Gelb": list(range(1, 9)),
        "Blau": list(range(1, 9))
    }

if "aktuell" not in st.session_state:
    st.session_state.aktuell = []  # enthält Tupel: (Farbe, Zahl)

if "out" not in st.session_state:
    st.session_state.out = []


st.header("🎯 Start")

for color, hex_code in colors.items():
    cols = st.columns(8)
    st.markdown(f"<div class='card-number' style='color:{hex_code}'>{' '.join(str(i) for i in st.session_state.start_deck[color])}</div>", unsafe_allow_html=True)
    for idx, i in enumerate(range(1, 9)):
        if i in st.session_state.start_deck[color]:
            if cols[idx].button(" ", key=f"{color}_{i}", help=f"{color} {i}"):
                if len(st.session_state.aktuell) < 5:
                    st.session_state.start_deck[color].remove(i)
                    st.session_state.aktuell.append((color, i))

st.markdown("---")
st.header("🖐 Aktuell")

aktuell_cols = st.columns(5)
for idx, card in enumerate(st.session_state.aktuell):
    color, num = card
    btn_label = f"{num}"
    if aktuell_cols[idx].button(btn_label, key=f"aktuell_{color}_{num}"):
        st.session_state.aktuell.remove(card)
        st.session_state.out.append(card)

st.markdown("---")
st.header("📤 Out")

if st.session_state.out:
    out_strs = [
        f"<span style='color:{colors[color]}; font-weight:bold; font-size:20px'>{num}</span>"
        for color, num in st.session_state.out
    ]
    st.markdown(" ".join(out_strs), unsafe_allow_html=True)
