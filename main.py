import pygame
import random

pygame.init()
pygame.font.init()

width = 680
length = 600

win = pygame.display.set_mode((width, length))
pygame.display.set_caption("Snake game")

green = (0, 255, 0)
red = (255, 0, 0)

lose_font = pygame.font.SysFont('comicsans', 100)
score_font = pygame.font.SysFont('comicsans', 30)

food_eaten = pygame.USEREVENT + 1

snake = pygame.image.load('green square.png')
grass = pygame.transform.scale(pygame.image.load('grass.png'), (680, 600))
food = pygame.transform.scale(pygame.image.load('apple.png'), (40, 40))

def draw(x, y, apple, snake_list, size):
    win.blit(grass, (0, 0))
    scoretext = score_font.render("Score: " + str(size - 1), 1, (0, 0, 255))
    win.blit(scoretext, (20,10))
    win.blit(food, (apple[0], apple[1]))
    for s in snake_list:
        win.blit(snake, (s[0],s[1]))
    pygame.display.update()

def movement(keys_pressed, x, y, last):
    if keys_pressed[pygame.K_LEFT]:
        x -= 40
        last = "left"
    # move right
    elif keys_pressed[pygame.K_RIGHT]:
        x += 40
        last = "right"
    # move up
    elif keys_pressed[pygame.K_UP]:
        y -= 40
        last = "up"
    # move down
    elif keys_pressed[pygame.K_DOWN]:
        y += 40
        last = "down"
    else:
        if last == "left":
            x -= 40
        elif last == "right":
            x += 40
        elif last == "up":
            y -= 40
        elif last == "down":
            y += 40
    return x, y, last

def lose():
    losetext = lose_font.render("You lost!", 1, (255, 255, 255))
    win.blit(losetext, (340 - losetext.get_width()//2, 300 - losetext.get_height()//2))
    pygame.display.update()
    print("--------------------You lost!--------------------")
    pygame.time.delay(3000)
    main()

def WIN():
    losetext = lose_font.render("You Won!", 1, (255, 255, 255))
    win.blit(losetext, (340 - losetext.get_width() // 2, 300 - losetext.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(10000)
    main()

def foodeat(x, y, apple):
    if apple[0] == x and apple[1] == y:
        pygame.event.post(pygame.event.Event(food_eaten))
        print("YUMMY!")
        return (random.choice([0,40,80,120,160,200,240,280,320,360,400,440,480,520,560,600,640]), random.choice([0,40,80,120,160,200,240,280,320,360,400,440,480,520,560]))
    return apple

def main():
    clock = pygame.time.Clock()
    run = True
    x = 120
    y = 280
    size = 1
    last = ""
    apple = (random.choice([0,40,80,120,160,200,240,280,320,360,400,440,480,520,560,600,640]), random.choice([0,40,80,120,160,200,240,280,320,360,400,440,480,520,560]))
    snake_list = []

    while run:
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == food_eaten:
                size += 1

        if x < 0 or x >= 680 or y < 0 or y >= 600:
            lose()

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > size:
            del snake_list[0]

        for s in snake_list[1:-1]:
            if s == snake_head:
                lose()

        if size == 255:
            WIN()

        keys_pressed = pygame.key.get_pressed()
        apple = foodeat(x, y, apple)
        x, y, last = movement(keys_pressed, x, y, last)
        draw(x, y, apple, snake_list, size)


main()