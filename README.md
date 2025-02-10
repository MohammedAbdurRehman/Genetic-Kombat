# Genetic-Kombat (A Fighting Game Using Genetic Algorithm)  

## Abstract  

This project simulates a Tekken-inspired combat game where a player competes against an AI in a fast-paced battle. The AI uses a **Genetic Algorithm (GA)** with diversity-driven optimization to generate move strategies, showcasing an innovative approach to game AI design.  

## Problem Statement  

The goal of this project is to integrate Genetic Algorithm principles into an interactive combat game to simulate intelligent AI behavior. The focus is on evolving effective move strategies that challenge human players while promoting diverse gameplay.  

## Proposed Solution  

The AI employs a **Genetic Algorithm** to generate optimized move strategies. The algorithm evaluates each move sequence for fitness, applies diversity penalties, and evolves over multiple generations to create a competitive AI player. Human interaction is enabled through keyboard inputs, with simultaneous move resolution between the player and AI.  

## Methodology  

### Initialization  
- The game is built using **Pygame**, with a custom game window, clock, and font setup.  
- A log file records the optimization process for AI moves.  

### Fighter Class  
- **Attributes**: Tracks each fighter’s health points (HP), current move, and cooldown.  
- **Methods**: Handles visual representation and move execution.  

### AI Move Generation  
- **Population**: AI strategies are initialized as a population of random move sequences.  
- **Fitness Evaluation**: Each strategy is scored based on its effectiveness in combat and penalized for move repetition or excessive similarity to other strategies.  
- **Evolution**: Crossover and mutation mechanisms create new strategies, dynamically adjusting mutation rates over generations.  

### Combat Resolution  
- **Simultaneous Moves**: Both player and AI perform moves simultaneously.  
- **Damage Logic**: Move combinations determine damage dealt based on rules (e.g., attacks are blocked if countered with "Block").  
- **Cooldown**: Ensures realistic pacing by introducing delays between consecutive moves.  

## Results  

The project achieves a dynamic, turn-based combat experience with:  
1. **Interactive Gameplay**: Players control their moves using keyboard inputs.  
2. **Evolving AI**: AI adapts over generations to execute optimized and diverse strategies.  
3. **Balanced Mechanics**: Damage and cooldown mechanics create a fair challenge for players.  

## Code Highlights  

### Genetic Algorithm:  
- **Dynamic Mutation Rate**: The mutation rate decreases over generations, mimicking real-world evolution.  
- **Diversity Promotion**: Similar move sequences are penalized to encourage varied strategies.  

### Combat Mechanics:  
- **Simultaneous Moves**: Both fighters perform moves at the same time, adding realism.  
- **Health Tracking**: The game ends when either player’s HP reaches zero.  

### AI Strategy Optimization:  
- **Fitness Evaluation**: Strategies are scored based on inflicted damage and diversity.  
- **Evolutionary Steps**: Top strategies are selected, crossed, and mutated for improvement.  

## Visualization  

The game features:  
- **Graphical Fighter Representation**: Fighters are displayed as rectangles with associated moves shown above them.  
- **Health Indicators**: HP for both players is displayed on the screen.  
- **Final Result Screen**: Indicates whether the player won or lost after the game ends.  

## Conclusion  

This project effectively applies **Genetic Algorithm principles** to create a competitive and challenging AI opponent. The diversity-driven optimization ensures varied gameplay, while the combat mechanics provide a fair balance between player and AI.  

### Future Improvements:  
1. Incorporate **real-time learning** for the AI to adapt during gameplay.  
2. Implement more advanced move interactions, such as counterattacks and combos.  
3. Enhance visualization with animations and effects for moves.  

## Inline Comments in Code  

The code includes comprehensive inline comments for clarity on:  
- **Genetic Algorithm Steps**: Explains each stage of initialization, evaluation, selection, crossover, and mutation.  
- **Combat Mechanics**: Describes damage rules, cooldown implementation, and simultaneous move resolution.  
- **Pygame Components**: Details the drawing of fighters, health bars, and updating the display.  

## Inputs and Outputs  

### Inputs  
- **Player Inputs**:  
  - `A`: Punch  
  - `S`: Kick  
  - `D`: Block  
  - `Q`: Uppercut  
  - `W`: Roundhouse Kick  
  - `E`: Low Kick  
  - `R`: Grab  
  - `T`: Dodge  

### Outputs  
- **On-Screen Visualization**: Fighter positions, current moves, and health bars.  
- **Final Result**: Displays a win/lose message upon game completion.  
- **Log File**: Records the AI optimization process across generations.  
