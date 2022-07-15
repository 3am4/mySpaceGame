import pygame
import os


WHITE = (255,255,255)
WIDTH, HEIGHT = 900, 500
MIDDLE_LINE = WIDTH//2
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
WIN = pygame.display.set_mode( (WIDTH,HEIGHT) )
FPS = 60
VEL = 4
ZERO_X2 = 0,0


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join( "Assets", "spaceship_yellow.png" )  )
YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP_IMAGE = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)
SPACE_IMAGE = pygame.image.load(os.path.join( "Assets", "space.png" )  )
SPACE_IMAGE = pygame.transform.scale(SPACE_IMAGE, (900,500))
SHOT_IMAGE = pygame.image.load(os.path.join("Assets", "shot.png"))
SHOT_IMAGE = pygame.transform.scale(SHOT_IMAGE, (50,45))
LINE_IMAGE = pygame.image.load(os.path.join("Assets", "line.png"))
LINE_IMAGE = pygame.transform.scale(LINE_IMAGE, (10,1000))

pygame.display.set_caption("space.py")


def draw_window(red, yellow):
    WIN.blit(SPACE_IMAGE, (ZERO_X2) )
    #WIN.fill(WHITE)
    WIN.blit(SHOT_IMAGE, (100, 300))
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x,red.y))
    #WIN.blit(LINE_IMAGE, (WIDTH//2,0) )
    pygame.draw.line(SPACE_IMAGE, (255,0,0), (WIDTH//2,0), (WIDTH//2,HEIGHT))
        
    pygame.display.update()



def main():
    red = pygame.Rect(800, 200, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 200, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True

    """
    yellow_shot = False
    red_shot = False
    """
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #print("yellow", yellow.x, yellow.y)
            #print("red" , red.x, red.y)
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_a]: #LEFT
            yellow.x -=VEL
            
        if keys_pressed[pygame.K_d]: #RIGHT
                yellow.x +=VEL
                
        if keys_pressed[pygame.K_w]: #UP
            yellow.y -= VEL
            
        if keys_pressed[pygame.K_s]: #DOWN
            yellow.y += VEL
        if keys_pressed[pygame.K_SPACE]:
            yellow_shot = True
            
            
        if keys_pressed[pygame.K_LEFT]: #LEFT
            red.x -=VEL
            
        if keys_pressed[pygame.K_RIGHT]: #RIGHT
                red.x +=VEL
                
        if keys_pressed[pygame.K_UP]: #UP
            red.y -= VEL
            
        if keys_pressed[pygame.K_DOWN]: #DOWN
            red.y += VEL
            
        if keys_pressed[pygame.K_e]:
            red_shot = True
            
        red.y = max(min(red.y, HEIGHT-SPACESHIP_WIDTH), 0)
        red.x = max(min(red.x, WIDTH-SPACESHIP_HEIGHT), MIDDLE_LINE)
        
        yellow.y = max(min(yellow.y, HEIGHT-SPACESHIP_HEIGHT), 0)
        yellow.x = min(max(yellow.x, 0), MIDDLE_LINE-(SPACESHIP_WIDTH-15))
        
        draw_window(red, yellow)
    
    pygame.quit()


if __name__ == "__main__":
    main()