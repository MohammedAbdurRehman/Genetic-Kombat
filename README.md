# Genetic-Kombat

#### **Abstract**
This script simulates a Tekken-inspired AI battle where a player competes against an AI using moves such as Punch, Kick, and Block. The AI employs a Genetic Algorithm-like method to generate moves, showcasing a basic application of randomness in decision-making.

#### **Problem Statement**
The project aims to demonstrate the application of Genetic Algorithm principles to simulate decision-making in a game setting. The focus is on optimizing AI behavior for realistic interaction with a human player.

#### **Proposed Solution**
The script applies Genetic Algorithm principles by pre-generating a sequence of moves for the AI. These moves mimic natural selection and variability, enabling the AI to "evolve" its responses. The interaction between the player and the AI is resolved through a rule-based combat mechanism.

#### **Methodology**
1. **Initialization**: Pygame is initialized, and the game window, clock, and font are set up.
2. **Fighter Class**:
   - Handles the player's and AI's attributes, including health points (HP), current move, and cooldown.
   - Includes methods for drawing fighters and performing moves.
3. **AI Move Generation**:
   - A function `generate_ai_moves` creates a list of 20 moves (`Punch`, `Kick`, or `Block`) for the AI using randomness, reflecting the Genetic Algorithm's stochastic nature.
4. **Game Loop**:
   - Processes player inputs and resolves moves.
   - AI executes its pre-generated moves sequentially.
   - Combat resolution reduces HP based on the move combination.
   - The loop ends when either player's HP reaches 0.
5. **Cooldown Mechanism**: Ensures that moves aren't spammed, creating a realistic combat dynamic.

#### **Results**
The script implements a simple, turn-based combat system where:
- Players interact with controls to perform moves.
- AI uses pre-generated moves influenced by Genetic Algorithm principles.
- The outcome (win, loss, draw) is determined based on remaining HP.

#### **Code Highlights**
- **Player Input**: Players use keyboard keys (`A` for Punch, `S` for Kick, `D` for Block) to attack or defend.
- **AI Logic**: AI moves are chosen from a pre-defined list generated randomly, simulating Genetic Algorithm diversity.
- **Move Resolution**: Damage rules based on the current moves of both players:
  - Punch/Kick deals damage unless blocked.
  - Player and AI HP decrements accordingly.

#### **Visualization**
The game includes:
- Graphical representation of fighters using rectangles.
- Text-based display of HP for both player and AI.
- Result display at the end of the game indicating victory, loss, or draw.

#### **Conclusion**
This project successfully applies Genetic Algorithm-like random move generation for AI in a combat simulation. The randomness adds unpredictability, making the AI challenging. Future improvements could include:
- Adding more complex AI strategies based on historical player moves.
- Including a mutation mechanism to adapt AI behavior over time.
- Incorporating dynamic visualization of Genetic Algorithm convergence.

#### **Inline Comments in Code**
The script includes inline comments explaining the logic for:
- Class methods (`draw`, `perform_move`).
- AI move generation (`generate_ai_moves`).
- Player and AI move resolution logic.
- Key Pygame mechanics for updating the game window.

#### **Inputs and Outputs**
- **Inputs**: Keyboard controls (`A`, `S`, `D`) for player moves.
- **Outputs**: Graphical game state, health bars, and a final result message.

