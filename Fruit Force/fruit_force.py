#Fruit Force

import pygame, sys, random
from pygame.locals import *

#Set up Pygame
pygame.init()
mainclock = pygame.time.Clock()

#Set up the window
WINDOWWIDTH = 1200
WINDOWHEIGHT = 900
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Fruit Force')
pygame.display.set_icon(pygame.image.load('images/ff_icon.png'))


#Colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 195, 0)
YELLOW = (255, 255, 0)
LIME = (0, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE =  (128, 0, 128)


#Constants
CENTERX = WINDOWWIDTH / 2
CENTERY = WINDOWHEIGHT / 2
CENTER = (CENTERX, CENTERY)
MAINFRUITSIZE = 120
FRUITMINSIZE = MAINFRUITSIZE / 1.5
FRUITMAXSIZE = MAINFRUITSIZE * 1.5
FPS = 60
FONT = 'freesansbold.ttf'
SPEED = 7


#Load Assets
bgimg1 = pygame.image.load('images/ff bgimg1.png')
bgimg1 = pygame.transform.scale(bgimg1, (WINDOWWIDTH, WINDOWHEIGHT))

bgimg2 = pygame.image.load('images/ff bgimg2.png')
bgimg2 = pygame.transform.scale(bgimg2, (WINDOWWIDTH, WINDOWHEIGHT))

meetingroomimg = pygame.image.load('images/ff meeting room.png')
meetingroomimg = pygame.transform.scale(meetingroomimg, (WINDOWWIDTH, WINDOWHEIGHT))

#Load sprites
playerimg = pygame.image.load('images/default_player.png')
playerimg = pygame.transform.scale(playerimg, (100, 200))
playerrect = playerimg.get_rect()
playerrect.center = CENTER

cherryimg = pygame.image.load('images/cherry.png')
cherryimg = pygame.transform.scale(cherryimg, (MAINFRUITSIZE, MAINFRUITSIZE))
cherryrect = cherryimg.get_rect()

appleimg = pygame.image.load('images/apple.png')
appleimg = pygame.transform.scale(appleimg, (MAINFRUITSIZE, MAINFRUITSIZE))
applerect = appleimg.get_rect()

pineappleimg = pygame.image.load('images/pineapple.png')
pineappleimg = pygame.transform.scale(pineappleimg, (MAINFRUITSIZE, MAINFRUITSIZE))
pineapplerect = pineappleimg.get_rect()

orangeimg = pygame.image.load('images/orange.png')
orangeimg = pygame.transform.scale(orangeimg, (MAINFRUITSIZE, MAINFRUITSIZE))
orangerect = orangeimg.get_rect()

#Load sounds
bite1 = pygame.mixer.Sound('sounds/carrotnom-92106.mp3')
bite2 = pygame.mixer.Sound('sounds/eat_crunchy-40919.mp3')
bites = [bite1, bite2]
pygame.mixer.music.load('sounds/Fruit Force Main Theme.wav')

#Set up the fruit data structures
fruitstrings = ['cherry', 'apple', 'pineapple', 'orange']
fruitimgs = [cherryimg, appleimg, pineappleimg, orangeimg]
fruitrects = [cherryrect, applerect, pineapplerect, orangerect]
fruitinfo = [['cherry', cherryimg, cherryrect], ['apple', appleimg, applerect], ['pineapple', pineappleimg, pineapplerect], ['orange', orangeimg, orangerect]]
loadedfruits = []

meetingfont = pygame.font.Font('freesansbold.ttf', 45)


def main():
	#Play the song
	pygame.mixer.music.play(-1, 0.0)

	#Run the game loop
	while True:
		title_screen()
		rungame()



def rungame():
	global score, bgimg, right, left, up, down, ft_frame, bgimg, im_frame, csi, tunm, bg_frame, cbg, meeting
	global num_ims, allfruits, tti, meetingcount, game_over, im_rate, im_count, loadedfruits


	#Set up variables for phase 1
	score = 0
	right = left = up = down = False
	bgimg = bgimg1
	ft_frame = 0
	im_frame = 0
	csi = True
	tunm = 1800
	bg_frame = 0
	cbg = True
	meeting = False
	allfruits = []
	tti = 0
	meetingcount = 1
	game_over = False
	im_rate = random.randint(100, tunm - 300)
	im_count = 0
	num_ims = 1
	allfruits.clear()
	loadedfruits.clear()
	playerrect.center = CENTER

	#Game Loop
	while True:
		if not game_over:
			if meeting == False:
				for event in pygame.event.get(): #Event handling loop
					if event.type == QUIT:
						terminate()
					if event.type == KEYDOWN:
						if event.key == K_ESCAPE:
							terminate()

						#Check for arrows
						if event.key == K_RIGHT:
							left = False
							right = True
						if event.key == K_LEFT:
							right = False
							left = True
						if event.key == K_UP:
							down = False
							up = True
						if event.key == K_DOWN:
							up = False
							down = True

					if event.type == KEYUP:
						if event.key == K_RIGHT:
							right = False
						if event.key == K_LEFT:
							left = False
						if event.key == K_UP:
							up = False
						if event.key == K_DOWN:
							down = False


				DISPLAYSURF.blit(bgimg, (0, 0))
				moveplayer()
				DISPLAYSURF.blit(playerimg, playerrect)

				checkspawnfruit()
				drawfruits()

				drawtimetext()

				drawtext('Level: ' + str(meetingcount), FONT, 14, DISPLAYSURF, 50, 10, PURPLE)
				pygame.display.update()
				mainclock.tick(FPS)

			else:
				if meetingcount == 1:
					meeting_one()

					right = left = up = down = False
					bgimg = bgimg1
					ft_frame = 0
					im_frame = 0
					csi = True
					tunm = 1800
					bg_frame = 0
					cbg = True
					meeting = False
					loadedfruits = []
					allfruits = []
					tti = 0
					meetingcount = 2
					im_rate = random.randint(100, tunm - 300)
					meeting = False
					num_ims = 1

				elif meetingcount == 2:
					meeting_one()

					score = 0
					right = left = up = down = False
					bgimg = bgimg1
					ft_frame = 0
					im_frame = 0
					csi = True
					tunm = 1800
					bg_frame = 0
					cbg = True
					meeting = False
					allfruits = []
					tti = 0
					meetingcount = 3
					game_over = False
					im_rate = random.randint(100, tunm - 300) / 2
					im_count = 0
					num_ims = 2

				elif meetingcount == 3:
					meeting_three()
					game_over = True

		else:
			if win == 'kill':
				imposter()
			elif win != True:
				gameover()
			else:
				win_screen()

			return


def title_screen():
	title = pygame.transform.scale(pygame.image.load('images/title_screen.png'), (WINDOWWIDTH + 600, WINDOWHEIGHT + 600))
	DISPLAYSURF.blit(title, (-300, -300))
	pygame.display.update()
	drawtext('Press a key to play...', FONT, 25, DISPLAYSURF, CENTERX, CENTERY, MAGENTA)

	x = CENTERX - 400
	y = CENTERY + 200
	for i in range(0, 4):
		fruitimg = pygame.transform.scale(fruitimgs[i], (200, 200))
		DISPLAYSURF.blit(fruitimg, (x, y))
		x += 200

	pygame.display.update()
	pygame.time.wait(1000)

	wait_for_key_press()
	return


def gameover():
	DISPLAYSURF.blit(bgimg1, (0, 0))
	drawtext('GAME OVER', FONT, 180, DISPLAYSURF, CENTERX, CENTERY - 200, MAGENTA)
	pygame.display.update()
	drawtext('Press a key to move on...', FONT, 40, DISPLAYSURF, CENTERX, CENTERY, MAGENTA)
	pygame.display.update()
	pygame.time.wait(1000)
	wait_for_key_press()
	return


def imposter():
	DISPLAYSURF.blit(bgimg1, (0, 0))
	drawtext('The Imposter has killed you...', FONT, 80, DISPLAYSURF, CENTERX, CENTERY - 200, MAGENTA)
	pygame.display.update()
	drawtext('Press a key to move on...', FONT, 40, DISPLAYSURF, CENTERX, CENTERY, MAGENTA)
	pygame.display.update()
	pygame.time.wait(1000)
	wait_for_key_press()
	return


def win_screen():
	DISPLAYSURF.blit(bgimg1, (0, 0))
	drawtext('Congratulations, you have beaten Fruit Force...', FONT, 50, DISPLAYSURF, CENTERX, CENTERY - 200, MAGENTA)
	pygame.display.update()
	drawtext('Press a key to move on...', FONT, 40, DISPLAYSURF, CENTERX, CENTERY, MAGENTA)
	pygame.display.update()
	pygame.time.wait(1000)
	wait_for_key_press()
	return


def wait_for_key_press():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()
				return


def meeting_three():
	global game_over, allfruits, loadedfruits, win
	cherryrect = cherryimg.get_rect()
	cherryrect.center = CENTER

	ims_found = 0

	random.shuffle(allfruits)

	DISPLAYSURF.blit(meetingroomimg, (0, 0))

	drawtext('Click on a fruit to vote it out. Vote out the the two fruits that you think are the imposters...', FONT,
			 28, DISPLAYSURF, CENTERX, CENTERY - 300, WHITE, BLACK)

	x = 10
	y = CENTER[0] - 325
	for fruit in allfruits:
		nextfruitimg = pygame.transform.scale(fruit[3], (fruit[2], fruit[2]))
		fruit[1] = nextfruitimg.get_rect()
		fruit[1].x = x
		fruit[1].y = y
		DISPLAYSURF.blit(nextfruitimg, fruit[1])

		x += 145
		if x >= WINDOWWIDTH - FRUITMAXSIZE - 20:
			x = 10
			y += FRUITMAXSIZE + 20

	while True:
		x = 10
		y = CENTER[0] - 325
		for fruit in allfruits:
			nextfruitimg = pygame.transform.scale(fruit[3], (fruit[2], fruit[2]))
			fruit[1] = nextfruitimg.get_rect()
			fruit[1].x = x
			fruit[1].y = y
			DISPLAYSURF.blit(nextfruitimg, fruit[1])

			x += 145
			if x >= WINDOWWIDTH - FRUITMAXSIZE - 20:
				x = 10
				y += FRUITMAXSIZE + 20


		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()

			if event.type == MOUSEBUTTONUP:
				for fruit in allfruits:
					if fruit[1].collidepoint(pygame.mouse.get_pos()):
						if fruit[6]: #Got the imposter
							allfruits.remove(fruit)
							DISPLAYSURF.blit(meetingroomimg, (0, 0))
							drawtext('That ' + str(fruit[0]) + ' was an imposter...', FONT, 30, DISPLAYSURF, CENTERX, CENTERY - 300, WHITE, BLACK)
							pygame.display.update()
							ims_found += 1
							if ims_found == 2:
								pygame.time.wait(2000)
								game_over = True
								win = True
								return


						else:
							DISPLAYSURF.blit(meetingroomimg, (0, 0))
							drawtext('That ' + str(fruit[0]) + ' was a crewmate... ', FONT, 30, DISPLAYSURF, CENTERX, CENTERY - 300, WHITE, BLACK)
							pygame.display.update()
							pygame.time.wait(4000)
							game_over = True
							win = False
							return

		pygame.display.update()
		mainclock.tick(FPS)


def meeting_one():
	global game_over, allfruits, loadedfruits, win
	cherryrect = cherryimg.get_rect()
	cherryrect.center = CENTER

	random.shuffle(allfruits)

	DISPLAYSURF.blit(meetingroomimg, (0, 0))

	drawtext('Click on a fruit to vote it out. Vote out the fruit who you think is the imposter...', FONT, 30,
			 DISPLAYSURF, CENTERX, CENTERY - 300, WHITE, BLACK)

	x = 10
	y = CENTER[0] - 325
	for fruit in allfruits:
		nextfruitimg = pygame.transform.scale(fruit[3], (fruit[2], fruit[2]))
		fruit[1] = nextfruitimg.get_rect()
		fruit[1].x = x
		fruit[1].y = y
		DISPLAYSURF.blit(nextfruitimg, fruit[1])

		x += 145
		if x >= WINDOWWIDTH - FRUITMAXSIZE - 20:
			x = 10
			y += FRUITMAXSIZE + 20

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()

			if event.type == MOUSEBUTTONUP:
				for fruit in allfruits:
					if fruit[1].collidepoint(pygame.mouse.get_pos()):
						DISPLAYSURF.blit(meetingroomimg, (0, 0))
						if fruit[6]: #Got the imposter
							drawtext('That ' + str(fruit[0]) + ' was the imposter. You move on to the next phase... ', FONT, 30, DISPLAYSURF, CENTERX, CENTERY - 300, WHITE, BLACK)
							pygame.display.update()
							pygame.time.wait(4000)
							loadedfruits.clear()
							allfruits.clear()
							return

						else:
							drawtext('That ' + str(fruit[0]) + ' was a crewmate... ', FONT, 30, DISPLAYSURF, CENTERX, CENTERY - 300, WHITE, BLACK)
							pygame.display.update()
							pygame.time.wait(4000)
							game_over = True
							win = False
							return

		pygame.display.update()
		mainclock.tick(FPS)


def drawtimetext():
	global tunm, meeting

	drawtext('Time until next meeting: ' + str(round(tunm / FPS)), FONT, 14, DISPLAYSURF, WINDOWWIDTH - 100, 10, PURPLE)
	tunm -= 1
	if tunm < 1:
		meeting = True


def drawtext(text, font, size, surface, x, y, color, bground = None):
    fontobj = pygame.font.Font(font, size)
    textobj = fontobj.render(text, size, color, bground)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def drawfruits():
	global tti, game_over, win

	for fruit in loadedfruits[:]:
		if bgimg == fruit[7]:
			fruitimg = pygame.transform.scale(fruit[3], (fruit[2], fruit[2]))
			fruit[1].center = (fruit[4], fruit[5])
			DISPLAYSURF.blit(fruitimg, fruit[1])
			if not fruit[6]: #Not the imposter
				if fruit[1].colliderect(playerrect):
					random.choice(bites).play()
					loadedfruits.remove(fruit)
			else:
				if fruit[1].colliderect(playerrect):
					if tti < 70:
						tti += 1

					if tti >= 70 and meetingcount != 1:
						game_over = True
						win = 'kill'


def placefruit(fruit, fruitimg, imposter):
	global allfruits

	newfruit = str(fruit)
	newfruitsize = random.randint(FRUITMINSIZE, FRUITMAXSIZE)
	newfruitimg = pygame.transform.scale(fruitimg, (newfruitsize, newfruitsize))
	newfruitrect = newfruitimg.get_rect()
	fruitx = random.randint(10, WINDOWWIDTH - 10)
	fruity = random.randint(10, WINDOWHEIGHT - 10)
	room = random.choice([bgimg1, bgimg2])
	loadedfruits.append([newfruit, newfruitrect, newfruitsize, fruitimg, fruitx, fruity, imposter, room])
	allfruits.append([newfruit, newfruitrect, newfruitsize, fruitimg, fruitx, fruity, imposter, room])


def checkspawnfruit():
	global ft_frame, csi, im_frame, im_count

	if ft_frame > random.randint(70, 1000):
		ft_frame = 0
		fobj = random.randint(0, 3)
		placefruit(fruitstrings[fobj], fruitimgs[fobj], False)
	else:
		ft_frame += 1

	if csi == True:
		if im_frame > im_rate:
			if (meetingcount == 1) or (meetingcount == 2):
				csi = False
			elif (meetingcount == 3):
				im_count += 1
				if im_count == 2:
					csi = False

			fobj = random .randint(0, 3)
			placefruit(fruitstrings[fobj], fruitimgs[fobj], True)
		else:
			im_frame += 1


def moveplayer():
	global bgimg, cbg, bg_frame

	if right == True:
		if not playerrect.right >= WINDOWWIDTH:
			playerrect.x += SPEED
	if left == True:
		if not playerrect.x <= 0:
			playerrect.x -= SPEED
	if up == True:
		if not playerrect.y <= 0:
			playerrect.y -= SPEED
	if down == True:
		if not playerrect.bottom >= WINDOWHEIGHT:
			playerrect.y += SPEED

	if (playerrect.x >= 1050 and playerrect.x <= WINDOWWIDTH) and (playerrect.y >= 400 and playerrect.y <= 515):
		if cbg == True:
			bg_frame = 0
			if bgimg == bgimg1:
				bgimg = bgimg2
				cbg = False
			else:
				bgimg = bgimg1
				cbg = False
		else:
			bg_frame += 1
			if bg_frame >= 32:
				cbg = True
				bg_frame = 0


def terminate():
	pygame.quit()
	sys.exit()


if __name__ == '__main__':
	main()
