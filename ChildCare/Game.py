import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireworks Show")

# Colors (expanded color scheme)
COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (255, 105, 180), (255, 192, 203), (255, 215, 0), (0, 191, 255), (138, 43, 226)]

# Firework class
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.exploded = False
        self.particles = []
        self.explode_time = random.randint(50, 80)
        self.color = random.choice(COLORS)

    def explode(self):
        self.exploded = True
        num_particles = random.randint(100, 150)
        for _ in range(num_particles):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(3, 10)
            lifetime = random.randint(50, 100)
            self.particles.append([self.x, self.y, math.cos(angle) * speed, math.sin(angle) * speed, lifetime, self.color])

    def update(self):
        if not self.exploded:
            self.y -= 5
            if self.y <= random.randint(200, 400):
                self.explode()
        else:
            self.explode_time -= 1
            if self.explode_time <= 0:
                self.particles = []

        for particle in self.particles:
            particle[0] += particle[2]
            particle[1] += particle[3]
            particle[3] += 0.2  # Adding gravity
            particle[4] -= 1

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 2)
        else:
            for particle in self.particles:
                pygame.draw.circle(screen, particle[5], (int(particle[0]), int(particle[1])), random.randint(1, 4))

# Main game loop
fireworks = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    # Launch new fireworks randomly
    if random.randint(0, 100) < 5:  # Increased frequency of launching fireworks
        for _ in range(random.randint(2, 4)):  # Launch multiple fireworks at once
            fireworks.append(Firework(random.randint(50, WIDTH - 50), HEIGHT))

    # Update and draw fireworks
    for firework in fireworks:
        firework.update()
        firework.draw()

    # Remove finished fireworks
    fireworks = [firework for firework in fireworks if not (firework.exploded and len(firework.particles) == 0)]

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
