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

#character
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height

#character direction
character_to_x = 0

#character speed
character_speed = 5

#weapon
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
#weapon speed
weapons = []
weapon_speed = 10

running = True
while running: 
    dt = clock.tick(30) #set up the amount of frames

    # 2. figure out the event (keyboard, mouse)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:# toTheLeft
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #toTheRight
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #weapon 
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapon.append([weapon_x_pos, weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
    
    # 3. positions of characters 
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #position of the weapons
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 4. check up the collision

    # 5. draw on the screen
    screen.blit(background, (0, 0))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    
    pygame.display.update()    

#pygame exit
pygame.quit()