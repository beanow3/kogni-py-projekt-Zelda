import pygame
pygame.init()
szerokosc = 800 # Obydwie osie zaczynają się pod ikonką.
wysokosc = 600
ekran = pygame.display.set_mode((szerokosc,wysokosc))

pygame.display.set_caption("Zelda")
ikonka = pygame.image.load('ikonka.png')
pygame.display.set_icon(ikonka)

Gracz_obrazek = pygame.image.load('normalka.png')
przeciwnik_obrazek = pygame.image.load('przeciwnik.png')
# pocisk_obrazek = pygame.image.load('pocisk.png')

ruch_pl_A = [pygame.image.load('Ruch pl_1.png'), pygame.image.load('Ruch pl_2.png') ]
ruch_gd_A = [pygame.image.load('Ruch gd_1.png'), pygame.image.load('Ruch gd_2.png')]


### Gracz
graczX = 370
graczY = 480
graczX_zmiana = 0
graczY_zmiana = 0
szybkosc = 1.8
###

###Przeciwnicy
przeciwnikX = 370
przeciwnikY = 100
przeciwnikX_zmiana = 0
przeciwnikY_zmiana = 0
szybkosc_p = 0.7
###
ruch_pl = False # prawo - lewo
ruch_gd = False # góra - dół

klatki = 0
def ekran_zmiana(): # Do "rysowania" na ekranie
    ekran.fill((0, 200, 0))
    gracz(graczX, graczY)
    przeciwnik(przeciwnikX,przeciwnikY)
    animacja_ruchu_gracza()
    pygame.display.update()


def gracz(x,y):
    ekran.blit(Gracz_obrazek, (x, y)) # Wielkosc 64X64
    pygame.draw.rect(ekran, (250,0,0),(graczX,graczY - 20, 64,10))


def przeciwnik(x,y):
    ekran.blit(przeciwnik_obrazek, (x, y)) # Wielkosc 64X64
    pygame.draw.rect(ekran, (250,0,0),(przeciwnikX,przeciwnikY - 20, 64,10))


def animacja_ruchu_gracza():
    global klatki
    if klatki + 1 >= 3:
        klatki = 0
    if ruch_pl == False and ruch_gd == False:
        ekran.blit(Gracz_obrazek, (graczX, graczY))
    elif ruch_pl == True:
        ekran.blit(ruch_pl_A[klatki], (graczX, graczY))
        klatki += 1
    elif ruch_gd == True:
        ekran.blit(ruch_gd_A[klatki], (graczX, graczY))
        klatki += 1

dziala = True
while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala = False

### Ruch gracza
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                graczX_zmiana = - szybkosc
                ruch_pl = True
                ruch_gd = False
            if event.key == pygame.K_RIGHT:
                graczX_zmiana = szybkosc
                ruch_pl = True
                ruch_gd = False
            if event.key == pygame.K_UP:
                graczY_zmiana =  - szybkosc
                ruch_pl = False
                ruch_gd = True
            if event.key == pygame.K_DOWN:
                graczY_zmiana = szybkosc
                ruch_pl = False
                ruch_gd = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                graczX_zmiana = 0
                ruch_gd = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                graczY_zmiana = 0
                ruch_pl = False
        if event.type == pygame.KEYUP:
            ruch_pl = False
            ruch_gd = False
    graczX += graczX_zmiana
    graczY += graczY_zmiana
###


### Ruch przeciwnik
    if graczX > przeciwnikX:
        przeciwnikX_zmiana =   szybkosc_p
    elif graczX < przeciwnikX:
        przeciwnikX_zmiana = - szybkosc_p
    if graczY > przeciwnikY:
        przeciwnikY_zmiana =   szybkosc_p
    elif graczY < przeciwnikY:
        przeciwnikY_zmiana =  - szybkosc_p
    przeciwnikX += przeciwnikX_zmiana
    przeciwnikY += przeciwnikY_zmiana
###




### Granica
    if graczX <= 0:
        graczX = 0
    elif graczX >= szerokosc - 64: # - szerokośc/wysokość naszego gracza
        graczX = szerokosc - 64
    if graczY <= 0:
        graczY = 0
    elif graczY >= wysokosc - 64:
        graczY = wysokosc - 64

    if przeciwnikX <= 0:
        przeciwnikX = 0
    elif przeciwnikX >= szerokosc - 64: # - szerokośc/wysokość naszego gracza
        przeciwnikX = szerokosc - 64
    if przeciwnikY <= 0:
        przeciwnikY = 0
    elif przeciwnikY >= wysokosc - 64:
        przeciwnikY = wysokosc - 64
###
    ekran_zmiana()
