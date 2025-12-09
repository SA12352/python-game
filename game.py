import streamlit as st
import random

# --- Word List ---
WORDS = ["python", "gaming", "mango", "streamlit", "developer", "facebook", "hangman"]

st.title("🎮 Guess The Word — One Letter At A Time")

# --- Setup session states ---
if "secret_word" not in st.session_state:
    st.session_state.secret_word = random.choice(WORDS)

if "lives" not in st.session_state:
    st.session_state.lives = 6

if "guessed_letters" not in st.session_state:
    st.session_state.guessed_letters = []

# --- Custom word Input ---
st.subheader("Want to play with your own secret word?")
custom = st.text_input("Enter custom word (optional):")

if st.button("Set Custom Word"):
    if custom.isalpha():
        st.session_state.secret_word = custom.lower()
        st.session_state.lives = 6
        st.session_state.guessed_letters = []
        st.success("Custom word set successfully!")
    else:
        st.error("Only alphabets allowed.")

# --- Display hidden word ---
display_word = ""
for letter in st.session_state.secret_word:
    if letter in st.session_state.guessed_letters:
        display_word += letter + " "
    else:
        display_word += "_ "

st.markdown(f"### Word: {display_word}")
st.markdown(f"❤️ **Lives Left:** {st.session_state.lives}")
st.markdown(f"🔎 **Guessed Letters:** {', '.join(st.session_state.guessed_letters) if st.session_state.guessed_letters else '-'}")

# --- Letter input ---
guess = st.text_input("Enter a letter").lower()

if st.button("Guess"):
    if len(guess) != 1 or not guess.isalpha():
        st.error("Please enter a single letter.")
    elif guess in st.session_state.guessed_letters:
        st.warning("You already guessed this letter!")
    else:
        st.session_state.guessed_letters.append(guess)

        if guess in st.session_state.secret_word:
            st.success("Correct guess!")
        else:
            st.session_state.lives -= 1
            st.error("Wrong guess!")

# --- Game over checks ---
if st.session_state.lives <= 0:
    st.error(f"💀 Game Over! The word was: **{st.session_state.secret_word}**")
    if st.button("Play Again"):
        st.session_state.secret_word = random.choice(WORDS)
        st.session_state.lives = 6
        st.session_state.guessed_letters = []

elif all(letter in st.session_state.guessed_letters for letter in st.session_state.secret_word):
    st.success(f"🎉 You won! The word was: **{st.session_state.secret_word}**")
    if st.button("Play Again"):
        st.session_state.secret_word = random.choice(WORDS)
        st.session_state.lives = 6
        st.session_state.guessed_letters = []
