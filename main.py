import pygame as pg

pg.init()
pg.display.set_caption("CGT115 Lab 5 - Compositing")

#Load images
img = pg.image.load("img/backgrounds/winter.png")
img2 = pg.image.load("img/characters/yoda.png")

#Set screen
width = img.get_width()
height = img.get_height()
screen = pg.display.set_mode((width, height))

#Pixel color to be replaced
baseline_color = img2.get_at((0,0))

for y in range(0, height):
    for x in range(0, width):
        #Get pixel from image
        c1 = img.get_at((x, y))
        c2 = img2.get_at((x, y))

        #Checks for green pixel
        if c2 == baseline_color:
            #Sets img as new pixel
            newColor = img.get_at((x, y))
            img.set_at((x, y), newColor)
        else:
            #Keeps img2 pixel
            newColor = img2.get_at((x, y))
            img.set_at((x, y), c2)

screen.blit(img, (0,0))

pg.display.flip()

#File save
pg.image.save(img, "mergedImg.png")

#Run
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            done = True

