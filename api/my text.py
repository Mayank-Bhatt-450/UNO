import pygame
class entry:
    def __init__(self,screen,text,x,y,w=100,h=10,
                 color=(0,0,0),bg_color=(200,200,200),
                 font='Audiowide-Regular.ttf',boder=1):
        self.screen=screen
        
        self.text=text
        self.x=x
        self.y=y
        self.active=True
        #self.event=event
        self.w=100#int(len(self.text)*(h/2))#w
        self.h=h
        self.color=color
        self.bg_color=bg_color
        self.font=font
        self.boder=boder
        self.w=100
        #self.places()
        '''
        self.=
        self.=
        self.=
        self.='''
    def places(self):
        
        self.box=pygame.draw.rect(self.screen,(0,0,0),(self.x-(self.boder),self.y-(self.boder),self.w+(self.boder*2),self.h+(self.boder*2)),)
        #print('self.bg_color=',self.bg_color)
        pygame.draw.rect(self.screen,self.bg_color,
                         (self.x,self.y,self.w,self.h)
                         )
        self.fontx=pygame.font.Font('Audiowide-Regular.ttf',self.h)
        self.place=self.fontx.render(self.text,True,self.color)
        self.screen.blit(self.place,(self.x,self.y))
        self.w=self.place.get_width()+25
    def event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if event.pos[0]>self.x and event.pos[1]>self.y and event.pos[0]<self.x+self.w and event.pos[1]<self.y+self.h:
                self.active = True
            else:
                self.active = False
            if self.active==False:
                #print('in')
                self.bg_color=(200,200,200)
            else:
                self.bg_color=(255,255,255)
            self.places()
            #print('lol',self.bg_color)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.places()
            
        
    def get(self):
        return self.text
        

def text_obj(text,font):
    t=font.render(text,True,(255,0,0))
    return (t)
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = True
text=entry(screen,'',100,100,h=100)
while done:
    
    screen.fill((255,0,255))
    #font=pygame.font.Font('Audiowide-Regular.ttf',20)
    #a=font.render('text to show _ ly|',True,(255,0,0))#text_obj('lol',font)
    
    #x=a.get_rect()
    #screen.blit(a,(50,20))
    #pygame.draw.rect(screen,(0,0,0),(0,0,100,50),0)
    
    text.places()
    pygame.display.update()
    for event in pygame.event.get():
        if len(pygame.event.get())>2:
            print(pygame.event.get())
        if event.type == pygame.QUIT:
            done = False
        text.event(event)
    
        
        
