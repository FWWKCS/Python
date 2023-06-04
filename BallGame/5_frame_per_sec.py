import pygame

pygame.init() # 초기화 (필수)

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Ball Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/김찬식/Desktop/Python Works/Import/BallGame/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/김찬식/Desktop/Python Works/Import/BallGame/character.png")
character_size = character.get_rect().size  # 이미지 크기 확인
character_width = character_size[0] # 가로 크기
character_height = character_size[1] # 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 맨 아래에 위치 

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.5

# 이벤트 루프
running = True # 게임 진행 여부
while running:
    dt = clock.tick(120) # 게임화면의 초당 프레임 수 설정

    # 캐릭터가 1초 동안에 100 만큼 이동 해야함
    # 10 fps : 1초 동안 10번 동작 -> 1번에 10만큼 이동하여 100을 이동

    # print(f"fps : {str(clock.get_fps())}") # fps 실시간 출력

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창 닫기 이벤트 발생 여부
            running = False
        
        if event.type == pygame.KEYDOWN: # 키보드 입력 확인
            if event.key == pygame.K_LEFT: # 왼쪽 방향키 입력시
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 오른쪽
                to_x += character_speed
            elif event.key == pygame.K_UP: # 위
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 아래
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 정지
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0 : 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width 

    # 세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height
    
    screen.blit(background, (0,0)) # 배경 그리기
    # 창의 좌측 최상단이 0,0 기본좌표

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
   
    pygame.display.update() # 화면에 다시 그리기 (필수)

# pygame 종료
pygame.quit()

