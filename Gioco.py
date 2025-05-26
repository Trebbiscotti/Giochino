import pygame
import random
from GameOver import schermata_game_over
from Menu import main  # Importa la funzione principale del menù

# Inizializzazione di Pygame
pygame.init()

# Dimensioni della finestra
LARGHEZZA_FINESTRA = 800
ALTEZZA_FINESTRA = 600
COLORE_SFONDO = (50, 150, 255)

# Variabili del giocatore
altezza_giocatore = 60
larghezza_giocatore = 40
posizione_giocatore_x = LARGHEZZA_FINESTRA // 2 - larghezza_giocatore // 2
posizione_giocatore_y = ALTEZZA_FINESTRA - altezza_giocatore - 10
velocita_giocatore = 15
numero_vite = 3
vite = 3

# Variabili degli oggetti cadenti
dimensioni_oggetto_cadente = 45
lista_oggetti_cadenti = []
velocita_oggetto_cadente = 5
probabilità_generazione = 15

# Punteggio
punteggio = 0
prossimo_aumento_velocita = 10
prossimo_incremento_vite = 50  # Il primo incremento avviene a 50 punti

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
    pygame.transform.scale(img, (larghezza_giocatore, altezza_giocatore))
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

def genera_cuori():
    global numero_vite
    image4 = pygame.image.load("cuore.png")
    image4 = pygame.transform.scale(image4, (30, 30))  # Ridimensiona il cuore
    x_offset = LARGHEZZA_FINESTRA - 40  # Posizione iniziale (a destra)
    y_offset = 10  # Posizione verticale (in alto)

    for i in range(numero_vite):
        schermo.blit(image4, (x_offset - i * 40, y_offset))  # Disegna i cuori con uno spazio tra loro

def resetta_gioco():
    global numero_vite, punteggio, lista_oggetti_cadenti, velocita_oggetto_cadente, probabilità_generazione, prossimo_aumento_velocita, prossimo_incremento_vite

    numero_vite = 3  # Numero iniziale di vite
    punteggio = 0  # Punteggio iniziale
    lista_oggetti_cadenti = []  # Lista vuota di oggetti cadenti
    velocita_oggetto_cadente = 5  # Velocità iniziale degli oggetti cadenti
    probabilità_generazione = 15  # Probabilità iniziale di generazione degli oggetti
    prossimo_aumento_velocita = 10  # Punteggio per il prossimo aumento di velocità
    prossimo_incremento_vite = 50  # Punteggio per il prossimo incremento di vite

# Funzione per aggiornare gli oggetti cadenti
def aggiorna_oggetti_cadenti():
    global lista_oggetti_cadenti, punteggio, velocita_oggetto_cadente, prossimo_aumento_velocita, probabilità_generazione, numero_vite, prossimo_incremento_vite

    for obj in lista_oggetti_cadenti:
        obj[1] += velocita_oggetto_cadente
        if obj[1] > ALTEZZA_FINESTRA:
            lista_oggetti_cadenti.remove(obj)
            punteggio += 1

            # Controlla se il punteggio ha raggiunto il prossimo incremento di vite
            if punteggio >= prossimo_incremento_vite:
                numero_vite += 1  # Aggiungi una vita
                prossimo_incremento_vite += 50  # Aggiorna il prossimo incremento

            # Aumenta la velocità degli oggetti cadenti ogni 10 punti
            if punteggio >= prossimo_aumento_velocita:
                velocita_oggetto_cadente += 1
                prossimo_aumento_velocita += 10

            # Riduci la probabilità di generazione ogni 10 punti
            if punteggio % 10 == 0:
                probabilità_generazione = max(4, probabilità_generazione - 1)

# Funzione per generare oggetti cadenti
def genera_oggetti_cadenti():
    global probabilità_generazione
    if random.randint(1, probabilità_generazione) == 1:
        pos_x = random.randint(0, LARGHEZZA_FINESTRA - dimensioni_oggetto_cadente)
        lista_oggetti_cadenti.append([pos_x, 0])

# Funzione per controllare le collisioni
def controlla_collisioni():
    global in_esecuzione, numero_vite
    rettangolo_giocatore = pygame.Rect(posizione_giocatore_x, posizione_giocatore_y, larghezza_giocatore, altezza_giocatore)
    for obj in lista_oggetti_cadenti:
        rettangolo_oggetto = pygame.Rect(obj[0], obj[1], dimensioni_oggetto_cadente, dimensioni_oggetto_cadente)
        if rettangolo_giocatore.colliderect(rettangolo_oggetto):
            lista_oggetti_cadenti.remove(obj)  # Rimuovi l'oggetto che ha colpito il giocatore
            numero_vite -= 1  # Riduci il numero di vite
            if numero_vite <= 0:
                in_esecuzione = False  # Termina il ciclo principale
                schermata_game_over(schermo, LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA, punteggio)  # Mostra la schermata di "Game Over"
                resetta_gioco()  # Reimposta le variabili del gioco
                main()  # Torna al menù principale

# Funzione principale per avviare il gioco
def avvia_gioco(personaggio_selezionato):
    global in_esecuzione, posizione_giocatore_x, velocita_giocatore, vite

    # Caricamento della musica del gioco
    pygame.mixer.init()
    pygame.mixer.music.load("sound_track.mp3")  # Sostituisci con il nome del file della tua musica
    pygame.mixer.music.set_volume(0.5)  # Imposta il volume (0.0 - 1.0)
    pygame.mixer.music.play(-1)  # Riproduci in loop (-1 per loop infinito)

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
        if tasti[pygame.K_RIGHT] and posizione_giocatore_x < LARGHEZZA_FINESTRA - larghezza_giocatore:
            posizione_giocatore_x += velocita_giocatore

        genera_oggetti_cadenti()
        aggiorna_oggetti_cadenti()
        controlla_collisioni()

        # Disegna gli oggetti e i cuori
        disegna_oggetti(immagine_giocatore)
        i = 0
        if i == 0:
            genera_cuori()
            i += 1
        
        pygame.display.update()
        if numero_vite != vite:
            genera_cuori()  
        vite = numero_vite  # Aggiorna il numero di vite      

        #pygame.display.update()
        orologio.tick(30)

    pygame.mixer.music.stop()  # Ferma la musica quando il gioco termina
    pygame.quit()