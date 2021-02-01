import os 
import pygame
#####################################################################################################################

#initialization
pygame.init() 

# size of board
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

#title 
pygame.display.set_caption("JI Pang")

#FPS
clock = pygame.time.Clock()

#####################################################################################################################

# 1. set up the game(background, game image coordinate, speed, font)
current_path = os.path.dirname(__file__) # show a location of current file
image_path = os.path.join(current_path, "images") 

#background
background = pygame.image.load(os.path.join(image_path,"background.png"))
# background = pygame.image.load("/Users/ji/Desktop/PythonWorkspace/pygame_project/images/background.png")


#stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # will use for a character 


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
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))

    pygame.display.update()    

#pygame exit
pygame.quit()