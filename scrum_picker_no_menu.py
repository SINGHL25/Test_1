
import streamlit as st
import random
import time

st.set_page_config(page_title="Scrum Host Picker", layout="wide")

st.markdown('<h1 style="text-align: center; color: red;">🏹⚔️ Scrum Host Battle Arena ⚔️🏹</h1>', unsafe_allow_html=True)

# Sidebar for names
st.sidebar.header("🛡️ Enter Warrior Names")
names = []
for i in range(1, 7):
    name = st.sidebar.text_input(f"Warrior {i}", f"Warrior{i}")
    names.append(name)

# Background and animation display
col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("⚔️ Begin Battle!"):
        st.markdown("## 🕒 The Battle Begins...")
        with st.spinner("Warriors are fighting..."):
            duration = 60  # seconds
            start_time = time.time()
            while time.time() - start_time < duration:
                warrior1, warrior2 = random.sample(names, 2)
                st.image("https://i.imgur.com/6aLz6dl.gif", width=400)
                st.markdown(f"### {warrior1} clashes with {warrior2}!")
                time.sleep(5)
                st.empty()

        winner = random.choice(names)
        st.balloons()
        st.markdown(f"<h2 style='color:green; text-align:center;'>🏆 {winner} will host today's Scrum! 🏆</h2>", unsafe_allow_html=True)
    else:
        st.image("https://i.imgur.com/6aLz6dl.gif", width=500)
        st.markdown("### Click the button above to begin the battle!")
