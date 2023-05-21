import pygame
# init pygame
pygame.init()

# create size variables
WIDTH = 280
HEIGHT = 500

# create surface
surface = pygame.display.set_mode((WIDTH, HEIGHT))
# create background
surface.blit(pygame.image.load("assets/images/background-day.png"), (0, 0))
# create base
surface.blit(pygame.image.load("assets/images/base.png"), (0, 400))
# set title
pygame.display.set_caption("flappy bird")

# game loop
# create running variable
running = True
# while running is true
while running:
	# for each event in pygame
	for event in pygame.event.get():
		# if event is quit
		if event.type == pygame.QUIT:
			# set running to false
			running = False
	# update display
	pygame.display.flip()
