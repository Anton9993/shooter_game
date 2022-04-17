from pygame import *
win_width = 700

win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

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
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
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


left_r = Player('ruka1.png', 10, 10, 85, 130,5)
right_r = Player('ruka2.png', 650, 10, 100, 130,5)
ball = GameSprite('pelmenball.png', 200,200,50,20,2)

game = True
while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    left_r.reset()
    right_r.reset()
    ball.reset()

    display.update()
    clock.tick()



    

