# Treasure Runner

## Overview

Treasure Runner is a simple 2D chase game I made using Python and PyGame. The player controls a blue square and moves around the screen collecting coins while an enemy follows and tries to catch them.
The main challenge is that the enemy gets faster as more coins are collected. This means the game starts off fairly easy, but becomes harder the longer the player survives.
I built this project to get more practice with PyGame, especially drawing objects on the screen, handling keyboard input, detecting collisions, and managing game state.

## Development Notes

The original plan for Treasure Runner included several features such as animations, sound effects, menus, and additional gameplay elements. As development progressed, I adjusted the scope of the project and focused on getting the core gameplay working well first.
The current version focuses on player movement, coin collection, scoring, health, enemy chasing, collision detection, restarting the game, and increasing difficulty as the player collects more coins.
Some of the features from the original plan were considered during development but were left for later improvements as I focused on making the main game mechanics stable and playable.


## Purpose

The main purpose of this project was to practice object-oriented programming and event-driven programming.
I also wanted to learn how to make a simple game where the difficulty changes while the player is playing. Instead of making the enemy use complicated AI, I used a simple chase/following system that moves the enemy toward the player.

## Features

* Player movement using the arrow keys
* Enemy that follows the player
* Coin collection and score tracking
* Health system
* Game restart using the `R` key
* Enemy speed increases as coins are collected
* Collision detection between the player, enemy, and coins

## Controls

| Key | Action       |
| --- | ------------ |
| ↑   | Move Up      |
| ↓   | Move Down    |
| ←   | Move Left    |
| →   | Move Right   |
| R   | Restart Game |

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Install PyGame

Open a terminal in the project folder and run:

```bash
pip install pygame
```

### 3. Run the Game

Run:

```bash
python main.py
```

## Project Structure

```text
TreasureRunner/
│
├── assets/        # Images and sprites
├── coin.py        # Coin logic
├── enemy.py       # Enemy behavior
├── game.py        # Main game loop
├── main.py        # Program entry point
├── player.py      # Player movement and health
├── settings.py    # Game constants and settings
└── README.md      # Project documentation
```

## Technologies Used

* Python 3
* PyGame

## Future Improvements

If I continue working on Treasure Runner, I would like to add:

* Sound effects when collecting coins and taking damage
* Background music
* Different types of enemies with different movement patterns
* Obstacles around the map
* A main menu with different difficulty levels
* A high-score system that saves scores between games

## Author

Wamala Bright
Github repo:  https://github.com/Wamala-Bright/HelloWorld
Loom video :  https://www.loom.com/share/bc17373dcef347a7ab29923b932f566a