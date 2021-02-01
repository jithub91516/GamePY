import pygame

#####################################################################################################################

#initialization
pygame.init() 

# size of board
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#title 
pygame.display.set_caption("JI gAmE")

#FPS
clock = pygame.time.Clock()

#####################################################################################################################

# 1. set up the game(background, game image coordinate, speed, font)



running = True
while running:
    dt = clock.tick(30) #set up the amount of frames

    # 2. figure out the event (keyboard, mouse)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    
    # 3. positions of characters 

    # 4. check up the collision

    # 5. draw on the screen

    pygame.display.update()    

#pygame exit
pygame.quit()