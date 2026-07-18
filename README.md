# Treasure Runner

## Overview

Treasure Runner is a 2D adventure game developed to improve my skills in software development, game programming, and object-oriented design. The purpose of this project is to create an interactive gaming experience where players explore environments, collect treasures, avoid enemies, unlock doors, and progress through challenging levels.

This software demonstrates concepts such as game loops, user input handling, collision detection, object-oriented programming, level management, asset organization, and modular software design. The project is designed with a focus on writing clean, maintainable code while continuously improving gameplay mechanics and user experience.

The current features of Treasure Runner include:

- Player movement using keyboard controls
- Treasure collection system
- Enemy movement and player chasing behavior
- Health and scoring system
- Level progression system
- Key and door unlocking mechanics
- Map obstacles and collision detection
- Sprite and asset management structure
- Modular game components using separate Python files

The goal of this project is to continue expanding the game into a complete adventure experience while developing stronger software engineering skills.

A demonstration video showing the software running and a walkthrough of the code can be found here:

[Software Demo Video] https://www.loom.com/share/5794b9abf37841a9a3f4d0454256886a

# Development Environment

This project was developed using the following tools:

- Visual Studio Code for coding and project management
- Git and GitHub for version control
- Python virtual environment for dependency management
- Windows PowerShell terminal for running and testing the application

Programming language used:

- Python

Libraries used:

- Pygame - for graphics, game development, keyboard input, collision detection, and game mechanics

---

# How to Run the Software

Follow these steps to run Treasure Runner locally.

### 1. Clone the repository

```bash
git clone https://github.com/Wamala-Bright/HelloWorld.git
```

### 2. Navigate into the project folder

```bash
cd HelloWorld
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 5. Install required dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the game

```bash
python src/main.py
```

---

# Project Structure

```
HelloWorld/

│
├── assets/
│   ├── images/
│   └── sounds/
│
├── src/
│   ├── main.py
│   ├── player.py
│   ├── enemy.py
│   ├── treasure.py
│   ├── level.py
│   ├── map.py
│   ├── obstacle.py
│   └── settings.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# Game Features

## Player System

- Keyboard-controlled player movement
- Collision detection with walls and obstacles
- Health tracking
- Score tracking
- Key inventory system

## Treasure System

- Collectible treasures placed throughout levels
- Score rewards for collecting items
- Progression through exploration

## Enemy System

- Enemies move toward the player
- Difficulty increases as levels progress
- Collision damage system
- Enemy spawning system

## Level System

- Multiple difficulty levels
- Level progression
- Locked doors requiring keys
- Expandable map system

---

# Useful Websites

- Pygame Documentation  
https://www.pygame.org/docs/

- Python Documentation  
https://docs.python.org/3/

- GitHub Documentation  
https://docs.github.com/

- Real Python - Python Game Development  
https://realpython.com/

- Kenney Game Assets  
https://kenney.nl/assets

---

# Future Improvements

Future versions of Treasure Runner will include:

- Animated player and enemy sprites
- Background music and sound effects
- More detailed maps and environments
- Inventory system
- Weapons and combat mechanics
- Boss battles
- Save and load functionality
- Improved menus and user interface
- More advanced enemy artificial intelligence
- Exporting the game into a standalone application

---

# Author

Wamala Bright

GitHub Profile:

https://github.com/Wamala-Bright

Project Repository:

https://github.com/Wamala-Bright/HelloWorld