import pygame
import sys

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 400
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street Fighter Clone")

# Load images
fighter1_img = pygame.image.load("images/fighter1.png")
fighter2_img = pygame.image.load("images/fighter2.png")
background_img = pygame.image.load("images/background.png")

# Scale images (optional, based on size)
fighter1_img = pygame.transform.scale(fighter1_img, (100, 100))
fighter2_img = pygame.transform.scale(fighter2_img, (100, 100))

# Game variables
fighter1_health = 100
fighter2_health = 100
fighter_speed = 5

# Fighter positions
fighter1_rect = fighter1_img.get_rect(topleft=(100, 250))
fighter2_rect = fighter2_img.get_rect(topleft=(600, 250))

# Main game loop
clock = pygame.time.Clock()

def draw_health_bars():
    # Fighter 1 health bar
    pygame.draw.rect(screen, RED, (20, 20, 200, 20))
    pygame.draw.rect(screen, BLUE, (20, 20, fighter1_health * 2, 20))

    # Fighter 2 health bar
    pygame.draw.rect(screen, RED, (580, 20, 200, 20))
    pygame.draw.rect(screen, BLUE, (580, 20, fighter2_health * 2, 20))

def handle_fighter_movement(keys):
    global fighter1_rect, fighter2_rect

    # Fighter 1 Movement
    if keys[pygame.K_a]:
        fighter1_rect.x -= fighter_speed
    if keys[pygame.K_d]:
        fighter1_rect.x += fighter_speed
    if keys[pygame.K_w]:
        fighter1_rect.y -= fighter_speed
    if keys[pygame.K_s]:
        fighter1_rect.y += fighter_speed

    # Fighter 2 Movement
    if keys[pygame.K_LEFT]:
        fighter2_rect.x -= fighter_speed
    if keys[pygame.K_RIGHT]:
        fighter2_rect.x += fighter_speed
    if keys[pygame.K_UP]:
        fighter2_rect.y -= fighter_speed
    if keys[pygame.K_DOWN]:
        fighter2_rect.y += fighter_speed

# Main game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Draw background
    screen.blit(background_img, (0, 0))

    # Draw fighters
    screen.blit(fighter1_img, fighter1_rect)
    screen.blit(fighter2_img, fighter2_rect)

    # Draw health bars
    draw_health_bars()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement
    keys = pygame.key.get_pressed()
    handle_fighter_movement(keys)

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
