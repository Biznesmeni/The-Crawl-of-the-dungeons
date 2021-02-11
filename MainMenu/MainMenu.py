import pygame #importē pygame lai var izmantot funkcijas
import sys
import referenceCode


pygame.init()#vajadzīgs, lai inicializētu funkcijas

pygame.display.set_caption('Piemērs')#Pārmaina ekrāna spēles nosaukumu ekrāna kreisajā augšā

icon = pygame.image.load('icon.png')#Dabū attēlu ikonai, jābūt 32x32 pikseļi
pygame.display.set_icon(icon)#Uzliek o Ikonu ekrāna stūrī


res = 1960, 1000
screen = pygame.display.set_mode((res))#izveido ekrānu (width,heigth)

#button_sound = pygame.mixer.Sound('ButtonSound(Placeholder).wav')
button_START_sound = referenceCode.Sounds('ButtonSound(Placeholder).wav')

referenceCode.PlayMusic('MainMenu.wav')

running = True


while running:#Pārbauda, vai spēle strādā, arī uztver, ja aiztaisa to ciet.
    for event in pygame.event.get():#Pārbauda, vai kaut kas notiek
        if event.type == pygame.QUIT:#uztver klikšķi uz x pogas
            running = False
            pygame.quit()
            sys.exit()
   
     
    screen.fill((0,0,0))#aizkrāso ekrānu oranžu RGB - (Red, Green, Blue)
    
    referenceCode.ButtonStart('StartUnclicked(PlaceHolder).png', 'StartClicked(PlaceHolder).png', 20, 100, button_START_sound, screen)#ieprieks veidotā 
    
    referenceCode.CursorReplace('Cursor.png', screen)#ieprieks veidotā funkcija
    
    referenceCode.background('Background_Menu(PlaceHolder).png', screen)#ieprieks veidotā funkcija  
    
    referenceCode.GameLogo('PlaceHolderLogo.png', screen)#ieprieks veidotā funkcija
    
    pygame.display.update()#Updato ekrānu, lai izdēstu bijusos frames.
    
    