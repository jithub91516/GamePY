import pygame

pygame.init() #initialization

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#재경 이미지 불러오기
background = pygame.image.load("/Users/ji/Desktop/PythonWorkspace/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/ji/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size #find out a size of the image
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)#put at the middle of the screen width
character_y_pos = screen_height - character_height#put at the bottom of the screen 

#coordinate to move
to_x = 0
to_y = 0

#화면 타이틀 
pygame.display.set_caption("JI gAmE") #game name 

#이벤트 루프
running = True
while running:
    for event in pygame.event.get(): #what kind of event has been come up?
        if event.type == pygame.QUIT: #tried to quit?
            running = False #no running more
        
        if event.type==pygame.KEYDOWN: #check that the key has been pressed
            if event.key == pygame.K_LEFT: #go left
                to_x -= 5 
            elif event.key == pygame.K_RIGHT: #go right
                to_x += 5
            elif event.key == pygame.K_UP: # go up 
                to_y -= 5
            elif event.key == pygame.K_DOWN: # go down 
                to_y += 5 
        
        if event.type == pygame.KEYUP: #stop when the player dont press
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

#hold the character not to run out of the screen 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background,(0,0)) #draw background

    screen.blit(character,(character_x_pos,character_y_pos)) #draw character

    pygame.display.update()    #update pixel display.
#pygame exit
pygame.quit()