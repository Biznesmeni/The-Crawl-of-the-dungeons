import pygame #importē pygame lai var izmantot funkcijas
import sys
import referenceCode

pygame.init()#vajadzīgs, lai inicializētu funkcijas

pygame.display.set_caption('Piemērs')#Pārmaina ekrāna spēles nosaukumu ekrāna kreisajā augšā

icon = pygame.image.load('icon.png')#Dabū attēlu ikonai, jābūt 32x32 pikseļi
pygame.display.set_icon(icon)#Uzliek o Ikonu ekrāna stūrī

res = 1960, 1000
screen = pygame.display.set_mode((res))#izveido ekrānu (width,heigth)

running= True
while running:#Pārbauda, vai spēle strādā, arī uztver, ja aiztaisa to ciet.
    for event in pygame.event.get():#Pārbauda, vai kaut kas notiek
        if event.type == pygame.QUIT:#uztver klikšķi uz x pogas
             running = False
             pygame.quit()
             sys.exit()
    pygame.display.update()#Updato ekrānu, lai izdēstu bijusos frames.