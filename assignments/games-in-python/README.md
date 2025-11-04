
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman word-guessing game in Python that uses strings, loops, conditionals, and user input. The program should be implemented as a console application and be robust to common input issues.

## 📝 Tasks

### 🛠️	Build the Hangman Game

#### Description
Create a console-based Hangman game where the program randomly selects a hidden word and the player guesses letters until they either reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select words from a predefined list contained in the program (or loaded from a small text file).
- Accept single-letter guesses and display the current progress using an underscore-separated format (e.g. _ a _ _ e).
- Track and display the number of incorrect guesses remaining (standard: 6 attempts or similar).
- End the game when the word is fully guessed or when attempts are exhausted and display an appropriate win/lose message revealing the word.
- Handle repeated guesses (do not count them twice) and ignore non-letter or empty input.
- Be case-insensitive for guesses (treat 'A' and 'a' the same).

##### Example session (simplified)

```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Good guess: _ a _ _ _
Incorrect guesses left: 6
```

### 🛠️	Stretch Goals (optional)

#### Description
Add one or more extra features to make the game more polished or challenging.

#### Requirements (pick any)

- Add simple ASCII-art for the hangman that progresses with each wrong guess.
- Provide difficulty levels (short list: easy/medium/hard) that change allowed attempts or word length.
- Allow the player to request a hint (e.g., reveal one letter) at the cost of extra incorrect guesses.
- Save and display a simple high-score list (local file) by number of wins or fewest guesses.

---

Follow the template and keep this file as `README.md` in the `assignments/games-in-python` folder. Include any starter code in `starter-code.py` and add sample word lists or data files to the assignment folder if you use them.
