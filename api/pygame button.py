import pygame
class button:
    def __init__(self,screen,text,x,y,color=(255,255,255),
                 
                 w=50,h=10,text_color=(0,0,0),
                 ):
        self.screen=screen
        self.text=text
        self.x=x
        self.y=y
        self.active=False
        self.w=w#w
        self.given_w=w
        self.h=h
        self.color=color
        self.temcolor=color
        self.text_color=text_color

    def place(self):
        pygame.draw.rect(self.screen,
                         (0,0,0),
                         (self.x+2,self.y+2
                          ,self.w,self.h))
        pygame.draw.rect(self.screen,
                         self.color,
                         (self.x,self.y
                          ,self.w,self.h))
        self.fontx=pygame.font.Font(None,self.h)
        self.places=self.fontx.render(self.text,True,self.text_color)
        self.screen.blit(self.places,(self.x+((self.w/2)-(self.places.get_width()/2)),
                                      self.y+((self.h/2)-(self.places.get_height()/2))))
        self.w=max(self.places.get_width()+25,self.given_w)

        
        
    def event(self,event):
        pos=pygame.mouse.get_pos()
        if (pos[0]>self.x and
        pos[1]>self.y and
        pos[0]<self.x+self.w and
        pos[1]<self.y+self.h):
            if self.active:
                self.color=(min(self.color[0]+20,255),min(self.color[1]+20,255),min(self.color[2]+20,255),)
                #(max(self.color[0]-self.presscolor),)
                print('self.color=',self.color)
                self.active=False
        else:
            self.active=True
            self.color=self.temcolor
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.color=(max(self.color[0]-40,0),max(self.color[1]-40,0),max(self.color[2]-40,0))
            return True
        self.place()
        
        

        

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = True
text=button(screen,'lol',100,100,w=200,h=50,color=(123,230,80))
while done:
    
    screen.fill((255,0,255))    
    text.place()
    pygame.display.update()
    for event in pygame.event.get():
        if len(pygame.event.get())>2:
            print(pygame.event.get())
        if event.type == pygame.QUIT:
            done = False
        if text.event(event):
            print('clicked')
    
        
        
