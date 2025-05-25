import pygame
import sys
from Gioco import avvia_gioco  # Importa la funzione principale del gioco

# Inizializzazione di Pygame
pygame.init()

# Dimensioni dello schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menù Meteore")
sfondo = pygame.image.load("sfondo1.png")
sfondo = pygame.transform.scale(sfondo, (SCREEN_WIDTH, SCREEN_HEIGHT)) 

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Caricamento font
font_title = pygame.font.Font(None, 100)
font_option = pygame.font.Font(None, 40)

# Testo del titolo
title_text = font_title.render("Attento alle meteore", True, WHITE)
title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))

selection_text = font_option.render("Scegli il tuo personaggio", True, WHITE)
selection_rect = selection_text.get_rect(center=(SCREEN_WIDTH // 2, 550))

# Caricamento immagini
image1 = pygame.image.load("astronauta.png")
image2 = pygame.image.load("Lebron.png")
image3 = pygame.image.load("Nurra.png")

# Ridimensionamento immagini
image1 = pygame.transform.scale(image1, (110, 150))
image2 = pygame.transform.scale(image2, (110, 150))
image3 = pygame.transform.scale(image3, (110, 150))

# Posizioni delle immagini
images = [
    {"image": image1, "rect": image1.get_rect(center=(SCREEN_WIDTH // 2 - 200, 370))},
    {"image": image2, "rect": image2.get_rect(center=(SCREEN_WIDTH // 2, 370))},
    {"image": image3, "rect": image3.get_rect(center=(SCREEN_WIDTH // 2 + 200, 370))},
]

# Caricamento sfondo
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.blit(sfondo, (0, 0))

# Indice della selezione corrente
current_selection = 0

# Funzione per disegnare il menù
def draw_menu():
    screen.blit(background, (0, 0))
    screen.blit(title_text, title_rect)
    screen.blit(selection_text, selection_rect)

    for i, item in enumerate(images):
        if i == current_selection:
            pygame.draw.rect(screen, WHITE, item["rect"].inflate(10, 10), 3)  # Evidenzia l'immagine selezionata
        screen.blit(item["image"], item["rect"])

# Funzione per avviare il gioco
def start_game():
    avvia_gioco(current_selection)  # Passa l'indice del personaggio selezionato

# Ciclo principale del menù
def main():
    global current_selection
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_selection = (current_selection - 1) % len(images)
                elif event.key == pygame.K_RIGHT:
                    current_selection = (current_selection + 1) % len(images)
                elif event.key == pygame.K_RETURN:  # Tasto Invio per avviare il gioco
                    start_game()

        draw_menu()
        pygame.display.flip()
        clock.tick(1000)

if __name__ == "__main__":
    main()