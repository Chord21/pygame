import pygame
pygame.init()

window = pygame.display.set_mode((500,500))
window.fill((255,255,255))
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255,255,255))
    pygame.draw.circle(window, (0,0,0), pygame.mouse.get_pos(), 10)
    pygame.display.flip()