'''
import sys
import pygame as pg
class flash_text:
    def __init__(self,screen,text,x,y,font=None,size=10,color=(0,0,0,255)):
        self.screen=screen
        self.text=text
        self.x=x
        self.y=y
        self.size=size
        self.color=color
        self.font=font
        self.alpha=255
    def place(self):
        self.fontx=pygame.font.Font(None,self.size)
        self.places=self.fontx.render(self.text,True,)

        self.txt_surf = self.fontx.render(self.text, True, self.color)
        self.alpha_img = pygame.Surface(self.txt_surf.get_rect().size, pygame.SRCALPHA)
        alpha_img.fill((255, 255, 255, self.alpha))
        self.txt_surf.blit(self.alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(self.txt_surf,(self.x,self.y))


def main():
    clock = pg.time.Clock()
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 64)
    gray = pg.Color('gray15')
    blue = pg.Color('dodgerblue2')

    txt_surf = font.render('translucent text', True, (0,0,0))
    alpha_img = pg.Surface(txt_surf.get_rect().size, pg.SRCALPHA)
    alpha_img.fill((255, 255, 255, 255))
    txt_surf.blit(alpha_img, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        screen.fill(gray)
        pg.draw.rect(screen, blue, (75, 20, 100, 150))
        screen.blit(txt_surf, (30, 60))
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()




'''
import pygame,threading,time
pygame.init()
pygame.display.set_caption('Image')
screen = pygame.display.set_mode((1200,800))#(1024,768))
pygame.display.set_caption("GU NO")
class flash_text:
    def __init__(self,screen,text,x,y,font='Audiowide-Regular.ttf',size=10,color=(0,0,0,255)):
        self.screen=screen
        self.text=text
        self.x=x
        self.y=y
        self.size=size
        self.color=color
        self.font=font
        self.alpha=255
    def place(self):
        self.fontx=pygame.font.Font('Arial.ttf',self.size)

        self.txt_surf = self.fontx.render(self.text, True, self.color)
        self.alpha_img = pygame.Surface(self.txt_surf.get_rect().size, pygame.SRCALPHA)
        self.alpha_img.fill((255, 255, 255, self.alpha))
        self.txt_surf.blit(self.alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(self.txt_surf,(self.x,self.y))
def neg(a):
    while True:
        if a.alpha>0:
            a.alpha-=1
            time.sleep(0.001)
        else:
            break
def thrd(a):
    thread=threading.Thread(target=neg,args=(a,))
    thread.daemon=True
    thread.start()






#test= pygame.image.load('preview.gif','32').convert_alpha()
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
def processs(screen):
    #a=pygame.Surface((500,500))
    a = pygame.Surface((1000,750), pygame.SRCALPHA)   # per-pixel alpha

    for angle in range(360):
        #a.fill((255,0,255,0))
        a.fill((255,255,255,0))
        #a.set_alpha(100)
        #a.set_colorkey((255,0,255,0))
        #pygame.changeSpriteImage(test,angle)
        #time.sleep(0.5)
        surf =rot_center(process_img, angle) #pygame.transform.rotate(process_img, angle)
        # and blit it to the screen
        a.blit(surf, (0, 0))
        screen.blit(a, (0, 0))
        pygame.display.update()
        input('-----')
        time.sleep(0.3)

        a.set_alpha(0)
        pygame.display.update()
        #
        #a.blit(surf, (0, 0))
        #screen.blit(a, (200, 200))
        pygame.display.update()
        input('-----')


a=flash_text(screen,'lol',0,0,size=100)
running=True
def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        target.blit(temp, location)

class process_animations:
    def __init__(self,screen,img,pos):
        self.img=img
        self.screen=screen
        self.a=pygame.Surface((500,500), pygame.SRCALPHA)
        self.angle=0
        self.alpha=0
        self.pos=pos
        self.image_dimension=(self.img.get_width(), self.img.get_height())
    def place(self):
        self.temp = pygame.Surface(self.image_dimension, pygame.SRCALPHA)#.convert()
        self.temp.fill((0,0,0,0))
        #self.temp.blit(self.screen, (-self.pos[0], -self.pos[1]))

        #self.temp.fill((0,0,0,))
        #self.temp.set_colorkey((0,0,0))
        self.surf =self.rot_center(self.img,self.angle)
        self.surf.set_alpha(5)#self.alpha)
        self.temp.blit(self.surf, (0, 0))
        #self.temp.set_alpha(self.alpha)
        self.screen.blit(self.temp, self.pos)


    def rot_center(self,image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
class process_animation:
    def __init__(self,screen,img,pos):
        self.img=img
        self.screen=screen
        self.a=pygame.Surface((500,500))
        self.angle=0
        self.alpha=0
        self.pos=pos
        self.image_dimension=(self.img.get_width(), self.img.get_height())
    def place(self):
        self.temp = pygame.Surface(self.image_dimension).convert()
        self.temp.blit(self.screen, (-self.pos[0], -self.pos[1]))
        self.surf =self.rot_center(self.img,self.angle)
        self.temp.blit(self.surf, (0, 0))
        self.temp.set_alpha(self.alpha)
        self.screen.blit(self.temp, self.pos)


    def rot_center(self,image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
class thrd(threading.Thread):
     # Thread class with a _stop() method.
    # The thread itself has to check
    # regularly for the stopped() condition.

    def __init__(self, *args, **kwargs):
        super(thrd, self).__init__(*args, **kwargs)
        #print(*args[0], **kwargs)

        q=args
        self.a=q[0]
        print(self.a)

    '''
    def __init__(self,a):
        self.a=a
        self._stop = True'''

    # function using _stop function
    def stop(self):
        self._stop=False

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        self.a.alpha=255
        while True:
            if self._stop!=False:
                return
            if self.a.angle<360:
                self.a.angle+=1
                time.sleep(0.001)
            else:
                self.a.angle=0
            #time.sleep(1)
thrd_flag=True
def  process_animation_thrd(a):
    global thrd_flag
    a.alpha=255

    while thrd_flag:
        if a.angle<360:
            a.angle+=1
            time.sleep(0.001)
        else:
            a.angle=0
            #break
    else:
        a.alpha=0
        thrd_flag=True
def process_animation_thrd_CALL(a):
    thread=threading.Thread(target=process_animation_thrd,args=(a,))
    thread.daemon=True
    thread.start()
process_img=pygame.image.load('process.png')
p=process_animation(screen,process_img,(00,00))
while running:
    screen.fill((255,255,255))
    #screen.draw.text("hello world", (100, 100), shadow=(1.0,1.0), scolor="blue")
    a.place()
    p.place()
    #blit_alpha(screen,process_img,(100,100),50)


    #processs(screen)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                print(event.key,type(event.key))#27==esc
                if event.key==27:
                    #thrd(a)
                    process_animation_thrd_CALL(p)
                    #ai=thrd(p)
                    #ai.start()
                if event.key==282:
                    thrd_flag=False

    pygame.display.update()
#'''
