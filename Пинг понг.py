from pygame import *
win_width = 700

win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("fon.jpg"), (win_width, win_height))

clock = time.Clock()

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 130:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 130:
            self.rect.y += self.speed

  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
 
# класс спрайта-врага   
class Enemy(GameSprite):
    # движение врага
    def update(self):
        self.rect.y += self.speed
        global lost
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.y = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1


left_r = Player('rukar.png', 0, 150, 100, 130,5)
right_r = Player('rukal.png', 600, 165, 100, 130,5)
ball = GameSprite('ball.png', 300,150,130,130,2)

font.init()

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

game = True
while game:
    window.blit(background, (0,0))

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
           speed_y *= -1

    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(left_r, ball)   or sprite.collide_rect(right_r, ball):
           speed_x *= -1


    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    left_r.reset()
    right_r.reset()
    ball.reset()
    left_r.update()
    right_r.update2()
    

    display.update()
    clock.tick()



    


    

