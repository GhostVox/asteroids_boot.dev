# Asteroids Game

A classic Asteroids-style arcade game built with Python and Pygame. This project was created as part of the [Boot.dev](https://www.boot.dev) curriculum to practice Object-Oriented Programming (OOP) concepts in Python.

## Game Overview

Navigate your spaceship through a field of asteroids, shooting them to survive! When you shoot large asteroids, they split into smaller pieces, creating an increasingly challenging environment. The game features:

- **Player-controlled spaceship** with rotation and thrust mechanics
- **Dynamic asteroid field** that continuously spawns new asteroids
- **Physics-based movement** with realistic momentum
- **Collision detection** between player, shots, and asteroids
- **Asteroid splitting mechanics** - large asteroids break into smaller ones when shot

## Controls

- **W** - Thrust forward
- **S** - Thrust backward
- **A** - Rotate left
- **D** - Rotate right
- **SPACE** - Shoot
- **Close window** or **Ctrl+C** - Exit game

## Prerequisites & Installation

### Required Software

- **Python 3.7+** - Download from [python.org](https://python.org)
- **pip** (usually comes with Python)

### Setting Up the Project

1. **Clone or download the repository**

   ```bash
   git clone [your-repo-url]
   cd asteroids_boot.dev
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   **On Windows:**

   ```bash
   venv\Scripts\activate
   ```

   **On macOS/Linux:**

   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

Once you have pygame installed, simply run:

```bash
python main.py
```

The game window will open at 1280x720 resolution. Use the controls listed above to play!

## Project Structure

```
asteroids_boot.dev/
├── main.py              # Main game loop and initialization
├── player.py            # Player spaceship class
├── asteroid.py          # Asteroid objects and splitting logic
├── asteroidfield.py     # Asteroid spawning system
├── shot.py              # Player projectiles
├── circleshape.py       # Base class for circular game objects
├── constants.py         # Game configuration and constants
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Game Mechanics

### Player Ship

- Triangle-shaped spaceship that can rotate and thrust
- Momentum-based movement (ship continues moving when not thrusting)
- Limited shooting rate with cooldown period
- Game ends when colliding with an asteroid

### Asteroids

- Spawn randomly from screen edges
- Move in straight lines across the screen
- Come in three different sizes (small, medium, large)
- Split into two smaller asteroids when shot (except smallest size)
- Smaller asteroids move faster than larger ones

### Shots

- Fire in the direction the ship is facing
- Travel at high speed across the screen
- Destroy themselves when hitting asteroids
- Limited by shooting cooldown to prevent spam

## Configuration

Game settings can be modified in `constants.py`:

- **Screen dimensions**: `SCREEN_WIDTH`, `SCREEN_HEIGHT`
- **Player settings**: `PLAYER_SPEED`, `PLAYER_TURN_SPEED`, `PLAYER_SHOOT_COOLDOWN`
- **Asteroid settings**: `ASTEROID_SPAWN_RATE`, `ASTEROID_MIN_RADIUS`, `ASTEROID_KINDS`
- **Shot settings**: `SHOT_RADIUS`, `PLAYER_SHOOT_SPEED`

## Learning Objectives

This project demonstrates key programming concepts:

- **Object-Oriented Programming**: Classes, inheritance, and encapsulation
- **Game development patterns**: Game loops, sprite groups, and collision detection
- **Vector mathematics**: 2D movement, rotation, and physics
- **Event handling**: Keyboard input and game state management
- **Code organization**: Modular design with separate classes for different game objects
- **Virtual environments**: Managing Python dependencies with venv

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'pygame'"**

- Make sure you've activated your virtual environment
- Install pygame: `pip install pygame`

**Game runs too fast/slow**

- The game is capped at 60 FPS. If performance issues occur, check your system specifications

**Virtual environment issues**

- Ensure you're in the correct directory when creating/activating venv
- Try recreating the virtual environment if activation fails

## Future Enhancements

Potential improvements you could add:

- Score system and high scores
- Multiple lives for the player
- Power-ups and special weapons
- Sound effects and background music
- Particle effects for explosions
- Menu system and pause functionality

## Dependencies

- **pygame 2.6.0** - Cross-platform game development library

Perfect for Python developers looking to learn game development fundamentals and practice OOP concepts in a fun, interactive project!
