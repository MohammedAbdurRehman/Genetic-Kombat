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

# Fighter class
class Fighter:
    def _init_(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.hp = 100
        self.move = None
        self.cooldown = 0  # Cooldown between moves

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 100))
        if self.move:
            text = font.render(self.move, True, BLACK)
            screen.blit(text, (self.x, self.y - 30))
