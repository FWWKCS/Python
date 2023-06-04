import pygame

pygame.init() # 초기화 (필수)

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Ball Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/김찬식/Desktop/Python Works/Import/BallGame/background.png")


# 이벤트 루프
running = True # 게임 진행 여부
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창 닫기 이벤트 발생 여부
            running = False
    

    screen.blit(background, (0,0)) # 배경 그리기
    # 창의 좌측 최상단이 0,0 기본좌표
    # screen.fill((0, 0, 255)) # RGB 색조합으로 화면 채우기

    pygame.display.update() # 화면에 다시 그리기 (필수)

# pygame 종료
pygame.quit()

