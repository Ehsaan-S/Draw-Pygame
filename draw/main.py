import pygame

pygame.init()

screen_width = 600
screen_height = 400

screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Draw Funtions")

def drawFigure(surface,colour,x,y,radius,):
    #Head
    pygame.draw.circle(surface,colour,(x,y-radius),radius)
    #body
    pygame.draw.line(surface,colour,(x,y))
    #arms
    pygame.draw.line(surface,colour,(x,y))
    pygame.draw.line(surface,colour,(x,y))
    #legs
    pygame.draw.line(surface,colour,(x,y+2*radius))
    pygame.draw.line(surface,colour,(x,y))



run = True
while run:
    screen.fill((255,255,255))
    
    drawFigure(screen,(255,0,0),50,100,30,)

   
   

   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
            
    pygame.display.flip()