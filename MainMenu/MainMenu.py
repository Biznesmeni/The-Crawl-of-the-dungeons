import pygame #importē pygame lai var izmantot funkcijas
import sys
import time

pygame.init()#vajadzīgs, lai inicializētu funkcijas

class Sounds:
    def __init__(self, sound_file):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sound_file)
        self.channel = None
        self.activated = False
    
    def activate(self, state):
        self.activated = state
        
    def play(self):
        if not (self.channel and self.channel.get_busy()) and not self.activated:
            self.channel = self.sound.play(loops=1, maxtime=500)
            self.activate(True)


res = 960, 540



screen = pygame.display.set_mode((res))#izveido ekrānu (width,heigth)

pygame.display.set_caption('Piemērs')#Pārmaina ekrāna spēles nosaukumu ekrāna kreisajā augšā

icon = pygame.image.load('Sprite-0002.png')#Dabū attēlu ikonai, jābūt 32x32 pikseļi
pygame.display.set_icon(icon)#Uzliek o Ikonu ekrāna stūrī

GameLogoImg = pygame.image.load('PlaceHolderLogo.png')#Šeit jāieliek spēles logo, vai titles.
GamelogoX = 0#kur atradīsies attēls y asī
GameLogoY = 0#kur atradīsies attēls y asī

BackgroundImg = pygame.image.load('Background_Menu(PlaceHolder).png')#atrod attēlu folderī
BackgroundX = 0 #kur atradīsies attēls x asī
BackgroundY = 0 #kur atradīsies attēls y asī

button_START = pygame.image.load('StartUnclicked(PlaceHolder).png')
button_START2 = pygame.image.load('StartClicked(PlaceHolder).png')
button_STARTx = 20#kur atradīsies attēls y asī
button_STARTy = 300#kur atradīsies attēls y asī

#button_sound = pygame.mixer.Sound('ButtonSound(Placeholder).wav')
button_START_sound = Sounds('ButtonSound(Placeholder).wav')

def CursorReplace():#izveido jaunu funkciju
    cursor_img = pygame.image.load('Cursor.png')#Šī līnija atrod vajadzīgo attēlu
    pygame.mouse.set_visible(False)#Šī līnija padara kursoru neredzamu
    xy = pygame.mouse.get_pos()#Šī līnija atrod kursora x un y koordinātes
    screen.blit(cursor_img, (xy))#Šī līnija printē izvēlēto attēlu kursora vietā
    
def Button(): #izveido jaunu funkciju
    xy = pygame.mouse.get_pos()#Šī līnija atrod kursora x un y koordinātes
    screen.blit(button_START,(button_STARTx, button_STARTy))
    buttonSTARTrect = button_START.get_rect()
    if buttonSTARTrect.left+button_STARTx <= xy[0] <= buttonSTARTrect.right+button_STARTx and buttonSTARTrect.top+button_STARTy <= xy[1] <= buttonSTARTrect.bottom+button_STARTy:#nosaka, vai kursors atrodas pareizajā vietā     
        button_START_sound.play()

    else:
        button_START_sound.activate(False)
            
def PlayMusic():#izveido jaunu funkciju
    pygame.mixer.music.load('MainMenu.wav') #Šī komanda atrod mūzikas failu
    pygame.mixer.music.play(-1) #Šī komanda spēlē mūziku bezgalīgi


def background():#izveido jaunu funkciju
    screen.blit(BackgroundImg, (BackgroundX,BackgroundY)) #izprintē pasu attēlu

def GameLogo():#izveido jaunu funkciju
    screen.blit(GameLogoImg, (GamelogoX, GameLogoY))    

PlayMusic()

running = True

while running:#Pārbauda, vai spēle strādā, arī uztver, ja aiztaisa to ciet.
    for event in pygame.event.get():#Pārbauda, vai kaut kas notiek
        if event.type == pygame.QUIT:#uztver klikšķi uz x pogas
            running = False
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))#aizkrāso ekrānu oranžu RGB - (Red, Green, Blue)
   
    Button()#ieprieks veidotā 
    


    background()#ieprieks veidotā funkcija  
    
    GameLogo()#ieprieks veidotā funkcija
        
    CursorReplace()#ieprieks veidotā funkcija\    
 
    

    
    pygame.display.update()#Updato ekrānu, lai izdēstu bijusos frames.
    
    