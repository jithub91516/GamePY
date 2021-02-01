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

#화면 타이틀 
pygame.display.set_caption("JI gAmE") #game name 

#이벤트 루프
running = True
while running:
    for event in pygame.event.get(): #what kind of event has been come up?
        if event.type == pygame.QUIT: #tried to quit?
            running = False #no running more

    screen.blit(background,(0,0)) #draw background

    screen.blit(character,(character_x_pos,character_y_pos)) #draw character

    pygame.display.update()    #update pixel display.
#pygame exit
pygame.quit()