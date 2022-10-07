import pygame as pg
import button1

pg.init()

fps = 30

run = True
menu_state = 'Main'

screen = pg.display.set_mode((600, 800))

button_img = pg.image.load('img.jpg').convert_alpha()
singleplayer_img = pg.image.load('singleplayer.png').convert_alpha()
multiplayer_img = pg.image.load('multiplayer.png').convert_alpha()
options_img = pg.image.load('options.png').convert_alpha()
end_img = pg.image.load('end.png').convert_alpha()
back_img = pg.image.load('back.png').convert_alpha()

singleplayer_button = button1.Button(200, 20, singleplayer_img , 1)
multiplayer_button = button1.Button(200, 210, multiplayer_img, 1)
options_button = button1.Button(200, 400, options_img, 1)
end_button = button1.Button(200, 590, end_img, 1)
back_button = button1.Button(360, 300, back_img, 1)

while run:
    screen.fill((255, 255, 255))

    if menu_state == 'Main':
        if singleplayer_button.draw(screen):
            pass
        if multiplayer_button.draw(screen):
            menu_state = 'Game'
        if options_button.draw(screen):
            menu_state = 'Options'
        if end_button.draw(screen):
            run = False
    if menu_state == 'Options':
        if back_button.draw(screen):
            menu_state = 'Main'
    if menu_state == 'Game':
        exec(open('main_game.py').read())

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game_pause = True
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()