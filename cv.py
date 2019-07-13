# -*- coding: utf-8 -*-
import pygame
import math
from point import Point





# screen's parameters
ww=500
wh=500

pygame.init()
size =(ww,wh)


# colours
white =(255,255,255)
red = (255,0,0)
blue =(0,0,255)
green = (0,255,0)
black =(0,0,0)
yellow =(255,255,0)
pinky = (255,0,255)
cyan =(0,255,255)
orenge =(255,128,0)

# number of frames/seconds
fr =60

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")

# number of players between 2 to 6
nump=2
# create a list of  alive players
win =[]

# create characters as the number of players.

g =  Point(green)
win.append(g)
r = Point(red)
win.append(r)
if nump>=3:
    b =Point(blue)
    win.append(b)
if nump>=4:
    p =Point(pinky)
    win.append(p)
if nump>=5:
    c =Point(cyan)
    win.append(c)
if nump>=6:
    o =Point(orenge)
    win.append(o)
# array of collisions
all_collision=[""]*ww

for i in xrange(ww):
    all_collision[i] = [i]*wh


for i in xrange(0,ww,1):
    for j in xrange(0,wh,1):
        if j==0 or j==(ww-1) or i==0 or i ==(wh-1):

            all_collision[i][j] = True


finese= False

# parameters of a movement
trg=False
tlg =False
trr=False
tlr =False
if nump>=3:
    trb1=False
    tlb =False
if nump>=4:
    trp1=False
    tlp =False
if nump>=5:
    trc1=False
    tlc =False
if nump>=6:
    tro1=False
    tlo =False





screen.fill(black)
while not finese:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finese = True
# shift to specific direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                trg=True
            if event.key == pygame.K_LEFT:
                tlg=True
            if event.key == pygame.K_a:
                trr = True
            if event.key == pygame.K_d:
                tlr=True
            if nump>=3:
                if event.key == pygame.K_1:
                    trb1 = True
                if event.key == pygame.K_3:
                    tlb=True
            if nump>=4:
                if event.key == pygame.K_g:
                    trp1 = True
                if event.key == pygame.K_j:
                    tlp=True
            if nump>=5:
                if event.key == pygame.K_8:
                    trc1 = True
                if event.key == pygame.K_0:
                    tlc=True
            if nump>=6:
                if event.key == pygame.K_b:
                    tro1 = True
                if event.key == pygame.K_m:
                    tlo=True
# Stop movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:

                trg = False
            if event.key == pygame.K_LEFT:
                tlg = False
            if event.key == pygame.K_a:
                trr = False
            if event.key == pygame.K_d:
                tlr = False
            if nump>=3:
                if event.key == pygame.K_1:
                    trb1 = False
                if event.key == pygame.K_3:
                    tlb = False
            if nump>=4:
                if event.key == pygame.K_g:
                    trp1 = False
                if event.key == pygame.K_j:
                    tlp=False
            if nump>=5:
                if event.key == pygame.K_8:
                    trc1 = False
                if event.key == pygame.K_0:
                    tlc=False
            if nump>=6:
                if event.key == pygame.K_b:
                    tro1 = False
                if event.key == pygame.K_m:
                    tlo=False
    # Check if there is a movement
    if trg:

        g.move_right()
    if tlg:
        g.move_left()
    if tlr:
        r.move_right()
    if trr:
        r.move_left()
    if nump>=3:
        if tlb:
            b.move_right()
        if trb1:
            b.move_left()
    if nump>=4:
        if tlp:
            p.move_right()
        if trp1:
            p.move_left()
    if nump>=5:
        if tlc:
            c.move_right()
        if trc1:
            c.move_left()
    if nump>=6:
        if tlo:
            o.move_right()
        if tro1:
            o.move_left()


    gp =g.play(all_collision,screen)


    if type(gp)==list:
        for i in gp:
            all_collision[i[0]][i[1]] =True
            all_collision[i[0]+1][i[1]] =True
            all_collision[i[0]-1][i[1]] =True
            all_collision[i[0]][i[1]+1] =True
            all_collision[i[0]][i[1]-1] =True
            all_collision[i[0]-1][i[1]+1] =True
            all_collision[i[0]-1][i[1]-1] =True
            all_collision[i[0]+1][i[1]+1] =True
            all_collision[i[0]+1][i[1]-1] =True
    rp = r.play(all_collision,screen)
    if type(rp)==list:
        for i in rp:
            all_collision[i[0]][i[1]] =True
            all_collision[i[0]+1][i[1]] =True
            all_collision[i[0]-1][i[1]] =True
            all_collision[i[0]][i[1]+1] =True
            all_collision[i[0]][i[1]-1] =True
            all_collision[i[0]-1][i[1]+1] =True
            all_collision[i[0]-1][i[1]-1] =True
            all_collision[i[0]+1][i[1]+1] =True
            all_collision[i[0]+1][i[1]-1] =True
    if nump>=3:
        bp = b.play(all_collision,screen)
        if type(bp)==list:
            for i in bp:
                all_collision[i[0]][i[1]] =True
                all_collision[i[0]+1][i[1]] =True
                all_collision[i[0]-1][i[1]] =True
                all_collision[i[0]][i[1]+1] =True
                all_collision[i[0]][i[1]-1] =True
                all_collision[i[0]-1][i[1]+1] =True
                all_collision[i[0]-1][i[1]-1] =True
                all_collision[i[0]+1][i[1]+1] =True
                all_collision[i[0]+1][i[1]-1] =True

    if nump>=4:
        pp = p.play(all_collision,screen)
        if type(pp)==list:
            for i in pp:
                all_collision[i[0]][i[1]] =True
                all_collision[i[0]+1][i[1]] =True
                all_collision[i[0]-1][i[1]] =True
                all_collision[i[0]][i[1]+1] =True
                all_collision[i[0]][i[1]-1] =True
                all_collision[i[0]-1][i[1]+1] =True
                all_collision[i[0]-1][i[1]-1] =True
                all_collision[i[0]+1][i[1]+1] =True
                all_collision[i[0]+1][i[1]-1] =True
    if nump>=5:
        cp = c.play(all_collision,screen)
        if type(cp)==list:
            for i in cp:
                all_collision[i[0]][i[1]] =True
                all_collision[i[0]+1][i[1]] =True
                all_collision[i[0]-1][i[1]] =True
                all_collision[i[0]][i[1]+1] =True
                all_collision[i[0]][i[1]-1] =True
                all_collision[i[0]-1][i[1]+1] =True
                all_collision[i[0]-1][i[1]-1] =True
                all_collision[i[0]+1][i[1]+1] =True
                all_collision[i[0]+1][i[1]-1] =True
    if nump>=6:
        op = o.play(all_collision,screen)
        if type(op)==list:
            for i in op:
                all_collision[i[0]][i[1]] =True
                all_collision[i[0]+1][i[1]] =True
                all_collision[i[0]-1][i[1]] =True
                all_collision[i[0]][i[1]+1] =True
                all_collision[i[0]][i[1]-1] =True
                all_collision[i[0]-1][i[1]+1] =True
                all_collision[i[0]-1][i[1]-1] =True
                all_collision[i[0]+1][i[1]+1] =True
                all_collision[i[0]+1][i[1]-1] =True


    pygame.display.flip()
    clock.tick(fr)
pygame.quit()
