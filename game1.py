import pygame
pygame.init()

window = pygame.display.set_mode((500,500))
window.fill((255,255,255))
pygame.display.flip()

red = pygame.Rect(40,40,150,150)
green = pygame.Rect(190,40,150,150)
blue = pygame.Rect(340,40,150,150)
purple = pygame.Rect(40,190,150,150)
orange = pygame.Rect(190,190,150,150)
pink = pygame.Rect(340,190,150,150)

rectsData = [(red, (255, 38, 71)),(green, (89 , 255, 89)), (blue, (43, 132, 255)), (purple, (111, 0, 255)), (orange, (255, 132, 0)), (pink, (246, 71, 255))]

running = True

def drawRectangles(margin_x,margin_y,win_size):
    space_x = win_size - (margin_x * 2)
    rect_size = space_x / 3
    for i in range (3):
        pos_x = margin_x + (i * rect_size)
        rectsData[i].append(pygame.Rect(pos_x, margin_y,rect_size, rect_size))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255,255,255))
    pygame.draw.circle(window, (0,0,0), pygame.mouse.get_pos(), 10)
    

    #Draw Rects
    for i in rectsData:
        pygame.draw.rect(window, i[1], i[0])

    
    pygame.display.flip()
