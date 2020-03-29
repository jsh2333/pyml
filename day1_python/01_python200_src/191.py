import pygame
import random

# 게임에 사용되는 전역 변수 정의
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640
fight_width = 36
fight_height = 38
enemy_width = 26
enemy_height = 20

# 게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
   global gamepad
   gamepad.blit(obj, (x,y))

# 게임 실행 메인 함수
def runGame():
   global gamepad, clock, fighter, enemy, bullet

   # 무기 좌표를 위한 리스트 자료
   bullet_xy = []

   # 전투기 초기 위치 설정
   x = pad_width*0.45
   y = pad_height*0.9
   x_change = 0

   # 적 초기 위치 설정
   enemy_x = random.randrange(0, pad_width-enemy_width)
   enemy_y = 0
   enemy_speed = 3

   doneFlag = False
   while not doneFlag:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            doneFlag = True
         
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               x_change -= 5
                    
            elif event.key == pygame.K_RIGHT:
               x_change += 5
      
            # 왼쪽 컨트롤 키를 누르면 무기 발사. 무기는 한번에 2발만 발사됨
            elif event.key == pygame.K_LCTRL:
               if len(bullet_xy) < 2:
                  bullet_x = x + fight_width/2
                  bullet_y = y - fight_height
                  bullet_xy.append([bullet_x, bullet_y])

         if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               x_change = 0

      gamepad.fill(BLACK)

      # 전투기의 위치 재조정
      x += x_change
      if x < 0:
         x = 0
      elif x > pad_width - fight_width:
         x = pad_width - fight_width

      drawObject(fighter, x, y)

      # 전투기 무기 발사 화면에 그리기
      if len(bullet_xy) != 0:
         for i, bxy in enumerate(bullet_xy):
            bxy[1] -= 10
            bullet_xy[i][1] = bxy[1]
 
            if bxy[1] <= 0:
               try:
                  bullet_xy.remove(bxy)
               except:
                  pass

      if len(bullet_xy) != 0:
          for bx, by in bullet_xy:
             drawObject(bullet, bx, by)

      # 적을 아래로 움직임
      enemy_y += enemy_speed        
      if enemy_y > pad_height:
         enemy_y = 0
         enemy_x = random.randrange(0, pad_width-enemy_width)
      
      drawObject(enemy, enemy_x, enemy_y)

      pygame.display.update()
      clock.tick(60)

   pygame.quit()

# 게임 초기화 함수
def initGame():
   global gamepad, clock, fighter, enemy, bullet

   pygame.init()
   gamepad = pygame.display.set_mode((pad_width, pad_height))
   pygame.display.set_caption('MyGalaga')
   fighter = pygame.image.load('fighter.png')
   enemy = pygame.image.load('enemy.png')
   bullet = pygame.image.load('bullet.png')
   clock = pygame.time.Clock()

initGame()
runGame()
