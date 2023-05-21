import pygame


class Bird(pygame.sprite.Sprite):
	def __init__(self):
		super(Bird, self).__init__()
		# create animation variables
		self.animUpflap = pygame.image.load("assets/images/yellowbird-upflap.png").convert_alpha()
		self.animDownflap = pygame.image.load("assets/images/yellowbird-downflap.png").convert_alpha()
		self.animMidflap = pygame.image.load("assets/images/yellowbird-midflap.png").convert_alpha()

		# create animation list
		self.animation = [self.animUpflap, self.animMidflap, self.animDownflap]
		# create animation index
		self.indexAnim = 0
		# create animation surface
		self.surf = self.animation[self.indexAnim]
		# create animation rectangle
		self.rect = pygame.Rect(100, 250, 30, 30)

	# create animation function
	def bird_animation(self):
		# increment animation index
		self.indexAnim += 1
		# if animation index is greater than 2
		if self.indexAnim > 2:
			# reset animation index
			self.indexAnim = 0
		# set animation surface to the new sprite
		self.surf = self.animation[self.indexAnim]

	# create update function
	def update(self, pressed_keys, height):
		# if space key is pressed
		if pressed_keys[pygame.K_SPACE]:
			# move bird up
			self.rect.move_ip(0, -10)
		else:
			# move bird down
			self.rect.move_ip(0, 5)
		# if bird is above the screen
		if self.rect.top <= 0:
			# set bird to the top of the screen
			self.rect.top = 0
		# if bird is below the screen
		if self.rect.bottom >= height:
			# set bird to the bottom of the screen
			self.rect.bottom = height
