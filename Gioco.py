import pygame
import random

# Inizializzazione di Pygame
pygame.init()

# Dimensioni della finestra
LARGHEZZA_FINESTRA = 800
ALTEZZA_FINESTRA = 600
COLORE_SFONDO = (50, 150, 255)

# Variabili del giocatore
dimensioni_giocatore = 60
posizione_giocatore_x = LARGHEZZA_FINESTRA // 2 - dimensioni_giocatore // 2
posizione_giocatore_y = ALTEZZA_FINESTRA - dimensioni_giocatore - 10
velocita_giocatore = 15

# Variabili degli oggetti cadenti
dimensioni_oggetto_cadente = 45
lista_oggetti_cadenti = []
velocita_oggetto_cadente = 1
probabilità_generazione = 15

# Punteggio
punteggio = 0
prossimo_aumento_velocita = 10

# Schermo e font
schermo = pygame.display.set_mode((LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA))
pygame.display.set_caption("Cattura gli oggetti cadenti")
font_punteggio = pygame.font.SysFont(None, 35)

# Caricamento immagini dei personaggi
immagini_personaggi = [
    pygame.image.load("astronauta.png"),
    pygame.image.load("Lebron.png"),
    pygame.image.load("Nurra.png")
]

# Ridimensiona le immagini dei personaggi
immagini_personaggi = [
    pygame.transform.scale(img, (dimensioni_giocatore, dimensioni_giocatore))
    for img in immagini_personaggi
]

# Caricamento immagine degli oggetti cadenti
immagine_oggetto_cadente = pygame.image.load("meteora.png")
immagine_oggetto_cadente = pygame.transform.scale(immagine_oggetto_cadente, (dimensioni_oggetto_cadente, dimensioni_oggetto_cadente))

# Funzione per disegnare gli oggetti
def disegna_oggetti(immagine_giocatore):
    global posizione_giocatore_x, posizione_giocatore_y, lista_oggetti_cadenti, punteggio

    schermo.fill(COLORE_SFONDO)
    schermo.blit(immagine_giocatore, (posizione_giocatore_x, posizione_giocatore_y))

    for obj in lista_oggetti_cadenti:
        schermo.blit(immagine_oggetto_cadente, (obj[0], obj[1]))

    testo_punteggio = font_punteggio.render(f"Punteggio: {punteggio}", True, (0, 0, 0))
    schermo.blit(testo_punteggio, (10, 10))

    pygame.display.update()

# Funzione per aggiornare gli oggetti cadenti
def aggiorna_oggetti_cadenti():
    global lista_oggetti_cadenti, punteggio, velocita_oggetto_cadente, prossimo_aumento_velocita, probabilità_generazione
    for obj in lista_oggetti_cadenti:
        obj[1] += velocita_oggetto_cadente
        if obj[1] > ALTEZZA_FINESTRA:
            lista_oggetti_cadenti.remove(obj)
            punteggio += 1

            if punteggio >= prossimo_aumento_velocita:
                velocita_oggetto_cadente += 1
                prossimo_aumento_velocita += 10
            
            if punteggio % 10 == 0:
                probabilità_generazione = max(2, probabilità_generazione - 1)

# Funzione per generare oggetti cadenti
def genera_oggetti_cadenti():
    global probabilità_generazione
    if random.randint(1, probabilità_generazione) == 1:
        pos_x = random.randint(0, LARGHEZZA_FINESTRA - dimensioni_oggetto_cadente)
        lista_oggetti_cadenti.append([pos_x, 0])

# Funzione per controllare le collisioni
def controlla_collisioni():
    global in_esecuzione
    rettangolo_giocatore = pygame.Rect(posizione_giocatore_x, posizione_giocatore_y, dimensioni_giocatore, dimensioni_giocatore)
    for obj in lista_oggetti_cadenti:
        rettangolo_oggetto = pygame.Rect(obj[0], obj[1], dimensioni_oggetto_cadente, dimensioni_oggetto_cadente)
        if rettangolo_giocatore.colliderect(rettangolo_oggetto):
            in_esecuzione = False

# Funzione principale per avviare il gioco
def avvia_gioco(personaggio_selezionato):
    global in_esecuzione, posizione_giocatore_x, velocita_giocatore

    # Seleziona l'immagine del giocatore in base al personaggio selezionato
    immagine_giocatore = immagini_personaggi[personaggio_selezionato]

    in_esecuzione = True
    orologio = pygame.time.Clock()

    while in_esecuzione:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                in_esecuzione = False

        tasti = pygame.key.get_pressed()
        if tasti[pygame.K_LEFT] and posizione_giocatore_x > 0:
            posizione_giocatore_x -= velocita_giocatore
        if tasti[pygame.K_RIGHT] and posizione_giocatore_x < LARGHEZZA_FINESTRA - dimensioni_giocatore:
            posizione_giocatore_x += velocita_giocatore

        genera_oggetti_cadenti()
        aggiorna_oggetti_cadenti()
        controlla_collisioni()
        disegna_oggetti(immagine_giocatore)

        orologio.tick(30)

    pygame.quit()