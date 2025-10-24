
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objetivo

Build the classic word-guessing game using Python strings, loops, and user input. Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tarefas

### 🛠️ Word Selection

#### Description
Implement a function that randomly selects a word from a predefined list to be used in the game.

#### Requirements
Completed program should:

- Create a list with at least 5-10 different words
- Use the `random` module to select a word randomly
- Return the selected word in lowercase for consistency

### 🛠️ Game Display

#### Description
Create functions to display the current state of the game, showing guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Display the word with unguessed letters as underscores (e.g., `_ _ _ _ _`)
- Show previously guessed letters
- Display the number of incorrect guesses remaining
- Use clear and formatted output for better user experience

### 🛠️ Game Logic

#### Description
Implement the core game logic that accepts letter guesses, validates input, and determines win/lose conditions.

#### Requirements
Completed program should:

- Accept single letter guesses from the user
- Validate that input is a single letter (not a number or multiple characters)
- Update the game state based on correct or incorrect guesses
- Track incorrect guesses with a maximum limit (e.g., 6 attempts)
- End the game when the word is fully guessed or attempts are exhausted
- Display appropriate win or lose messages with the revealed word
