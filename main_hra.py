import pygame
import button
import button1
from PIL import Image

pygame.init()


screen = pygame.display.set_mode((600, 800))

button_img = pygame.image.load('img.jpg').convert_alpha()
singleplayer_img = pygame.image.load('singleplayer.png').convert_alpha()
multiplayer_img = pygame.image.load('multiplayer.png').convert_alpha()
options_img = pygame.image.load('options.png').convert_alpha()
end_img = pygame.image.load('end.png').convert_alpha()
back_img = pygame.image.load('back.png').convert_alpha()


X_img = pygame.image.load('X.png')
O_img = pygame.image.load('O.png')

img1 = Image.open(r"X.png")

img_button1 = button.Button(5, 5, button_img, 1)
img_button2 = button.Button(205, 5, button_img, 1)
img_button3 = button.Button(405, 5, button_img, 1)
img_button4 = button.Button(5, 205, button_img, 1)
img_button5 = button.Button(205, 205, button_img, 1)
img_button6 = button.Button(405, 205, button_img, 1)
img_button7 = button.Button(5, 405, button_img, 1)
img_button8 = button.Button(205, 405, button_img, 1)
img_button9 = button.Button(405, 405, button_img, 1)
singleplayer_button = button1.Button(200, 20, singleplayer_img , 1)
multiplayer_button = button1.Button(200, 210, multiplayer_img, 1)
options_button = button1.Button(200, 400, options_img, 1)
end_button = button1.Button(200, 590, end_img, 1)
back_button = button1.Button(360, 300, back_img, 1)


fps = 30 


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

game_pause = True
menu_state = 'Main'

turn = False

font = pygame.font.SysFont('arialblack', 40)
TEXT_COL = (0, 0, 0)

run = True
while run:
    
    screen.fill((255, 255, 255))
    if game_pause == False:
        draw_text('Press ESC to pause', font, TEXT_COL, 85, 700)
        if img_button1.draw(screen):
            if turn == False:
                draw_text('Ted hraje X.', font, TEXT_COL, 185, 600)
                X_img.paste(img_button1, (0,0), mask = img_button1)
                turn == True
            if turn == True:
                draw_text('Ted hraje O.', font, TEXT_COL, 185, 600)
                screen.blit(O_img, (5, 5))
                turn== False
            print('1')
        if img_button2.draw(screen):
            print('2')
        if img_button3.draw(screen):
            print('3')
        if img_button4.draw(screen):
            print('4')
        if img_button5.draw(screen):
            print('5')
        if img_button6.draw(screen):
            print('6')
        if img_button7.draw(screen):
            print('7')
        if img_button8.draw(screen):
            print('8')
        if img_button9.draw(screen):
            print('9')
            
    if game_pause == True:
        if menu_state == 'Main':
            if singleplayer_button.draw(screen):
                pass
            if multiplayer_button.draw(screen):
                game_pause = False
            if options_button.draw(screen):
                menu_state = 'Options'
            if end_button.draw(screen):
                run = False
        if menu_state == 'Options':
            if back_button.draw(screen):
                menu_state = 'Main'

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_pause = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()