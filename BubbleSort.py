import pygame
import random

pygame.init()

w, h = 800, 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Bar Chart Sorting || Demo'ing Sorting Algorithms")

xPos = [i * 8 for i in range(100)]
yPos = [500] * 100

barSize = [random.randint(1, 100) for i in range(100)]

def bubble_sort():
    global barSize
    n = len(barSize)
    for i in range(n):
        for j in range(0, n-i-1):
            if barSize[j] > barSize[j+1]:
                barSize[j], barSize[j+1] = barSize[j+1], barSize[j]

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not all(barSize[i] == barSize[0] for i in range(len(barSize))):
        bubble_sort()

    for i in range(len(barSize)):
        pygame.draw.rect(screen, RED, (xPos[i], yPos[i], 8, barSize[i]))

    pygame.display.flip()

pygame.quit()
