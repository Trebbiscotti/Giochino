import pygame
import random

pygame.init()

LARGHEZZA_FINESTRA = 800
ALTEZZA_FINESTRA = 600
COLORE_SFONDO = (50, 150, 255)

dimensioni_giocatore = 45
#colore_giocatore = (255, 255, 255)
posizione_giocatore_x = LARGHEZZA_FINESTRA // 2 - dimensioni_giocatore // 2
posizione_giocatore_y = ALTEZZA_FINESTRA - dimensioni_giocatore -10
velocita_giocatore = 10

#colore_oggetto_cadente = (255, 0, 0)
dimensioni_oggetto_cadente = 45
lista_oggetti_cadenti = []
velocita_oggetto_cadente = 5

punteggio = 0

schermo = pygame.display.set_mode((LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA))
pygame.display.set_caption("Cattura gli oggetti cadenti")

font_punteggio = pygame.font.SysFont(None, 35)

immagine_giocatore = pygame.image.load("giocatore.png")
immagine_oggetto_cadente = pygame.image.load("oggetto_cadente.png")

def disegna_oggetti():
    global posizione_giocatore_x, posizione_giocatore_y, lista_oggetti_cadenti, punteggio

    schermo.fill(COLORE_SFONDO)

    schermo.blit(immagine_giocatore, (posizione_giocatore_x, posizione_giocatore_y))

    for obj in lista_oggetti_cadenti:
        schermo.blit(immagine_oggetto_cadente, (obj[0], obj[1]))

    testo_punteggio = font_punteggio.render(f"Punteggio: {punteggio}", True, (255, 255, 255))