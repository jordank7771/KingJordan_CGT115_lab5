import pygame as pg

pg.init()

pg.display.set_caption("Hello World")

img = pg.image.load("C:\Users\spagh\OneDrive\Desktop\images1\backgrounds\winter.png")
img2 = pg.image.load("C:\Users\spagh\OneDrive\Desktop\images1\characters\yoda.png")

width = img.get_width()
height = img.get_height()
screen = pg.display.set_mode((width, height))
for y in range(0, height):
    for x in range(0, width):
        c1 = img.get_at((x, y))
        c2 = img2.get_at((x, y))
        newColor = ((c1.r + c2.r) // 2, (c1.g + c2.g) // 2, (c1.b + c2.b) // 2)
        img.set_at((x, y), newColor)

screen.blit(img, (0,0))

pg.display.flip()

pg.image.save(img, "BW.png")

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            done = True

