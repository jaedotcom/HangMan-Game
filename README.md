# Hangman Game

This repository contains the implementation of the classic Hangman game in Python. The objective of the Hangman game is for a player to guess a word by guessing the letters it contains. Each incorrect guess results in part of the gallows being drawn. The game is over when the gallows are fully printed out (player loses) or the player successfully guesses all the letters in the word within the 7 phases.

## Features

- Random word selection from a dictionary file
- Interactive gameplay with feedback on guesses
- Drawing of the gallows as the game progresses

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/jaedotcom/HangMan-Game.git
   cd HangMan-Game
   ```

2. Ensure you have a dictionary file with valid words (one word per line).

### Usage

1. Run the game:

   ```sh
   python Hangman.py
   ```

2. Follow the on-screen instructions to play the game.

## Files

- `Hangman.py`: Main file to run the Hangman game.
- `Dictionary_Reader.py`: Contains the `DictionaryReader` class to read and validate words from the dictionary file.
- `Word.py`: Contains the `Word` class to manage the word being guessed.
- `Drawing.py`: Contains the `Drawing` class to manage the drawing of the gallows.

## Author

- Jae Kim
