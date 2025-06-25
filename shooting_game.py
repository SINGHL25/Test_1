
import streamlit as st
import random
import time

st.set_page_config(page_title="🎯 6-Player Shooting Game", layout="centered")

st.title("🔫 6-Player Max Bullet Shooting Contest")

# Player name inputs
st.subheader("🔧 Edit Player Names")
players = []
for i in range(6):
    name = st.text_input(f"Player {i+1} Name", value=f"Player{i+1}")
    players.append(name)

if st.button("🔥 Start Shooting Challenge"):
    st.subheader("🎮 Shooting in Progress (30 seconds)...")

    scores = {player: 0 for player in players}
    start_time = time.time()

    progress_bar = st.progress(0)
    status_text = st.empty()

    while time.time() - start_time < 30:
        shooter = random.choice(players)
        points = random.randint(5, 20)  # Random points per shot
        scores[shooter] += points
        status_text.markdown(f"🎯 **{shooter}** hit the target and scored **{points}** points!")
        time.sleep(1)
        progress = min(1.0, (time.time() - start_time) / 30)
        progress_bar.progress(progress)

    st.subheader("🏁 Time's up! Final Scores:")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for player, score in sorted_scores:
        st.write(f"🔸 {player}: **{score}** points")

    winner = sorted_scores[0][0]
    st.success(f"🏆 The winner is: **{winner}**! Well played.")
