import pygame
import os


WHITE = (255,255,255)
WIDTH, HEIGHT = 900, 500
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
VEL = 4
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP_IMAGE = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

pygame.display.set_caption("space.py")


def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x,red.y))
    
    pygame.display.update()



def main():
    red = pygame.Rect(800, 200, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 200, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: #LEFT
            yellow.x -=VEL
            
        if keys_pressed[pygame.K_d]: #RIGHT
                yellow.x +=VEL
                
        if keys_pressed[pygame.K_w]: #UP
            yellow.y -= VEL
            
            
        draw_window(red, yellow)
    
    pygame.quit()


if __name__ == "__main__":
    main()