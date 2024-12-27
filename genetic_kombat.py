import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Genetic Kombat with Genetic Algorithm")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Log file setup
LOG_FILE = "ga_ai_moves_log.txt"
with open(LOG_FILE, "w") as log:
    log.write("AI Move Strategy Optimization Log\n\n")

# Genetic Algorithm Parameters
POPULATION_SIZE = 10  # Number of move strategies
MOVE_SEQUENCE_LENGTH = 12  # Moves per strategy
GENERATIONS = 20  # Number of generations
MUTATION_RATE = 0.2  # Probability of mutation per move

# Moves
MOVES = [
    "Punch", "Kick", "Block", "Uppercut", "Roundhouse Kick", "Low Kick",
    "Grab", "Dodge", "Spin Kick", "Elbow Strike", "Knee Strike", "Backflip Kick",
    "Counter", "Feint Attack", "Parry", "Rolling Attack"
]

class Fighter:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.hp = 100
        self.move = None
        self.cooldown = 0  # Cooldown between moves

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 100))
        if self.move:
            text = font.render(self.move, True, WHITE)
            screen.blit(text, (self.x, self.y - 30))

    def perform_move(self, move):
        if self.cooldown == 0:
            self.move = move
            self.cooldown = 30  # Add cooldown to prevent spamming moves

# Display HP function
def display_hp():
    player_hp_text = font.render(f"Player HP: {player.hp}", True, BLUE)
    ai_hp_text = font.render(f"AI HP: {ai.hp}", True, RED)
    screen.blit(player_hp_text, (50, 50))
    screen.blit(ai_hp_text, (WIDTH - 200, 50))

# Evaluate fitness of a move sequence
def evaluate_fitness(move_sequence):
    temp_player = Fighter(200, HEIGHT - 200, BLUE)
    temp_ai = Fighter(WIDTH - 300, HEIGHT - 200, RED)
    total_damage = 0
    last_move = None
    repetition_penalty = 0

    for move in move_sequence:
        temp_ai.perform_move(move)
        # Damage calculation
        if move in ["Punch", "Low Kick"]:
            total_damage += 10 if temp_player.move != "Block" else 0
        elif move in ["Kick", "Roundhouse Kick", "Spin Kick"]:
            total_damage += 15 if temp_player.move != "Block" else 0
        elif move in ["Uppercut", "Elbow Strike"]:
            total_damage += 20 if temp_player.move != "Block" else 0
        elif move == "Grab":
            total_damage += 25 if temp_player.move != "Dodge" else 0
        elif move == "Backflip Kick":
            total_damage += 30 if temp_player.move != "Counter" else 0

        # Penalize repeated moves
        if move == last_move:
            repetition_penalty += 5
        last_move = move

        # Random player move to simulate combat
        temp_player.perform_move(random.choice(MOVES))

    return total_damage - repetition_penalty

# Diversity penalty: Calculate similarity between strategies
def calculate_similarity(strategy1, strategy2):
    return sum(1 for a, b in zip(strategy1, strategy2) if a == b) / len(strategy1)

# Evaluate fitness with diversity promotion
def evaluate_fitness_with_diversity(strategy, population):
    fitness = evaluate_fitness(strategy)
    diversity_penalty = 0

    for other_strategy in population:
        similarity = calculate_similarity(strategy, other_strategy)
        if similarity > 0.7:  # Threshold for similarity
            diversity_penalty += similarity * 10  # Penalize similar strategies

    return fitness - diversity_penalty

# Generate initial population
def generate_population():
    return [[random.choice(MOVES) for _ in range(MOVE_SEQUENCE_LENGTH)] for _ in range(POPULATION_SIZE)]

