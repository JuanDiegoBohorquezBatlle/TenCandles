from pygame import *
import time

init()

running = True

h = 0
i = 0
alpha = 0
width, height = display.get_desktop_sizes()[0]
end = False
ch = False

screen = display.set_mode((width, height), RESIZABLE)
display.set_caption("Ten Candles")
humo = transform.scale(image.load("resources/humo.png"), (100, 100))

#Ciclo Main

def draw():
	if end == False:
		#Localizaciones de Velas

		posrel= [0.07143*height,	 0.14286*height, 0.32857*height,
				0.448*width,		 0.267*width,	 0.137*width]

		c1 	= (posrel[3]							,posrel[0])
		c2 	= (posrel[4]							,posrel[1])
		c3 	= (posrel[5]							,posrel[2])
		c4 	= (posrel[5]							,0.21	*	height	+	posrel[2])
		c5 	= (posrel[4]							,0.586	*	height	+	posrel[1])
		c6 	= (posrel[3]							,0.7286	*	height	+	posrel[0])
		c7 	= (0.181	*	width	+	posrel[3]	,0.586	*	height	+	posrel[1])
		c8 	= (0.628	*	width	+	posrel[5]	,0.21	*	height	+	posrel[2])
		c9 	= (0.628	*	width	+	posrel[5]	,posrel[2])
		c10	= (0.181	*	width	+	posrel[3]	,posrel[1])

		pos = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]


		#Update

		bg = transform.scale(image.load("resources/Fondo.jpeg"), (width, height))
		Black = transform.scale(image.load("resources/black.png"), (width, height))

		screen.blit(bg, (0,0))

		for j in range(i, 10):
			screen.blit(transform.scale(image.load("resources/vela1.png"), (100, 100)), (pos[j]))
		for j in range (0, i):
			screen.blit(transform.scale(image.load("resources/vela0.png"), (100, 100)), (pos[j]))
			screen.blit(humo, (pos[j][0] - 35, pos[j][1] - 50))

		Black.set_alpha(alpha)
		screen.blit(Black, (0,0))


while running:
	for ev in event.get():
		if ev.type == QUIT:
			running = False

		elif ev.type == VIDEORESIZE:
			width, height = ev.w, ev.h
			screen = display.set_mode((width, height), RESIZABLE)
			
		elif ev.type == KEYDOWN:
			if ev.key == K_F11:
				if ch == False:
					width, height = display.get_desktop_sizes()[0]
					screen = display.set_mode((width, height))
					ch = True
				else:
					width, height = 1000, 700
					screen = display.set_mode((width, height), RESIZABLE)
					ch = False

			if ev.key == K_F1:
				if i >= 0 and i < 10:
					i += 1
					alpha = min(i * 26, 255)

	draw()

	if end == True:
		fin = transform.scale(image.load("resources/fin.png"), (width, height))
		fin.set_alpha(h)

		screen.blit(fin, (0,0))
		h += 2

	time.sleep(0.1)
	display.flip()

	if i == 10 and end == False:
		end = True
		time.sleep(3)