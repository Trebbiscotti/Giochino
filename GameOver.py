import pygame
import sys

def schermata_game_over(schermo, larghezza_finestra, altezza_finestra, punteggio):
    schermo.fill((0, 0, 0))  # Sfondo nero
    font_game_over = pygame.font.SysFont(None, 120)
    font_punteggio = pygame.font.SysFont(None, 100)
    font_istruzioni = pygame.font.SysFont(None, 50)
    testo_game_over = font_game_over.render("Game Over", True, (255, 255, 255))
    testo_istruzioni = font_istruzioni.render("Premi INVIO per tornare al menu", True, (255, 255, 255))
    testo_punteggio = font_punteggio.render(f"Punteggio: {punteggio}", True, (255, 255, 255))

    schermo.blit(testo_game_over, (larghezza_finestra // 2 - testo_game_over.get_width() // 2, altezza_finestra // 2 - 250))
    schermo.blit(testo_istruzioni, (larghezza_finestra // 2 - testo_istruzioni.get_width() // 2, altezza_finestra // 2 + 250))
    schermo.blit(testo_punteggio, (larghezza_finestra // 2 - testo_punteggio.get_width() // 2, altezza_finestra // 2 + 10))
    pygame.display.update()

    # Aspetta che l'utente prema INVIO o ESC
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Tasto INVIO per tornare al menu
                    return  # Esci dalla funzione e torna al menu
                elif evento.key == pygame.K_ESCAPE:  # Tasto ESC per uscire
                    pygame.quit()
                    sys.exit()