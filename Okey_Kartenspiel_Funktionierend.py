
import streamlit as st

st.set_page_config(page_title="Okey Kartenspiel", layout="centered")

st.markdown("""<h1 style='color:#2c3e50;'>🃏 Okey Kartenspiel</h1>""", unsafe_allow_html=True)

# Kartenfarben und deren Styling
colors = {
    "rot": {"rgb": "#e74c3c", "range": range(1, 9)},
    "gelb": {"rgb": "#e67e22", "range": range(1, 9)},
    "blau": {"rgb": "#2980b9", "range": range(1, 9)}
}

# Initialisierung des Session State
if "aktuell" not in st.session_state:
    st.session_state.aktuell = []

if "out" not in st.session_state:
    st.session_state.out = []

if "verfügbar" not in st.session_state:
    st.session_state.verfügbar = {
        f"{zahl}{farbe[0]}": True for farbe in colors for zahl in colors[farbe]["range"]
    }

# --- START-Deck ---
st.subheader("🎯 Start")
for farbe, info in colors.items():
    cols = st.columns(8)
    for i, zahl in enumerate(info["range"]):
        key = f"{zahl}{farbe[0]}"
        if st.session_state.verfügbar.get(key, True):
            if cols[i].button(str(zahl), key=f"{key}_start", help=f"{farbe.capitalize()} {zahl}",
                              use_container_width=True):
                if len(st.session_state.aktuell) < 5:
                    st.session_state.aktuell.append((zahl, farbe))
                    st.session_state.verfügbar[key] = False
                    st.experimental_rerun()
                else:
                    st.warning("Maximal 5 Karten im 'Aktuell'-Deck erlaubt.")

# --- Aktuelles Deck ---
st.markdown("---")
st.subheader("🖐 Aktuell")
cols = st.columns(5)
for i, (zahl, farbe) in enumerate(st.session_state.aktuell):
    btn_style = f"color: {colors[farbe]['rgb']}; font-weight: bold"
    if cols[i].button(str(zahl), key=f"aktuell_{i}", help=f"{farbe.capitalize()} {zahl}", use_container_width=True):
        st.session_state.out.append((zahl, farbe))
        st.session_state.aktuell.pop(i)
        st.experimental_rerun()

# --- Out Deck ---
st.markdown("---")
st.subheader("🏡 Out")
out_str = ""
for zahl, farbe in st.session_state.out:
    color = colors[farbe]["rgb"]
    out_str += f"<span style='color:{color}; font-weight:bold; font-size:18px'>{zahl}</span> "
st.markdown(out_str, unsafe_allow_html=True)
