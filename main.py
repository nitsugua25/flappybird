import pygame

pygame.init()

WIDTH = 280
HEIGHT = 500

surface = pygame.display.set_mode((WIDTH, HEIGHT))
surface.blit(pygame.image.load("assets/images/background-day.png"), (0, 0))

pygame.display.set_caption("flappy bird")

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()
