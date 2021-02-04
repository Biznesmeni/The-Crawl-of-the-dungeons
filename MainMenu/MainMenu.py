import pygame #importē pygame lai var izmantot funkcijas

BackgroundImg = pygame.image.load('Background_Menu(PlaceHolder).png')#atrod attēlu folderī
BackgroundX = 0 #kur atradīsies attēls x asī
BackgroundY = 0 #kur atradīsies attēls y asī

def background():#izveido jaunu funkciju
    screen.blit(BackgroundImg, (BackgroundX,BackgroundY)) #izprintē pāsu attēlu
    
 
  
pygame.init()#vajadzīgs, lai inicializētu funkcijas

screen = pygame.display.set_mode((960,540))#izveido ekrānu (width,heigth)

pygame.display.set_caption('Piemērs')#Pārmaina ekrāna spēles nosaukumu ekrāna kreisajā augšā
icon = pygame.image.load('Sprite-0002.png')#Dabū attēlu ikonai, jābūt 32x32 pikseļi
pygame.display.set_icon(icon)#Uzliek o Ikonu ekrāna stūrī

#Pārbauda, vai spēle strādā, arī uztver, ja aiztaisa to ciet.
running = True
while running:
    for event in pygame.event.get():#Pārbauda, vai kaut kas notiek
        if event.type == pygame.QUIT:#uztver klikšķi uz x pogas
            running = False
    # screen.fill((255,165,0))#aizkrāso ekrānu oranžu RGB - (Red, Green, Blue)
    
    background()#iepriek veidotā funkcija
    pygame.display.update()#Updato ekrānu, lai izdēstu bijusos framus.
    
    





    
            
    
