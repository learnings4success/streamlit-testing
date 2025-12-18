import streamlit as st
import random

# --- 1. SETUP SESSION STATE (To remember history) ---
# If 'scores' doesn't exist in memory, create an empty list
if 'scores' not in st.session_state:
    st.session_state.scores = []

# Constants for points
WINNING_SCORE = 10
LOOSER_SCORE = 0
DRAW_SCORE = 5

st.title("🪨📄✂️ Stone Paper Scissor")
st.write("Enter names, click Play, and watch them fight!")

# --- 2. INPUTS (Get Player Names) ---
# We use columns to make it look nice side-by-side
col1, col2 = st.columns(2)

with col1:
    player1_name = st.text_input("Player 1 Name")

with col2:
    player2_name = st.text_input("Player 2 Name")

# --- 3. THE GAME LOGIC (Triggered by Button) ---
# This button replaces the "while start == 'yes'" loop
if st.button("Play Round 👊"):
    
    game_options = ["stone", "paper", "scissor"]
    
    # Random selection for BOTH players (Simulation)
    action_1 = random.choice(game_options)
    action_2 = random.choice(game_options)

    # Dictionary to map words to Emojis for display
    emoji_map = {"stone": "🪨", "paper": "📄", "scissor": "✂️"}

    # --- Display Moves ---
    st.markdown("### Result:")
    
    # Show big visual results
    r1, r2 = st.columns(2)
    with r1:
        st.info(f"{player1_name}: {emoji_map[action_1]}")
    with r2:
        st.info(f"{player2_name}: {emoji_map[action_2]}")

    # --- Determine Winner ---
    result_msg = ""
    
    # LOGIC: Check who won
    if action_1 == action_2:
        result_msg = f"It's a Draw! Both get {DRAW_SCORE} points."
        st.warning(result_msg)
        # Save to history
        st.session_state.scores.append((player1_name, DRAW_SCORE, player2_name, DRAW_SCORE))
        
    elif (action_1 == "stone" and action_2 == "scissor") or \
         (action_1 == "paper" and action_2 == "stone") or \
         (action_1 == "scissor" and action_2 == "paper"):
        
        result_msg = f"🎉 {player1_name} Wins! ({action_1} beats {action_2})"
        st.success(result_msg)
        # Save to history
        st.session_state.scores.append((player1_name, WINNING_SCORE, player2_name, LOOSER_SCORE))
        
    else:
        result_msg = f"🎉 {player2_name} Wins! ({action_2} beats {action_1})"
        st.success(result_msg)
        # Save to history
        st.session_state.scores.append((player2_name, WINNING_SCORE, player1_name, LOOSER_SCORE))

# --- 4. DISPLAY HISTORY (Scoreboard) ---
st.divider()
st.subheader("📊 Score History")

if len(st.session_state.scores) > 0:
    # We display the list stored in session_state
    for i, score in enumerate(st.session_state.scores):
        p1, s1, p2, s2 = score
        st.write(f"**Round {i+1}:** {p1} ({s1}) vs {p2} ({s2})")
        
    # Button to clear history
    if st.button("Reset Scoreboard 🗑️"):
        st.session_state.scores = []
        st.rerun()
else:
    st.write("No games played yet.")