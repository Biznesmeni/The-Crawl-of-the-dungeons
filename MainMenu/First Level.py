import pygame
import referenceCode
import sys

pygame.init()
pygame.display.set_caption('Piemērs')
icon = pygame.image.load('icon.png')#Dabū attēlu ikonai, jābūt 32x32 pikseļi
pygame.display.set_icon(icon)#Uzliek o Ikonu ekrāna stūrī
res = 1960, 1000
screen = pygame.display.set_mode((res))#izveido ekrānu (width,heigth)

running = True
while running:#Pārbauda, vai spēle strādā, arī uztver, ja aiztaisa to ciet.
    for event in pygame.event.get():#Pārbauda, vai kaut kas notiek
        if event.type == pygame.QUIT:#uztver klikšķi uz x pogas
             running = False
             pygame.quit()
             sys.exit()
             
    referenceCode.PlayerStartPos(0, 0, 'PlayerImage Idle1(Placeholder).png', screen)
    referenceCode.Movement()

