import pygame
import Pygame_Plus as pg_plus
import random

dis = 350
vis = 150
speed = 3

width, height = 800, 800

kol_dol = [pg_plus.Kvadrat(800, random.randrange(20 + vis, height - 20), 60, 1000, 0, speed, pg_plus.color.green),
           pg_plus.Kvadrat(1050, random.randrange(20 + vis, height - 20), 60, 1000, 0, speed, pg_plus.color.green),
           pg_plus.Kvadrat(1300, random.randrange(20 + vis, height - 20), 60, 1000, 0, speed, pg_plus.color.green),
           pg_plus.Kvadrat(1550, random.randrange(20 + vis, height - 20), 60, 1000, 0, speed, pg_plus.color.green)]

kol_gor = [pg_plus.Kvadrat(kol_dol[0].x, kol_dol[0].y - kol_dol[0].h - vis, 60, 1000, 0, speed, pg_plus.color.green),
           pg_plus.Kvadrat(kol_dol[1].x, kol_dol[1].y - kol_dol[1].h - vis, 60, 1000, 0, speed, pg_plus.color.green),
           pg_plus.Kvadrat(kol_dol[2].x, kol_dol[2].y - kol_dol[2].h - vis, 60, 1000, 0, speed, pg_plus.color.green),
           pg_plus.Kvadrat(kol_dol[3].x, kol_dol[3].y - kol_dol[3].h - vis, 60, 1000, 0, speed, pg_plus.color.green)]

bird = pg_plus.Kvadrat(60, 400, 50, 30, 0, 0, pg_plus.color.yellow)


def Move():
    global kol_dol
    for i in kol_dol:
        i.x -= i.vel


def DrAw(win):
    win.fill(pg_plus.color.cyan)
    for i in kol_dol:
        i.draw(win)
    for i1 in kol_gor:
        i1.draw(win)
    bird.draw(win)
    pygame.display.update()


g = 30
V = 0
rV = 0


def Grav(g, V, fps):
    V -= g / fps
    return V


pygame.init()

win = pygame.display.set_mode((width, height))


clock = pygame.time.Clock()
fps = 60
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if kol_dol[0].x < -kol_dol[0].w:
        kol_dol.pop(0)
        kol_dol.append(pg_plus.Kvadrat(kol_dol[2].x + dis, random.randrange(20 + vis, height - 20), 60, 1000, 0, speed, pg_plus.color.green))

    kol_gor = [pg_plus.Kvadrat(kol_dol[0].x, kol_dol[0].y - kol_dol[0].h - vis, 60, 1000, 0, speed, pg_plus.color.green),
               pg_plus.Kvadrat(kol_dol[1].x, kol_dol[1].y - kol_dol[1].h - vis, 60, 1000, 0, speed, pg_plus.color.green),
               pg_plus.Kvadrat(kol_dol[2].x, kol_dol[2].y - kol_dol[2].h - vis, 60, 1000, 0, speed, pg_plus.color.green),
               pg_plus.Kvadrat(kol_dol[3].x, kol_dol[3].y - kol_dol[3].h - vis, 60, 1000, 0, speed, pg_plus.color.green)]

    V = Grav(g, V, fps)
    rV = round(V)
    bird.y -= rV

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        V = 8

    Move()
    DrAw(win)

pygame.quit()