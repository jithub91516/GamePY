import pygame

pygame.init() #초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#재경 이미지 불러오기
background = pygame.image.load("/Users/ji/Desktop/PythonWorkspace/pygame_basic/background.png")

#화면 타이틀 
pygame.display.set_caption("JI gAmE") #game name 

#이벤트 루프
running = True
while running:
    for event in pygame.event.get(): #어떤 이벤트가 생겼나?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생 하였는가?
            running = False #진행중이 아님

    screen.blit(background,(0,0)) #배경그리기
    pygame.display.update()    #게임 화면을 다시 그리기  
#pygame 종료 
pygame.quit()