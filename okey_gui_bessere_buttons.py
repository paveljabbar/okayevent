
import streamlit as st

st.set_page_config(layout="centered")
st.markdown("<style>body { background-color: #f0f0f0; }</style>", unsafe_allow_html=True)

st.markdown("### 🃏 **Okey Kartenspiel**")

colors = {"rot": "red", "gelb": "orange", "blau": "blue"}
color_keys = list(colors.keys())
zahlen = list(range(1, 9))

if "start" not in st.session_state:
    st.session_state.start = [(str(i), farbe) for farbe in colors for i in zahlen]
if "aktuell" not in st.session_state:
    st.session_state.aktuell = []
if "out" not in st.session_state:
    st.session_state.out = []

st.markdown("#### 🎯 Start")
for farbe in color_keys:
    cols = st.columns(8)
    for i, z in enumerate(zahlen):
        karte = (str(z), farbe)
        if karte not in st.session_state.start:
            cols[i].empty()
        else:
            label = f":{colors[farbe]}[{z}]"
            if cols[i].button(label, key=f"{farbe}_{z}_start"):
                if len(st.session_state.aktuell) < 5:
                    st.session_state.start.remove(karte)
                    st.session_state.aktuell.append(karte)

st.markdown("---")
st.markdown("#### 🖐 **Aktuell**")
cols = st.columns(5)
for i, karte in enumerate(st.session_state.aktuell):
    z, farbe = karte
    label = f":{colors[farbe]}[{z}]"
    if cols[i].button(label, key=f"{farbe}_{z}_aktuell"):
        st.session_state.aktuell.remove(karte)
        st.session_state.out.append(karte)

st.markdown("---")
st.markdown("#### 🏠 **Out**")
out_cols = st.columns(8)
for i, karte in enumerate(st.session_state.out):
    z, farbe = karte
    out_cols[i % 8].markdown(f"<span style='color: {colors[farbe]}; font-weight: bold; font-size: 20px'>{z}</span>", unsafe_allow_html=True)
