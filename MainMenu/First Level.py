import pygame
import referenceCode
import sys
import PlayerVariables
import Monster

pygame.init()

playerCoordsX = 0
playerCoordsY = 0

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
        if event.type == pygame.KEYDOWN:
            # if event.key == event.key == ord('e'):
                # if monster.rect in attack.rect:
                #     monsterHP = monsterHp - PlayerDamage
                # print ('attack')
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                playerCoordsX = playerCoordsX - 2
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                playerCoordsX = playerCoordsX + 2
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
                playerCoordsY = playerCoordsY - 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')          
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                    
    screen.fill((0,0,0))         
    referenceCode.PlayerImage(playerCoordsX, playerCoordsY, 'PlayerImage Idle1(Placeholder).png', screen)
    pygame.display.update()

