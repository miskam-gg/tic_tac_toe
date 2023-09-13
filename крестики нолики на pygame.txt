import pygame
import sys

def WIN(mas,sign):
    zeroes = 0
    for row in mas:
        zeroes+= row.count(0)
        if row.count(sign)==3:
            return sign
    for column in range(3):
        if mas[0][column]==sign and mas[1][column]==sign and mas[2][column]==sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes==0:
        return "ничья"
    return False

pygame.init()

s_block = 100               # s = "size"
s_gap = 2
width = height = s_block*3 + s_gap*4

s_window = (width, height)
screen = pygame.display.set_mode(s_window)
pygame.display.set_caption("крестики-нолики")
# pygame.display.set_icon(pygame.image.load("icon.png"))

# colors:
black = (0, 0, 0)
white = (255, 255, 255)
white_2 = (255, 255, 254)
white_3 = (255, 254, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

mas = [[0]*3 for i in range(3)]
query = 0
clock = pygame.time.Clock()
FPS = 30
over = False
fl_running = True
while fl_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            fl_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (s_block+s_gap)
            row = y_mouse // (s_block+s_gap)
            if mas[row][column] == 0:
                if query % 2 == 0:
                    mas[row][column] = "победа -х-"
                else:
                    mas[row][column] = "победа -o-"
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            over = False
            mas = [[0] * 3 for i in range(3)]
            query=0
            screen.fill(black)

    if not over:
        for row in range(3):
            for column in range(3):
                if mas[row][column] == "победа -х-":
                    color = white
                elif mas[row][column] == "победа -o-":
                    color = white_2
                else:
                    color = white_3
                x = column * s_block + (column + 1) * s_gap
                y = row * s_block + (row + 1) * s_gap
                pygame.draw.rect(screen, color, (x, y, s_block, s_block))
                if color == white:
                    pygame.draw.line(screen,blue, (x+5,y+5), (x+s_block-5, y+s_block-5), 9)
                    pygame.draw.line(screen, blue, (x + s_block - 5, y + 5), (x+5, y + s_block - 5), 9)
                elif color == white_2:
                    pygame.draw.circle(screen,red, (x+s_block//2, y+s_block//2), s_block//2-3,9)
    if (query-1)%2==0:
        over = WIN(mas, "победа -х-")
    else:
        over = WIN(mas, "победа -o-")

    if over:
        screen.fill(black)
        font = pygame.font.SysFont("stxingkai", 60)
        text_1 = font.render(over, True, white)
        test_rect = text_1.get_rect()
        text_x = screen.get_width() / 2 - test_rect.width / 2
        text_y = screen.get_height() / 2 - test_rect.height / 2
        screen.blit(text_1, [text_x, text_y])

    pygame.display.update()

clock.tick(FPS)
