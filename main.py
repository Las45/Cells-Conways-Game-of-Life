import pygame

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))  # Fill the window with black color
    pygame.display.flip()  # Update the display