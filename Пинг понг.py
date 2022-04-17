from pygame import *
win_width = 700

win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

clock = time.Clock()

game = True
while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick()

