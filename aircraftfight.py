# -*- coding: utf-8 -*-
"""Aircraftfight.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h2siYFIGpXax6KXlkZV3rHgZesS_o2Eu

# New Section
"""

import streamlit as st
import random
import time

st.set_page_config(page_title="✈️ Mars Aircraft Battle", layout="centered")

st.title("🚀 Intergalactic Aircraft Fight on Mars")

# Player name inputs
st.subheader("👨‍🚀 Name Your Space Pilots")
players = []
for i in range(6):
    name = st.text_input(f"Pilot {i+1} Name", value=f"Pilot{i+1}")
    players.append(name)

if st.button("🔥 Launch Battle!"):
    st.subheader("🌌 Mars Battle in Progress...")

    st.write("Each pilot flies a combat aircraft. They'll fight with missiles, lasers, and shields. Last one flying wins!")
    hp = {player: 100 for player in players}
    alive_players = players.copy()
    logs = st.empty()
    progress = {player: st.progress(100) for player in players}

    time.sleep(2)

    while len(alive_players) > 1:
        attacker, target = random.sample(alive_players, 2)
        damage = random.randint(10, 30)
        hp[target] -= damage
        logs.markdown(f"💥 **{attacker}** attacked **{target}** for **{damage}** damage!")

        if hp[target] <= 0:
            hp[target] = 0
            alive_players.remove(target)
            logs.markdown(f"☠️ **{target}** has been shot down!")

        for p in players:
            progress[p].progress(hp[p])

        time.sleep(1.5)

    winner = alive_players[0]
    st.success(f"🏆 The Champion of Mars is: **{winner}**! Glory to the skies!")