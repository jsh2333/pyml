import pygame

# 게임에 사용되는 전역 변수 정의
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640

# 게임 실행 메인 함수
def runGame():
   global gamepad, clock

   doneFlag = False
   while not doneFlag:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            doneFlag = True

      # 게임 화면을 검정색으로 채우고 화면을 업데이트 함
      gamepad.fill(BLACK)
      pygame.display.update()
      clock.tick(60)

   pygame.quit()

# 게임 초기화 함수
def initGame():
   global gamepad, clock

   pygame.init()
   gamepad = pygame.display.set_mode((pad_width, pad_height))
   pygame.display.set_caption('MyGalaga')
   clock = pygame.time.Clock()

initGame()
runGame()
