import pygame
import random

#####################################################################################################################

#initialization
pygame.init() 

# size of board
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#title 
pygame.display.set_caption("quiz")

#FPS
clock = pygame.time.Clock()

#####################################################################################################################

# 1. set up the game(background, game image coordinate, speed, font)
# background 
background = pygame.image.load("/Users/ji/Desktop/PythonWorkspace/pygame_basic/background.png")

#character
character = pygame.image.load("/Users/ji/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height) - character_height

#location
to_x = 0
to_y = 0
character_speed = 10

#dump 
dump = pygame.image.load("/Users/ji/Desktop/PythonWorkspace/pygame_basic/enemy.png")
dump_size = dump.get_rect().size
dump_width = dump_size[0]
dump_height = dump_size[1]
dump_x_pos = random.randint(0,screen_width - dump_width)
dump_y_pos = 0
dump_speed = 10

running = True
while running:
    dt = clock.tick(30) #set up the amount of frames

    # 2. figure out the event (keyboard, mouse)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    
    # 3. positions of characters 
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    dump_y_pos += dump_speed

    if dump_y_pos > screen_height:
        dump_y_pos = 0
        dump_x_pos = random.randint(0,screen_width - dump_width)

    # 4. check up the collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    dump_rect = dump.get_rect()
    dump_rect.left = dump_x_pos
    dump_rect.top = dump_y_pos

    if character_rect.colliderect(dump_rect):
        print("ouch =_=")
        running = False

    # 5. draw on the screen
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(dump,(dump_x_pos,dump_y_pos))


    pygame.display.update()    

#pygame exit
pygame.quit()