# Selection: Choose top strategies based on fitness
def select_top_strategies(population, fitnesses):
    sorted_population = [x for _, x in sorted(zip(fitnesses, population), reverse=True)]
    return sorted_population[: POPULATION_SIZE // 2]

# Crossover: Create offspring by combining two strategies
def crossover(parent1, parent2):
    split_point = random.randint(1, MOVE_SEQUENCE_LENGTH - 1)
    return parent1[:split_point] + parent2[split_point:]

# Adjust mutation rate dynamically
def dynamic_mutation_rate(current_generation, total_generations):
    return MUTATION_RATE * (1 - current_generation / total_generations)

# Genetic Algorithm with diversity
def genetic_algorithm_with_diversity():
    population = generate_population()

    for generation in range(GENERATIONS):
        fitnesses = [evaluate_fitness_with_diversity(strategy, population) for strategy in population]
        best_fitness = max(fitnesses)
        best_strategy = population[fitnesses.index(best_fitness)]

        with open(LOG_FILE, "a") as log:
            log.write(f"Generation {generation + 1}: Best Fitness = {best_fitness}\n")
            log.write(f"Best Strategy: {best_strategy}\n\n")

        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

        # Selection
        top_strategies = select_top_strategies(population, fitnesses)

        # Crossover and Mutation with dynamic mutation rate
        new_population = top_strategies[:]
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.sample(top_strategies, 2)
            child = crossover(parent1, parent2)
            mutation_rate = dynamic_mutation_rate(generation, GENERATIONS)
            child = [
                random.choice(MOVES) if random.random() < mutation_rate else move
                for move in child
            ]
            new_population.append(child)

        population = new_population

    return best_strategy

# Initialize player and AI
player = Fighter(200, HEIGHT - 200, BLUE)
ai = Fighter(WIDTH - 300, HEIGHT - 200, RED)

# Run Genetic Algorithm to find the best move sequence
best_move_sequence = genetic_algorithm_with_diversity()
ai_move_index = 0

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window event
            run = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the fighters
    player.draw()
    ai.draw()

    # Display HP
    display_hp()

    # Player move input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.cooldown == 0:  # Punch
        player.perform_move("Punch")
    elif keys[pygame.K_s] and player.cooldown == 0:  # Kick
        player.perform_move("Kick")
    elif keys[pygame.K_d] and player.cooldown == 0:  # Block
        player.perform_move("Block")
    elif keys[pygame.K_q] and player.cooldown == 0:  # Uppercut
        player.perform_move("Uppercut")
    elif keys[pygame.K_w] and player.cooldown == 0:  # Roundhouse Kick
        player.perform_move("Roundhouse Kick")
    elif keys[pygame.K_e] and player.cooldown == 0:  # Low Kick
        player.perform_move("Low Kick")
    elif keys[pygame.K_r] and player.cooldown == 0:  # Grab
        player.perform_move("Grab")
    elif keys[pygame.K_t] and player.cooldown == 0:  # Dodge
        player.perform_move("Dodge")

    # AI move logic (loop through best sequence)
    if ai.cooldown == 0:
        ai.perform_move(best_move_sequence[ai_move_index % len(best_move_sequence)])
        ai_move_index += 1

    # Resolve moves simultaneously
    if player.move and ai.move:
        # Damage resolution
        if player.move in ["Punch", "Low Kick"] and ai.move != "Block":
            ai.hp -= 10
        if player.move in ["Kick", "Roundhouse Kick", "Spin Kick"] and ai.move != "Block":
            ai.hp -= 15
        if player.move in ["Uppercut", "Elbow Strike"] and ai.move != "Block":
            ai.hp -= 20
        if player.move == "Grab" and ai.move != "Dodge":
            ai.hp -= 25
        if player.move == "Backflip Kick" and ai.move != "Counter":
            ai.hp -= 30
        if ai.move in ["Punch", "Low Kick"] and player.move != "Block":
            player.hp -= 10
        if ai.move in ["Kick", "Roundhouse Kick", "Spin Kick"] and player.move != "Block":
            player.hp -= 15
        if ai.move in ["Uppercut", "Elbow Strike"] and player.move != "Block":
            player.hp -= 20
        if ai.move == "Grab" and player.move != "Dodge":
            player.hp -= 25
        if ai.move == "Backflip Kick" and player.move != "Counter":
            player.hp -= 30

        # Reset moves after resolution
        player.move = None
        ai.move = None

    # Cooldowns for player and AI (ensures they can't spam moves)
    if player.cooldown > 0:
        player.cooldown -= 1
    if ai.cooldown > 0:
        ai.cooldown -= 1

    # Check for game over
    if player.hp <= 0 or ai.hp <= 0:
        run = False

    # Update the display
    pygame.display.update()
    clock.tick(30)

# Display game over message
screen.fill(WHITE)
if player.hp <= 0:
    result_text = font.render("You Lost! AI Wins.", True, RED)
elif ai.hp <= 0:
    result_text = font.render("You Win! AI Defeated.", True, BLUE)
screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2))
pygame.display.update()
pygame.time.delay(3000)
pygame.quit()
