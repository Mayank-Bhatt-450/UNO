import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 32)
#font = pygame.font.SysFont("comicsansms", 72)

#clock = pygame.time.Clock()
input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False
gameloop=True
class text_input:
    def __init__(self,x,y,text='',color='black'):
        self.rect=pygame.Rect(x,y ,140, 32)
        self.font=pygame.font.Font(None, 32)
        self.text=text
        self.color=pygame.Color('black')
        self.active = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def get(self):
        return self.text
text_inputs = text_input(100, 100)    
        
while gameloop:
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            gameloop=False
        text_inputs.handle_event(i)
        
    screen.fill((30, 30, 30))
    text_inputs.draw(screen)
    '''
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface, (0,0))'''
    pygame.display.flip()
