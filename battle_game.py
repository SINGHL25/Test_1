
import streamlit as st
import random
import time

st.set_page_config(page_title="6-Player O/X Battle", layout="centered")

st.title("🎮 6-Player O/X Battle Game")

# Player name inputs
st.subheader("🔧 Edit Player Names")
players = []
for i in range(6):
    name = st.text_input(f"Player {i+1} Name", value=f"Player{i+1}")
    players.append(name)

if st.button("⚔️ Start Battle"):
    st.subheader("🕹️ Battle in Progress...")

    battle_log = []
    contenders = players.copy()

    round_num = 1

    while len(contenders) > 1:
        random.shuffle(contenders)
        new_round = []

        st.markdown(f"### 🧨 Round {round_num}")
        for i in range(0, len(contenders) - 1, 2):
            p1 = contenders[i]
            p2 = contenders[i + 1]
            winner = random.choice([p1, p2])
            battle_log.append(f"🔥 {p1} vs {p2} → **{winner} wins**")
            st.write(f"{p1} ❌ vs {p2} ⭕ → 🏆 **{winner}** advances")
            time.sleep(2)  # Delay for realism

        # If odd number, last one moves automatically
        if len(contenders) % 2 == 1:
            lucky = contenders[-1]
            st.write(f"🎁 {lucky} advances automatically!")
            new_round.append(lucky)
            time.sleep(1)

        contenders = new_round
        round_num += 1

    st.success(f"🏅 Winner is: **{contenders[0]}**! Congratulations!")
