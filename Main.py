import pygame as pg
import random as rd
pg.init()
screen = (800, 600)
white = (255, 255, 255)
red = (255, 52, 0)
gameopen = True
pos_x = screen[0]/2
pos_y = screen[1]/2
# movedirs = 0   # Indices 0 => up ; 1 => dn ; 2 => lt ; 3 => rt
# moving = True
speed = 1.0
clock = pg.time.Clock()
headpos = [pos_x, pos_y]
player = [headpos]
loc_x = rd.randrange(0, screen[0], 10)
loc_y = rd.randrange(0, screen[1], 10)

score = 0
direction = 'UP'
change_to = direction


def spawn(_food):
    _food[0] = rd.randrange(0, screen[0], 10)
    _food[1] = rd.randrange(0, screen[1], 10)
    item = pg.draw.rect(window, red, _food)
    return item


def eaten(pl, f):
    if pl[0][0] == f[0] and pl[0][1] == f[1]:
        return True
    return False


# --------------Game Loop
while gameopen:
    # -------------Window Display
    window = pg.display.set_mode(screen)
    hpiece = pg.Rect(headpos[0], headpos[1], 16, 16)
    # bpiece = pg.Rect(pos_x+16, pos_y+16, 16, 16)
    food = pg.Rect(loc_x, loc_y, 16, 16)

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            gameopen = False
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_UP or ev.key == ord('w'):
                change_to = 'UP'
            if ev.key == pg.K_DOWN or ev.key == ord('s'):
                change_to = 'DOWN'
            if ev.key == pg.K_LEFT or ev.key == ord('a'):
                change_to = 'LEFT'
            if ev.key == pg.K_RIGHT or ev.key == ord('d'):
                change_to = 'RIGHT'

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            headpos[1] -= speed
        if direction == 'DOWN':
            headpos[1] += speed
        if direction == 'LEFT':
            headpos[0] -= speed
        if direction == 'RIGHT':
            headpos[0] += speed

        pg.draw.rect(window, red, food)


        # pg.draw.rect(window, white, [0, 0, 16, 16])

        # ------------MOVEMENT TRY #1-----------------------------------------------------------------------------------

        # -----------------Checking For Held Keys
        # if ev.type == pg.KEYDOWN:
        #     if ev.key == pg.K_UP:
        #         keys[0] = 1
        #
        # if ev.type == pg.KEYUP:
        #     if ev.key == pg.K_UP:
        #         keys[0] = 0
        # # ------------------Doing the Movement
        # if keys[0]:
        #     pos_y -= speed

        # -------- MOVEMENT TRY #2--------------------------------------------------------------------------------------

        # if ev.type == pg.KEYDOWN:
        #     if ev.key == pg.K_UP and movedirs != 0:
        #         movedirs = 0
        #
        #     if ev.key == pg.K_DOWN and movedirs != 1:
        #         movedirs = 1
        #
        #     if ev.key == pg.K_LEFT and movedirs != 2:
        #         movedirs = 2
        #
        #     if ev.key == pg.K_RIGHT and movedirs != 3:
        #         movedirs = 3
        #
        #     if movedirs == 0:
        #         headpos[1] -= speed
        #     elif movedirs == 1:
        #         headpos[1] += speed
        #     elif movedirs == 2:
        #         headpos[0] -= speed
        #     elif movedirs == 3:
        #         headpos[0] += speed
        # ----------------- COULDN'T FIGURE OUT MOVEMENT SO CTRL+C,CTRL+V-----------------------------------------------

        for hpos in player:
            pg.draw.rect(window, white, pg.Rect(hpos[0], hpos[1], 16, 16))

        if eaten(player, food):
            print("Food Eaten at " + str(food[0]) + ", " + str(food[1]))
            spawn(food)
            score += 1
            player.insert(0, list(headpos))

        pg.display.flip()
        clock.tick(60)

print(player)
print(score)
pg.quit()


# TODO : create a dirn array for snake movement
