from kandinsky import fill_rect, draw_string
from ion import keydown, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from time import sleep
from random import randint

def play():
    x, y = 160, 110 
    dx, dy = 10, 0
    snake = [[160, 110], [150, 110], [140, 110]]
    food = [randint(0, 31)*10, randint(0, 21)*10]
    score = 0

    while True:
        if keydown(KEY_UP) and dy == 0: dx, dy = 0, -10
        elif keydown(KEY_DOWN) and dy == 0: dx, dy = 0, 10
        elif keydown(KEY_LEFT) and dx == 0: dx, dy = -10, 0
        elif keydown(KEY_RIGHT) and dx == 0: dx, dy = 10, 0

        x = (x + dx) % 320
        y = (y + dy) % 220
        new_head = [x, y]

        if new_head in snake:
            draw_string("GAME OVER! GC IS COMING!", 60, 100)
            break

        snake.insert(0, new_head)

        if x == food[0] and y == food[1]:
            score += 1
            food = [randint(0, 31)*10, randint(0, 21)*10]
        else:
            tail = snake.pop()
            fill_rect(tail[0], tail[1], 10, 10, (255, 255, 255))

        fill_rect(snake[0][0], snake[0][1], 10, 10, (0, 0, 0))
        fill_rect(food[0], food[1], 10, 10, (255, 0, 0))
        
        sleep(0.1)

play()
