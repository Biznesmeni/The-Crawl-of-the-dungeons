import pygame

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

def CursorReplace(cursor_img, screen):#izveido jaunu funkciju
    cursor_img = pygame.image.load(cursor_img)#Šī līnija atrod vajadzīgo attēlu
    pygame.mouse.set_visible(False)#Šī līnija padara kursoru neredzamu
    xy = pygame.mouse.get_pos()#Šī līnija atrod kursora x un y koordinātes
    screen.blit(cursor_img, (xy))#Šī līnija printē izvēlēto attēlu kursora vietā
    
def Button(first, second, x, y, sound, screen): #izveido jaunu funkciju
    button = pygame.image.load(first)
    button2 = pygame.image.load(second)
    buttonx = x#kur atradīsies attēls y asī
    buttony = y#kur atradīsies attēls y asī
    xy = pygame.mouse.get_pos()#Šī līnija atrod kursora x un y koordinātes
    buttonrect = button.get_rect()
    if buttonrect.left+buttonx <= xy[0] <= buttonrect.right+buttonx and buttonrect.top+buttony <= xy[1] <= buttonrect.bottom+buttony:#nosaka, vai kursors atrodas pareizajā vietā     
        sound.play()
        screen.blit(button2, (buttonx, buttony))
    else:
        screen.blit(button, (buttonx, buttony))
        sound.activate(False)
            
def PlayMusic(music):#izveido jaunu funkciju
    pygame.mixer.music.load(music) #Šī komanda atrod mūzikas failu
    pygame.mixer.music.play(-1) #Šī komanda spēlē mūziku bezgalīgi


def background(background_img, screen):#izveido jaunu funkciju
    BackgroundImg = pygame.image.load(background_img)#atrod attēlu folderī
    BackgroundX = 0 #kur atradīsies attēls x asī
    BackgroundY = 0 #kur atradīsies attēls y asī
    screen.blit(BackgroundImg, (BackgroundX,BackgroundY)) #izprintē pasu attēlu

def GameLogo(logo_img, screen):#izveido jaunu funkciju
    GameLogoImg = pygame.image.load(logo_img)#Šeit jāieliek spēles logo, vai titles.
    GamelogoX = 0#kur atradīsies attēls y asī
    GameLogoY = 0#kur atradīsies attēls y asī
    screen.blit(GameLogoImg, (GamelogoX, GameLogoY))  
