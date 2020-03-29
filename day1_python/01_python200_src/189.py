import pygame

# 게임에 사용되는 전역 변수 정의
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640
fighter_width = 36
fighter_height = 38

# 게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
   global gamepad
   gamepad.blit(obj, (x,y))

# 게임 실행 메인 함수
def runGame():
   global gamepad, clock, fighter

   # 전투기 초기 위치 (x, y) 설정
   x = pad_width*0.45
   y = pad_height*0.9
   x_change = 0

   ongame = False
   while not ongame:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            ongame = True
         
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               x_change -= 5
                    
            elif event.key == pygame.K_RIGHT:
               x_change += 5

         if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               x_change = 0

      gamepad.fill(BLACK)

      # 전투기의 위치를 재조정
      x += x_change
      if x < 0:
         x = 0
      elif x > pad_width - fighter_width:
         x = pad_width - fighter_width

      drawObject(fighter, x, y)
      pygame.display.update()
      clock.tick(60)

   pygame.quit()

# 게임 초기화 함수
def initGame():
   global gamepad, clock, fighter

   pygame.init()
   gamepad = pygame.display.set_mode((pad_width, pad_height))
   pygame.display.set_caption('MyGalaga')
   fighter = pygame.image.load('fighter.png')
   clock = pygame.time.Clock()

initGame()
runGame()
