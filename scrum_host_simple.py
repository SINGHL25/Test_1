
import streamlit as st
import random
import time

# Set page config
st.set_page_config(page_title="Battle Arena for Scrum Host", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: darkred;'>⚔️ Battle Arena for Scrum Host ⚔️</h1>", unsafe_allow_html=True)

# Sidebar input for names
st.sidebar.header("🛡️ Enter Warrior Names")
names = [st.sidebar.text_input(f"Warrior {i+1}", f"Warrior{i+1}") for i in range(6)]

# Placeholder for display
placeholder = st.empty()

if st.button("🔥 Begin Battle!"):
    st.markdown("<h2 style='text-align: center; color: orange;'> Result...</h2>", unsafe_allow_html=True)

    start_time = time.time()
    duration = 15  # seconds

    while time.time() - start_time < duration:
        w1, w2 = random.sample(names, 2)
        with placeholder.container():
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color: navy;'>{w1} ⚔️ vs ⚔️ {w2}</h2>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        time.sleep(3)

    winner = random.choice(names)
    st.balloons()
    st.markdown(f"<h2 style='text-align: center; color: green;'>🏆 {winner} will host tomorrow's Scrum! 🏆</h2>", unsafe_allow_html=True)

else:
    with placeholder.container():
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown("<h4>Click 'Begin Battle!' to start the Scrum host selection.</h4>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
